# RNA-Seq Resistome profiling of Acinetobacter baumannii
- For this project, you will:
    - parse and organize RNAseq data.
    - generate a boxplot illustrating gene expression differences between sample types 

## Recomended modules 
Matplotlib

Pandas

Numpy

### Input Files
1. "k\_table.csv" is a comma-separated file containing expression information for each sample type (i.e. bacterial isolate + condition) and for each transcript in the genome. Note that each sample type was run in triplicate. The replicates can be identified because they all have the same name ("sample" column), with two exceptions: 

    1.  Each replicate has a different final identifier following the "\_". 
    2.  Each replicate has a different lowercase letter (a, b or c) just prior to the TX or TZ in the sample name.

So, for example, ACS-TG22182**a**TX-xx-uu-USA-xxxx-077-JB_**S1**, ACS-TG22182**b**TX-xx-uu-USA-xxxx-077-JB_**S2**, ACS-TG22182**c**TX-xx-uu-USA-xxxx-077-JB_**S3** are three replicates of a single sample type. 

Columns of interest within this file include sample replicate name (sample) transcript  name (target\_id), normalized read counts for each transcript (est\_count), drug resistance information (resistance_profile), and treatment type (treatment).

2. "s\_table.csv" is a csv file containing the output of a statistical analysis comparing levels of transcript expression from the different isolates/conditions. Columns of interest include: the name of the differentially expressed transcript (target_id), the p-value (pval) and the adjusted p-vaule (qval). 

3. There is also one "abundance.tsv" file for each bioreplicate organized within a set of directories starting with the 'indiv\_replicates' directory and including one subdirectory for each bioreplicate. These tab-delimited files contain the raw output from kallisto (an RNA-seq analysis algorithm). Info from these files were combined to form "k\table.csv".


### Expected Output

Your aims are two-fold: 

1. Read in the data from "k\_table.csv" and "s\_table.csv", and generate a new tab-delimited output file containing a subset of the columns from these two input files, as well as a few new columns with summary statistics. The output file should be called "Output.txt" and should include the following columns:

    1. "target\_id" (from s\_table)
    2. "pval" (from s\_table)
    3. "qval" (from s\_table)
    4. "sigma\_sq" (from s\_table)
    5. Mean est\_count for each sample type (4 columns in total, calculated using all replicates from k\_table)
    6. Standard deviation in est\_count for each sample type (4 columns in total, calculated using all replicates from k\_table)


2. For the transcript with the lowest p-value in "s\_table.csv", generate a boxplot displaying normalized read counts for each sample contained within "k\_table.csv" (i.e., one box per sample generated using all three replicates for each sample).


### Extra credit

Add option to your script for est\_count data to be read in from the individual abundance.tsv files (1 per replicate), instead of from k\_table.



