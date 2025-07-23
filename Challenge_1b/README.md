# 🔍 Challenge 1b: Persona-Driven Document Intelligence

## 🎯 Objective
Build an intelligent document analysis system that extracts and ranks **relevant sections** from a collection of **PDFs**, based on a **persona** and a **job-to-be-done**.

---

## 📁 Folder Structure
```
Challenge_1b/
├── Collection_1/
│   ├── PDFs/                         # Input documents
│   ├── challenge1b_input.json        # Input config (persona, job, doc list)
│   └── challenge1b_output.json       # Output (auto-generated)
├── main.py                           # Entry point
├── input_parser.py                   # Parses input JSON and query
├── pdf_reader.py                     # Reads and chunks PDF content
├── chunk_embedder.py                 # Embeds chunks + query
├── ranker.py                         # Ranks chunks by relevance
├── output_writer.py                  # Builds final JSON output
├── requirements.txt                  # Python dependencies
├── Dockerfile                        # Container setup
└── README.md                         # You are here
```

---

## 🧠 Approach

1. **Input Parser** (`input_parser.py`)  
   Reads persona, job, and document titles from `challenge1b_input.json`.

2. **PDF Reader** (`pdf_reader.py`)  
   Extracts clean text from PDFs and chunks it per section or paragraph.

3. **Embedding Model** (`chunk_embedder.py`)  
   Converts both query and content into semantic vectors using Sentence Transformers (`MiniLM` or similar ≤1GB model).

4. **Ranking Engine** (`ranker.py`)  
   Uses cosine similarity to rank the most relevant document chunks.

5. **Output Generator** (`output_writer.py`)  
   Selects top N sections and refined text snippets, outputs `challenge1b_output.json`.

---

## 🛠️ Technologies Used

- Python 3.10+
- `pdfplumber` for PDF text extraction
- `sentence-transformers` (MiniLM model)
- `scikit-learn` for similarity scoring
- Docker for environment consistency

---

## ⚙️ Usage Instructions

### 🐳 Run with Docker

Build the image:
```bash
docker build -t persona-doc-intel .
```

Run the solution:
```bash
docker run --rm -v $(pwd)/Collection_1:/app/Collection_1 persona-doc-intel Collection_1
```

Output will be saved in `Collection_1/challenge1b_output.json`.

---

## 📄 Input Format

### challenge1b_input.json
```json
{
  "challenge_info": {
    "challenge_id": "round_1b_002",
    "test_case_name": "travel_planner"
  },
  "documents": [
    { "filename": "doc1.pdf", "title": "Doc 1" }
  ],
  "persona": { "role": "Travel Planner" },
  "job_to_be_done": { "task": "Plan a 4-day trip to the South of France" }
}
```

---

## 📤 Output Format

### challenge1b_output.json
```json
{
  "metadata": {
    "input_documents": ["doc1.pdf"],
    "persona": "Travel Planner",
    "job_to_be_done": "Plan a 4-day trip to the South of France",
    "processing_timestamp": "2025-07-23T12:34:56.789Z"
  },
  "extracted_sections": [
    {
      "document": "doc1.pdf",
      "section_title": "Things to Do",
      "importance_rank": 1,
      "page_number": 3
    }
  ],
  "subsection_analysis": [
    {
      "document": "doc1.pdf",
      "refined_text": "Beach hopping, wine tasting, city walks...",
      "page_number": 3
    }
  ]
}
```

---

## ✅ Features

- 🔍 **Persona-aware section selection**
- 🧠 **Semantic similarity ranking**
- 📄 **Multi-document support**
- 🧩 **Clean JSON output with metadata**
- ⚡ **Fast processing under 60s**
- 📦 **CPU-only, ≤1GB model footprint**

---

## 👥 Authors

- 🚀 Built by **Raman**
- 🤝 Shout out to teammates **Ram** and **Rishabh**
- 🏁 Submitted for **Adobe India Hackathon 2025 – Round 1B**
