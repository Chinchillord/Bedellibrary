# Idea: For running our various data processing procedures (e.x. extracting all of the prolog
# comments from a pdf), we will want to keep track somewhere of *when these actions were last preformed*
# and compare that with the *date last modified* of each of the files to determine when 
# to re-run our data processing procedures.

# Note: Files should have simple, and unique Prolog identifiers, we'll need a simple way of handling this.
# -- maybe this can be extracted somehow from file names/title descriptions?

import os
from pyswip import Prolog

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
	    
def initalizeDirectory(filetypes : [str], dir : str):
	""" Initialize a directory by creating .file_DATA directories for all files 
	    with extension in *filetypes* which are (recursively) in directory *dir* """
	# TODO: I'm not sure if this works, needs to be tested.
	# We'll definitely want to use some libraries for file path manipulation here
	# (if they exist).
	for root, dirs, files in os.walk(dir):
		for file in files:
			if file.extension() in filetypes:
				# Create the required directory
				os.mkdir("." + file_name(file) + "_DATA")
				# Create the required files
				open("." + file_name(file) + "_DATA/data.pl", 'a').close()
				open("." + file_name(file) + "_DATA/config.yaml", 'a').close()
				
def loadFileOntology():
	""" loads the basic file system ontology into memory in pyswip at dir. For instance,
		this allows one to query:
			? title(file_id, X).
			? file_path(file_id, X).
			? date_modified(file_id, X).
			...etc 
		(TODO: more examples) """
		
def addTagToFile(tag : str, filepath : str):
	""" Adds a tag to the file given by *filepath* """
	
	# Check to see if file has already been initialized
	# If not, initialize if
	
	# If tag is not already contained in filepath/.file_DATA/data.pl, append it
	# to the end of the file.
	return None
