#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=8
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --output=qual_nuc_out_%j.log
#SBATCH --error=qual_nuc_err_%j.log

mamba activate QAA

Cco="Cco_com123_EO_6cm_1_1.fastq.gz"

/usr/bin/time -v ./qual_by_nuc.py -f "$Cco" -k 150 -o Cco_1_1
