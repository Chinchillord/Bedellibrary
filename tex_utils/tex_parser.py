#############################################################################
# tex_parser.py
# 
# Utility functions for processing latex files with embedded prolog comments.
#
#############################################################################

import sys
import re


def parse_tags(s : str) -> List[str]:
	""" Given a string s, returns the list of everything between [[ ]]
		brackets. """
	return re.findall('\[\[(.*?)\]\]',s)


def parse_line_comments(file : Iterator[str]) -> List[str]:
	""" Takes a file, inputed as a stream of lines,
	    and returns a list of all lines starting with %%
	    -- which should be interpreted as statements in prolog """
		tags = []
		for line in file:
			tags + parseTags(line)
		return tags

			
def refresh_tex_comments(infile : str, outfile : str):
    """ takes a tex file *infile*, and a prolog file *outfile*, and
        updates *outfile* with all of the new prolog annotations in
        *infile*.

        Note: To make the algorithm more efficent, there should be a
        cannonical order for extracted prolog comments, for instance:
            * Extracted in-line annotations
            * Extracted line annotations
        (delimited by comments in the prolog source file for clarity)
        where in each section, the comments are listed in the order that
       they appear in the document. """

        # Generate a list of line_comments in the text, in order.
        line_comments = []
        with open(infile) as input_file:
            for line in input_file:
                if line[0:2] == '%%':
                    line_comments + line[3:]
        			
        # Generate a list of in-line comments in the text, in order.
        inline_comments = parseLineComments(input_flile)
        
        # Update the output file
        with open(outfile, 'w+') as output_file:
            # if outputfile not created:
				# create outputfile
				# format outputfile
			# if outputfile not in correct format
				# return error
			# else:
				# Find delimiters in the file for where the line comments
				# and the inline comments start and end
				inline_comments_start = None
                inline_comments_end = None
                line_comments_start = None
                line_comments_end = None
                # update-in-place the inline comments
                    # ... TODO
				# update-in-place the line comments
                    # ... TODO
					
if __name__ == "__main__":
    refresh_tex_comments(sys.argv[1], sys.argv[2])
