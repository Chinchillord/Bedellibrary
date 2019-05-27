from functools import reduce
from pl_parse import parse_prolog_file

def parse_pl_type(s : str) -> str:
    """  """
    s = strip_whitespace(s)
    i1 = s.find(":")
    term = s[:i1]
    type_sig = s[i1+1:]
    type_sig = type_sig.split("->")
    
def type_check(pl_source_path : str, schema_path : str) -> bool:
    """ Takes a prolog file with path pl_source_path and checks to see whether or not
        all the data in the file typechecks with respect to the schema at schema_path """
    schema = parse_pl_type(open(schema_path))
    facts = parse_prolog_file(open(pl_source_path))
    # TODO: implement this
    
