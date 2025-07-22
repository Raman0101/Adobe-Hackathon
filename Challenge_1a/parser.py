# parser.py
import pdfplumber

def extract_text_data(pdf_path):
    data = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                data.append({
                    "page": i + 1,
                    "text": text.strip()
                })
    return data
