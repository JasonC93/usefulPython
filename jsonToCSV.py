import json
import csv

# File paths
input_file = r'C:\Users\yourfile.json'  # Path to your line-delimited JSON file
output_file = r'C:\Users\yourfile.csv'  # Path to save the resulting CSV
log_file = r'C:\Users\yourfile.log'  # Log file path

# Step 1: Collect all unique headers (keys)
headers = set()

# First pass: Extract unique keys
with open(input_file, 'r', encoding='utf-8') as infile, open(log_file, 'w', encoding='utf-8') as logfile:
    for line in infile:
        try:
            record = json.loads(line.strip())  # Parse each JSON object
            headers.update(record.keys())  # Collect unique keys
        except json.JSONDecodeError:
            #print(f"Skipping invalid JSON line: {line}")
            logfile.write(f"Skipping invalid JSON line: {line}\n")

headers = sorted(headers)  # Sort headers for consistent column order

# Step 2: Write to CSV without storing all records
with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile, \
     open(log_file, 'a', encoding='utf-8') as logfile:
    writer = csv.DictWriter(outfile, fieldnames=headers, quoting=csv.QUOTE_ALL, quotechar='"')
    writer.writeheader()  # Write CSV header
    
    for line in infile:
        try:
            record = json.loads(line.strip())  # Parse each JSON object
            writer.writerow(record)  # Write each record to the CSV
        except json.JSONDecodeError:
            #print(f"Skipping invalid JSON line: {line}")
            logfile.write(f"Skipping invalid JSON line: {line}\n")

print(f"CSV file saved to: {output_file}")
