from tinydb import TinyDB, Query # Here we use tinydb for users for our flask server
from pyswip import Prolog
from typing import Any, Union, Dict

class PrologServer():
    def __init__(self):
        self.is_running = False
        self.loaded_databases = []
        self.asserted_facts = []
        self.prolog = Prolog()
        
    def pl_server_start(self) -> bool:
        """ Start the server if it is not already running. Returns true if 
            server started successfully, returns false otherwise. """
        if not self.is_running:
            self.prolog = Prolog()
            self.is_running = True
            return True
        else:
            return False
        
    def restart_prolog_server(self):
        """ """
        self.prolog = Prolog()

    def load_database_from_file(self, database_path : str) -> bool:
        if self.is_running:
            self.prolog.consult(database_path)
            return True
        else:
            return False
    def load_database(self, database : Dict[str, Any]) -> bool:
        """ (I'm honestly not sure what I had in mind with this) """
        if isRunning:
            return False
            # TODO: implement this
        else:
            return False
        
    def close_database(self, database) -> bool:
        """ """
        if self.is_running:
            for fact in database:
                self.prolog.retract(fact)
            self.loaded_databases.remove(database)
        	
            return True
        else: 
            return False
        
    def pl_server_stop(self) -> bool:
        """ """
        if self.is_running:
            self.prolog = None
            return True
        else:
            return False

    def pl_server_query_direct(self):
        """ """
        return self.prolog.query(query)

    def pl_server_query(self, query: str):
        """ """
        return self.prolog.query(query)

    def pl_server_ontology_add(self, s : str):
        """ """


    def pl_server_fact_add(self, query : str):
        """ """
        return self.db.add(query)


    def pl_server_assert(self, query : str):
        """ """
        return self.prolog.assertz(query)
