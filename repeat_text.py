import argparse


def repeat_text(text, n_times):
    for i in range(n_times):
        print(text)


parser = argparse.ArgumentParser("repeat_text.py")
parser.add_argument("text", type=str, help="Input text to repeat (required)")
parser.add_argument("-n", "--n_times", type=int, default=3, help="Number of times to repeat [3]")


if __name__ == "__main__":
    args = parser.parse_args()
    repeat_text(args.text, args.n_times)
