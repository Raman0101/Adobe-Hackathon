# 📦 Adobe India Hackathon 2025 – Team TechnoidX - Unified Solutions Overview

This repository contains two lightweight, CPU-only solutions optimized for fast, containerized execution under tight constraints (≤1 GB RAM, ≤60 s runtime):

---

## 🧠 Challenge 1a – PDF Outline Extractor

**Goal:** Extract document titles and hierarchical outlines (bookmarks/TOC) from one or more PDFs into structured JSON.

**Approach & Tools:**
- 📄 Scans PDFs using `PyMuPDF`
- 🔍 Retrieves the title and nested outline entries (`text`, `level`, `page`)
- Outputs per-PDF JSON files ready for schema validation

**Key Highlights:**
- Fully Dockerized (`python:3.10-slim`)
- Runtime ~0.3 seconds per 50-page PDF
- Offline-safe, scalable, skips files without outlines

---

## 🤖 Challenge 1b – Persona‑Driven Document Intelligence

**Goal:** Given a persona and job-to-be-done, extract and rank the most relevant PDF segments (chunks) using embeddings.

**Pipeline & Tools:**
1. **Input Parsing**: Reads `challenge1b_input.json` with persona, task, and document list  
2. **Chunking**: Uses `pdfplumber` to generate overlapping 150‑word chunks  
3. **Embedding**: Uses `sentence-transformers` (`all-MiniLM-L6-v2`, ~80 MB) to embed chunks + query  
4. **Ranking**: Computes cosine similarity to select top‑k relevant chunks  
5. **Output**: Writes results in `challenge1b_output.json` with `document`, `page_number`, and snippet

**Key Highlights:**
- CPU-only, under 60 seconds per run (~35 seconds tested)
- Docker container with minimal dependencies (Torch + ST libs)
- Handles multiple PDFs per collection smoothly

---

## 🧩 Shared Traits & Best Practices

| Feature               | Details for Both Projects |
|-----------------------|---------------------------|
| **Containerization**  | Docker ensures portability & offline use |
| **Model Constraints** | Lightweight models (<100 MB), CPU-only |
| **Efficient I/O**     | JSON-based inputs/outputs for easy automation |
| **Performance**       | Fast execution — seconds per document |
| **Scalability**       | Easily parallelizable for large batches |

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/Adobe-Hackathon-Solutions.git
cd Adobe-Hackathon-Solutions
```

### 2. Build Docker Image (Example: Challenge 1b)

```bash
cd Challenge_1b
docker build -t persona-doc-intel .
```

### 3. Run the Container

```bash
docker run --rm \
  -v "$(pwd)/Collection_1":/app/Collection_1 \
  persona-doc-intel python src/main.py Collection_1
```

### 4. Inspect the Output

Check the generated output JSONs inside the `Collection_1/` folder (for 1b) or `output/` folder (for 1a).

---

## 👨‍💻 Team TechnoidX

**Raman Kumar** [@Raman0101](https://github.com/Raman0101)
**Rishabh Dubey** [@dubeyrishabh123](https://github.com/dubeyrishabh123)
**Ram Samujh Singh** [@ramsamujhsingh70](https://github.com/ramsamujhsingh70)

Special thanks to the Adobe India Hackathon team and these open-source projects:

- [PyMuPDF](https://pymupdf.readthedocs.io/)  
- [pdfplumber](https://github.com/jsvine/pdfplumber)  
- [Sentence Transformers](https://www.sbert.net/)  
- [Hugging Face Hub](https://huggingface.co/)

---

Concise, modular, and ready to extend—these solutions demonstrate practical document intelligence with speed, accuracy, and portability.


[def]: https://github.com/dubeyrishabh123