"""
    This tool is used to merge content onto a stationary.
    It will do this for the first page.

    Help with fitz: https://documentation.help/PyMuPDF/tutorial.html

    Install fitz: `pip install pymupdf`
    On Apple arm64 this builds the package, which requires swig:
        `brew install swig`
"""
import fitz
import glob

# configure the path to your stationary
STATIONARY =    "./Briefkopf/Briefkopf.pdf"
DOC_FOLDER =    "./Dokumente/"
OUTPUT_FOLDER = "./PDF/"

# retrieve all *.pdf files from DOC_FOLDER and subdirecories
content_files = glob.glob(DOC_FOLDER+"*.pdf" , recursive=True)

# iterate files and merge
for content_file in content_files:
    
    # open both files
    stat = fitz.open(STATIONARY)
    cont = fitz.open(content_file)

    # iterate pages
    page = stat.load_page(0) # index 1/0?
    page_front = fitz.open()
    page_front.insert_pdf(cont, from_page=1, to_page=1)
    page.show_pdf_page(page.rect, page_front, pno=0, keep_proportion=True, overlay=True, oc=0, rotate=0, clip=None)

    # output file name and dir
    result_file = content_file.replace(DOC_FOLDER, OUTPUT_FOLDER)
    print(result_file)

    stat.save(result_file)