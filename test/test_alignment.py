import sys
sys.path.append('/Users/matt/OneDrive/ucsf/algorithms/HW3')
from smith_waterman import scoringMatrixParse, matrix, traceback, evaluate, mutate
import os
import numpy as np


def test_alignment_format():
    seqA = "AtCtggTTcc"
    seqB = "atcTgccTcT"
    sub_mtx = scoringMatrixParse(os.path.join("/Users/matt/OneDrive/UCSF/algorithms/HW3/scoring_matrices/", "BLOSUM50"))
    M = matrix(seqA, seqB, sub_mtx, -9, -3)
    assert np.issubdtype(M.dtype, np.dtype('int64'))

def test_matrix():
    ############-- Online check --############################
    # Program: water
    # Rundate: Mon 25 Feb 2019 00:21:17
    # Commandline: water
    #    -auto
    #    -stdout
    #    -asequence emboss_water-I20190225-002115-0388-17773373-p2m.asequence
    #    -bsequence emboss_water-I20190225-002115-0388-17773373-p2m.bsequence
    #    -datafile EBLOSUM50
    #    -gapopen 10.0
    #    -gapextend 1.0
    #    -aformat3 pair
    #    -sprotein1
    #    -sprotein2
    # Align_format: pair
    # Report_file: stdout
    ########################################

    #=======================================
    #
    # Aligned_sequences: 2
    # 1: HBA_HUMAN
    # 2: HBA_MOUSE
    # Matrix: EBLOSUM50
    # Gap_penalty: 10.0
    # Extend_penalty: 1.0
    #
    # Length: 26
    # Identity:      18/26 (69.2%)
    # Similarity:    21/26 (80.8%)
    # Gaps:           0/26 ( 0.0%)
    # Score: 135.0
    #
    #
    #=======================================

    seqA = "MVLSPADKTNVKAAWGKVGAHAGEYG"
    seqB = "MVLSGEDKSNIKAAWGKIGGHGAEYGAE"
    sub_mtx = scoringMatrixParse(os.path.join("../scoring_matrices/", "BLOSUM50"))
    M = matrix(seqA, seqB, sub_mtx, -10, -1)
    s = traceback(M, True, b=seqB, b_="", old_i=0)
    assert s == 135
