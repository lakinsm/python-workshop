
## Imports
import glob
import argparse
import re
import os

## Command-line Arguments
parser = argparse.ArgumentParser('python grep.py')
parser.add_argument('pattern', type=str, help='Pattern to search')
parser.add_argument('path', type=str, help='File(s) to search')
parser.add_argument('-r', '--recursive', action='store_true', help='Search recursively')

args = parser.parse_args()
search_pattern = args.pattern
files = glob.glob(args.path)
files = [x.replace("\\", "/") for x in files]  # For Windows

## Define function for pattern searching
def grep(pattern, path):
    for file in path:
        if os.path.isdir(file):
            if args.recursive:
                recurse = glob.glob(file+'/*')
                recurse = [x.replace("\\","/") for x in recurse]
                grep(pattern, recurse)
            continue
        with open(file, 'r') as f:
            for line in f.read().split():
                if not all(x is None for x in [re.search(pattern, line)]):
                    stem = file.split("/")[-1]
                    print stem+":\t"+re.sub('('+pattern+')', '\033[31m' + r'\1' + '\033[0m', line)

## Main
grep(search_pattern, files)
