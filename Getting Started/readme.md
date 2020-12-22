# Tasks to be completed before the first class
- This document outlines several tasks that should be completed **before** our first meeting, including:
    - Completing the pre-course survey
    - Setting up a GitHub account and cloning the course repository
    - Installing a plain text editor
    - Ensuring you have access to a command-line interface

## 1. Complete the pre-course survey
- A quick survey to help me gauge your level of experience and interest in the topics that will be covered.
- You can access the survey [here](http://nau.co1.qualtrics.com/jfe/form/SV_1OeGOgNC5d4KMex)

## 2. GitHub
- GitHub is a web-based hosting service used primarily for open-source software development, but which can also be used to host additional content
- All of the materials for this class, including exercise instructions and files will be hosted on GitHub.
- The easiest way to access files for the class will be to clone a copy of the course repository onto your laptop. To do this, please follow these steps:
    1. If you don't already have one, sign up for a **free** GitHub account [here](https://github.com/)

- If you are a Mac or Windows user:
    1. Download and install the [GitHub Desktop client](https://desktop.github.com/). This will include signing into your GitHub account. 
    2. Sign into your GitHub account within your internet browser
    3. Open the [Courses repository](https://github.com/jtladner/Courses) within your browser.
    4. Click on the green "Clone or download" box on the right side of the screen and then choose "Open in Desktop". At this point, you will need to choose a location on your personal computer to locally store your copy of the repository. The default name of the repository directory will be 'Courses'.
    5. To update the contents of this directory to match the online version (e.g., to download new files that have been added), simply select "Courses" as your "Current Repository" within the Desktop Client (upper left) and then select "Pull origin" (upper right). If there are no updates available you will not see a "Pull origin" option. Instead you will see "Fetch origin", which will look for differences between your local copy and the online repository.

- If you are a Linux user, you will need to clone the repository from the command line:
    1. Open a terminal window and check that you have git installed by running the command:
    ```
    which git
    ```
    If git is installed, this command will return the location of the git executable. If you get an error, follow the instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install git.
    
    2. Make a directory to hold your git repositories and change into this directory. For example:
    ```
    mkdir ~/GitHub
    cd ~/GitHub
    ```
    
    3.  Clone the repository from github
    ```
    git clone https://github.com/jtladner/Courses.git
    ```
    
    This clones the repository and all of the files contained within, as well as the git history of the repository.
    
    4. To get updates from the repository, change into the repository root directory and execute the git command 'pull':
    
    ```
    cd Courses
    git pull
    ```
    

## 3. Download a powerful plain text editor
- For this course, you will need a plain text editor with support for regular expressions. There are several different options for different operating systems, but I make some recommendations below (all are free to download)
- For Mac I suggest the **free version** of [BBEdit](https://www.barebones.com/products/bbedit/). This free version is roughly equivalent to TextWrangler, which is used in the PCfB book. If you are downloading the program for the first time, they will provide you a trial version of the full BBEdit, but you can continue to use the editor with a limited set of functions after this period. This "limited" set of functions will likely still be sufficient for the majority of your uses.
    - You should also consider installing the bbedit command line tools. These will allow you to open text files in bbedit directly from your Terminal window. If you downloaded BBEdit from the link provided above, you can install these from within the BBEdit program by first selecting "BBEdit" from the menus bar at the top of your screen and then selecting "Install Command Line Tools...". Otherwise, if you installed the program through the Mac App store utilized this [installer](https://www.barebones.com/support/bbedit/cmd-line-tools.html)
- For Windows, I suggest [Notepad++](https://notepad-plus-plus.org/)
- For Linux, there are many options, but I have had a good experience with [Komodo Edit](https://www.activestate.com/komodo-edit)

## 4. Ensure that you have access to a command-line interface
- Mac and Linux users do not need to do anything. There is a terminal application built into these operating systems, which provides a command-line interface. 
- For Windows users, there are a few different options:
    1. For Windows 10 users, follow these [instructions](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/) to install the bash terminal
    2. For other Windows operating systems, you have two options. Appendix 1 in the PCfB book walks through these options in more detail (though the instructions may be somewhat outdated):
        1. Install [Cygwin](http://www.cygwin.com/)
        2. Install Linux (e.g., [Ubuntu](https://www.ubuntu.com/) or [CentOS](https://www.centos.org/)) within a virtual machine (e.g., [VirtualBox](https://www.virtualbox.org/))
     

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