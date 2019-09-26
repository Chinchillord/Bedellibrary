module Entities where

data Animal = Animal {
  age :: Int,
  weight :: Double,
  name :: String
} -- Note: Instead of a source-to-source translation, we could do: deriving(Entity).
  -- which would produce:

data AnimalE = AnimalE {
  ageQ :: Maybe Int,
  weightQ :: Maybe Double,
  nameQ :: Maybe String
} 

data Entity = EAnimal

data Prop a b where
  Age    :: Prop Animal Int
  Weight :: Prop Animal Double
  Name   :: Prop Animal String

-- Example

bob = AnimalE {
  ageQ = Just 15,
  weightQ = Just 57,
  nameQ = Just "Bob"
}
