awk 'NR > 1' WTplusandminus.txt > WTplusandminusnoN.txt
awk 'BEGIN {OFS="\t"}; {print $1, $2-1, $2-0}' WTplusandminusnoN.txt > WTplusandminusnoN.bed
bedtools getfasta -tab -fi /location of MANE FASTA file -bed WTplusandminusnoN.bed -fo WTplusandminusnoN.seq
paste WTplusandminusnoN.txt WTplusandminusnoN.seq > WTplusandminuswithN.txt
