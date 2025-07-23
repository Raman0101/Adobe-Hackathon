import os
import sys

from input_parser import load_input_config
from pdf_reader import extract_all_chunks_from_folder
from chunk_embedder import embed_chunks, embed_query
from ranker import rank_chunks
from output_writer import generate_output_json

def run_pipeline(input_dir):
    input_json_path = os.path.join(input_dir, "challenge1b_input.json")
    pdf_dir = os.path.join(input_dir, "PDFs")
    output_path = os.path.join(input_dir, "challenge1b_output.json")

    print(f"[INFO] ✅ Loading input configuration from {input_json_path}...")
    config = load_input_config(input_json_path)

    print(f"[INFO] 📄 Extracting chunks from PDFs in {pdf_dir}...")
    chunks = extract_all_chunks_from_folder(pdf_dir, config)

    print(f"[INFO] 🧠 Embedding document chunks...")
    embedded_chunks = embed_chunks(chunks)

    print(f"[INFO] 🔍 Embedding persona + job-to-be-done query...")
    query = config["persona"]["role"] + " " + config["job_to_be_done"]["task"]
    query_vec = embed_query(query)

    print(f"[INFO] 📊 Ranking document chunks...")
    top_sections = rank_chunks(embedded_chunks, query_vec)

    print(f"[INFO] 📝 Generating output at {output_path}...")
    generate_output_json(config, top_sections, output_path)

    print("[SUCCESS] 🎉 Output JSON generated successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/main.py <input_directory>")
        sys.exit(1)
    run_pipeline(sys.argv[1])
