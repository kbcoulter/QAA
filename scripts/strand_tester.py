#!/bin/bash python

import argparse

def get_args():
     parser = argparse.ArgumentParser(description="A script to test strandedness in htseq.txt output.")
     parser.add_argument("-f", "--filenames", help="Stranded THEN Reverse .txt files (order matters)", required=True, type=str, nargs="+")
     return parser.parse_args()

args = get_args()

def total_assigned(file):
    total = 0
    with open(file) as f:
        for line in f:
            if line.startswith("__"):
                continue  
            total += int(line.strip().split("\t")[1])
    return total

yes_total = total_assigned(args.filenames[0])
rev_total = total_assigned(args.filenames[1])
print("\n#####################################################################")
print(f"ASSUMING STRANDED YES: {args.filenames[0]} \n \n\tAND \n \nREVERSE ASSUMING: {args.filenames[1]}")
print("#####################################################################")
print(f"Total reads assigned (stranded=yes): {yes_total}")
print(f"Total reads assigned (stranded=reverse): {rev_total}")
if yes_total > rev_total:
    print("\nRecommendation: use stranded='yes'")
else:
    print("\nRecommendation: use stranded='reverse'")
print("#####################################################################\n")