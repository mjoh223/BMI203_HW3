import itertools
import numpy as np
import pandas as pd
import csv
from itertools import dropwhile
#Implemented from https://tiefenauer.github.io/blog/smith-waterman/

#The goal of the smith-waterman algorithm is to find the optimal local subalignment between two sequences
#It starts with by progressivly creating a scoring matrix (see matrix()) based on a gap penalty and a substitution matrix
#The scoring matrix is then tracedback (see traceback()) by starting at the element with the highest score and tracing along the matrix until a zero is encountered. This ensures the optimal subalignment is found.

def matrix(a, b, match_score, gap_cost, gap_extension):
    #Purpose: create a scoring matrix of two input sequences
    #Input: two sequences, a substitution matrix, and an affine gap penalty
    #Output: scoring matrix between the two input sequences and

    H = np.zeros((len(a) + 1, len(b) + 1), np.int) #initalize a matrix between two sequences (a, b) of size a+1, b+1
    #create a dictionary for the amino acids and their index in the matrix
    keys = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V", "B", "Z", "X", "*"]
    values = range(0,24)
    dictionary = dict(zip(keys, values))
    gapA_list = []
    gapB_list = []
    for i, j in itertools.product(range(1, H.shape[0]), range(1, H.shape[1])):
        x = dictionary[a[i-1]] #substitution matrix coordinate for first amino acid
        y = dictionary[b[j-1]] #substitution matrix coordinate for second amino acid
        ms = match_score[x, y] #ms is the score from the substition matrix
        #match is defined as the two given amino acids being the same, in which a score is given as the top left element's score + the substitution score, s(a, b) or the ms variable used here.
        gapA = [H[i,j-k] + gap_cost + (gap_extension*k) for k in range(1,j+1)]
        gapB = [H[i-k,j] + gap_cost + (gap_extension*k) for k in range(1,i+1)]
        match= [H[i-1,j-1] + (ms if a[i-1] == b[j-1] else - ms)]
        H[i,j] = max( max(gapA), max(gapB), max(match), 0 )
    return H

def traceback(H, b, b_='', old_i=0):
    #Purpose: find the highest scoring subsequence between between the two sequences
    #Input: scoring matrix and query sequence (doesn't matter which in pairwise)
    #output: the local alignment between A and B sequences

    #flip H to get index of **last** occurrence of H.max() with np.argmax()
    H_flip = np.flip(np.flip(H, 0), 1)
    i_, j_ = np.unravel_index(H_flip.argmax(), H_flip.shape)
    i, j = np.subtract(H.shape, (i_ + 1, j_ + 1))  #(i, j) are **last** indexes of H.max()
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
