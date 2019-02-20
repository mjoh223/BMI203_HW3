import argparse
from smith_waterman import scoringMatrixParse, matrix, traceback
import os

def main():
    parser = argparse.ArgumentParser(description = "pairwise local alignment")
    parser.add_argument("gap_cost", help="affine gap penalty cost", type = int)
    parser.add_argument("gap_extension", help = "gap extension cost", type = int)
    parser.add_argument("matrix", help="scoring matrix")
    args = parser.parse_args()
    matrix_path = os.path.join("/Users/matt/OneDrive/UCSF/algorithms/HW3/scoring_matrices/", args.matrix)
    M = scoringMatrixParse(matrix_path)
    H = matrix("GGTTGACTA", "TGTTACGG", M, args.gap_cost, args.gap_extension)
    print(H)
    #print(traceback(H, "TGTTACGG"))
    #print(M)
if __name__ == "__main__":
    main()


