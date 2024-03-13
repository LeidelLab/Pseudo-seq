def load_gene_annotation(file_path):
    gene_annotation = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            fields = line.strip().split('\t')
            if fields[2] in ['gene', 'transcript', 'exon', 'CDS', 'start_codon', 'stop_codon', 'UTR']:
                attributes = dict(item.strip().split(' ') for item in fields[8].strip().split(';') if item)
                if 'transcript_id' in attributes:
                    transcript_id = attributes['transcript_id'].strip('"')
                    if transcript_id not in gene_annotation:
                        gene_annotation[transcript_id] = {'exons': [], 'cds': [], 'start_codon': None, 'stop_codon': None, 'utr': [], 'strand': fields[6]}
                    if fields[2] == 'transcript':
                        gene_annotation[transcript_id]['start'] = int(fields[3])
                        gene_annotation[transcript_id]['end'] = int(fields[4])
                    elif fields[2] == 'exon':
                        gene_annotation[transcript_id]['exons'].append((int(fields[3]), int(fields[4])))
                    elif fields[2] == 'CDS':
                        gene_annotation[transcript_id]['cds'].append((int(fields[3]), int(fields[4])))
                    elif fields[2] == 'start_codon':
                        gene_annotation[transcript_id]['start_codon'] = (int(fields[3]), int(fields[4]))
                    elif fields[2] == 'stop_codon':
                        gene_annotation[transcript_id]['stop_codon'] = (int(fields[3]), int(fields[4]))
                    elif fields[2] == 'UTR':
                        gene_annotation[transcript_id]['utr'].append((int(fields[3]), int(fields[4])))
    return gene_annotation

def determine_transcript_region(gene_annotation, transcript_id, transcript_position):
    if transcript_id not in gene_annotation:
        return 'Transcript not found in gene annotation'

    transcript_info = gene_annotation[transcript_id]

    if transcript_position < transcript_info['start']:
        return '5UTR' if transcript_info['strand'] == '+' else '3UTR'

    for exon_start, exon_end in transcript_info['exons']:
        if exon_start <= transcript_position <= exon_end:
            # Check if it's in the start codon region
            if transcript_info['start_codon'] and transcript_info['start_codon'][0] <= transcript_position <= transcript_info['start_codon'][1]:
                return 'Start Codon'
            
            # Check if it's in the CDS
            for cds_start, cds_end in transcript_info['cds']:
                if cds_start <= transcript_position <= cds_end:
                    return 'CDS'

            # Check if it's in a UTR region
            in_utr = False
            for utr_start, utr_end in transcript_info['utr']:
                if utr_start <= transcript_position <= utr_end:
                    in_utr = True
                    break

            if in_utr:
                # Check strand to determine UTR
                if transcript_info['strand'] == '+':
                    if transcript_position < transcript_info['start_codon'][0]:
                        return '5UTR'
                    elif transcript_position >= transcript_info['stop_codon'][0] and transcript_position <= transcript_info['stop_codon'][1]:
                        return 'Stop Codon'
                    else:
                        return '3UTR'
                else:
                    if transcript_position > transcript_info['start_codon'][1]:
                        return '5UTR'
                    elif transcript_position >= transcript_info['stop_codon'][0] and transcript_position <= transcript_info['stop_codon'][1]:
                        return 'Stop Codon'
                    else:
                        return '3UTR'

    return 'Unknown'

def process_input_table(table_path, gtf_file_path):
    gene_annotation = load_gene_annotation(gtf_file_path)

    with open(table_path, 'r') as input_table:
        for line in input_table:
            transcript_id, transcript_position_str = line.strip().split('\t')
            transcript_position = int(transcript_position_str)
            region = determine_transcript_region(gene_annotation, transcript_id, transcript_position)
            print(f'Transcript {transcript_id}, position {transcript_position} is in the {region}')

# Example usage
table_path = 'sites_input_table.txt'
gtf_file_path = 'MANE.GRCh38.v1.0.ensembl_genomic.gtf'
process_input_table(table_path, gtf_file_path)

