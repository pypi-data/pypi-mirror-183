import argparse


def use_parser():
    parser = argparse.ArgumentParser(description="Find uniq letters from strings")
    parser.add_argument('--string', type=str, default=None, help="Enter your string")
    parser.add_argument('--file', type=str, default=None, help="Enter your file path")
    args = parser.parse_args()
    return args.string, args.file