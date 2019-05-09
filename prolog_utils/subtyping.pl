%
% subtyping.pl
%

% One feature of knowledge representation that I would like to implement ix 
% the notion of *subtyping*.

% The following states that the is_a predicate is a *transitive*, *reflexive*,
% and symmetric relation -- i.e. a poset:

:- module(subtyping).

is_a(X,X).
is_a(X,Z) :- is_a(X,Y), is_a(Y,Z).
is_a(X,Y) :- is_a(Y,Z). 

