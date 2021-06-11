from numpy import dot
from numpy.linalg import norm
import numpy as np

def cos_sim(a, b):
    return dot(a, b) / (norm(a) * norm (b))

def make_matrix(feats, list_data):
    freq_list = []
    for feat in feats:
        freq = 0
        for word in list_data:
            if feat == word:
                freq += 1
        freq_list.append(freq)
    return freq_list

text1 = ['컴', '퓨', '터', '공', '학', '부']
text2 = ['컴', '퓨', '터', '공', '학', '전', '공']

v3 = text1 + text2

feats = set(v3)

v1_arr = np.array(make_matrix(feats, text1))
v2_arr = np.array(make_matrix(feats, text2))

cs1 = cos_sim(v1_arr, v2_arr)

print(cs1)