import os
import tldextract

# Path to the folder containing the input and output files
folder_path = "./lists"

# File paths
source_file = os.path.join(folder_path, 'source.txt')
master_file = os.path.join(folder_path, 'master.txt')
abp_file = os.path.join(folder_path, 'abp.txt')

# Read domains from source.txt
with open(source_file, 'r') as file:
    lines = file.readlines()

# Initialize set for registered domains (to ensure uniqueness)
registered_domains = set()

# Process each line
for line in lines:
    domain = line.strip()  # Remove any leading/trailing whitespace
    if not domain:  # Skip empty lines
        continue

    # Extract the registered domain using tldextract
    extracted = tldextract.extract(domain)
    registered_domain = extracted.registered_domain

    if registered_domain:
        registered_domains.add(registered_domain)

# Sort the registered domains
sorted_domains = sorted(registered_domains)

# Generate entries for master.txt and ABP.txt
master_entries = [f"{domain}\n" for domain in sorted_domains]
abp_entries = [f"||{domain}^\n" for domain in sorted_domains]

# Write to master.txt
with open(master_file, 'w') as file:
    file.writelines(master_entries)

# Write to ABP.txt
with open(abp_file, 'w') as file:
    file.writelines(abp_entries)

print(f"Processing complete. Output files saved in {folder_path}")
