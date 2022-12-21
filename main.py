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
from pathlib import Path
import re
from convert_to_pdf import convert_to_pdf

# configure the path to your stationary
STATIONARY =      "Briefkopf/Briefkopf.pdf"
BACKSIDE_CT =     "Briefkopf/CT_Rückseite.pdf"
BACKSIDE_MRT =    "Briefkopf/MRT_Rückseite.pdf"
HEADER_HERZBILD = "Briefkopf/Briefkopf_Herzbild.pdf"
DOC_FOLDER =      "Dokumente"
OUTPUT_FOLDER =   "PDF"

# convert .docx files in DOC_FOLDER to .pdf
convert_to_pdf(DOC_FOLDER)

content_files = [(path, Path(str(path).replace(DOC_FOLDER, OUTPUT_FOLDER))) for path in Path(DOC_FOLDER).glob("**/*.pdf")]

stat = fitz.open(STATIONARY)
backside_CT = fitz.open(BACKSIDE_CT)
backside_MRT = fitz.open(BACKSIDE_MRT)
header_herzbild = fitz.open(HEADER_HERZBILD)

# iterate files and merge
for input_path, output_path in content_files:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    cont = fitz.open(input_path)

    page = cont.load_page(0)
    page_front = fitz.open()
    if re.match(".*HerzBild", input_path.stem):
        stat = header_herzbild
    page_front.insert_pdf(stat, from_page=0, to_page=0)
    page.show_pdf_page(page.rect, page_front, pno=0, keep_proportion=True, overlay=False, oc=0, rotate=0, clip=None)

    # only add second page if not already exists
    if cont.page_count == 1:
        if re.match(r"^Aufkl.rung_CT", input_path.stem):
            cont.insert_pdf(backside_CT)
        elif re.match(r"^Aufkl.rung_MRT", input_path.stem):
            cont.insert_pdf(backside_MRT)

    cont.save(output_path, encryption=fitz.PDF_ENCRYPT_KEEP)
