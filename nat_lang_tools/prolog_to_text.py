############################################################
# prolog_to_text.py
#
############################################################


def to_text(s : str) -> str:
    """ Convert a prolog predicate """
    # TODO: I still need this to handle cases like
    # "is_a(full, property(functors))."
    # -> "fullness is a property of functors."
    # This needs a lot of work.
    s = s.strip() # Strip whitespace
    head, uargs = s[:-2].split("(",1) # Strip ). at the end of the predicate
                                      # and split up the head and the arguments
	args = uargs.split(",") # split into individual arguments
    head = head.replace("_", " ")
    return args[0].capitalize() + " " + head + " " + args[1] + "."
