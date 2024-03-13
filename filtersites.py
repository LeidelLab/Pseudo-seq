import pandas as pd

# Read the tab-delimited table without headers
data = pd.read_csv("WTplusandminuswithN.txt", sep="\t", header=None)

# Add the filtering conditions

filtered_data = data[
    (data.iloc[:, 44] > 3.5) &
    (data[14] > 50) &
    (data[13] > 5) &
    (data[12] > 5) &
    (data[11] > 5) &
    (data[10] > 5) &
    (data[9] > 5) &
    (data[8] > 5) &
    (data[36] > 50) &
    (data[21] > 0.2) &  # Adding the condition for column 22
    [False] + (data.iloc[:-1, 46] == "T").tolist()
]
# Write the filtered data to an output file
filtered_data.to_csv("WTplusandminuswithNfiltered44_35_22_02_cov50.txt", sep="\t", index=False, header=False, quoting=2)
