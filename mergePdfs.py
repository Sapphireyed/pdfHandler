import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdfs):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)

    merger.write('super.pdf')
    merger.close()

pdf_combiner(inputs)