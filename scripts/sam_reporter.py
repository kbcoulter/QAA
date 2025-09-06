#!/bin/bash python

import argparse
### !! COPIED FROM PS8 -> Altered for QAA !!

### USER VARIABLES ###
def get_args():
     parser = argparse.ArgumentParser(description="A script to return the number of mapped and umapped reads from SAM files ")
     parser.add_argument("-f", "--filenames", help="Input SAM file(s)", required=True, type=str, nargs="+")
     return parser.parse_args()

args = get_args()

### USE ###
for inputfile in args.filenames:
    mapped_counter = 0
    unmapped_counter = 0

    with open (inputfile, "r") as file:
        for line in file:
            if line[0] != "@":
                mapped = False # SET FALSE EVERY LINE
                secondary_mapping = True # SET TRUE EVERY LINE
                line = line.split()
                flag = int(line[1])
                if((flag & 4) != 4):
                    mapped = True

                if ((flag & 256) != 256):
                    secondary_mapping = False

                if mapped and not secondary_mapping: # MAPPED AND NOT REPEATED
                    mapped_counter += 1
                elif not mapped and not secondary_mapping: # NOT MAPPED AND NOT REPEATED
                    unmapped_counter += 1

    print (f"{inputfile}, Mapped:{mapped_counter}, Unmapped:{unmapped_counter}")
   
