####################################
# parse_pdf_comments.py
#
####################################

#
# Note: the goal of this file is to extract all of the comments from a pdf file so that they can be stored as
# Prolog data. Comments should be uniquely identifiable, and this should not depend on the order in which they are created
# in the document. Comments should also have associated with them a *date* and *time* of creations.
#
# For instance, in prolog, this would look something like:
#
# text(comment_id, "This is text text of the comment that was extracted from the pdf.").
# time(comment_id, "13:42").      % NOTE: 24-hr format used internally for simplicity.
# date(comment_id, "2019-05-18"). % NOTE: Use ISO standard for dates.
# file(comment_id, file_id)       % file_id is the file the comment appears in
# page_number(comment_id, 4)      % This gives the page_number the comment appears on. 
#
# Note that *the file_id* together with the *comment_id* uniquely determine a given comment. Two comments
# from different files can have the same comment_id.
#
# Note: This doesn't have to nescesarialy be stored serially in this prolog format. We may want to use
# csv, or even a dedicated database for this purpose.
#
# TODO: For now, we can just focus on implementing extracting the actual data from the pdfs.
#

import PyPDF2
from PyPDF2 import PdfFileWriter
# all of these are potentially useful for interfacing with this library.
from PyPDF2.generic import createStringObject, NameObject, DictionaryObject


f = open("example.pdf", "rb")
out = open("output.pdf","wb")

writer = PdfFileWriter()
# writer.write(out) # -- to write to the file ``output.pdf''

pdf = PyPDF2.PdfFileReader(f)

page = pdf.getPage(0)
types = page["/Type"]
contents = page["/Contents"]
resources = page["/Resources"]
mediaBox = page["/MediaBox"]
parents = page["/Parent"]
annots = page["/Annots"]

def format_pdf_string_iso(s :str):
     return s[:4] + "-" + s[4:6] + "-" + s[6:8] \
        + "T" + s[8:10] + ":" + s[10:12]

for indirect in annots:
    annotation = indirect.getObject()
    if ("/Contents" in annotation):
        content = annotation["/Contents"]
    if ("/M" in annotation):
        timestamp = format_pdf_string_iso(annotation["/M"])
    print( content + " (Made at time: " + timestamp + ")")

    # e.x. -- modifying the metadata of a annotation with specific prolog
    # information:
    #    x = annots[1]
    #    x[NameObject("/PrologMetadata")] = createStringObject("test.")
    #    writer.write(out)

# Note -- everything here is mutable, so if we want to create a new pdf with
# our updated metadata, we just have to write our pdf to file.



# Note: It would be nice to have a way to distinguish between text comments
# and highlight comments. For the highlighted comments, it would be nice to be able to
# record what text has actually been highlighted.

# Note: We can look at '/Subtype' : '/Highlight' to determine if it is a highlight comment
# It doesn't look like you can extract the information of what has been highlighted from the
# pdf file -- at least not with how my 







