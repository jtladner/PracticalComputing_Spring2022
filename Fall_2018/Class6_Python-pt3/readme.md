# Class 6 - Oct. 5th 2018
- In this first class we will:
    - Learn how to load and use Python modules

### Required Reading (**Must be completed ahead of time**)
Practical Computing for Biologists, Chapter 12


### Exercises

1. We are only a few weeks away from starting the class hackathons. For the hackathons, we will divide into teams of 3-4 people. Use the standard Python module called [random](https://docs.python.org/2/library/random.html#module-random) to write a script that:

    1. Reads in a list of student names from a text file
    2. Randomly assigns students to a team 
    3. Saves the team assignments to a text file

Make sure that every student is assigned to a team, and that no students are assigned to more than one team.

2. The [glob module](https://docs.python.org/2/library/glob.html#module-glob) will allow you to use regular expressions to extract a list of filenames from your computer, just as you have done within your bash shell. Similarly, the [os module](https://docs.python.org/2/library/os.html#module-os) replicates a lot of the other functionality of the bash commands you've learned (e.g., creating/deleting files and directories). Use these two modules, in combination, to write a Python script that will accomplish all of the tasks outline in Exercises 2 and 3 from Class 3. 

3. The argparse module provides an easy way to parse arguments from the command line to be used within your script, and it also automatically generates a help menu for your script. Read through [this tutorial](https://docs.python.org/2/howto/argparse.html), and then use the argparse module to update your script from Exercise 1 so that the file with the list of student names and any other needed parameters can be provided directly on the command line when the program is executed (instead of being hard coded into the script). 

## Extra fun

[learnpython tutorial](https://www.learnpython.org/en/Modules_and_Packages)

Copyright (C) 2017  Jason Ladner

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



