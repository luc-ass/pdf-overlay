# ๐ pdf-overlay
This small tool merges a stationary pdf ontop of the first page of a content-pdf. It has been built to combine content files with a letterhead. This enables you to update the letterhead of files much faster.

## Usage
### โ๏ธ Installation
On Windows systems download the pdf-overlay.exe into a folder. The folder structure should now look something like this:
```
working_dir/
โโโ Briefkopf/
โ   โโโ Briefkopf.pdf
โโโ Dokumente/
โ   โโโ Input_PDF_1.pdf
โ   โโโ Input_PDF_2.pdf
โโโ PDF/
โโโ pdf-overlay.exe
```
Things you need to know:
1. `./Briefkopf/Briefkopf.pdf` is a fixed name. You should not rename this.
2. `./Dokumente` is a fixed folder name. It should not be changed. Within this folder all subdirectories and PDFs are processed.
3. `.PDF` and neccesary subdirectories are automatically created if they do not exist when the program is run. Existing PDFs will be overwritten.
### ๐งช DEV
The following is only needed if you are developing...

```sh
# Only needed on Apple/arm_64 architecture as pymupdf does not have a corresponding wheel and will build using swig
brew install swig

# install (and build) PyMuPDF
pip3 install pymupdf
```
### Edit configuration within main.py
### Run Script
`python3  main.py`

