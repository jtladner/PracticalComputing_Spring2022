# Class 4 - Sept. 21st 2018
- In this class we will learn:
    - about three different ways to run Python code
    - to use strings, integers and floating point numbers in Python
    - how to write and execute a custom Python script

### Required Reading (**Must be completed ahead of time**)
Practical Computing for Biologists, Chapters 7-8

[Jupyter Notebook Tutorial](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook)

### Exercises

1. Use Jupyter Notebook to open "PythonPt1-Class4.ipynb". This notebook will introduce you to the Python syntax for strings, integers and floating points. Read through each cell of the notebook and execute the contained code using "control+enter" or by pressing the play button at the top of the Notebook. Four of the cells contain exercises to complete. Enter your code for each exercise directly within the notebook cells describing the exercises. However, feel free to also make changes to the code contained in the other cells to further explore Python's syntax. 

2. Open your terminal and enter the interactive Python shell (the command ```python``` should do the trick). 
    1. One potential use for this interface...a handy calculator! Quick, what's 346783/87268939? Does the result look different from what you expected? Don't forget about the difference between floats and integers. 
    2. The other reason this interface is really useful is as a test bed, to make sure that commands work as you expect before adding them to your script. One topic that wasn't covered in exercise 1 is how to extract substrings from a string in python. This is done with the use of brackets (e.g., string[:4], string[1:-1]). Using the interactive shell, create your own string variable, and then use it to experiment with this syntax for substring extraction. 

3.  Now that you're familiar with the python syntax for strings, integers and floats, it's time to write a python script contained within a text file for execution within your bash shell. Your script should 1) take as input a DNA sequence provided by the user (see ```raw_input``` example in PCfB p. 137-139), 2) calculate and report the GC content of the sequence (i.e., % of total bases that are G or C) and 3) generate the reverse complement of the provided sequence. 

- The reverse complement of a DNA sequence is formed by reversing the letters and interchanging A and T and interchanging C and G. Thus the reverse complement of ACCTGAG is CTCAGGT.

- Hint: [to reverse a string](https://stackoverflow.com/questions/931092/reverse-a-string-in-python)

## Extra fun

[Python Challenge](http://www.pythonchallenge.com/)

Copyright (C) 2018  Jason Ladner

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



