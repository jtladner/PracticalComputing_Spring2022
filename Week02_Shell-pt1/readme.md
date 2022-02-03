# Week 2 - Jan. 21st 2022
- In this class we will:
    - Learn to use the shell/terminal to interact with your computer

### Required Reading (**Must be completed ahead of time**)
Practical Computing for Biologists, Chapters 4-5

### Prep for next class

If you're using a Mac and you haven't installed the Xcode command line tools, follow the instructions [here](https://macpaw.com/how-to/install-command-line-tools#)

### Basic shell configuration instructions

1. Open your command line interface and, just for fun, use it to see whether bash configuration files already exist on your computer. These files should be stored in your home directory, which can be accessed using ```~``` as a shortcut. So, type the following to view all the files present in your home directory:

```ls -la ~/```

   - Do you see ```.bash_profile``` or ```.bashrc``` or ```.zshrc```? If so, take a look at what's inside using ```less```. For example:
   
   ```less  ~/.bash_profile```
   
   - **Note 1**: You can exit ```less``` by typing ```q```.
   
   - **Note 2**: It's fine if you don't already have copies of these files. The commands in step two will open existing files or create new files, if they don't already exist. 
   

2. **Linux/Windows users only.** Open your .bash_profile in a terminal-based text editor. This command will create the file if it doesn't exist. For example:  

```nano ~/.bash_profile```

   - Add the following lines of code and save your changes. These will ensure that commands within .bashrc will also be run when only your .bash_profile is executed:

```
if [ -f ~/.bashrc ]; then
   source ~/.bashrc
fi
```


3. Open your .bash_profile or .zshrc (Mac) or .bashrc (Linux/Windows) file for editing.

   - For **Mac** users, if you've installed the bbedit command line tools use the following command to open your configuration file in bbedit (This command will create the file if it doesn't exist):

```bbedit ~/.bash_profile```

or

