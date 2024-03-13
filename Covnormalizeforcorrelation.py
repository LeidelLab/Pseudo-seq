
import pandas as pd

# Replace 'your_input_file.txt' with the actual path to your input file
input_file = 'PUS1plusandminuswithNfiltered_cov50minusCMC.txt'

# Read the tab-delimited table without a header
df = pd.read_csv(input_file, header=None, sep='\t')

# Loop through columns 3 to the last column and normalize each column
for col in range(2, df.shape[1]):
    df[col] = df[col] / df[col].sum()

# Replace 'your_output_file.txt' with the desired output file path
output_file = 'PUS1minusCMCnormalized.txt'

# Write the normalized values to a new tab-delimited file
df.to_csv(output_file, sep='\t', header=False, index=False)





