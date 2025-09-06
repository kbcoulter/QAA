#!/usr/bin/env python

"""
THIS SCRIPT WAS REPURPOSED FROM KBCOULTER DEMULTIPLEX FOR A QAA ANALYSIS.
"""

##### IMPORTS #####
import argparse
import numpy as np
import matplotlib.pyplot as plt
import gzip
import bioinfo # IMPORTS convert_phred (Set to 33 encoding)

##### COLLECT ARGS #####
def get_args():
     parser = argparse.ArgumentParser(description="A script to average the quality scores at each position for all reads and generate a per nucleotide mean distribution of quality scores for read1, read2, index1, and index2.")
     parser.add_argument("-f", "--filename", help="An input FASTQ file", required=True, type=str)
     parser.add_argument("-k", "--readsize", help="Size (length) of the reads", required=True, type=int)
     parser.add_argument("-o", "--outname", help="A name for the output histogram: <outname>.png", required=True, type=str)
     return parser.parse_args()

args = get_args()
filename = args.filename
readsize = args.readsize
outname = args.outname

##### SCRIPT BODY #####
qscores = np.zeros(readsize, dtype = float) # Will hold summed qscores then the mean after div.
num_records = 0

#with open(filename, "rt") as fastq: # FOR ALL FILES, AS WE HAVE ZCATTED THE FILE IN USING OUR SLURM SCRIPT...
with gzip.open(filename, "rt") as fastq: # FOR REAL FILES
     for index_line, line_data in enumerate(fastq):
            if index_line % 4 == 3:
                num_records += 1
                for ascii_ind, ascii_char in enumerate(line_data.strip()):
                    qscores[ascii_ind] += (ord(ascii_char) - 33) # REPLACE BIOINFO.PY TO CUT OVERHEAD

qscores = (qscores / num_records) # Div sum by num records and update the qscores arr

##### PLOTS #####
plt.bar(range(readsize), qscores, color = "indianred", edgecolor = "dimgrey")
plt.xlim(-1,readsize)
plt.ylim(30, 37)
plt.xlabel("Base Position in Read (0 Ind.)", fontsize = 14)
plt.ylabel("Mean Quality Score", fontsize = 14)
plt.title(f"{outname} Mean Quality Score by Base Position", fontsize = 16, fontweight = "bold")
plt.grid(axis='y', linestyle='--', color = "grey", alpha=0.5)
plt.tight_layout()
plt.savefig(f"{outname}.png")