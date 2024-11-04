import json
import os
import re

def slugify(text):
    # Remove non-word characters (everything except numbers and letters)
    text = re.sub(r'[^\w\s-]', '', text.lower())
    # Replace all runs of whitespace with a single dash
    return re.sub(r'[-\s]+', '-', text).strip('-')

def split_json(input_file, output_dir, schema_url):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Read the input JSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Iterate through first-level properties
    for key, value in data.items():
        # Create a new dictionary with the current property and add $schema
        new_data = {
            "$schema": schema_url,
            key: value
        }

        # Create a safe filename
        safe_key = slugify(key)
        output_file = os.path.join(output_dir, f"{safe_key}.json")

        # Write the new JSON to a file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=2, ensure_ascii=False)

        print(f"Created: {output_file}")

# Example usage
input_file = "schemas.json"
output_dir = "schemas"
schema_url = "https://json-schema.org/draft/2020-12/schema"

split_json(input_file, output_dir, schema_url)