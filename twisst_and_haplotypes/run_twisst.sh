vcf_pref=""
ploidy=""
min_calls= # 80% of number of samples
groups=""

python3 genomics_general/VCF_processing/parseVCF.py -o ${vcf_pref}.gen --ploidyFile $ploidy -i ${vcf_pref}.vcf.gz --minQual 30 --gtf flag=DP min=8
python3 genomics_general-0.4/filterGenotypes.py -i ${vcf_pref}.gen --ploidyFile $ploidy -o ${vcf_pref}_filt.gen --verbose --minCalls $min_calls --minAlleles 2 --minVarCount 5 -t 26 --maxHet 0.75
python3 genomics_general-0.4/phylo/phyml_sliding_windows.py --windType sites -w 100 -g ${vcf_pref}_filt.gen -p ${vcf_pref} -T 15 -Mi 20 --model GTR --optimise n
python3 twisst.py -t ${vcf_pref}.trees.gz -w ${vcf_pref}.wheights.tsv -g EE_4n  -g EE_2n -g Austria_2n -g Austria_4n  -g outgroup --groupsFile $groups
