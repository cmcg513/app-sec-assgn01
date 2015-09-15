# Secure Turing Complete Sandbox Challenge
# Assignment 1, Part 1
# Application Security CS-GY 4753
# Prof. Justin Cappos
# 
# Sandbox Source Code
# Author: Casey McGinley <cmm771>


import tokenize
import sys

print "<<<<<< Secure Turing Complete Sandbox >>>>>>"
print "Author: Casey McGinley <cmm771>\n"

# Program source code and data can only be read from a pre-ordained file
PROGRAM = "sboxed_program.lpy"
DATA = "sboxed_data.dat"

# A list of problematic keywords to be prevented from executing
BAD_KEYWORDS = ['import', 'exec', 'from', 'del']

try:
	# Open the data file and read it into memory prior to executing 
	# program source
	data_file = open(DATA, 'r')
	data_string = data_file.read()
	data_file.close()
except IOError:
	# If data file not found, display warning and proceed under the assumption
	# that any necesary data is included with program source
	print "----> No data file found. If separate data file is desired it must be named \'sboxed_data.dat\'."
	print "----> Proceeding without \'sboxed_data.dat\'."
	data_string = ""
except:
	raise

# Create a 'whitelist' dictionary of appropriate built-in functions and
# constants that the user may utilize in the program
GLOBAL_DICT = dict()
GLOBAL_DICT['int'] = __builtins__.int
GLOBAL_DICT['float'] = __builtins__.float
GLOBAL_DICT['bool'] = __builtins__.bool
GLOBAL_DICT['str'] = __builtins__.str
GLOBAL_DICT['list'] = __builtins__.list
GLOBAL_DICT['len'] = __builtins__.len
GLOBAL_DICT['long'] = __builtins__.long
GLOBAL_DICT['object'] = __builtins__.object
GLOBAL_DICT['chr'] = __builtins__.chr
GLOBAL_DICT['ord'] = __builtins__.ord
GLOBAL_DICT['range'] = __builtins__.range
GLOBAL_DICT['tuple'] = __builtins__.tuple
GLOBAL_DICT['False'] = __builtins__.False
GLOBAL_DICT['True'] = __builtins__.True
GLOBAL_DICT['None'] = __builtins__.None

# Add the data from 'sboxed_data.dat' so that the program may accessit 
# without file I/O
GLOBAL_DICT['__data__'] = data_string

# Remove the reference to the __builtins__ module; this module contains many 
# potentially dangerous functions including 'eval' and 'execfile'. Any 
# 'safe' and usefule functions/constants have been included above in the
# dict I've defined to be passed along to the execution environment.
GLOBAL_DICT['__builtins__'] = None

# We open the program and tokenize it. Note that this tokenizer utilizes
# the same parsing logic the Python interpreter itself relies on.
target_program = open(PROGRAM, 'r')
itr = tokenize.generate_tokens(target_program.readline)
tokens = [t[1] for t in itr]
target_program.close()

# Cycle through our banned statements/keywords
for kword in BAD_KEYWORDS:
	# If any token matches one of the banned keywords, the error is reported and 
	# an exception raised
	if kword in tokens:
		print "----> Illegal keyword used. Refer to README and below for further details."
		msg = "The keyword \'" + kword + "\' cannot be used in this sandbox."
		raise Exception(msg)

# We can now safely execute the file. If the program reached this point, then
# no 'blacklisted' keywords appeared in the program. We explicitly pass on 
# a dictionary for the global (and local as well, by default) names available
# in the execution environment. No functions or constants other than those 
# 'whitelisted' above will be accessible in the execution environment.
print "~~~~~~~~~~~~~~~~ ** START output ** ~~~~~~~~~~~~~~~~"
execfile(PROGRAM, GLOBAL_DICT)
print "~~~~~~~~~~~~~~~~~ ** END output ** ~~~~~~~~~~~~~~~~~"
