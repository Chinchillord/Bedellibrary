# Idea: For running our various data processing procedures (e.x. extracting all of the prolog
# comments from a pdf), we will want to keep track somewhere of *when these actions were last preformed*
# and compare that with the *date last modified* of each of the files to determine when 
# to re-run our data processing procedures.

# Note: Files should have simple, and unique Prolog identifiers, we'll need a simple way of handling this.
# -- maybe this can be extracted somehow from file names/title descriptions?

def rqueryBasedOnTags(tags : List[str], dir : str) -> Iterable[str]:
	""" Takes a list of tags and a directory, and recrusively
	    searches through all subdirectories of dir to find 
	    the files matching all of the given tags. """
	    
def matchesTags(tags : List[str], filepath : str) -> bool:
	""" Takes a list of tags and a filepath, and checks to see if 
	    the file matches all of the given tags. """
	
	# e.x. a prolog query might look like:
	# has_tag(X, intuitionistic_logic).
	# 
	# but in the filesystem itself, we have a list of *tag* predicates that get interpreted
	# as has_tag(X,t), where X is the file associated to the prolog knowledge base in question.

def semanticQuery(query : str, dir : str):
	""" Takes a prolog query and a directory, and recrusively
	    searches through all subdirectories of dir to find 
	    the files satisfying the prolog query. """
	    
	    # Example:
	    #    query = relatedTo(X, intuitionistic_logic), relatedTo(X, category_theory).
	
def matchesQuery(query : str, filepath : str) -> bool:
	""" Takes a prolog query, and a filepath, and returns whether or not
	    the given file matches the prolog query. """
