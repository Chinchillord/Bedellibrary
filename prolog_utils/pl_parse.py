#
# Note: The dict format for Prolog rules should look something like:
#
# { "head" : pl_to_dict("p(x)"), "args" : [pl_to_dict("q(x)"), pl_to_dict("r(x)")] }
#
# and so a Prolog file is just paresed as a list of these

from functools import reduce
from typing import *
from dict_to_pl import pl_to_dict

def strip_whitespace(s : str) -> str:
    """ removes all whitespace from the string s. """
    return ''.join(s.split())


def parse_prolog_file(lines : [str]) -> [Dict[str, Any]]:
    """  """
    lines = strip_whitespace(lines)
    lines = reduce(lambda x, y: x+y, lines, "")
    statements = lines.split(".")
    return map(parse_prolog_statement, statements)


def parse_prolog_statement(s : str) -> Dict[str, Any]:
    """ Parses a single prolog statement into dict format.
        
        Example:
                          "p(x):-q(x),r(x)" 
                                 ~~>  
                    { "head" : pl_to_dict("p(x)"), 
                        "args" : [pl_to_dict("q(x)"),
                                   pl_to_dict("r(x)")] }
    """
    sep_index = s.find(":-")
    head = s[:sep_index]
    body = s[sep_index+2:]
    
    parsed_head = pl_to_dict(head)
    parsed_body = pl_to_dict(body)

    return { "head" : parsed_head, "args" : parsed_body }

