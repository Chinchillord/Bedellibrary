#######################################################################################################################
# query_filesystem.py
#
# Sends out (natural language? prolog?) queries to the semantic filesystem, calling if necessary utility functions
# to generate prolog output from source (i.e. pdf, md, tex) files.
#
# I also have some methods here for *modifying* the ontology, as well as for giving *explanations* for the
# queries. The explanation bit should probably be implemented in Prolog.
#
#######################################################################################################################

from pyswip import Prolog
# TODO: How do we import python files from other parts of our project directory here?
# I'm not sure if what I have below is the right syntax.
# from Bedelllibrary.nat_lang_tools.prolog_to_text import toText
# from Bedelllibrary.nat_lang_tools.parse_queries import *

def prologQueryFilesystem(query : str) -> Iterator[str]:
    """ Sends out a plain prolog query to the filesystem """
    # Pseudocode:
    # if query in pdf_path:
    #    for file in pdf_path:
    #        Prolog.consult(file)
    # if query in tex_path:
    #    for file in tex_path:
    #         Prolog.consult(file)
    # if query in md_path:
    #    for file in md_path:
    #         Prolog.consult(file)
    #
    # return Prolog.query(query)

def natLangQueryFilesystem(query : str) -> str:
    """ Sends out a plain prolog query to the filesystem, and generates
        a natural language response. """
    # Basic implementation -- this will need to change
    return prologQueryFilesystem(toText(query))

def updateOntology(request : str):
    """ Should be called when a user makes a request to modify the ontology. Note that some ontologies
        (such as basic_ontology.pl) should probably be marked as *immutable* -- whereas other ontologies
        can be modified. This (whether or not an ontology can be modified by user requests) should in
        general be specified in a configuration file. """

def explainQueryResults(query : str) -> str:
    """ Takes a natural language query, and produces a natural language output explaining
        how the result of this query was arrived at. """
    # NOTE: This should probably be implemented in terms of a simpler function, for instance,
    # a function that produces a *trace* of the relevant query results.