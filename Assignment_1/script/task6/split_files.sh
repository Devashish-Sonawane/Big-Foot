#!/bin/bash

# Check if jq is installed
command -v jq >/dev/null 2>&1 || { echo >&2 "jq is required but it's not installed. Aborting."; exit 1; }

# Input JSON file
input_file="nonumerical.json"

# Output directory
output_dir="output"

# Create output directory if it doesn't exist
mkdir -p "$output_dir"

# Split the JSON file into chunks of 100 lines
jq -c --slurp 'reduce range(0;length) as $i ([]; . + [.[ $i: $i+100 ]]) | .[]' "$input_file" | \
awk 'NR%100==1{x="output/chunk"int(NR/100)+1".json"} {print > x}' "$1"/*.json

echo "JSON file has been divided into chunks of 100."