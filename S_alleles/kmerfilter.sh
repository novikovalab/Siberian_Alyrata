
#! /bin/bash
#BSUB -J kmerfilter[1-38]
#BSUB -q multicore20
#BSUB -M 10000 -R "rusage[mem=10000] "
#BSUB -n 10
#BSUB -o kmerfilter_%J_output.txt
#BSUB -e kmerfilter_%J_error.txt

samples="/netscratch/dep_mercier/grp_novikova/A.Lyrata/S_locus/uliana/NGSgenotyp-master/feb_23/list1"
echo "STARTING JOB"

num=${LSB_JOBINDEX}\p

acc=`sed -n ${num} ${samples}`
echo ${acc}

out='/netscratch/dep_mercier/grp_novikova/A.Lyrata/S_locus/uliana/NGSgenotyp-master'
cd ${out}

source ~/.bashrc
conda init bash
conda activate /home/ukolesnikova/anaconda3/envs/slocusenv1
input='/biodata/dep_mercier/grp_novikova/A.Lyrata/lyrata_raw_February2023/trimmed'


./NGSgenotyp.py kmerRefFilter -k 20 -o ${out}/feb_23/kmerresultsSRK \
   -1 ${input}/${acc}_1.paired.fq.gz -2 ${input}/${acc}_2.paired.fq.gz \
   -r /netscratch/dep_mercier/grp_novikova/A.Lyrata/S_locus/uliana/NGSgenotyp-master/DB_DATABASES/SRK_DB_Brassicaceae_new_202022/SRK_DB_Brassicaceae_arenosa_caps1_11022022.fasta

echo "FINISHED JOB"

# Submit with bsub < BSUB_TEMPLATE.sh
# Check status with bjobs
# Check output during run with bpeek JOBID
