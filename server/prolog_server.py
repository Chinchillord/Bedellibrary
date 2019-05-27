from tinydb import TinyDB, Query # Here we use tinydb for users for our flask server
from pyswip import Prolog
from typing import Any, Union

class PrologServer():
    def __init__(self):
        self.isRunning = False
        self.loaded_databases = []
        self.asserted_facts = []
        self.prolog = Prolog()
        
    def startServer(self) -> bool:
        """ Start the server if it is not already running. Returns true if 
            server started successfully, returns false otherwise. """
        if self.isRunning == False:
            self.prolog = Prolog()
        	self.isRunning = True
        	return True
        else:
            return False
        
    def restartPrologServer(self):
        """ """
        self.prolog = Prolog()
        
    def loadDatabase(self, database : Dict[str, Any]) -> Bool:
        """ """
        if isRunning:
            # TODO: implement this
        else:
            return False
        
    def closeDatabase(self, database) -> bool:
        """ """
        if isRunning:
        	for fact in database:
        	    self.prolog.retract(fact)
        	self.loaded_databases.remove(database)
        	
        	return True
        else: 
            return False
        
    def stopServer(self) -> Bool:
        """ """
        if self.isRunning:
            self.prolog = None
            return True
        else:
            return False
