#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --output=htseq_out_%j.log
#SBATCH --error=htseq_err_%j.log

mamba activate QAA

htseq-count \
 -i gene_id \
 --stranded=yes \
 star_aligned/Campy_Crh_rhy116_sort_marked.sam \
 campy_data/campylomormyrus.gtf > Crh_rhy116_EO_adult_3_htseqcounts_[forORrev]stranded.txt

htseq-count \
 -i gene_id \
 --stranded=reverse \
 star_aligned/Campy_Crh_rhy116_sort_marked.sam \
 campy_data/campylomormyrus.gtf > Crh_rhy116_EO_adult_3_htseqcounts_[forORrev]reverse.txt

htseq-count \
 -i gene_id \
 --stranded=yes \
 star_aligned/Campy_Cco_com123_sort_marked.sam \
 campy_data/campylomormyrus.gtf > Cco_com123_EO_6cm_1_htseqcounts_[forORrev]stranded.txt

htseq-count \
 -i gene_id \
 --stranded=reverse \
 star_aligned/Campy_Cco_com123_sort_marked.sam \
 campy_data/campylomormyrus.gtf > Cco_com123_EO_6cm_1_htseqcounts_[forORrev]reverse.txt