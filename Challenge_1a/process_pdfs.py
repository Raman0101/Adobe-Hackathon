# process_pdfs.py
from pathlib import Path
import json
from parser import extract_text_data
from json_generator import build_json

def process_pdfs():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    for pdf_path in input_dir.glob("*.pdf"):
        data = extract_text_data(pdf_path)
        structured_output = build_json(data, pdf_path.stem)

        output_file = output_dir / f"{pdf_path.stem}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(structured_output, f, indent=2)

if __name__ == "__main__":
    process_pdfs()
