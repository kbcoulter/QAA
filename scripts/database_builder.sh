#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
#SBATCH --time=2:00:00
#SBATCH --output=db_build_out_%j.log
#SBATCH --error=db_build_err_%j.log


/usr/bin/time -v STAR --runThreadN 8 --runMode genomeGenerate --genomeDir /projects/bgmp/kcoulter/bioinfo/Bi623/QAA/campy_data/align_db/ --genomeFastaFiles /projects/bgmp/kcoulter/bioinfo/Bi623/QAA/campy_data/campylomormyrus.fasta --sjdbGTFfile /projects/bgmp/kcoulter/bioinfo/Bi623/QAA/campy_data/campylomormyrus.gtf