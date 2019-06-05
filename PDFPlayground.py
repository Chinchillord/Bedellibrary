import PyPDF2

f = open("example.pdf", "rb")

pdf = PyPDF2.PdfFileReader(f)

page = pdf.getPage(0)
types = page["/Type"]
contents = page["/Contents"]
resources = page["/Resources"]
mediaBox = page["/MediaBox"]
parents = page["/Parent"]
annots = page["/Annots"]

for indirect in annots:
    annotation = indirect.getObject()
    if ("/Contents" in annotation):
        print(annotation["/Contents"])

