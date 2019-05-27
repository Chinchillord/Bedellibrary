from typing import Dict, Union, Any, Optional

# represents the prolog term k(p(x),q(x)).
testd = {'head': 'k',
           'args' : [{'head' : 'p', 'args' : [{'head' : 'x'}]},
                     {'head' : 'q', 'args' : [{'head' : 'y'}]}
                    ]
        }

def format_args(args : [str]) -> str:
    """ Helper function to format a list of arguments as a 
        string of comma seperated characters """
    x = args[0]
    for i in args[1:]:
        x += ","
        x += i
    return x

def dict_to_pl(d : Dict[str, Any]) -> Optional[str]:
    """ Takes a dictionary representation of a prolog term
        and converts it to a nested string representation. """
    head = d["head"]
    try:
        args = d["args"]
    except KeyError as e:
        return head
    else:
        return (head + "(" + format_args(list(map(dict_to_pl, args))) + ")")
            

def pl_to_dict(s : str) -> Optional[Dict[str, Any]]:
    """ Parse prolog facts into dict format so that they can be stored in a database. """
    # Find the outermost pair of parentheses
    i1 = s.find("(")
    # i2 = s.find(")") # This is wrong
    i2 = -1
    # Find the right paren matching the paren at index i1:
    i = 1 # set a index for the signed number of left/right parens
    for j in range(i1+1,len(s)):
        if s[j] == "(":
            i += 1
        if s[j] == ")":
            i -= 1
        if i == 0:
            i2 = j
            break
    
    # If nothing to parse, then we are done.
    if ((i1==-1) and (i2==-1)):
        return {"head" : s}

    # Do exception handling here 
    if ((i1==-1) ^ (i2==-1)):
        raise Exception("Parse error: Found open/closed without matching closed/open parenthesis.")
    # if (i2 != len(s)):
    #    raise Exception("Parse error: Closing parenthesis not in correct position.")

    # Find the relevant components of the string 
    head = s[:i1]
    body = s[i1+1:i2]
    args = body.split(",")
    
    # recurse by parsing all of the sub-strings
    return { "head" : head, "args" : list(map(pl_to_dict, args)) }
    
    
     
