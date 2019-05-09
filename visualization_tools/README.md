# About this project

This is an ambitious and multi-faceted (currently unnamed!) project that aims to provide
 a number of simple, inter-connected, open-source tools for the assistance of research and the
 organization of knowledge. This was motivated by one of the author's own frustrations with both
 traditional (paper) note-keeping, as well as with existing proprietary solutions such as Mendeley.
 
 This project is currently in active development, so stay tuned for more updates, as well as
 specifications for the desired behaviour of our application, and example use-cases.  
 
 ## Sub-projects:
 
 ### A simple semantic filesystem based on Prolog
 
 As a part of our framework, we will develop a simple, extensible semantic file system based
 on associating information to files via Prolog knowledge bases. For example, associated with
  `\sfilesys\directory\example.pdf ` is a Prolog file `\sfilesys\directory\.example.pdf.pl`
  containing semantic tags associated with the file `example.pdf`.
  
 Although this filesystem will play an integral role to the other components of our system, we also 
 hope to provide a simple command line interface to this component directly, so that it can be used 
 on its own.
 
 ### Semantic document annotations in Prolog
 
 A number of different document types that one comes across during research, such as pdf and tex files
 will be supported, in which the user can directly make annotations which will be indexed by the 
 semantic file system, and accessible via Prolog queries

 
 ### Simple Prolog and natural language based interfaces
 
 We would like to eventually support integration with an AI personal assistant,
  such as [Mycroft](https://github.com/MycroftAI) or [Zamia](https://github.com/gooofy/zamia-ai).
 However, both direct Prolog and text-based natural language inputs will also be supported. This
 is where most of the use cases of our project all come together. For instance, one might imagine the user
 of this software (eventually) making queries such as:
 
    * "Mycroft, what was the quote that I liked about paraconsistent logic that I read a few
     months ago?"
    * "Mycroft, list me some of the papers related to categorical quantum mechanics that I have 
       in my library of pdfs."
    * "Mycroft, copy the bibtex reference of this paper."
 
  
 ### Visualization tools for ontologies
 
 Somewhat orthogonal to the ideas listed above, I'd also like to be able to provide some visualization
 tools for the ontologies that are curated through the use of a system such as this one. For example:
    
    * "Mycroft, display some of the relationships between homotopy type theory and logic that I've 
       found in my personal library."
       
 imagining a tool similar to [philosophies.space](http://philosophies.space/).
 
 ### The interface between formal and "informal" ontologies
 
 Further reading:
 
 * [English as a formal language](https://philpapers.org/rec/MONEAA-2)
 * [The mathematics of sentence structure](https://www.tandfonline.com/doi/abs/10.1080/00029890.1958.11989160?journalCode=uamm20)
 * [Knowledge representation in bicategories of relations](https://arxiv.org/pdf/1706.00526.pdf)
 * [Toward formalizing ologs](https://arxiv.org/pdf/1503.08326.pdf)
 
 #### Disclaimer:
  This project is currently in its experimental/prototype stages. However, we would very much like to have this project
  polished up and production-ready one day. The end goal is to have this goal to be as accessible
  as possible -- thus, we welcome any suggestions/contributions.