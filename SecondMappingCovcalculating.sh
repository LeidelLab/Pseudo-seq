#!/usr/bin/bash

for i in *trimFinal.fastq.gz

 do fn=$(basename $i trimFinal.fastq.gz)

 bowtie2 -p 20 -x /MANE_Reference -U $i |
 samtools sort > $fn'_trimFinalsorted.bam'

 done

for i in *.bam

 do fn=$(basename $i .bam)

 samtools index $i


 done

for i in *.bam

 do fn=$(basename $i .bam)

 bedtools genomecov -ibam $i -d -5 |
 sort -S 75% --parallel=20 -k 1,1 -k2,2n -r > $fn'RTstop'

 done

for i in *.bam

 do fn=$(basename $i .bam)

 samtools sort -l 0 -@ 8 -m 5G -n $i |
 bedtools bamtobed -i stdin | 
 sort-bed --max-mem 5G - |
 bedtools genomecov -i stdin -d -g /location of MANE genomefile |
 sort -S 75% --parallel=20 -k 1,1 -k2,2n -r > $fn'coverage'
 done

paste *WT*plus*coverage *WT*plus*RTstop | awk 'BEGIN {OFS="\t"};{print $1,$2,$3,$6,$9,$12,$15,$18,$21,$24,$27,$30,$33,$36}' > WTpluscombined.coverage
paste *WT*minus*coverage *WT*minus*RTstop | awk 'BEGIN {OFS="\t"};{print $1,$2,$3,$6,$9,$12,$15,$18,$21,$24,$27,$30,$33,$36}' > WTminuscombined.coverage
paste *PUS1*plus*coverage *PUS1*plus*RTstop | awk 'BEGIN {OFS="\t"};{print $1,$2,$3,$6,$9,$12,$15,$18,$21,$24,$27,$30,$33,$36}' > PUS1pluscombined.coverage
paste *PUS1*minus*coverage *PUS1*minus*RTstop | awk 'BEGIN {OFS="\t"};{print $1,$2,$3,$6,$9,$12,$15,$18,$21,$24,$27,$30,$33,$36}' > PUS1minuscombined.coverage
paste *PUS3*plus*coverage *PUS3*plus*RTstop | awk 'BEGIN {OFS="\t"};{print $1,$2,$3,$6,$9,$12,$15,$18,$21,$24,$27,$30,$33,$36}' > PUS3pluscombined.coverage
paste *PUS3*minus*coverage *PUS3*minus*RTstop | awk 'BEGIN {OFS="\t"};{print $1,$2,$3,$6,$9,$12,$15,$18,$21,$24,$27,$30,$33,$36}' > PUS3minuscombined.coverage