```bbedit ~/.zshrc```


   - Alternatively use this command to open your configuration file in a terminal-based text editor (This command will create the file if it doesn't exist):

```nano ~/.bash_profile```

or

```nano ~/.zshrc```


   - For **Linux/Windows**, open your .bashrc file instead (This command will create the file if it doesn't exist):

```nano ~/.bashrc```


4. Add the following lines of code and save your changes:

   - For **Bash** users:

```
set -o noclobber

# For incremental search capabilities
bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'

# Add time stamp to bash history
HISTTIMEFORMAT="%d/%m/%y %T "
```

   - For **Zsh** users:

```
set -o noclobber

# For incremental search capabilities
bindkey '\eOA' history-beginning-search-backward
bindkey '\e[A' history-beginning-search-backward
bindkey '\eOB' history-beginning-search-forward
bindkey '\e[B' history-beginning-search-forward
```


5. In order to execute the newly added commands for use in your current session, run the following command from the terminal window:

   - **For Mac users:**

```source ~/.bash_profile```

or

```source ~/.zshrc```


   - **For Linux/Windows users:**

```source ~/.bashrc```


6. To test that noclobber is working as expetced, run the following two commands in succession:

```
touch test.txt
cat test.txt >test.txt
```


   - You should receive the following message: 

```-bash: test.txt: cannot overwrite existing file```


7. To test the incremental search capabilities, type the letter 's' and hit the up arrow. This should bring up the 'source' command you entered in step 4, as opposed to the last 'cat' command. 


8. For **Bash** users, test the history time stamps by running the following command, which will print the last 10 commands to the screen:

```history | tail -n 10```

   - In addition to seeing the command number prior to the actual command, you should also see the date and time the command was run. 

   - **For Assignment: Copy and paste the last five commands from your history into the Assignment Answer Sheet.**
   
   **Note**: Zsh users, use ```fc -li``` intead of history to grab your commands for the answer sheet.

9. **Mac users only.** In order to install the ```rename``` command, you must first install [homebrew](https://brew.sh/). Then run the following command:

```brew install rename```

10. **Mac users only.** Check to see if ```curl``` is installed using ```which curl```. If it is, the location of the program will be printed to the screen. If it isn't, nothing will be printed to the screen. If you need to, you can install ```curl``` using homebrew:

```brew install curl```



### Assignment

For today's assignment, you should work in the shell within a copy of the 'Assignment' directory, which is located within the GitHub directory for this week's class (```Week02_Shell-pt1```). To get there, use the 'cd' command. For example, on my computer, I would use the following:

```cd ~/Documents/GitHub/PracticalComputing_Spring2022/Week02_Shell-pt1/Assignment```

Once there type ```ls -1``` and you should see the following list of files and directories (```-1``` results in contents being presented, one per line, but without the extra info you get with ```-l```):

```
bunchoffiles
structure_hidden.pdb
```

1. Parsing ```structure_hidden.pdb```

    1. Use one of the commands we covered today to determine the number of lines contained in ```structure_hidden.pdb```. Generate two different versions of this command, one using a relative file path and the other using an absolute file path. **Enter both commands AND the # of lines in the Assignment Answer Sheet.**

    2. Use a combination of ```head``` and ```tail```, within a single command in order to view **ONLY** lines 4532-4539 of ```structure_hidden.pdb```. **Enter the command you used AND lines 4532-4539 in the Assignment Answer Sheet.**

    3. Design a simple ```grep``` command that will generate the same output generated in the previous step (i.e., display lines 4532-4539 only). (hint: compare the content on lines 4532-4539 to the rest of the file). **Enter your command in the Assignment Answer Sheet.**
    
    4. Use the ```man``` command to learn about other options that can be used with ```grep```. Two particularly useful options specify a number of "context lines" to report (-A and -B). These context lines are lines that occur before or after any line that matches the query. Design a command that uses a combination of these options to generate the same output that was generated in the two previous steps (i.e., display lines 4532-4539 only). **Enter your command in the Assignment Answer Sheet.**

    5. ```.pdb``` is a file format used to describe the 3D structures of molecules held in the [Protein Data Bank](https://www.rcsb.org/). Each line that starts with ```ATOM``` describes the spatial coordinates of an atom that is part of the protein. How many atoms are part of the protein structure described in ```structure_hidden.pdb```? **Enter the command you used and the number of atoms in the Assignment Answer Sheet.**

2. Exploring ```bunchoffiles```

    1. Using the commands you've learned, explore the contents of the ```bunchoffiles``` directory. As you will see, this directory contains files with multiple different file extensions. Count the number of files with each file extension and **enter this info AND the commands used in the Assignment Answer Sheet.**

    2. Make a directory named 'halfthefiles' and then, with a single command, move all of the files with a .txt file extension to this new folder. **Enter all of the commands used in the Assignment Answer Sheet.**
    
    3. Use ```cat``` to concatenate all of the .txt files (now in 'halfthefiles') into a single file called "all.txt". Generate this file within the main Assignment directory. **Enter the command used in the Assignment Answer Sheet.**
    
    4. Count the number of lines in 'all.txt' and the original .txt files to verify that the concatenation worked properly. **Enter the number of lines in "all.txt" and the command used in the Assignment Answer Sheet.**
    
    5. Delete the 'halfthefiles' directory, including all of the indiviudal .txt files. **Enter the commands used in the Assignment Answer Sheet.**
    
    6. Use ```ls``` to look at the remaining files in 'bunchoffiles'. When the files were generated, a typo resulted in many of the files being named with the string 'tres' instead of 'trees'. How many files were impacted by this mistake? **Enter the number and the command used in the Assignment Answer Sheet.**
    
    7. Use ```rename``` to correct this mistake for all files with a single command. **Enter the command used in the Assignment Answer Sheet.**

3. In this exercise, you will use ```curl``` to download a file from the internet and then explore and manipulate that file through the command line.
    
    1. Create a directory called ```betalactam``` and move into this directory. **Enter the commands used in the Assignment Answer Sheet.**
    
    2. Use  ```curl``` to download a fasta file with betalactamase sequences from NCBI (ftp://ftp.ncbi.nlm.nih.gov/pathogen/betalactamases/Allele-dna.fa). **Enter the command used in the Assignment Answer Sheet.**
    
    3. Use ```less``` to take a look at the file contents and familiarize yourself with the fasta file format (**Note: a single sequence can span multiple lines**). 
    
    4. Count the number of sequences in this file (**NOT the number of lines!**). **Enter the number of sequences and command used in the Assignment Answer Sheet.**
    
    5. How many of the sequence names start with 'AA'? **Enter the number of sequences and command used in the Assignment Answer Sheet.**
    
    6. How many sequence names end with '0'? **Enter the number of sequences and command used in the Assignment Answer Sheet.**
    
    7. Using ```head```, ```grep``` and some trial and error (i.e. multiple commands while changing parameters) determine how many lines you need to cover the first 500 sequences. Then generate a new fasta file containing the just the first 500 sequences. (**Make sure you include the entire 500th sequence**). How many **lines** are contained in this new files? **Enter the number of lines and command used in the Assignment Answer Sheet.**


## Extra fun

Explore for "extra credit" or in the event that you finish all of the other exercises.

[Cmd Challenge](https://cmdchallenge.com)

[Additional configuration suggestions](https://natelandau.com/my-mac-osx-bash_profile/)


Copyright (C) 2022  Jason Ladner

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



