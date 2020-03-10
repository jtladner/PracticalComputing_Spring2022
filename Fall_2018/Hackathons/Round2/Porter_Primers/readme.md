# Hackathon\_Project_Porter

### Background
Degenerate primers are often used to increase the amount of diversity that a PCR assay can cover. These degeneracies produce “populations” of primers within an assay allowing specific subpopulations to amplify particular target groups. In this project, you will examine sequences of the pyrG gene from several Borrelia species to identify if our designed primers will theoretically amplify all Borrelia species. However, the designed script should work for any primer/target pairs and at any scale (i.e., for a single sequence and primer pair or thousands of sequences with hundreds of primers). 

### Overview 
Create a script that:
1.	Allows users to specify the “input.fasta” and “primers.fasta” files from the command line (example: “primer.py –s input.fasta –p primers.fasta”) (hint: consider the use of the “argparse” module)
2.	Identifies _if_ sequences match specific primers (potentially multiple times) and the sequence location (base pair numbers) at which the match(es) occurred. This information should be saved as output in a tab-delimited file (output.txt).  
3.	Provides a summary.txt file indicating the percent of sequences that match each primer.

### Input files
1.	primers.fasta
2.	example.fasta

### Output files
1.	output.txt
2.	summary.txt

### Expected steps
1.	Convert primers that have ambiguities/degeneracies into several non-ambiguous primers using the IUPAC nucleotide code. This step will result in the creation of at least 2 different primers for every primer that includes ambiguity.  
2.	Loop through the .fasta file to identify if each sequence will match each primer, creating an “output.txt” file. The “output.txt” file should include the .fasta sequence name and identify if each unambiguous primer either matched the given sequence (“TRUE”) or did not match the sequence (“FALSE”). If the primer matches the sequence, the script should provide the base pair numbers (start-end) at which the primer matched.
3.	Finally, this script should summarize the results from the “output.txt” identifying the percent of sequences that match the original degenerate primers in a summary file (“summary.txt”).

### Details to consider
-	Primers may have more than one degeneracy
-	Sequences could be different lengths producing different primer annealing locations

Thank you for your time and consideration on this project!
