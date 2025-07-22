# json_generator.py
def build_json(data, filename):
    return {
        "filename": filename,
        "pages": [
            {
                "page_number": entry["page"],
                "content": entry["text"]
            } for entry in data
        ]
    }
