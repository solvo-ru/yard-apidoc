import json
import os

def split_json(input_file, output_dir, schema_url):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Read the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Iterate through first-level properties
    for key, value in data.items():
        # Create a new dictionary with the current property and add $schema
        new_data = {
            "$schema": schema_url,
            key: value
        }

        # Create output file name
        output_file = os.path.join(output_dir, f"{key}.json")

        # Write the new JSON to a file
        with open(output_file, 'w') as f:
            json.dump(new_data, f, indent=2)

        print(f"Created: {output_file}")

# Example usage
input_file = "schemas.json"
output_dir = "schemas"
schema_url = "https://json-schema.org/draft/2020-12/schema"

split_json(input_file, output_dir, schema_url)