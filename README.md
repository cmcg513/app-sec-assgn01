# app-sec-assgn01
Secure Turing Complete Sandbox Challenge
Assignment 1, Part 1
Application Security CS-GY 4753
Prof. Justin Cappos

README
Author: Casey McGinley <cmm771>

My sandbox utilizes Python. As per the instructions, a Makefile has been included, but as I am using Python, it has been left blank. My sandbox code relies on Python 2.7, the default distribution on Ubuntu 12.X and on most systems.

My sandbox is run with the following command:

python sbox.py

Programs and data to be used in my sandbox must be stored under two pre-ordained file names:
	- sboxed_program.lpy
	- sboxed_data.dat
If the user wishes to keep program source code and data together in a single file, then only 'sboxed_program.lpy' is needed. The sandbox can funtion without an existing 'sboxed_data.dat' file, but NOT, of course, without an 'sboxed_program.lpy' file.

My two example programs are stored in a sub-directory called 'examples'. Neither of my examples rely on a separate data file. Thus, from the current directory (that of sbox.py and this README) example #1, the powers of 2 from 1 to 128, can be run as follows:
	> cp examples/example1.lpy sboxed_program.lpy
	> python sbox.py
The 2nd example, the first 10 Fibonnaci numbers would be run much the same way:
	> cp examples/example2.lpy sboxed_program.lpy
	> python sbox.py

Additonally, to demonstrate how my sandbox might be used with a separate data file, I've included a slight variation on my code for the first example, where the limit of 128 for the powers of 2 is stored separately in a data file. Here, we would run it as follows:
	> cp examples/example1_withdatfile.lpy sboxed_program.lpy
	> cp examples/example1.dat sboxed_data.dat
	> python sbox.py

For any clarification of my logic, please refer to the inlcluded PDF "(Casey McGinley) Writeup.pdf"