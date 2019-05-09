####################################################################
# process_latex.py
#
# A basic script to compile latex source code while in addition 
# parsing the prolog comments from the latex source code.
#
####################################################################

import sys
import os

if __name__ == '__main__':
	# TODO: The following line won't work -- we need to first strip
	# our LaTeX document of all [[ ]] tags
	os.system('pdflatex ' + sys.argv[1] + '.tex')
	# TODO: Consider allowing command line arguments for which 
	# LaTeX compiler to use -- i.e. pdflatex, lualatex, etc...
	# as well as passing on additional arguments to these
	# commands.
	os.system('python basic_tex_parser.py ' + sys.argv[1] + '.tex ' \ 
	           + sys.argv[1] + '.kb.pl')
	os.system('rm *.aux & rm *.log')

