
-- Problem statement:
--   We have 
--
--

-- utility function
enumValues :: (Enum a) => [a]
enumValues = enumFrom (toEnum 0)

-- "a" here is the type of predicate identifiers, whereas
-- "b" is the type of term identifiers
data PrologTerm a b = Predicate a [b]

type RawPrologTerm = PrologTerm String String

head :: PrologTerm a b -> a
head (Predicate x ys) = x

body :: PrologTerm a b -> [b]
body (Predicate x ys) = ys

class (Show a, Enum a, Show b, Enum b) => Schema a b where
   conj :: a
   disj :: a
   typeid :: a -> Bool
   
   types :: [a]
   relns :: [a]

   typeOf :: b -> a

data MySchema =
    Type MySchemaType
  | Pred MySchemaPred

data MySchemaType = 
    String
  | Bool
  | List MySchemaType
  | Person
  | ProgrammingLanguage
  | ProgrammingLanguageLibrary

data MySchemaPred =
    Name
  | String
  | Age
  | CreatedOn
  | LastModified
  | LanguagesUsedIn

class (Show a, Enum a) => PrologPredicateSchema a where
   conj :: a
     -- such that "show conj == ","" 
   disj :: a
     -- such that "show disj == ";""

   -- a predicate to determine if a type is a type identifier or not
   typeid :: a -> Bool
   
   -- list of all types
   types :: [a]
   types = filter typeid enumValues
   
   -- list of all relations
   relns :: [a]
   relns = filter (not . typeid) enumValues

class (Show b, PrologPredicateSchema a) => PrologTermSchema a b where
   typeOf :: b -> a
   -- associates with each term a unique type identifier
       