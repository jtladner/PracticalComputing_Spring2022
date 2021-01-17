# Class 3 - Jan. 29th 2021
- In this class we will:
    - Learn to download, install and run open source software
    - Learn to use for loops in bash to batch run multiple similar commands
    - Learn to combine bash commands within a file to create shell scripts

### Required Reading (**Must be completed ahead of time**)
Practical Computing for Biologists, Chapter 6, 21

### Preparation for next class

Python scripts are generally simple text files that are executed on the command line, just like the bash shell scripts we will be generating in today's class. However, there are also GUIs available that allow for python scripts (and those written in other programming languages), to be written and executed without needing the command line. We will use this type of interactive interface for our initial introduction to Python programming next week and again, later in the class, when we learn how to use Python to generate figures. The interactive GUI we will use is called Jupyter Notebook (NOT Jupyter Lab!). 

1. Install Jupyter Notebook

There are multiple ways that you can [install the Jupyter Notebook](http://jupyter.org/install), but I highly recommend installing using the [Anaconda Distribution](https://www.anaconda.com/download/). Anaconda is available for Windows, Linux and MacOS and the Jupyter Notebook is automatically installed as a part of the Anaconda distribution. Please install the Python 3 version of Anaconda. Although your book uses Python 2, Python 3 is the is the current version and it is pretty easy to translate commands between the two versions. 

After Anaconda has been installed, open a terminal window (Mac/Linux) or the "Anaconda Prompt" (Windows) and run the following command: ```jupyter notebook```

This should automatically open the jupyter notebook within your default browser. 

### Assignment

1. Follow the instructions on PCfB p.85-88 to set up your own ```scripts``` and ```programs``` directories and add these directory to your system's PATH. After you've finished, run the following command in the shell and copy and paste the output in the **Assignment Answer Sheet**.

```echo $PATH```

2. Downloading and using a precompiled binary

    1. Download a precompiled binary for the [Muscle alignment tool](https://www.drive5.com/muscle/downloads.htm) that is  appropriate for your operating system. After downloading, move this binary into your ```programs``` directory. If needed, decompress with ```tar -xf```.
    
    2. Use ```chmod``` to ensure that the newly downloaded binary is executable. Veryify the permissions are set properly using ```ls -l```. Enter the commands you used and the current permissions for the binary in the **Assignment Answer Sheet**.
    
    3. Within the shell, move into  the ```muscle``` directory, which is located within the ```Assignment``` directory for this week's class (```Week03_Shell-pt2/Assignment```).
    
    4. If you have properly added the ```programs``` directory to your PATH, and the muscle binary is executable, you should be able to use muscle from anywhere on your computer just using the name of the binary (i.e., without specifying the location of the binary). Check that this works by simply typing the name of the binary you downloaded in your shell and hitting ```return```. If things are working as expected, you should see help info for muscle printed to your terminal window. 
    
    5. Now, use the newly downloaded Muscle binary to align the Coronavirus Spike protein sequences contained in ```????``` using the following command:
    
    ```muscle3.8.31_i86darwin64 -in CoV_Spike_MSA_unaligned.fasta  -out  CoV_Spike_MSA_aligned_muscle.fasta```
    
    **Note**: Replace ```muscle3.8.31_i86darwin64``` with the name of the binary you downloaded. 
    
    Enter the command you used in the **Assignment Answer Sheet** and **upload the aligned fasta file** to Bb Learn along with the Assignment Answer Sheet. 


3. Download and compile source code
    
    1. Download the source code for [RaxML from GitHub](https://github.com/stamatak/standard-RAxML) just as shown in today's demo. If desired, move source code to ```source``` directory then decompress with ```tar -xf```. 
    
    2. Within the shell, move into the decompressed source code directory. 
    
    3. Compile the RaxML program using ```make```. It may take a few tries to find a source code version that is compatible with your precessor and operating system. See [manual](https://github.com/stamatak/standard-RAxML/tree/master/manual ) for details. Here is an example of a command that worked on my laptop:
    
    ```make -f Makefile.AVX.gcc```
    
    In the **Assignment Answer Sheet**, record the version of the source code that compiled correctly on your system. 
    
    4. Use the ```-h``` option to view the help documentation associated with the RaxML program and copy the first 10 lines into the **Assignment Answer Sheet**.
    
    *Hint*: remember the ```head``` command covered last week.  


4. Move into ```Week03\_Shell-pt2/Assignment/zika\_genomes```. This directory contains 89 fasta files. 88 of these each containing a single Zika virus genome, and each sequence containing line within these fasta files has a maximum length of 70 nucleotides. The other is a test file containing a dummy sequence wrapped 5 nucleotides per line.

    This directory also contains a simple python script - "wrap_fasta.py" - that changes the length of the sequence lines in a fasta file. Here is an example command that will take an input fasta and generate a new version with sequence containing lines up to 20,000 nucleotides long:

    ```wrap_fasta.py  input.fasta  output.fasta 20000```

    1. Copy this python script into your 'scripts' directory and make it executable.  

    2. Test that the program is working by running the following command:

    ```wrap_fasta.py  dummy.fasta  dummy_singleline.fasta 20```

    3. This command should create a new file within your working directory called "dummy_singleline.fasta" and in this file, the dummy sequence should now be contained on a single line (instead of being split across four lines, as in dummy.fasta)

    4. Use a for loop (entered directly within the terminal window) to batch process all of these Zika virus genomes, using wrap_fasta.py to create new versions in which each viral genome sequence will be contained on a single line.
    
    **Hint 1**: the Zika virus genome is a little less than 11,000 nucleotides long. 
    **Hint 2**: Make sure that you do not overwrite the original versions of the fasta sequences (i.e., the output.fasta name must be different from the input.fasta name). 
    
    Enter your successful for loop in the **Assignment Answer Sheet** and **upload 1 of the output fasta files** to Bb Learn along with the Assignment Answer Sheet. 

5. Move into the ```Week03\_Shell-pt2/Assignment``` directory. Within this directory, you will find a file called ```dummy.txt```. Write and execute a simple shell script called ```dummy.sh``` that will:
    1. Create a new directory within ```Week03\_Shell-pt2/Assignment``` called "dummy_dir"
    2. Move "dummy.txt" into this new directory
    3. Rename "dummy.txt" to "done.txt"
    
    **Upload your shell script** to Bb Learn along with the Assignment Answer Sheet. 


6. Move into ```Week03\_Shell-pt2/images```. This directory contains several pdf files. Using ```ls``` in combination with regular expressions within your text editor, as described in PCfB p.91-96, generate a shell script called called ```renamer.sh``` that will create renamed copies of all of these pdf files within a new sub-directory called "images\_renamed". For the image files that start with "test\_", the new names should omit "test\_3.6.7\_" from the beginning of the file names and ".txt" from within the file names. For the remaining files, omit the portion of the name that comes prior to the '-' character (and the '-' character itself).

    **Upload your shell script** to Bb Learn along with the Assignment Answer Sheet. 



## Extra fun

[Terminus game](http://web.mit.edu/mprat/Public/web/Terminus/Web/main.html)

[Command-line Murder Mystery](https://github.com/veltman/clmystery/)

Copyright (C) 2021  Jason Ladner

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.



