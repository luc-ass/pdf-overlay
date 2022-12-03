import comtypes.client
import os
import pathlib
import json
import hashlib

word_PDF_format = 17

DOC_FOLDER = "./Dokumente/"


def convert_to_pdf(doc_folder: str) -> None:
    file_list = [(str(file_path.absolute()), str(file_path.with_suffix(".pdf").absolute())) for file_path in pathlib.Path(doc_folder).glob('**/*.[dD][oO][cC][xX]')]

    word = comtypes.client.CreateObject("Word.Application")
    word.Visible = False

    curr_files = {}
    file_db_exists = os.path.exists(f"{doc_folder}/file_hashes.json")
    if file_db_exists:
        with open("file_hashes.json", "r") as file:
            _prev_files = json.load(file)

    for input_file, output_file in file_list:
        checksum = hashlib.md5(open(input_file, "rb").read()).hexdigest()
        curr_files[input_file] = checksum
        if file_db_exists and os.path.exists(output_file):
            if _prev_files[input_file] == checksum:
                continue
        doc = word.Documents.Open(input_file)
        doc.SaveAs(output_file, FileFormat=word_PDF_format)
        doc.Close()

    word.Quit()

    with open("file_hashes.json", "w") as file:
        json.dump(curr_files, file, sort_keys=True, indent=4)


if __name__ == "__main__":
    convert_to_pdf(DOC_FOLDER)
