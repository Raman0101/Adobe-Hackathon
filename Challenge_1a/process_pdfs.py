from pathlib import Path
from parser import extract_pdf_data
from json_generator import write_json_output

def process_pdfs():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    for pdf_file in input_dir.glob("*.pdf"):
        try:
            print(f"Processing {pdf_file.name}...")
            data = extract_pdf_data(pdf_file)
            output_file = output_dir / f"{pdf_file.stem}.json"
            write_json_output(data, output_file)
            print(f"✅ {output_file.name} generated.")
        except Exception as e:
            print(f"❌ Failed to process {pdf_file.name}: {e}")

if __name__ == "__main__":
    process_pdfs()
