#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --nodes=1
#SBATCH --mem=30G
#SBATCH --time=1:00:00
#SBATCH --output=lendist_out_%j.log
#SBATCH --error=lendist_err_%j.log

mamba activate QAA

Cco1="final_reads/Cco_com123_EO_6cm_1_1_cut_paired.fastq.gz"
Cco2="final_reads/Cco_com123_EO_6cm_1_2_cut_paired.fastq.gz"
Crh1="final_reads/Crh_rhy116_EO_adult_3_1_cut_paired.fastq.gz"
Crh2="final_reads/Crh_rhy116_EO_adult_3_2_cut_paired.fastq.gz"

/usr/bin/time -v ./read_len_dist.py -f "$Cco1" "$Cco2" -o Cco_com123_EO_6cm_1 -c indianred,dodgerblue -l read1,read2

/usr/bin/time -v ./read_len_dist.py -f "$Crh1" "$Crh2" -o Crh_rhy116_EO_adult_3 -c orange,darkorchid -l read1,read2

