#! /bin/bash
#BSUB -J nQuire[1-48]
#BSUB -q multicore40
#BSUB -M 40000 -R "rusage[mem=40000] "
#BSUB -n 20
#BSUB -o nquire_%I_%J_output.txt
#BSUB -e nquire_%I_%J_error.txt


samples='/biodata/dep_mercier/grp_novikova/A.Lyrata/lyrata_raw_February2023/sample_accessions.tsv'
in='/netscratch/dep_mercier/grp_novikova/A.Lyrata/map_feb23_to_NT1'
out='/netscratch/dep_mercier/grp_novikova/A.Lyrata/map_feb23_to_NT1/nquire'
echo "STARTING JOB"

num=${LSB_JOBINDEX}\p
acc=`sed -n ${num} ${samples} | cut -f2`
echo ${acc}


cd /netscratch/dep_mercier/grp_novikova/software/nQuire
./nQuire create -b ${in}/${acc}.fixmate.sort.markdup.bam -o ${out}/${acc}.fixmate.sort.markdup.bam
./nQuire denoise ${out}/${acc}.fixmate.sort.markdup.bam.bin -o ${out}/${acc}.denoised
./nQuire lrdmodel -t 20 ${out}/${acc}.denoised.bin >>  ${out}/lrmodel_output_denoised.txt


echo "FINISHED JOB"

# Submit with bsub < BSUB_TEMPLATE.sh
# Check status with bjobs
# Check output during run with bpeek JOBID
