#
# flask_server.py
#
# #### Usage examples: #### 
#
# First off, we should be able to directly start and stop the service with out api
# (assuming the user has admin privileges):
#
#         /query?password=thisisthepassword?pl_server_start=true
#         /query?password=thisisthepassword?pl_server_stop=true
#
# We should also be able to have the ability to directly provide queries to the Prolog service.
# Note: for security reasons, this should only be available to admin users.
#
#                 /query?password=thisisthepassword?pl_server_query_direct="p(x)."
#
# The following should be available to users of all security levels. This should not allow commands like
# ``assert'' and the like. The code should probably only be executed if the Prolog file matches
# our relevant ontology.
#
#                 /query?password=thisisthepassword?pl_server_query="p(x)."
#
# The user should also be able to update the ontology with appropriate permissions.
#
#                 /query?password=thisisthepassword?pl_server_ontology_add="p : o."
#                 /query?password=thisisthepassword?pl_server_ontology_add="dog : entity -> o"
#                 /query?password=thisisthepassword?pl_server_ontology_add="p : o."?db="main"
#
# The user (with valid permissions) should alo be able to add Prolog facts to different databases 
#
#                 /query?password=thisisthepassword?pl_server_fact_add="p(x)."?db="main"
#
# Note: one useful feautre to have would be to have the user be able to "suppose" various facts. Rather than being
# added to specific files in the database, then, these facts are simply asserted.
#

# { "username" : "admin", "password" : "ayylmaothisismypassword" }

from flask import Flask, request
from enum import Enum
import urllib.parse # This is important for parsing data sent over http: urllib.parse.quote_plus("text")

class SecurityLevel(Enum):
    """ Classes of security privileges """
    Admin          = 1
    ReadOnlyUser   = 2
    ReadWriteUser  = 3
    
class AccessParameter(Enum):
    """ A list of all possible actions that users are allowed to take """
    start_server = 1
    stop_server = 2
    server_ontology_add = 3
    make_guarded_query = 4
    make_unrestricted_queries = 5
    server_fact_add = 6
    
# Define the actions that users at different security levels are allowed to use
security_level_params = { SecurityLevel.Admin         : [e for e in AccessParameter], # Admin has all privileges
                          SecurityLevel.ReadOnlyUser  : [AccessParameter.make_guarded_query],
                          SecurityLevel.ReadWriteUser : [AccessParameter.make_guarded_query,
                                                         AccessParameter.server_ontology_add,
                                                         AccessParameter.server_fact_add] 
                        }


def get_user_database():
    """ """
    return TinyDB('users.json')
    


app = Flask("Bedell library service") 

@app.route('/query')
def query():

    users = get_user_database()
    
    password = request.args.get('password')
    user = request.args.get('user')
    
    pl_server_start_request        = request.args.get('pl_server_start')
    pl_server_stop_request         = request.args.get('pl_server_stop')
    pl_server_query_direct_request = request.args.get('pl_server_query_direct')
    pl_server_query_request        = request.args.get('pl_server_query')
    pl_server_ontology_add_request = request.args.get('pl_server_ontology_add')
    pl_server_fact_add_request     = request.args.get('pl_server_fact_add')
    
    inputBoolArgs = [pl_server_start_request, pl_server_stop_request, pl_server_query_direct_request,
                     pl_server_query_request, pl_server_ontology_add_request, pl_server_fact_add_request]
    
    try:
        bool_args = map(to_bool, input_bool_args)
    except Exception as e:
        # TODO: handle bad http request
    
    if (password is not None) & (user is not None) & exactly_one_true(bool_args):
        # TODO: Check user privileges, preform the relevant action
        # if the user is allowed to.
    else:
        # TODO: do error handling


def pl_server_start():
    """ """
    prolog = Prolog()


def pl_server_stop():
    """ """


def pl_server_query_direct():
    """ """


def pl_server_query(query : str):
    """ """
    return prolog.query(query)


def pl_server_ontology_add():
    """ """


def pl_server_fact_add(query : str):
    """ """
    return db.add(query)


def pl_server_assert(query : str):
    """ """
    return prolog.assertz(query)


if __name__ == '__main__':
    app.run(debug=True, port=42069, ssl_context='adhoc') # run app in debug mode on port 42069
