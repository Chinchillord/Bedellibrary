import Data.Text
import Data.Bson
-- import Database.MongoDB
-- import Data.Aeson.Bson -- convert from Bson to Aeson
-- package aeson-bson -- lets the user convert between aeson and bson formats.
-- package aeson-pretty -- allows one to pretty print aeson

-- playing around and some examples of the Data.Bson package

document :: Document
document = [pack "label" := val "key-value"]


value :: Maybe Value
value = look (pack "label") document

data PrologTerm a = Predicate a [PrologTerm a]
  deriving (Show, Eq)

ex_term = Predicate "loves" [Predicate "Nate" [], Predicate "Cat" []]

-- Note, this should be the same representation of prolog terms that I have been using 
-- in Python.
to_document :: Val a => PrologTerm a -> Document
to_document (Predicate x []) = 
    [ pack "head" := val x,
      pack "args" := val ([] :: [Value]) ]
to_document (Predicate x args) =
    [ pack "head" := val x,
      pack "args" := val (Prelude.map to_document args) ]                            
