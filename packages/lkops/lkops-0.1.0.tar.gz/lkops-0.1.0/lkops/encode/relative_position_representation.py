# -*- encoding: utf-8 -*-
'''
@Time    :   2022-07-29 10:22:57
@Author  :   songhaoyang
@Version :   1.0
@Contact :   songhaoyanga@enn.cn
'''

import numpy as np
import torch 
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoConfig, AutoTokenizer, add_start_docstrings

class RelativePosition(nn.Module):
    def __init__(self, num_units, max_relative_position):
        super().__init__()
        self.num_units = num_units
        self.max_relative_position = max_relative_position
        self.embeddings_table = nn.Parameter(torch.Tensor(max_relative_position * 2 + 1, num_units))
        nn.init.xavier_uniform_(self.embeddings_table)
    
    def forward(self, length_q, length_k):
        range_vec_q = torch.arange(length_q)
        range_vec_k = torch.arange(length_k)
        distance_mat = range_vec_k[None, :] - range_vec_q[:, None]
        distance_mat_clipped = torch.clamp(distance_mat, -self.max_relative_position, self.max_relative_position)
        final_mat = distance_mat_clipped + self.max_relative_position
        
        # watch final_mat.cpu().numpy() 0-max_relative_position * 2的对角矩阵 表示其他词对某个token的相对位置 此处最大位置步取2
        final_mat = torch.LongTensor(final_mat).cuda()
        # watch embeddings.detach().cpu().numpy()   len_q, len_k, head_dim
        embeddings = self.embeddings_table[final_mat].cuda()
        return embeddings

class MultiHeadAttentionLayer(nn.Module):
    def __init__(self, hid_dim, n_heads, dropout, device):
        super().__init__()
        assert hid_dim % n_heads ==0

        self.hid_dim = hid_dim
        self.n_heads = n_heads
        self.head_dim = hid_dim//n_heads
        self.max_relative_position = 2
        self.relative_position_k = RelativePosition(self.head_dim, self.max_relative_position)
        self.relative_position_v = RelativePosition(self.head_dim, self.max_relative_position)

        self.fc_q = nn.Linear(hid_dim, hid_dim)
        self.fc_k = nn.Linear(hid_dim, hid_dim)
        self.fc_v = nn.Linear(hid_dim, hid_dim)

        self.fc_o = nn.Linear(hid_dim, hid_dim)

        self.dropout = nn.Dropout(dropout)

        self.scale = torch.sqrt(torch.FloatTensor([self.head_dim])).to(device)

    def forward(self, query, key, value, mask=True):
        # query.shape == key.shape == value.shape
        batch_size = query.shape[0]
        
        len_k = key.shape[1]
        len_q = query.shape[1]
        len_v = value.shape[1]

        query = self.fc_q(query)
        key = self.fc_k(key)
        value = self.fc_v(value)

        # bn, n_heads, seq_len, head_dim
        r_q1 = query.view(batch_size, -1, self.n_heads, self.head_dim).permute(0, 2, 1, 3)
        r_k1 = key.view(batch_size, -1, self.n_heads, self.head_dim).permute(0, 2, 1, 3)
        
        # attn1 batch_size, n_heads, seq_len, seq_len
        attn1 = torch.matmul(r_q1, r_k1.permute(0,1,3,2))

        r_q2 = query.permute(1, 0, 2).contiguous().view(len_q, batch_size * self.n_heads, self.head_dim)    # seq_len, n_heads, head_dim
        r_k2 = self.relative_position_k(len_q, len_k)

        # n_heads, len_q, len_k
        attn2 = torch.matmul(r_q2, r_k2.transpose(1, 2)).transpose(0, 1)
        # batch_size, n_heads, len_q, len_k
        attn2 = attn2.contiguous().view(batch_size, self.n_heads, len_q, len_k)

        attn = (attn1 + attn2) / self.scale

        if mask is not None:
            mask = torch.stack([mask]*attn.shape[1], dim=1)
            attn = attn.masked_fill(mask == 0, -1e10)
        
        attn = self.dropout(torch.softmax(attn, dim=-1))

        # attn [batch,nheads,len_q, len_k]
        r_v1 = value.view(batch_size, -1, self.n_heads, self.head_dim).permute(0, 2, 1, 3)
        weight1 = torch.matmul(attn, r_v1)
        r_v2 = self.relative_position_v(len_q, len_v)
        weight2 = attn.permute(2, 0, 1, 3).contiguous().view(len_q, batch_size*self.n_heads, len_k)
        weight2 = torch.matmul(weight2, r_v2)
        weight2 = weight2.transpose(0, 1).contiguous().view(batch_size, self.n_heads, len_q, self.head_dim)

        x = weight1 + weight2
        # x [batch, len_q, nheads, head_dim]

        x = x.permute(0, 2, 1, 3)

        # x [batch, len_q, nheads, head_dim]
        x = x.reshape(batch_size, -1, self.hid_dim)

        # x [batch, len_q, hid_dim]
        x = self.fc_o(x)

        # x [batch, len_q, hid_dim]
        return x

def make_mask(mask):
    """
    构造mask方阵，形如
    [[1,1,1,1,0,0,0],
     [1,1,1,1,0,0,0],
     [1,1,1,1,0,0,0],
     [1,1,1,1,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0]]
    """
    mask = mask.numpy()
    l = mask.shape[1]
    res = []
    for mat in mask:
        l0 = sum(mat==0)
        l1 = sum(mat==1)
        m1 = [mat] * l1 + [np.zeros(l,dtype=int)] * l0
        res += [m1]
    return torch.tensor(res)

if __name__ == "__main__":
    # cache_dir = "/home/tico/.cache/huggingface/hub/bert-base-uncased"
    model_prefix = "bert-base-uncased"
    cfg = AutoConfig.from_pretrained(model_prefix)
    tokenizer = AutoTokenizer.from_pretrained(model_prefix)
    device = ("cuda" if torch.cuda.is_available() else "cpu")
    model = MultiHeadAttentionLayer(cfg.hidden_size, cfg.num_attention_heads, cfg.attention_probs_dropout_prob, device)
    model = model.to(device)
    token_embedding = nn.Embedding(cfg.vocab_size, cfg.hidden_size)

    text = ["小明没有偷同桌的橡皮，是其他同学偷得。","我不知道啊"]
    t = tokenizer(text, return_tensors="pt", add_special_tokens=False, padding=True)
    input_ids = t.input_ids
    mask = make_mask(t.attention_mask.cpu()).cuda()
    token = token_embedding(input_ids)
    print(f"token shape: {token.shape}")

    q = k = v = token.cuda()

    model(q, k, v, mask)