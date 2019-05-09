%
% utils.pl
%
% Contains various useful prolog utilities that will be used
% in this project.
%

:- module(utils).

% Construct the transitive closure of a given relation.
transitive_closure(R,X,Y) :- 
	R(X,Y).
transitive_closure(R,X,Z) :- 
	R(X,Y), R(Y,Z).
	
% Construct the reflexive closure of a given relation.
reflexive_closure(R,X,Y) :- 
	R(X,Y).
reflexive_closure(R,X,X).

% Construct the symmetric closure of a given relation.
symmetric_closure(R,X,Y) :-
	R(X,Y).
symmetric_closure(R,X,Y)) :-
	R(Y,X).

% Construct the least poset containing a given relation R.
poset_closure(R,X,Y) :-
	R(X,Y).
poset_closure(R,X,X).
poset_closure(R,X,Z) :-
	R(X,Y), R(Y,Z).
