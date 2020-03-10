# Overview

For this project you will be parsing data from 3 MAGPix results CSV files and selecting two data types, Median and Count, to parse and re-organize for further project analyses.

## Analysis Steps

1. Read in the "protein_dict.txt" file. This file contains a list of the protein names you will encounter in the MAGPix CSV file (1st column) and a corresponding list of names that should be used instead within the output files (column 2). The order of the rows in "protein\_dict.txt" (top-to-bottom) should also be used to re-order the protein data columns in the output files (left-to-right).

2. Read in the "Assay_metadata.txt" file. In this file, there are four data columns- Assay, Plate, Lines, Disease State, and Isotype. The 'Assay' column refers to the .csv run file such that '1' under the 'Assay' column will signify 'Assay1'. The 'Plate' column refers to either the first, '1', or the second, '2', plate on the particular Assay. In a .csv run file, the plate number is listed in a 96-well plate format as (1,A1) or (2,H3). The 'Lines' column refers to the literal lines in the .csv run file in which the Sample (S00###-0#) needs to be matched with a Disease State and Isotype (the last two columns in the Assay_metadata.txt file). Use this file to add two new columns to the output data files. One column will be 'Disease State' and a second 'Isotype'. 'Disease State' should be placed on the left side of 'Sample' and 'Isotype' on the right side of 'Sample'.

3. Read in the 3 MAGPix CSV files "Assay1.csv", "Assay2.csv", "Assay3.csv". From these files, extract the 'Median' and 'Count' data tables. (hint: look at Dan Sanchez's Google group post on converting CSV to TSV). 

4. For the Median data type, output 3 individual tab-delimited files, one for each run. In addition, also create a "combo" tab delimited file with the Median results of all three runs. All of these files should 1) contain the two additional columns specified in step #2, 2) have re-ordered protein columns based on "protein\_dict.txt" and 3) have new header names for the individual protein columns also based on "protein\_dict.txt". 

5. Repeat step 4 for Count data type.

6. Use the Combo Count tab delimited file to output a file of "low bead counts". To do 
this, assign a cutoff count of 30, and so any value below 30 must be copied into an 
outlier outputfile along with the protein it corresponds with. In addition, list the 
number of instances that a particular protein was below the cutoff value.



