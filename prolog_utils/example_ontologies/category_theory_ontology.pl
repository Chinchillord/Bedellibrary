%
% category_theory_ontology.pl
%

:- module(category_theory_ontology).

is_a(faithful, property(functors)).
is_a(full, property(functors)).
is_a(injective, property(morphisms)).
is_a(epimorphic, property(morphisms)).

is_a(category, mathematical_structure).
is_a(category, essentially_algebraic_structure).
has_a(category, ob_set).
has_a(C, hom_set(X,Y)) :- in(X,Y,ob_set(C)).

