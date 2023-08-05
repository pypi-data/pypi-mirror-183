import argparse
import sys

from kevbase64.encode import base64_encode
from kevbase64.decode import base64_decode


def main():
    parser = argparse.ArgumentParser(
        prog="pbase64",
        description="Encode and decode using Base64 representation with Kev's implementation",
    )
    parser.add_argument(
        "-d",
        "-D",
        "--decode",
        help="Decode incoming Base64 stream into binary data.",
        action="store_true",
    )
    parser.add_argument(
        "-i",
        "--input_file",
        help="Read input from input_file.  Default is stdin; passing - also represents stdin.",
        default="-",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        help="Write output to output_file.  Default is stdout; passing - also represents stdout.",
        default="-",
    )
    parser.add_argument(
        "-b",
        "--break",
        help="Insert line breaks every count characters.  Default is 0, which generates an unbroken stream.",
        type=int,
        default="0",
        dest="_break",
    )
    args = parser.parse_args()

    prev_stdin = sys.stdin
    prev_stdout = sys.stdout
    if args.input_file != "-":
        sys.stdin = open(args.input_file, "r")
    if args.output_file != "-":
        sys.stdout = open(args.output_file, "w")

    data = sys.stdin.read()

    if args.decode:
        for i, char in enumerate(base64_decode(data), 1):
            sys.stdout.write(char)
            if args._break and i % args._break == 0:
                sys.stdout.write("\n")
    else:
        for i, char in enumerate(base64_encode(bytes(data, encoding="utf-8")), 1):
            sys.stdout.write(char)
            if args._break and i % args._break == 0:
                sys.stdout.write("\n")
    sys.stdout.write("\n")
    sys.stdin = prev_stdin
    sys.stdout = prev_stdout


if __name__ == "__main__":
    sys.exit(main())
