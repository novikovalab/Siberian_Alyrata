#! /bin/bash
#BSUB -J map[1-192]
#BSUB -q multicore20
#BSUB -M 40000 -R "rusage[mem=40000] "
#BSUB -n 4
#BSUB -o map_%I_%J_output.txt
#BSUB -e map_%I_%J_error.txt


samples='/biodata/dep_mercier/grp_novikova/A.Lyrata/lyrata_raw_data_February2022/samples'

echo "STARTING JOB"
num=${LSB_JOBINDEX}\p
acc=`sed -n ${num} ${samples} | cut -d " " -f1`
echo ${acc}

raw="/biodata/dep_mercier/grp_novikova/A.Lyrata/lyrata_raw_data_February2022/renamed"
ref='/netscratch/dep_mercier/grp_novikova/A.Lyrata/S_locus/NT1_assembly/final_NT1/NT1_220222'
out="/netscratch/dep_mercier/grp_novikova/A.Lyrata/S_locus/lyrata_February2022_to_NT1_220222"

#### TRIMM PAIRED READS
java -ea -Xmx18g -Xms1g -XX:ParallelGCThreads=4 -cp /opt/share/software/packages/BBMap_38.90/bin/current/ jgi.BBDuk t=4 in=${raw}/${acc}_1.fq.gz in2=${raw}/${acc}_2.fq.gz \
    out=${raw}/${acc}_1.paired.fq.gz out2=${raw}/${acc}_2.paired.fq.gz \
    outm=${raw}/${acc}_1.unpaired.fq.gz outm2=${raw}/${acc}_2.unpaired.fq.gz \
    ref=/netscratch/dep_mercier/grp_novikova/shared/adapters.fa \
    ktrim=r k=23 mink=11 hdist=1 tbo tpe qtrim=rl trimq=15 minlen=70

#### Map reads
#bwa index ${ref}.fasta # the reference needs to be indexed before mapping, only one time
bwa mem -t 4 -M -R '@RG\tID:lyr_'${acc}'\tSM:'${acc}'\tPL:Illumina\tLB:lyr_'${acc} ${ref}.fasta ${out}/${acc}_1.paired.fq.gz ${out}/${acc}_2.paired.fq.gz > ${out}/${acc}.sam
samtools view -bh -t ${ref}.fasta.fai -o ${out}/${acc}.bam ${out}/${acc}.sam
wait
rm ${out}/${acc}.sam
samtools sort ${out}/${acc}.bam -o ${out}/${acc}.sort.bam -T ${out}/${acc}_temp
wait
rm ${out}/${acc}.bam
samtools sort -n ${out}/${acc}.sort.bam -o ${out}/${acc}.sortn.bam -T ${out}/${acc}_temp
wait
rm ${out}/${acc}.sort.bam
samtools fixmate -rm ${out}/${acc}.sortn.bam ${out}/${acc}.fixmate.sortn.bam
wait 
rm ${out}/${acc}.sortn.bam
samtools sort ${out}/${acc}.fixmate.sortn.bam -o ${out}/${acc}.fixmate.sort.bam -T ${out}/${acc}_temp
wait
rm ${out}/${acc}.fixmate.sortn.bam
samtools markdup -rs ${out}/${acc}.fixmate.sort.bam ${out}/${acc}.fixmate.sort.markdup.bam
samtools index ${out}/${acc}.fixmate.sort.markdup.bam
rm ${out}/${acc}.fixmate.sort.bam

#### Estimate coverage with goleft
if test -f "${out}/${acc}.fixmate.sort.markdup.bam"; then
source ~/.profile
source ~/.bashrc
module load goleft/0.2.3
goleft covstats ${out}/${acc}.fixmate.sort.markdup.bam > ${out}/goleft/${acc}.covstats
fi

#### Call Haplotypes
# Before calling create a dictionary for the reference, needs to be done only one time
java -jar ${PICARD_HOME}/picard.jar CreateSequenceDictionary R=${ref}.fasta O=${ref}.dict
# Run Haplotype Caller
gatk --java-options "-Xmx35G" HaplotypeCaller  \
   -R ${ref}.fasta \
   -I ${out}/${acc}.fixmate.sort.markdup.bam \
   -O ${out}/${acc}.g.vcf.gz \
   -ERC GVCF \
   --sample-ploidy 2 \
   --output-mode EMIT_ALL_CONFIDENT_SITES

