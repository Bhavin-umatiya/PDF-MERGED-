from pypdf import PdfMerger
import os

pdfs =["sample.pdf","sample.pdf"]  # PDF NA NAME CHE

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merger.pdf")
merger.close()


