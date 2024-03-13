# Define dictionaries to store data from both tables
table1_data = {}
table2_data = {}

# Read and process data from Table 1
with open('SitespresentinWTandPUS1.txt', 'r') as file1:
    for line in file1:
        parts = line.strip().split('\t')
        transcript_id = parts[0]
        position = int(parts[1])
        column45_value = float(parts[44])
        table1_data[(transcript_id, position)] = column45_value

# Read and process data from Table 2
with open('PUS3plusandminuswithN.txt', 'r') as file2:
    for line in file2:
        parts = line.strip().split('\t')
        transcript_id = parts[0]
        position = int(parts[1])
        column45_value = float(parts[44])
        table2_data[(transcript_id, position)] = column45_value

# Create an output file to write the results
with open('SitespresentinWTandPUS1butnotPUS3.txt', 'w') as output_file:
    # Compare the data and find rows where column 45 value is two times higher in Table 1
    for (transcript_id, position), value1 in table1_data.items():
        if (transcript_id, position) in table2_data:
            value2 = table2_data[(transcript_id, position)]
            if value1 >= 2 * value2 and value2 < 3.5:
                # Output the full row from Table 1 and include the value from Table 2
                output_file.write(f"{transcript_id}\t{position}\t{value1}\t{value2}\n")

