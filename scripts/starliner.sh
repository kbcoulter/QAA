#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --nodes=1
#SBATCH --cpus-per-task=16
#SBATCH --time=2:00:00
#SBATCH --output=STAR_out_%j.log
#SBATCH --error=STAR_err_%j.log

/usr/bin/time -v STAR \
 --runThreadN 8 \
 --runMode alignReads \
 --outFilterMultimapNmax 3 \
 --outSAMunmapped Within KeepPairs \
 --alignIntronMax 1000000 \
 --alignMatesGapMax 1000000 \
 --readFilesCommand zcat \
 --readFilesIn /projects/bgmp/kcoulter/bioinfo/Bi623/QAA/final_reads/Cco_com123_EO_6cm_1_1_cut_paired.fastq.gz /projects/bgmp/kcoulter/bioinfo/Bi623/QAA/final_reads/Cco_com123_EO_6cm_1_2_cut_paired.fastq.gz \
 --genomeDir /projects/bgmp/kcoulter/bioinfo/Bi623/QAA/campy_data/align_db/ \
 --outFileNamePrefix Campy_Cco_com123_aligned &

 /usr/bin/time -v STAR \
 --runThreadN 8 \
 --runMode alignReads \
 --outFilterMultimapNmax 3 \
 --outSAMunmapped Within KeepPairs \
 --alignIntronMax 1000000 \
 --alignMatesGapMax 1000000 \
 --readFilesCommand zcat \
 --readFilesIn /projects/bgmp/kcoulter/bioinfo/Bi623/QAA/final_reads/Crh_rhy116_EO_adult_3_1_cut_paired.fastq.gz /projects/bgmp/kcoulter/bioinfo/Bi623/QAA/final_reads/Crh_rhy116_EO_adult_3_2_cut_paired.fastq.gz \
 --genomeDir /projects/bgmp/kcoulter/bioinfo/Bi623/QAA/campy_data/align_db/ \
 --outFileNamePrefix Campy_Crh_rhy116_aligned &

 wait 