data Concept = Concept {
  primary_identifier :: String,
  
}

-- Note: For the sake of seperation of concerns, we should sepearate a master
-- ontology (for instance, sepcified in LambdaProlog), from how facts about this
-- ontology are stored, and how to query facts about this ontology.
about :: Concept -> Concept -> o.

-- Perhaps, by using the same names as in our ontology schema, we can automatically 
-- conncet our ORM to our schema, e.x, given an ontology:

ontology {
  Concept : Type.
  Topic : Type.
  description : Topic -> String.
  description : Concept -> String.
  primary_identifier : Concept -> String.
  about : Concept -> Topic -> o.
}

we could then specify the Haskell type

data Concept = Concept {
  primary_identifier :: String,
  about :: Topic
}

data Topic = Topic {
  primary_identifier :: String,
  description :: String
}

to explain how this data is stored. 

Idea: But, instead of this, we could have a notion of a *relationally dependent tuple*, e.x.

type Tup = (c : Concept, description c, about c)

which is implicitly converted to something like:

type Tup' = (Concept, String, Topic)

In other words, what I'm proposing here is something like *semantically enriched types*.

Is it possible to have something like this notion of semantically enriched types in Idris, Caledon,
Lambda Prolog?

I'm not sure, but I think this is an important concept.

Also, I think there's something about this which is inherently somehwhat object-oriented in nature -- We're looking at objects as individual concepts that can change over time and evolve, rather than a specific data type -- and we can have different semantic information associated with an object. So, perhaps a language like Scala might be a good choice of implementaton for this? For instance, annotations might be good for this, but I'm not sure how something like this would be possible e.x.
in Haskell. Perhaps with phantom types and type erasure (and implicits?) something like this might
be possible in Idris.

