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


content_files = []
output_dirs = [OUTPUT_FOLDER] # add base dir to list

# retrieve all *.pdf files and directories/subdirectories from DOC_FOLDER
for root, dirs, files in os.walk(DOC_FOLDER):
    for name in files:
        if name.lower().endswith(".pdf"):
            content_files.append(os.path.join(root, name))
    for name in dirs:
        output_dirs.append(str.replace(os.path.join(root, name), DOC_FOLDER, OUTPUT_FOLDER))

print(content_files)
print(output_dirs)

# create missing folders from list
for directory in output_dirs:
    if not os.path.exists(directory):
        os.mkdir(directory)

# iterate files and merge
for content_file in content_files:
    
    cont = fitz.open(content_file)
    stat = fitz.open(STATIONARY)

    page = cont.load_page(0)
    page_front = fitz.open()
    page_front.insert_pdf(stat, from_page=0, to_page=0)
    page.show_pdf_page(page.rect, page_front, pno=0, keep_proportion=True, overlay=True, oc=0, rotate=0, clip=None)

    # output file name and dir
    result_file = content_file.replace(DOC_FOLDER, OUTPUT_FOLDER)

    cont.save(result_file, encryption=fitz.PDF_ENCRYPT_KEEP)