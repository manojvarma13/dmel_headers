#!/usr/bin/env python
# open_file.py
#To use regular expressions you need to import re
import re
#Set the path of the file to use the data in the fasta sequence further in the program. 
dmel_genome_path = '/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta'
line_count = 0
# Initialize a sequence variable
head = ""
i = 1
with open(dmel_genome_path) as dmel_genome:
    for line in dmel_genome:
        # Increment the head count by one
        line_count += 1
        if i != 51:
            # This allows python command to check for the lines starting with '>' the header lines. 
            if re.match('^>', line):
                head += line
                i = i+1
#This is to print the first 50 Header lines to a file named "dmel_headers.txt"
print(head)
filename = "dmel_headers.txt"
with open (filename, 'w') as out:   
    out.write(head)
