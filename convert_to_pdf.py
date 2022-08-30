import comtypes.client
import os

word_PDF_format = 17

DOC_FOLDER = "Dokumente/"


def scantree(path):
    """Recursively yield DirEntry objects for given directory."""
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)
        else:
            yield entry


def convert_to_pdf(doc_folder: str) -> None:
    input_file_list = [file.path for file in scantree(doc_folder) if file.name.lower().endswith(".docx")]
    file_list = [(file_path, file_path.replace("docx", "pdf")) for file_path in input_file_list]

    word = comtypes.client.CreateObject("Word.Application")

    for input_file, output_file in file_list:
        doc = word.Documents.Open(input_file)
        doc.SaveAs(output_file, FileFormat=word_PDF_format)
        doc.Close()

    word.Quit()


if __name__ == "__main__":
    convert_to_pdf(DOC_FOLDER)