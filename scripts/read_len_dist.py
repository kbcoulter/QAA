#!/usr/bin/env python

import matplotlib.pyplot as plt
import argparse
import gzip

def get_args():
     parser = argparse.ArgumentParser(description="A script to return the distribution of trimmed read lengths in a gzipped fastq")
     parser.add_argument("-f", "--filenames", help="Input FASTQ files (gzipped)", required=True, type=str, nargs="+")
     parser.add_argument("-o", "--outname", help="Name for the output histogram: <outname>.png", required=True, type=str)
     parser.add_argument("-c", "--colors", help="Comma sep. colors for plot", required=False, type=str, default = "orange,red")
     parser.add_argument("-l", "--labels", help="Labels for Legend", required=False, type=str, default = " , ")
     return parser.parse_args()

args = get_args()
filenames = args.filenames
outname = args.outname
labels = args.labels.split(",")
colorcs = args.colors.split(",")


plt.figure()

data_plot = []

for i, filename in enumerate(filenames):
     lens_list = []
     with gzip.open(filename, "rt") as fastq:
          for index_line, line_data in enumerate(fastq):
               if index_line % 4 == 1: # SEQLINE
                    lens_list.append(len(line_data.strip()))
     data_plot.append(lens_list)

plt.hist(data_plot,
          color = colorcs,
          edgecolor = "dimgrey", 
          alpha = 0.7, 
          label = labels,
          stacked = False)

plt.yscale('log')  # log scale for y-axis (frequency)
plt.xlabel("Read Length (bp)", fontsize = 14)
plt.ylabel("Count (log scale)", fontsize = 14)
plt.title(f"{outname} Length Distribution", fontsize = 16, fontweight = "bold")
plt.grid(axis='y', linestyle='--', color = "grey", alpha=0.5, zorder=-1)
plt.legend()
plt.tight_layout()
plt.savefig(f"{outname}_readlen.png")
