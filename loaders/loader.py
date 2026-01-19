from pathlib import Path
from pypdf import PdfReader

def load_documents(folder):
    texts = []
    for file in Path(folder).glob("*.pdf"):
        reader = PdfReader(file)
        for page in reader.pages:
            if page.extract_text():
                texts.append(page.extract_text())
    return texts
