#!/usr/bin/env python
# open_file.py

# I am setting the path to a fasta file i downloaded manually to get the hang of this program.
# I downloaded a fasta file locally and scp'd it to the module-02 directory. 
# Set the file path to the fasta sequence of Human Clock Protein.
Human_Clock_Protein = '/home/tekumalla.sa/module-2-manojvarma13/module-02-manojvarma13/sequence.fasta'

# Initialize a line counter
line_count = 0

# Open the genome file
with open(Human_Clock_Protein) as Human_Clock:
    # Iterate over the lines in the file
    for line in Human_Clock:
        # Increment the line count by one
        line_count += 1
        # If the line count is less than 5, print the line
        if line_count < 5:
            print(line)
