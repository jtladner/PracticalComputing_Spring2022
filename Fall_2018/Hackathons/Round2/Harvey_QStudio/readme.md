# Quant Studio 12 Kapa Quant Quality Control Script

### Overview

- The objective of this script is to automate quality control processing for Kapa Quant assays.
- The script will accept arguments from the user regarding sample details, read raw text files from the instrument, and then calculate and display the results.

### Script Input
1. Input File: "MH 3-8\_QuantStudio_export.txt"

    - Tab-delimited text file containing Kapa Quant data on 12 samples, 6 standards, and one NTC (no template control).
    - The important colums are "Sample Name" and "Ct Mean". These are the only columns needed for calculations and analysis. Ignore instrument parameters at the begenning of file and the melt curve data at the end of the file.
    - Each sample is ran in triplicate. Average Ct for each sample is automatically calculated by the instrument.

2. Arguments:
    - The script should adjust its calculations based on input from the user about the samples. These values should be provided on the command line and will be used in calculations within the script.
        - Average fragment length: The average fragment length (in base pairs) of the amplicon that is being analyzed. For this experiment, the fragment is 248 bp.
        - Sample dilution factor: The dilution factor that the samples were ran at. For these data, the dilution factor was 1:100,000.

### Script Output
1. Calculate and plot a linear regression for the 6 standards. This will require the [scikit-learn module](https://scikit-learn.org/stable/).
    - X axis = log(standard concentration in pmols). Displayed in table below.
    - Y axis = Average Cq (taken from "MH 3-8\_QuantStudio_export.txt")
    - Display the R^2 value and the linear regression equation in the y= mx + b format on the plot.

|Standard Name|Concentration (pmols)|log(Concentration in pmols)|
| ------------|:-------------------:| -------------------------:|
|STD 1        |20                   |1.30                       |
|STD 2        |2                    |0.30                       |
|STD 3        |.2                   |-0.70                      |
|STD 4        |.02                  |-1.70                      |
|STD 5        |.002                 |-2.70                      |
|STD 6        |.0002                |-3.70                      |


2. Create a tab-delimited output text file with these 3 columns. Include concentration data for each sample and each standard:

|Sample Name|Concentration (pmols)|Concentration (ug/mL)|
|-----------|:-------------------:|--------------------:|

Use the following calculations to generate values for the output table file. "Slope" and "Y intercept" come from the linear regression of the 6 standards.

- Size-adjusted sample concentration in pM

 ```(Dilution Factor)*((10^((average sample Cq – Y intercept)/Slope))*(452/Average fragment length in bp))```

- Size-adjusted sample concentrations in ug/uL

```(concentration in pM*10^-15)*(Average fragment length in bp*617.9)*10^6```

### Recomended modules 
- Matplotlib
- Numpy
- SciPy
- scikit-learn




