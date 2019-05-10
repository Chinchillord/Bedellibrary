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
# time(comment_id, "13:42"). % NOTE: 24-hr format used internally for simplicity.
# date(comment_id, "2019-05-18"). % NOTE: Use ISO standard for dates.
#
# Note: This doesn't have to nescesarialy be stored serially in this prolog format. We may want to use
# csv, or even a dedicated database for this purpose.
#
# TODO: For now, we can just focus on implementing extracting the actual data from the pdfs.
#




