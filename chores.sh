#!/bin/bash

# Specify the directory containing the JSON files
DIR="./models/props"

# Create an output directory
OUTPUT_DIR="./models/props_new"
mkdir -p "$OUTPUT_DIR"

# Loop through all JSON files in the directory
for file in "$DIR"/*.json; 
do
    # Get the base name of the file (without path)
    base_name=$(basename "$file")
    
    # Run the jq command and save the output to the output directory
    jq 'walk(if type == "object" then del(.["x-stoplight"]) else . end)' "$file" > "${OUTPUT_DIR}/${base_name}"
done