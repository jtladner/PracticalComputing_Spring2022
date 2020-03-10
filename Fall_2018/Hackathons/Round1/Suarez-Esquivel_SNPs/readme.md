# Hackathon project


### Some background

Brucella is a monophyletic genus of bacteria, that produces a zoonotic disease. In animals
the infection induces abortion and reduced productiveness; in humans the disease is known
as undulant fever, a debilitating chronic condition frequently under-diagnosed.
Humans get infected by contact with reproductive fluids of infected animals, and by
consuming unpasteurized milk products.

As this bacterium is monophyletic, we are more interested in finding differences that could
help us to understand its host and environmental adaptation.

Our group sequenced several genomes of Brucella isolates from Costa Rica and included other
sequences available at public databases (NCBI, ebi) from around the world to provide
context, and we are currently working on the analysis of an large amount of information.

For this hackathon project we will be working on the analysis of Brucella abortus genomes,
the most important Brucella species in Costa Rica.

We mapped and aligned all the genomes (n= 150) to a known and well annotated reference, and
called the variant sites from there. As part of the output we have a huge text file (tab
delimited) that includes detailed information of the position of those variant sites.


### Input for the analysis

The text file that will be the input for our goal script(s) includes a line for each variable
position, or SNP, in the alignment to the reference.

The file has a column for each one of the following details:
- Position in alignment
- Position in "reference genome"
- Characteristics of the position where the SNP is located: coding sequence (CDS), rRNA,
  tRNA or intergenic position.
- Strand where the SNP is located: forward (indicated by "1") or reverse ("-1")
- Name or locus tag of the gene where the SNP is found. A "-" is indicated when it is
  located at an intergenic region.
- Product encoded by that gene. A "-" is indicated for intergenic regions.
- Synonymous/Non synonymous meaning of the SNP: S for synonymous, NS for not-synonymous,
  SNOP for SNPs causing pseudogenes by premature stop codons, SNOP2 for both premature stop
  and codon deletions.
- Ref base: Base in the reference genome.
- SNP base: base substitute in the alternative genotype. Some positions have more than one 
  substitution. For example, the base in the reference is "A", some genotypes show a "T" at
  that position, but other genotypes show a "G". In this case, the column will indicate
  "T,G".
- Total: number of genomes included in the alignment with the alternative genotype in the indicated position.
  Similar to the previous column, if more than one type of substitution is found, it will
  be indicated as "24,3" which means that 24 genomes show a "T", and 3 showed a "G".
- A column for each genome included in the alignment; 149 additional columns in our input
  file. This specifies the SNP base found in that genome. If the base is the same one as
  the reference, a dot (".") is indicated.


### Aims of the project
- The aims of this project will be to create a script, or several, that will produce:
    - Priority 1: A text file with information for SNPs shared by a given subgroup of
      genomes within the alignment, and that are unique for that single group.
    - Priority 2: Graphs for (i) SNP density, (ii) non-synonymous SNP density,
      (iii) synonymous SNP density, and (iv) non-synonymous/synonymous SNP density along the alignment. It would be cool
      to produce these graphs within a sliding window!


### Details to consider
- We will have to deal with commas and dots as part of the input. That will complicate a
  bit the coding. If needed, we could use some regex to change the input file previously.
- The names of the genomes are varied, as some come from databases. The genomes that we
  sequenced are identified with the sequencing lane, for example "11502_1#17". The symbol
  "#" usually is confusing. Also, numbers and letters combinations are used for the public
  databases genomes.
  
  
### To test the scripts
- Several of the genomes correspond to isolates obtained from a particular outbreak, a single geographic region
  or the same host species. So we could expect some shared SNPs among them that are unique to
  those groups.
- Three groups that could be used for testing the script(s) are:
  1. The group of the genomes id as (n=12): "B_\d{3}_S"
     - Manual review of these isolates showed 44 unique SNPs for the group, however no one
       is shared among all, but only for two or three. This could be found if the script
       filters all unique, and then all shared among those unique.
  2. The group of the genomes id as (n=53): "\d{5}_SJC_\d#\d"
     - This group includes 13 unique and shared SNPs, plus 22 SNPs unique for them, but not
       shared by all.
  3. The complete group of Costa Rican isolates (n=78): "\d{5}_\w{1,3}_\d#\d" + "B_\d{3}_S", but
    excluding "\d{5}_Sp_\d#\d" and "\d{5}_Nig\d#\d", that are from Spain (n=3) and Nigeria
    (n=6).
    - This group shares 50 SNPs unique and shared among them, plus 139 unique but not shared. 
  
  
    
  Thanks in advance to all! I hope that this (or these) script(s) will not only help us to
  develop coding skills but that also, with some modifications, they will be useful to all
  of us.
