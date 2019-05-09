###############################################################################
# process_prolog_comments.py
#
# Command line utility for parsing the prolog comments from tex scource code.
# Prolog source code will be extracted from both line comments starting with 
# %%, as well as in-between [[ ]] brackets.
# 
# See example.tex for a simple test document. Since [[ ]] are not valid
# inline tex comments, these have to be parsed out in order to properly
# compile the latex source. This can be accomplished by the process_latex.py
# script in this same directory.
#
###############################################################################

from tex_parser import *

if __name__ == "__main__":
	refreshTexComments(sys.argv[1], sys.argv[2])
