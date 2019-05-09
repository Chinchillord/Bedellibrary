%
% algebraic_ontology.pl
%

:- module(algebraic_ontology).

is_a(monoid,    algebraic_structure).
is_a(semigroup, algebraic_structure).
is_a(group,     algebraic_structure).
	is_a(group, monoid).
	is_a(monoid, semigroups).
is_a(ring,      mathematical_structure).
is_a(field,     mathematical_structure).

is_a(field, ring).

% some examles of groups.
is_a(s_3, group).
is_a(s_4, group).
is_a(dih3,). % Group of symmetries of a triangle.
is_a(dih4,). % Group of symmetries of a square.
is_a(s_n, fam(group)). % S_n is a family of groups consisting of...
is_a(freegrp, fam(group)). % The free groups on some set is a family of groups...
