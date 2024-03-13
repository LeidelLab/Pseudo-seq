import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Replace 'your_table.txt' with the actual path to your data file
file_path = 'Input.txt'

# Read the tab-delimited table with no header
df = pd.read_csv(file_path, delimiter='\t', header=None)

# Assign generic column names
columns = ['TranscriptID', 'Position', 'Replicate1', 'Replicate2', 'Replicate3', 'Replicate4', 'Replicate5', 'Replicate6']
df.columns = columns

# Log transformation for specified columns (e.g., Replicate1 to Replicate6)
columns_to_transform = ['Replicate1', 'Replicate2', 'Replicate3', 'Replicate4', 'Replicate5', 'Replicate6']
small_constant = 1e-10

for col in columns_to_transform:
    df[col] = np.log(df[col] + small_constant)

# Calculate the correlation matrix
correlation_matrix = df[columns_to_transform].corr()

# Display the correlation matrix
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Set up seaborn style
sns.set(style="whitegrid")

# Generate a heatmap using Seaborn with color range from -1 to 1
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5, vmin=-1.0, vmax=1.0)

# Set x-axis and y-axis labels
replicate_labels = ['Replicate 1', 'Replicate 2', 'Replicate 3', 'Replicate 4', 'Replicate 5', 'Replicate 6']
heatmap.set_xticklabels(replicate_labels)
heatmap.set_yticklabels(replicate_labels)

plt.title('Correlation Plot for Normalized Coverage Across Replicates')
plt.xlabel('Replicates')
plt.ylabel('Replicates')
plt.savefig('Correlationplot.pdf')
plt.show()
