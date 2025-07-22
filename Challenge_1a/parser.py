import fitz  # PyMuPDF

def extract_pdf_data(pdf_path):
    doc = fitz.open(pdf_path)

    # Get document title from metadata or fallback to first line of first page
    title = doc.metadata.get("title", "").strip()
    if not title:
        title = doc[0].get_text().split('\n')[0].strip()

    # Extract outline (Table of Contents)
    outline = []
    toc = doc.get_toc(simple=True)  # [level, text, page]
    for level, text, page in toc:
        outline.append({
            "level": str(level),
            "text": text.strip(),
            "page": page
        })

    return {
        "title": title,
        "outline": outline
    }
