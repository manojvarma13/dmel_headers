#!/usr/bin/env python
# parse_file.py

# To use regular expressions you need to import re
import re

# Set the file path to the Human Clock Protein fasta sequence thats saved in module-2 dir of defiance.
Human_Clock_Protein = '/home/tekumalla.sa/module-2-manojvarma13/module-02-manojvarma13/sequence.fasta'

# Initialize a line counter
line_count = 0

# Initialize a sequence variable
seq = ''

with open(Human_Clock_Protein) as Human_Clock:
    for line in Human_Clock:
        # Increment the line count by one
        line_count += 1
        # If the line count is less than 5
        if line_count < 5:
            # Check to see if the line is a header line (starts with >)
            if re.match('^>', line):
                # Print the header
                print(line)
            else:
                # This is a sequence line so append to seq
                seq += line

# Print the seq variable
print(seq)
