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

## 🛠️ Folder Structure

```
Challenge_1a/
├── Dockerfile
├── README.md
├── json_generator.py         # Script to generate mock PDFs with outlines
├── output_schema.json        # JSON schema for validation (optional)
├── parser.py                 # PDF outline/title extractor logic
├── process_pdfs.py           # Entry point script
├── requirements.txt
├── input/                    # Input PDFs
│   └── file01.pdf
└── output/                   # Output JSONs
    └── file01.json
```

---

## 🧪 Output Format

Each output `.json` conforms to this schema:

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
      "text": "Section 1.1",
      "page": 2
    }
  ]
}
```

You can validate this using the `output_schema.json` file.

---

## 🐳 Docker Usage

### 🔧 Build Docker Image

```bash
docker build -t pdf-processor .
```

### 🚀 Run the Container

```bash
docker run --rm \
  -v $(pwd)/input:/app/input:ro \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-processor
```

> Mounts local folders inside the container and ensures no internet usage.

---

## 🧠 How It Works

* `process_pdfs.py`: Loops through all PDFs in `input/` and writes results to `output/`
* `parser.py`: Extracts metadata title and outline using PyMuPDF
* `json_generator.py`: (Optional) Script to generate test PDFs with outlines

---

## ⏱ Performance Snapshot

For a **50-page PDF with outlines**:

```
Processing file01.pdf...
✅ file01.json generated.

real    0m0.339s
user    0m0.009s
sys     0m0.017s
```

Well under the required **10-second** constraint.

---

## 📦 Dependencies

Installed via `requirements.txt`:

```
PyMuPDF==1.22.3
```

---

## 🧪 Testing With Sample PDF

You can generate a testable PDF using:

```bash
python json_generator.py
```

This creates a file like `outlined_50_pages.pdf` in your input folder with structured bookmarks.

---

## ✅ Features

* Clean, structured JSON output
* Supports multiple input PDFs
* Fully offline, Docker-safe
* Scalable and fast
* Auto skips PDFs with no outlines

---

## 🚀 Getting Started Locally

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/Challenge_1a.git
cd Challenge_1a
```

### 2. Place PDFs

Put your input `.pdf` files into the `input/` folder.

### 3. Run the Pipeline

```bash
docker build -t pdf-processor .
docker run --rm \
  -v $(pwd)/input:/app/input:ro \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-processor
```


---

## 🙏 Acknowledgements

* Adobe India Hackathon Team
* [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)

---

## 👨‍💻 Author

**Raman Kumar**
GitHub: [@Raman0101](https://github.com/Raman0101)
