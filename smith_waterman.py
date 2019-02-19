import argparse
import itertools
import numpy as np
import pandas as pd
import csv
from itertools import dropwhile
#Implemented from https://tiefenauer.github.io/blog/smith-waterman/

def matrix(a, b, match_score, gap_cost=2):
    H = np.zeros((len(a) + 1, len(b) + 1), np.int)
    #import matrix of interest
    keys = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V", "B", "Z", "X" "*"]
    values = range(0,24)
    dictionary = dict(zip(keys, values))
    for i, j in itertools.product(range(1, H.shape[0]), range(1, H.shape[1])):
        x = dictionary[a[i-1]]
        y = dictionary[b[j-1]]
        ms = match_score[x, y]
        match = H[i - 1, j - 1] + (ms if a[i - 1] == b[j - 1] else - ms)
        delete = H[i - 1, j] - gap_cost
        insert = H[i, j - 1] - gap_cost
        H[i, j] = max(match, delete, insert, 0)
    return H

def traceback(H, b, b_='', old_i=0):
    # flip H to get index of **last** occurrence of H.max() with np.argmax()
    H_flip = np.flip(np.flip(H, 0), 1)
    i_, j_ = np.unravel_index(H_flip.argmax(), H_flip.shape)
    i, j = np.subtract(H.shape, (i_ + 1, j_ + 1))  # (i, j) are **last** indexes of H.max()
    if H[i, j] == 0:
        return b_, j
    b_ = b[j - 1] + '-' + b_ if old_i - i > 1 else b[j - 1] + b_
    return traceback(H[0:i, 0:j], b, b_, i)

def is_comment(s):
    # return true if a line starts with # or A
    return s.startswith(('#', " A"))

def scoringMatrixParse(matrix_filename):
    #input: path to matrix
    #output: parsed np array
    M = np.eye(24)
    with open(matrix_filename,'r') as fh:
        for i, row in enumerate(dropwhile(is_comment, fh)):
            for j in range(0, len(row.split())):
                M[i,j] = row.split()[j]
    return M 
M = scoringMatrixParse("/Users/matt/OneDrive/UCSF/algorithms/HW3/scoring_matrices/PAM250")
H = matrix('GGTTGACTA', 'TGTTACGG', M, 2)
print(H)
#print(traceback(H, 'TGTTACGG'))
#print(H)
