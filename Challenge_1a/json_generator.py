import json
from jsonschema import validate
from pathlib import Path

def validate_output(data, schema_path="output_schema.json"):
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    validate(instance=data, schema=schema)

def write_json_output(data, output_path, schema_path="output_schema.json"):
    validate_output(data, schema_path)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
