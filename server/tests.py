import unittest
import prolog_server
from flask_server import security_level_params

test_user_database = [{ "username" : "user1", "password" : "password1", "security_level" : SecurityLevel.Admin },
         { "username" : "user2", "password" : "password2", "security_level" : SecurityLevel.ReadOnlyUser },
         { "username" : "user2", "password" : "password2", "security_level" : SecurityLevel.ReadWriteUser }]

class FlaskServerSecurityTests(unittest.TestCase):
    """ """
    def test_run(self):


class PrologServerTests(unittest.TestCase):
    """ """
    def test_run(self):
