# 🧠 Persona-Driven Document Intelligence – Challenge 1b

A fast, containerized solution for **Adobe India Hackathon 2025 - Challenge 1b**.  
This system extracts and ranks the most relevant sections from a PDF document collection based on a **persona** and their **job-to-be-done** — all within **1GB model size**, **CPU-only**, and under **60 seconds** runtime.

---

## 🌐 Overview

This project performs:

- ✅ **Query parsing** from persona & job-to-be-done  
- 📄 **PDF chunking** using `pdfplumber`  
- 🧠 **Text embeddings** using `sentence-transformers`  
- 🎯 **Chunk ranking** via cosine similarity  
- 📤 **Top-k output generation** in JSON format  

---

## 🛠️ Folder Structure

```plaintext
Challenge_1b/
├── Collection_1/
│   ├── PDFs/
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── src/
│   ├── main.py
│   ├── input_parser.py
│   ├── pdf_reader.py
│   ├── chunk_embedder.py
│   ├── ranker.py
│   └── output_writer.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 📥 Input Format

### `challenge1b_input.json`

```json
{
  "challenge_info": {
    "challenge_id": "1b",
    "collection_id": "Collection_1"
  },
  "persona": {
    "role": "Data Scientist"
  },
  "job_to_be_done": {
    "task": "Understand infrastructure pain points"
  },
  "documents": [
    "infra_guide.pdf"
  ]
}
```

---

## 📤 Output Format

### `challenge1b_output.json`

```json
{
  "persona": "Data Scientist",
  "job_to_be_done": "Understand infrastructure pain points",
  "answers": [
    {
      "document": "infra_guide.pdf",
      "page_number": 2,
      "text": "The biggest challenge in infrastructure is balancing compute and cost..."
    }
  ]
}
```

---

## 🐳 Docker Instructions

### 🔧 Build the Image

```bash
docker build -t persona-doc-intel .
```

### 🚀 Run the Container

```bash
docker run --rm \
  -v $(pwd)/Collection_1:/app/Collection_1 \
  persona-doc-intel python src/main.py Collection_1
```

---

## 🧠 How It Works

| Step               | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `input_parser.py`  | Parses `challenge1b_input.json` for persona and task                        |
| `pdf_reader.py`    | Extracts 150-word overlapping chunks from PDFs using `pdfplumber`           |
| `chunk_embedder.py`| Embeds chunks and query using `all-MiniLM-L6-v2` via `sentence-transformers`|
| `ranker.py`        | Ranks chunks by cosine similarity to the query                              |
| `output_writer.py` | Writes top-ranked chunks to final output JSON                               |

---

## 📦 Dependencies

### `requirements.txt`

```txt
pdfplumber
numpy
scikit-learn
sentence-transformers==2.2.2
huggingface_hub==0.14.1
```

---

## 🐳 Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir torch==2.2.2+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]
```

---

## ⚡ Performance Snapshot

```plaintext
[INFO] ✅ Loaded input configuration
[INFO] 📄 Extracting chunks from PDFs in Collection_1/PDFs...
[INFO] 🧠 Embedding chunks...
[INFO] 🔍 Embedding query...
[INFO] 🎯 Ranking chunks...
[INFO] ✅ Output written to Collection_1/challenge1b_output.json
Total time: ~35 seconds on CPU (≤1GB RAM)
```

---

## ✅ Features

- 100% CPU-only inference  
- Supports multiple PDFs per collection  
- Compact model: ~80MB  
- Fully Dockerized & offline-safe  
- Compliant with 1GB model and 60s runtime constraints  

---

## 👨‍💻 Author

**Raman Kumar**  
GitHub: [@Raman0101](https://github.com/Raman0101)

---

## 🙏 Acknowledgements

- Adobe India Hackathon Team  
- Sentence Transformers  
- pdfplumber
