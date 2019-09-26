class Rel(signature: List[EntityType]) extends Identifiable[String] {                                                                                                                                        
  def facts: List[Any]                                                                                  
} 

trait Identifiable[A] {                                                                                 
  def primaryId:  A                                                                                     
  def rep: A => A                                                                                       
  def identities: List[A]                                                                               
}

class EntityType(primaryId: String) extends Identifiable[String] {                                      
  def identifies = List(pimaryId)                                                                       
  def rep        = (x : String) => x                                                                    
}

// A resource is something like a book, or an article, or a code snippet.
trait Resource[A] extends Identifiable[A] 

trait FrozenResource[A,T] extends Resource[A] {                                                         
  def data: T                                                                                           
  def timestamp: String                                                                                 
} 

// A resource that the user has annotated with some kind of annotation                                  
// For example, a frozen HTML page that we have highlighted something                                   
// in                                                                                                   
trait AnnotatedResource[A, Annot, T] extends FrozenResource[A,T] {                                      
  // Content of the annotation                                                                          
  def annotation: Annot                                                                                 
}

case class Person[A](                                                                                   
    name:       String,                                                                                 
    age:        Int,                                                                                    
    primaryId:  A,                                                                                      
    identities: List[A],                                                                                
    rep:        A => A                                                                                  
) extends Identifiable[A]                                                                               
                                                                                                        
case class Book[A](                                                                                     
    title:      String,                                                                                 
    authors:    List[Person[A]],                                                                        
    pages:      Int,                                                                                    
    sections:   List[Section[A]],                                                                       
    primaryId:  A,                                                                                      
    identities: List[A],                                                                                
    rep:        A => A                                                                                  
) extends Resource[A]

// Stuff for dealing with sections of a book.

sealed trait SectionType                                                                                
case object Section    extends SectionType                                                              
case object Chapter    extends SectionType                                                              
case object Subsection extends SectionType                                                              
                                                                                                        
case class Section[A](                                                                                  
    title: String,                                                                                      
    sectionType: SectionType,                                                                           
    belongsTo: Resource[A],                                                                             
    subsectionOf: Option[Section[A]],                                                                   
    primaryId: A,                                                                                       
    identities: List[A],                                                                                
    rep: A => A                                                                                         
) extends Identifiable[A]

// Stuff for interfacing with databases
sealed trait ContentType                                                                                
case object PDF extends ContentType                                                                     
case object Article extends ContentType                                                                 
case object Query extends ContentType                                                                   
                                                                                                        
sealed trait Note                                                                                       
case class Journal(id: Int, datetime: String, content: String) extends Note                             
case class PrologNote(id: Int, datetime: String, content: String) extends Note                          
// Note: In MySQL, contentType can be declared as an Enum                                               
case class WebNote(id: Int, contentType : ContentType, datetime: String, content: String)
