"""
    This tool is used to merge content onto a stationary.
    It will do this for the first page.

    Help with fitz: 
    https://documentation.help/PyMuPDF/tutorial.html
    https://pymupdf.readthedocs.io/en/latest/page.html

    Install fitz: `pip install pymupdf`
    On Apple arm64 this builds the package, which requires swig:
        `brew install swig`
"""
import fitz
import os


# configure the path to your stationary
STATIONARY =    "Briefkopf/Briefkopf.pdf"
DOC_FOLDER =    "Dokumente/"
OUTPUT_FOLDER = "PDF/"


# retrieve all *.pdf files from DOC_FOLDER and subdirecories
content_files = [file.path for file in os.scandir(DOC_FOLDER) if file.name.endswith(".pdf")]

print(content_files)

# iterate files and merge
for content_file in content_files:
    
    doc1 = fitz.open(content_file)
    doc2 = fitz.open(STATIONARY)

    page = doc1.load_page(0)
    page_front = fitz.open()
    page_front.insert_pdf(doc2, from_page=0, to_page=0)
    page.show_pdf_page(page.rect, page_front, pno=0, keep_proportion=True, overlay=True, oc=0, rotate=0, clip=None)

    # output file name and dir
    result_file = content_file.replace(DOC_FOLDER, OUTPUT_FOLDER)
    
    # create output directory if not exists
    if not os.path.exists(OUTPUT_FOLDER):
        os.mkdir(OUTPUT_FOLDER)

    doc1.save(result_file, encryption=fitz.PDF_ENCRYPT_KEEP)