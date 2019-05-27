import unittest
from dict_to_pl import pl_to_dict, dict_to_pl

class TestDictPlParser(unittest.TestCase):
    """ Tests the basic functionality of the function 
        dict_to_pl """
    def test_run(self):
        return

class TestPlDictParser(unittest.TestCase):
    """ Tests the basic functionality of the function
        pl_to_dict """
    def test_run(self):
        test_cases = [ ({'head': 'k',
                          'args' : [{'head' : 'p', 'args' : [{'head' : 'x'}]},
                                    {'head' : 'q', 'args' : [{'head' : 'y'}]}
                                   ]}, "k(p(x),q(y))") ]
        for test in test_cases:
            self.assertEqual(dict_to_pl(test[0]),test[1])

class TestPlDictInverse(unittest.TestCase):
    """" The functions pl_to_dict and dict_to_pl
         should be inverse. """
    def test_run(self):
        test_cases = ["p(x)", "q", "abcd(efg,hijk)", "s(s(z))",
                      "is_a(document, kind_of(file))", 
                      "p(x)."]
        for test in test_cases:
            self.assertEqual(test, dict_to_pl(pl_to_dict(test)))

class TestPlParseFiles(unittest.TestCase):
    """ Tests the basic functionality of parse_prolog_file """
    def test_run(self):
        return

if __name__ == '__main__':
    unittest.main()
