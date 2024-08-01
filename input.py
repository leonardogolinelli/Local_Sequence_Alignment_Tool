#!/home/leonardo/miniconda3/envs/numpy_env/bin/python
import argparse

def fetch_arguments():
    parser = argparse.ArgumentParser(description="Process alignment scoring parameters and sequences.")
    
    # Adding arguments
    parser.add_argument("--match", type=int, default=3, help="Score for a match")
    parser.add_argument("--mismatch", type=int, default=-3, help="Score for a mismatch")
    parser.add_argument("--gap", type=int, default=2, help="Score for a gap")
    parser.add_argument("--top_sequence", type=str, default="TGTTACGG", help="Top sequence")
    parser.add_argument("--bottom_sequence", type=str, default="GGTTGACTA", help="Bottom sequence")
    parser.add_argument("--sequence_file", type=str, help="Path to file containing sequences")

    args = parser.parse_args()

    scores = {
        "match": abs(args.match),
        "mismatch": -1 * abs(args.mismatch),
        "gap": abs(args.gap)
    }

    if args.sequence_file:
        with open(args.sequence_file, 'r') as file:
            lines = file.readlines()
            top_sequence = lines[0].strip()
            bottom_sequence = lines[1].strip()
    else:
        top_sequence = args.top_sequence
        bottom_sequence = args.bottom_sequence

    print("")
    print("######### ALGORITHM INITIALIZATION #########")
    print("Scores:", scores)
    print("Top sequence:", top_sequence)
    print("Bottom sequence:", bottom_sequence)
    print("")

    return scores, top_sequence, bottom_sequence

if __name__ == "__main__":
    fetch_arguments()
