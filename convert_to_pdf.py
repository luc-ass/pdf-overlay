import comtypes.client
import os
import pathlib

word_PDF_format = 17

DOC_FOLDER = "./Dokumente/"


def convert_to_pdf(doc_folder: str) -> None:
    file_list = [(str(file_path.absolute()), str(file_path.with_suffix(".pdf").absolute())) for file_path in pathlib.Path(doc_folder).glob('**/*.[dD][oO][cC][xX]')]

    word = comtypes.client.CreateObject("Word.Application")
    word.Visible = False

    for input_file, output_file in file_list:
        doc = word.Documents.Open(input_file)
        doc.SaveAs(output_file, FileFormat=word_PDF_format)
        doc.Close()

    word.Quit()


if __name__ == "__main__":
    convert_to_pdf(DOC_FOLDER)
