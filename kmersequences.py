from Bio import SeqIO

# Function to extract 5-mer sequence with the specified position in the middle
def extract_kmer(transcript_sequence, position):
    k = 5
    half_k = k - 2
    start_position = max(0, position - half_k)
    end_position = start_position + k
    return transcript_sequence[start_position:end_position]

# Read transcripts from the FASTA file
def read_fasta(fasta_file):
    return SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))

# Input and output file names
input_file = "input_table.txt"
output_file = "output_table.txt"

# Read transcripts from the FASTA file
transcript_file = "MANE.GRCh38.v1.0.select_ensembl_rna_plusMT_singleline.fna"
transcript_records = read_fasta(transcript_file)

# Read input table and process each entry
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    outfile.write("Transcript_ID\tPosition\t5-mer\n")  # Header for the output table
    for line in infile:
        parts = line.strip().split("\t")
        if len(parts) == 2:
            transcript_id, position = parts
            position = int(position)
            
            if transcript_id in transcript_records:
                transcript_sequence = str(transcript_records[transcript_id].seq)
                kmer_sequence = extract_kmer(transcript_sequence, position)
                outfile.write(f"{transcript_id}\t{position}\t{kmer_sequence}\n")
            else:
                print(f"Transcript ID {transcript_id} not found in the provided FASTA file.")
        else:
            print(f"Skipping invalid line: {line}")

