data EntityCommand : List (String, VarType) -> Type where
  NOP : EntityCommand []
  NewEntity : (cmds : EntityCommand xs) -> (s : String) -> EntityCommand (xs ++ [(s, Entity)])
  NewDatasource : 
        (cmds : EntityCommand xs) 
     -> (s : String)
     -> (field : ToyObjectFields)
     -> (IO (assocType field))
     -> EntityCommand (xs ++ [(s, Datasource)])
  Sequence : 
       EntityCommand xs
    -> EntityCommand ys
    -> {auto p : Disjoint xs ys}
    -> EntityCommand (xs ++ ys)
  RemoveEntity : 
        (cmds : EntityCommand xs) 
     -> (s : String)
     -> {auto p : Elem s (map fst xs)}
     -> EntityCommand (?remove s xs)
  MakeQuery : 
        (cmds : EntityCommand xs)
     -> (s : ValidEntityRef xs)
     -> ToyObjectFields
     -> EntityCommand xs
