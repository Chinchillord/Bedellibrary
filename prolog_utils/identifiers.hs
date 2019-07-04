module Bedelllibrary.Data.Identifier (
	Identifier
        makeIdentifier
) where

-- Note: The identifier type can be modified during run-time. 

import Control.Monad.Reader

validIdentifiers :: Reader [String] ()
validIdentifiers = pure []

makeIdentifier :: Reader [String]
