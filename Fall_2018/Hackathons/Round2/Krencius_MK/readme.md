# Identifying and Cataloguing Polymorphisms in miRNA Binding Sites

### Input files:

1. Fasta files, each identified by the organisms being compared (ex: human-gorilla.fas). Each contains three sequences (human reference, human SNPs, and the animal reference seqeunce).
2. Text files identified by miRNA name(s) (ex: miR7.txt, miR7and876.txt).

### Desired Functionality and Output:

1. Read in data from one fasta file and one miRNA file.
2. Identify locations in the "human reference" sequence from the fasta file that match the sequence(s) contained in the miRNA file. These are miRNA "sequence motifs".
3. Identify variations between the sequence "human reference" and the other two seqeunces.
4. Count differences (i.e. SNPs) between Seq1 (human reference) and Seq2 (human SNPs), and Seq1 (human reference) and Seq3(animal reference), cataloguing each variation by whether or not it is present in one of the identified sequence motifs. Refer to variations bewteen Seq1 and Seq2 as P (i.e. polymorphisms within species), and variations between Seq1 and Seq3 as D (i.e. divergence between species). Variations that are within the motif should be indicated as N, and ones that are not should be indicated as S. (So the final four counts should be labelled PS, PN, DS, and DN.) Do not include variations in the count if any of the three sequences shows "-" (i.e. a gap) at that position. 
4. Output a text file including the four counts. 

### Extra Credit:

1. Add functionality to allow the user to provide multiple fasta/miRNA file pairs.

2. Pipe the output into a classic McDonald-Kreitman test (equations given in PowerPoint) to determine NI and alpha. Incude a chi-square test to determine p-value, and output NI, alpha, chi-square, and p with the raw counts.

