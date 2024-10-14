import PyPDF2

with open('./pdfs/dummy.pdf', 'rb') as dummy:
    reader = PyPDF2.PdfFileReader(dummy)
    writer = PyPDF2.PdfFileWriter()
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer.addPage(page)

    with open('rotted_dummy', 'wb') as file:
        writer.write(file)