-- import Text.Parsec
import Text.ParserCombinators.Parsec
import Control.Monad
import Data.List
import Text.Parsec.Expr -- helper module to parse expressions

interleave :: [a] -> [a] -> [a] 
interleave xs ys = concat (transpose [xs, ys])

parsePrologTags :: GenParser Char st (PrologTerm Ids)
parsePrologTags = do
    _ <- oneOf "["
    _ <- oneOf "["
    text <- many $ noneOf "[]:"
    _ <- oneOf ":"
    _ <- optional $ many $ oneOf " "
    tag <- prologExpression
    _ <- optional $ many $ oneOf " "
    _ <- oneOf "]"
    _ <- oneOf "]"
    return tag

--prologExpression :: GenParser Char st (PrologTerm Ids)
--prologExpression = buildExpressionParser table prologTerm
--  where table = [binary "," (bin_op_and) AssocLeft,
--                 binary ";" (bin_op_or) AssocLeft]
--        bin_op_and p q = Predicate And [p,q]
--        bin_op_or  p q = Predicate Or  [p,q]
--        binary  name fun assoc = Infix (do{ oneOf name ; return fun }) assoc

-- Note: See https://wiki.haskell.org/Parsing_expressions_and_statements for an example
-- of how to properly do this.

prologExpression :: GenParser Char st (PrologTerm Ids)
-- Note: None of this currently takes into account operator
-- precedence.
prologExpression = chainl1 prologTerm ops
  where ops = do{ oneOf ","; return (bin_op_and)   }
          <|> do{ oneOf ";"; return (bin_op_or) }
        bin_op_and p q = Predicate And [p,q]
        bin_op_or  p q = Predicate Or  [p,q]

prologExpression'' :: GenParser Char st String
-- Note, this should convert a prolog expression
-- with infix operators into an honest-to-goodness prolog
-- term.
prologExpression'' = do 
  -- Note: this probably isn't very efficent
  args <- lookAhead $ prologTerm `sepBy` (oneOf ",;")
  let parse_ops = do
      _    <- prologTerm
      ops  <- (oneOf ",;") `sepEndBy` prologTerm
      return ops
  ops <- lookAhead parse_ops
  return $ show $ (ops, args)

prologTerm :: GenParser Char st (PrologTerm Ids)
prologTerm =  do
      (Predicate head _) <- prologPredicate
      let parse_args = optionMaybe $ do
          _     <- oneOf "("
          args  <- prologTerm `sepBy` (oneOf ",")
          _     <- oneOf ")"
          _     <-  optional (oneOf ".")
          return args
      output <- parse_args
      case output of
          Nothing -> return (Predicate head [])
          Just args -> return (Predicate head args)

prologPredicate :: GenParser Char st (PrologTerm Ids)
prologPredicate = try (do
    string <- many (noneOf ";,\n().")
    -- (eof >> return ' ') <|> (try $ noneOf "()")
    guard (string `elem` idenfitiers)
    case string of 
       "cat"      -> return $ Predicate Cat []
       "dog"      -> return $ Predicate Dog []
       "person"   -> return $ Predicate Person []
       "animal"   -> return $ Predicate Animal []
       "is_a"     -> return $ Predicate Is_a []
       "has_a"    -> return $ Predicate Has_a []
       "possibly" -> return $ Predicate Possibly []
       "self"     -> return $ Predicate Self []
       otherwise -> undefined) 
  <|> (do string <- many (noneOf "().")
          guard (string `elem` ["','","';'"])
          case string of
             "','" -> return $ Predicate And []
             "';'" -> return $ Predicate Or [])
  where idenfitiers = ["cat","dog","person","animal","is_a","has_a","possibly","','","';'","self"]

data Ids = Cat | Dog | Person | Animal | Is_a | Has_a | Possibly | And | Or | Self
  deriving (Eq, Enum)

data BaseType = Entity 
data TypeSig a = Type a | Fun (TypeSig a) (TypeSig a) 

arities :: Ids -> (Int -> Bool)
-- Takes an identifier and returns a function specifying whether or not 
-- a given function is a valid arity for the identifier 
arities Cat      = (==1)
arities Dog      = (==1)
arities Person   = (==1)
arities Animal   = (==1)
arities Is_a     = (==2)
arities Has_a    = (==2)
arities Possibly = (==1)
arities And      = (>=2)
arities Or       = (>=2)
arities Self     = (==0)

types :: Ids -> TypeSig BaseType
-- Assigns a list of possible type signatures to each prolog identifier
types = undefined

type_check :: PrologTerm Ids -> Maybe (TypeSig BaseType)
-- Takes a prolog expression and checks to see if it is well-typed. 
-- if so, returns the type of the given term.
type_check = undefined

instance Show Ids where
  show Cat      = "cat"
  show Dog      = "dog"
  show Person   = "person"
  show Animal   = "animal"
  show Is_a     = "is_a"
  show Has_a    = "has_a"
  show Possibly = "possibly"
  show And      = "','"
  show Or       = "';'"
  show Self     = "self"

-- Note: by default ',' and ';' are only defined in prolog as predicates of arity 2
-- but in our program we might decide to make these predicates of arity 3. 

data PrologTerm a = Predicate a [PrologTerm a]
  deriving (Show, Eq)
