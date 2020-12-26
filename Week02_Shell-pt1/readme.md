# Week 2 - Jan. 22nd 2021
- In this class we will:
    - Learn to use the shell/terminal to interact with your computer

### Required Reading (**Must be completed ahead of time**)
Practical Computing for Biologists, Chapters 4-5

### Basic shell configuration instructions

1. Open your command line interface and confirm that you are in your home directory by typing the command:

```pwd```

   - For **Mac** users, the reponse should be similar to the following with 'uname' replaced with your username:

```/Users/uname```

   -   For **Linux/Windows** users, The reponse should be similar to the following with 'uname' replaced with your username:

```/home/uname```

   -   If you're not in the right place, or you're not sure, execute the following command ("~" is a shortcut for your home directory):

```cd ~/```

   - The following will also work because if you don't specify a location, the default for cd is to move to your home directory:

```cd```


2. **Linux/Windows users only.** Open your .bash_profile in a terminal-based text editor. This command will create the file if it doesn't exist:  

```nano .bash_profile```

   - Add the following lines of code and save your changes. These will ensure that commands within .bashrc will also be run when only your .bash_profile is executed:

```
if [ -f ~/.bashrc ]; then
   source ~/.bashrc
fi
```


3. Open your .bash_profile (Mac) or .bashrc (Linux/Windows) file for editing.

   - For **Mac** users, if you've installed the bbedit command line tools use the following command to open your .bash_profile in bbedit (This command will create the file if it doesn't exist):

```bbedit .bash_profile```

   - Alternatively use this command to open your .bash_profile in a terminal-based text editor (This command will create the file if it doesn't exist):

```nano .bash_profile```

   - For **Linux/Windows**, open your .bashrc file instead (This command will create the file if it doesn't exist):

```nano .bashrc```


4. Add the following lines of code and save your changes:

```
set -o noclobber

# For incremental search capabilities
bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'

# Add time stamp to bash history
HISTTIMEFORMAT="%d/%m/%y %T "
```


5. In order to execute the newly added commands for use in your current session, run the following command from the terminal window:

   - **For Mac users:**
```source .bash_profile```

   - **For Linux/Windows users:**
```source .bashrc```


6. To test that noclobber is working as expetced, run the following two commands in succession:

```
touch test.txt
cat test.txt >test.txt
```


   - You should receive the following message: 

```-bash: test.txt: cannot overwrite existing file```


7. To test the incremental search capabilities, type the letter 's' and hit the up arrow. This should bring up the 'source' command you entered in step 4, as opposed to the last 'cat' command. 


8. To test the history time stamps, execute the following command, which will print the last 10 commands to the screen.:
```history | tail -n 10```

   - In addition to seeing the command number prior to the actual command, you should also see the date and time the command was run. 

9. **Mac users only.** In order to install the ```rename``` command, you must first install [homebrew](https://brew.sh/). Then run the following command:

```brew install rename```

10. **Mac users only.** Check to see if ```curl``` is installed using ```which curl```. If it isn't, install using homebrew:

```brew install curl```



### Exercises

For today's execises, you should work in the shell within the 'sandbox' directory, which is located within the GitHub directory for this week's class ('Class2_Shell-pt1'). To get there, use the 'cd' command. For example, on my computer, I would use the following:

```cd /Users/jtladner/Documents/GitHub/Courses/PracticalComputing/Fall_2018/Class2_Shell-pt1/sandbox```

Once there type ```ls -1``` and you should see the following list of files and directories:

```
bunchoffiles
structure_hidden.pdb
```

1. Use the ```man``` command to learn more about ```head``` and ```tail```. 
The file 'structure\_hidden.pdb' has 9291 lines. You can check this using the command:
```wc -l structure\_hidden.pdb```

    1. Rewrite the command above, specifying an absolute path for 'structure_hidden.pdb' (hint: use ```pwd```)

    2. Now, use a combination of ```head``` and ```tail```, within a single command in order to view **ONLY** lines 4532-4539 of 'structure_hidden.pdb'.

    3. Design a simple ```grep``` command that will generate the same output generated in the previous step

2. Use ```ls``` to look inside 'bunchoffiles'. This directory contains 100 files. All are plain text files, but they have three different file extensions. 

    1. Make a directory named 'halfthefiles' and then, with a single command, move all of the files with a .txt file extension to this new folder. 
    
    2. Use ```cat``` to concatenate all of the .txt files (now in 'halfthefiles') into a single file called "all.txt". Generate this file within the main sandbox directory.
    
    3. Count the number of lines in 'all.txt' and the original .txt files to verify that the concatenation worked properly.
    
    4. Delete the 'halfthefiles' directory, including all of the indiviudal .txt files. 
    
    5. Use ```ls``` to look at the remaining files in 'bunchoffiles'. Use a combination of ```ls``` and ```grep``` to count the number of files with each file extension.
    
    6. When the files were generated, a typo resulted in many of the files being named with the string 'tres' instead of 'trees'. Use ```rename``` to correct this mistake for all files with a single command.

3. In this exercise, you will use ```curl``` to download a file from the internet and then explore and manipulate those files through the command line.
    
    1. Use  ```curl``` to download a fasta file with betalactamase sequences from NCBI (ftp://ftp.ncbi.nlm.nih.gov/pathogen/betalactamases/Allele-dna.fa).
    
    2. Use ```less``` to take a look at the file contents and familiarize yourself with the fasta file format. 
    
    3. Use ```grep``` to count the number of sequences in this file (**NOT the number of lines!**)
    
    4. How many of the sequence names start with 'AA'?
    
    5. How many sequence names end with '0'?
    
    6. Using ```head```, ```grep``` and some trial and error, generate a new fasta file containing the first 500 sequences. **Make sure you include the entire 500th sequence**

4. Use the ```history``` command to generate a text file that includes all of the commands that you used for exercises 1-3.

## Extra fun

Explore for "extra credit" or in the event that you finish all of the other exercises.

[Cmd Challenge](https://cmdchallenge.com)



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



