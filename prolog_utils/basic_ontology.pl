%
% basic_ontology.pl
%
% This file defines some of the basic ontological notions that our knowledge 
% representation engine will use.
%

:- module(basic_ontology).
:- use_module(utils).

% # Entities
% To begin, we define a number of different *entities*. These are all different
% sorts of external resources that might be relevant to the researcher using 
% the library. These different classes of entities are relevant, because
% different entities have different types of data associated with them.

entity(thesis).
entity(article).
entity(book).
entity(volume).
entity(webpage).

% Subtyping is relevant here, as some categories are more or less specific
% than other categories. For instance, a thesis is essentially a specail type
% of article, so we can say:

is_a(thesis, article).

% # topics
% Another important relation in our knowledge representation engine is an
% entity being about a topic. First, we list a few examples of *topics* below:
 
topic(category_theory).
topic(logic).
topic(intro_category_theory).
topic(2_category_theory).
topic(double_category_theory).
topic(higher_category_theory).
topic(security).
topic(formal_theorem_proving).
topic(programming_languages).
topic(philosophy).
topic(epistemology).
topic(metaphysics).
topic(foundations_of_mathematics).
topic(intuitionism).
topic(relevant_logic).
topic(paraconsistent_logic).
topic(sheaf_theory).
topic(topological_data_analysis).
topic(constructive_analysis).

% Again, here the sub-typing relation is relevant -- perhaps more relevant than for entities. For instance:

is_a_subtopic_of(intuitionism, mathematics).
is_a_subtopic_of(relevant_logic, logic).
is_a_subtopic_of(logic, mathematics).

% # Relatedness
% One topic can also be *related to* another topic. Thus, we have 
% another relation for just this. The user of our framework can define
% *atomic* relationships between different topics or concepts either
% by stating this as a plain fact, *or*, by providing an additional
% explanation by using a third argument:

arelated_to(epistemic_logic, security,"Epistemic logic can be used to characterize security protocols.").

% From this *atomic* related_to relation, we can construct its symmetric,
% transitive, and reflexive closure, closed under sub-typing:

related_to(X,Y) :- 
	poset_closure(arelated_to,X,Y). 


% is_a(mathematical_object, entity).

