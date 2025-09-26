#useful if you ever need to split large data for some reason

import os

# File paths
input_file = r'C:\Users\yourfile.txt'
output_dir = r'C:\Users\yourfolder'
chunk_size = 1000000  # Number of lines per chunk

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

with open(input_file, 'r', encoding='utf-8') as infile:
    header = infile.readline()  # Read the header
    chunk_count = 1
    line_count = 0
    outfile = open(f"{output_dir}/chunk_{chunk_count}.csv", 'w', encoding='utf-8')
    outfile.write(header)
    for line in infile:
        outfile.write(line)
        line_count += 1
        if line_count % chunk_size == 0:
            outfile.close()
            chunk_count += 1
            outfile = open(f"{output_dir}/chunk_{chunk_count}.csv", 'w', encoding='utf-8')
            outfile.write(header)
    outfile.close()
