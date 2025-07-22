# PDF Outline Extractor 📖

A blazing-fast PDF processing solution built for **Adobe India Hackathon 2025 - Challenge 1a**. This project extracts structured data including **document title** and **table of contents (outline)** from PDF files and outputs it as a JSON file. Fully containerized and compliant with resource and performance constraints.

---

## 🌐 Overview

This solution parses a PDF file to extract:

* **Title** of the document
* **Hierarchical outline** (like bookmarks or ToC entries), including:

  * `text` (heading text)
  * `level` (outline depth)
  * `page` (starting page number)

The output is saved in a well-defined JSON format for each PDF.

---

## 🛁 Folder Structure

```
Challenge_1a/
├── Dockerfile
├── main.py                  # Core logic for PDF processing
├── utils.py                 # Helper functions (e.g. title, outlines)
├── input/                   # Input folder (read-only in container)
│   └── file01.pdf
├── output/                  # Output folder (where JSONs are saved)
│   └── file01.json
├── requirements.txt
└── README.md                # This file
```

---

## 🪖 Dockerized Execution

### ✅ Build the Docker Image

```bash
docker build -t pdf-processor .
```

### ⚡ Run the Container

```bash
docker run --rm \
  -v $(pwd)/input:/app/input:ro \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-processor
```

> This command mounts the input and output folders into the container, disables internet access, and runs the processor.

---

## ⏱ Performance Snapshot

```bash
Processing file01.pdf...
✅ file01.json generated.

real    0m0.339s
user    0m0.009s
sys     0m0.017s
```

* **Time Taken**: \~0.33s for a 50-page PDF
* **Within Constraint**: ✔ Under 10s limit

---

## 🔠 Output Schema

Each output `.json` follows the structure:

```json
{
  "title": "Document Title",
  "outline": [
    {
      "level": "1",
      "text": "Chapter 1",
      "page": 1
    },
    {
      "level": "2",
      "text": "Chapter 1 - Section 1",
      "page": 2
    }
    // ... more entries
  ]
}
```

---

## 🔧 Dependencies

Installed inside Docker via `requirements.txt`:

```txt
PyMuPDF==1.22.3
```

---

## 🎨 Sample Input/Output

### Input: `file01.pdf` (50 pages)

PDF includes a hierarchical table of contents embedded as outline.

### Output: `file01.json`

```json
{
  "title": "Sample Document with TOC",
  "outline": [
    { "level": "1", "text": "Chapter 1", "page": 1 },
    { "level": "2", "text": "Chapter 1 - Section 1", "page": 1 },
    ...
  ]
}
```

---

## 🧬 Additional Features

* Skips files with no outline gracefully
* Robust handling of bookmarks with multiple depths
* Title extracted directly from PDF metadata
* Easily extensible for multiple input files

---

## 🚀 Getting Started Locally

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/Challenge_1a.git
cd Challenge_1a
```

### 2. Place PDFs

Add your PDF files inside the `input/` directory.

### 3. Build & Run Docker

```bash
docker build -t pdf-processor .
docker run --rm \
  -v $(pwd)/input:/app/input:ro \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-processor
```

---

## 📄 License

MIT License

---

## 🙏 Acknowledgements

* Adobe India Hackathon Team for the challenge
* [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) for fast PDF processing

---

## 📢 Author

**Raman Kumar**
GitHub: [@Raman0101](https://github.com/Raman0101)
