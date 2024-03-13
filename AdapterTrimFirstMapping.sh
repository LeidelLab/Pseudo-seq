#!/usr/bin/bash

for i in *fastq.gz

 do fn=$(basename $i fastq.gz)

 cutadapt --no-indels -q 30,30 --trimmed-only -j 20 -a GATATCGTCAAGATCGGAAGAGCACACGTCTGAA -m 10 -o $fn'_{name}_trim.fastq.gz' $i 1> $fn'_log.txt'

 done

for i in *trim.fastq.gz

 do fn=$(basename $i trim.fastq.gz)

 cutadapt -j 20 -m 10 -u 2 -o $fn'_trimFinal.fastq.gz' $i

 done


for i in *trimFinal.fastq.gz

 do fn=$(basename $i trimFinal.fastq.gz)

 bowtie2 -p 20 -x /MANE_Reference -U $i |
 samtools sort > $fn'_trimFinalsorted.bam'

 done

for i in *.bam

 do fn=$(basename $i .bam)

 samtools index $i


 done
