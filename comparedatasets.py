import pandas as pd

# Load your data into Pandas DataFrames without headers
table1 = pd.read_csv('Table1.txt', header=None, delimiter='\t')  # Replace 'table1.txt' with your file path
table2 = pd.read_csv('Table2.txt', header=None, delimiter='\t')  # Replace 'table2.txt' with your file path

# Specify the columns to check in table1 (adjust column indices as needed)
columns_to_check = [0, 1]  # Assuming the first and second columns (0-based index) should be checked

# Check if the values in columns_to_check exist in table2
matching_rows = table1[table1[columns_to_check].apply(tuple, axis=1).isin(table2[columns_to_check].apply(tuple, axis=1))]

# Save the matching rows to a new tab-delimited text file (optional)
matching_rows.to_csv('Sitespresentinbothtables.txt', sep='\t', index=False)  # Replace 'matching_rows.txt' with your desired output file name

# Display the matching rows (optional)
print("Matching Rows:")
print(matching_rows)

