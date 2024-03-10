# Pseudo-seq
Custom scripts used for pseudo-seq data analysis

Adjust AdapterTrimFirstMapping.sh according to your input file names, adapter sequence, computational power and reference location. Execute script to cut the adapter and remove the 2 5' nucleotides from the RT primer followed by mapping of the adjusted FASTQ file to the reference using bowtie2.
Adjust Correct5prime.py for inpute file names, make sure BAM and respective FASTQ files are in the same folder and execute to correct for the TdT activity of the RT.
Adjust SecondMappingCovcalculating.sh for input file names and references. Execute to map the corrected FASTQ files and calculate the 5' read coverage and overall coverage and combine the files of one genotype in one file for CMC treated and one file for mock treated samples for WT, PUS1-/- and PUS3-/-.
Adjust Calculations.R for inpute file names and execute to calculate mean coverage, 5'coverage/coverage of all samples, average 5'coverage/coverage and the psi score by dividing the average 5'coverage/coverage value of CMC treated by the average 5'coverage/coverage value of mock treated samples.
Adjust Addnucleotides.sh for inpute file names and reference and execute to add the nucleotide of every transcript position to the file.
Adjust filtersites.py for input file names and filtering criteria and execute to filter sites according to criteria.
Adjust compare.py for input file names and execute to compare sites in WT datasets to sites in PUS1/3 datasets. Output are sites that are present in both datasets. This script was used to find sites that are present in WT and PUS1-/- datasets.
Adjust PUSdependentsites.py for input file names and filtering criteria and execute to determine sites that are present in the WT and PUS1 datasets but do not reach the threshold in the PUS3 dataset.
Adjust ENSTtogenomiclocation.R for input file names to transform transcript ID and position to genmoic coordinates.

Adjust Covnormalizeforcorrelation.py for inpute file names. To create correlation plots, sites with a minimum average read coverage of 50 were used in each dataset to remove noise. The coverage value of every repliate at the transcript position was normalized to the sum of all coverage values of that replicate (library size normalization). The Log correlation plot was created with Logcorrelationplot.py.
