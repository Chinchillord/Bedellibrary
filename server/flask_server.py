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
# https://127.0.0.1:42069/query-api?pl_server_start=true&user=admin&password=password

# { "username" : "admin", "password" : "ayylmaothisismypassword", "security_level" : SecurityLevel.Admin }

import json
from flask import Flask, request
from enum import Enum
import urllib.parse # This is important for parsing data sent over http: urllib.parse.quote_plus("text")
from tinydb import TinyDB, Query
from flask import render_template, current_app
from prolog_server import PrologServer

class SecurityLevel(Enum):
    """ Classes of security privileges """
    Admin          = 0
    ReadOnlyUser   = 1
    ReadWriteUser  = 2
    
class AccessParameter(Enum):
    """ A list of all possible actions that users are allowed to take """
    start_server = 0
    stop_server = 1
    server_ontology_add = 2
    make_guarded_query = 3
    make_unrestricted_queries = 4
    server_fact_add = 5
    
# Define the actions that users at different security levels are allowed to use
security_level_params = { 0         : [e for e in AccessParameter], # Admin has all privileges
                          SecurityLevel.ReadOnlyUser  : [AccessParameter.make_guarded_query],
                          SecurityLevel.ReadWriteUser : [AccessParameter.make_guarded_query,
                                                         AccessParameter.server_ontology_add,
                                                         AccessParameter.server_fact_add] 
                        }


def get_user_database():
    """ """
    return TinyDB('users.json')
    
def user_and_pwd_in_dict(username : str, password : str, users) -> bool:
    for u in users:
        if (u["username"] == username) & (u["password"] == password):
            return True
    return False

def user_authorized(username : str, query_type : AccessParameter, users):
    user = next(x for x in users if x["username"] == username)
    security_level = user["security_level"]
    return query_type in security_level_params[security_level]

def exactly_one_true(bools : [bool]) -> bool:
    """ Returns true if and only if exactly one element of bools is true """
    return len(list(filter(lambda x: x, bools))) == 1

def run_request(server, p : AccessParameter):
    # Note: I might need to add more arguments to this function in order to get it to work.
    if p == AccessParameter.start_server:
        # Load master.pl for debugging purposes
        serverStarted = server.pl_server_start()
        if serverStarted:
            try:
                server.load_database_from_file("../prolog_utils/master.pl")
            catch:
            
            return json.dumps({"message" : "Prolog server started successfully."})
        else:
            return json.dumps({"error" : "Prolog server already started."})
        
    if p == AccessParameter.stop_server:
        server.pl_server_stop()
    if p == AccessParameter.server_ontology_add:
        return server.pl_server_ontology_add(request.args.get("pl_server_ontology_add"))
    if p == AccessParameter.make_guarded_query:
        query = request.args.get("pl_server_query")
        # if (sytax_ok(query)):
        return server.pl_server_query(query)
        # else:
        #    return json.dumps({"error" : "Syntax error: Malformed Prolog expression."})
        
        # For testing purposes:
        # if (query == "bool"):
        #    return json.dumps({ "query_result" : True })
        # else:
        #    return json.dumps({ "query_result" : ["book1","book2","book3","book4","book5"] })
    if p == AccessParameter.make_unrestricted_queries:
        print("make_unrestricted_queries")
        query = request.args.get("pl_server_query")
        return server.pl_server_query_direct(query)
    if p == AccessParameter.server_fact_add:
        server.pl_server_fact_add(request.args.get("pl_server_fact_add"))

app = Flask("Bedell library service") 
app.config['STATIC_FOLDER'] = "../../scratch/example_wiki/" 

def make_enum_md_list(header: str, content: [str]) -> str:
    """ Generates a markdown file with a header and an enumerated list """
    line_headings = map(lambda x: "  "+str(x)+". ",range(1,len(content)+1))
    result = header+"\n"
    for (head, line) in zip(line_headings, content):
        result += head + line + "\n"
    return result

def make_itemized_md_list(header: str, content: [str]) -> str:
    """ Generates a markdown file with a header and an unordered listk """
    result = header+"\n"
    for line in content:
        result += "  * " + line + "\n"
    return result

@app.route('/wiki/<path:subpath>')
def handle_server_request(subpath):
    message = "Hello, World"
    print(subpath)
    # Note: I think the only way this is going to work (unless I can figure out something else with 
    # flask is if we do something like:
    # if subpath == "index.html#!somethingdynamic.md"
    # # (actually, subpath.split("#!")[1].split(".")[0] in some_list_of_dynamic_pages)
    #     run procedure to generate semethingdynamic.md
    #     return current_app.send_static_file(subpath)
    return current_app.send_static_file(subpath)
    # return render_template('index.html')
    # Note: for an actual template, we can use e.x. render_template('index.html',message=message)

def to_bool(s):
    if s == "true":
        return True
    if s == "faslse":
        return False
    if s == None:
        return False
    return True
    
@app.route('/query-api')
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
    
    input_bool_args = [pl_server_start_request, pl_server_stop_request, pl_server_query_direct_request,
                       pl_server_query_request, pl_server_ontology_add_request, pl_server_fact_add_request]

    print(pl_server_query_request)
    # try:
    bool_args = list(map(to_bool, input_bool_args))
    # except Exception as e:
    # TODO: handle bad http request
    if (password is not None) & (user is not None) & exactly_one_true(bool_args):
        request_index = bool_args.index(True)
        the_request = AccessParameter(request_index)
        if user_and_pwd_in_dict(user, password, users) & user_authorized(user, the_request, users):
            return run_request(server, the_request)
    else:
        return json.dumps({"error" : "The conditions for making a valid query were not satisfied."})


if __name__ == '__main__':
    server = PrologServer()
    app.run(debug=True, port=42069, host='0.0.0.0')
    #app.run(debug=True, port=42069, ssl_context='adhoc', host='0.0.0.0') # run app in debug mode on port 42069
    #app.run(port=8000)
