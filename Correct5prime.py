import re
import pysam
import tqdm
import gzip

bam_path = "PATHtoBAM"
fastq_file_path = bam_path.replace(".bam", ".fastq.gz")
fastq_output_file_path = fastq_file_path + ".corrected"

clipped = 0
total = 0
replace = {}

bam = pysam.AlignmentFile(bam_path, "rb")
for read in tqdm.tqdm(bam):
    total += 1
    try:
        tag = read.get_tag("MD")
    except KeyError:
        continue
    match = re.match(r"^(0\w)+", tag)
    if match is None:
        continue
    clip_leading = match.group(0).count("0")
    if clip_leading > 0:
        clipped += 1
        replace[read.qname] = [read.seq[clip_leading:], read.qual[clip_leading:]]

print(clipped, total)

skip_until_next = False
n_replaced = 0
with gzip.open(fastq_file_path, "rt") as input_file, gzip.open(
    fastq_output_file_path, "wt"
) as output_file, tqdm.tqdm(desc="while") as pbar:
    while True:
        header = input_file.readline().strip()
        if not header:
            break
        sequence = input_file.readline().strip()
        plus = input_file.readline().strip()
        quality = input_file.readline().strip()
        abbrev_header = header.lstrip("@").split(" ")[0]
        if abbrev_header in replace:
            sequence, quality = replace[abbrev_header]
            n_replaced += 1
        if sequence.startswith("T"):
            output_file.write(f"{header}\n{sequence[1:]}\n+\n{quality[1:]}\n")
        else:
            output_file.write(f"{header}\n{sequence}\n+\n{quality}\n")
        pbar.update(1)

print(n_replaced)
print(n_replaced / total)
