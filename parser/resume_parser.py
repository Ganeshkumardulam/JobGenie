import docx2txt
import fitz  # PyMuPDF
from fastapi import UploadFile

def parse_resume(file: UploadFile) -> str:
    content = ""
    if file.filename.endswith(".pdf"):
        doc = fitz.open(stream=file.file.read(), filetype="pdf")
        for page in doc:
            content += page.get_text()
    elif file.filename.endswith(".docx"):
        content = docx2txt.process(file.file)
    else:
        raise ValueError("Unsupported file format")
    return content.strip()
