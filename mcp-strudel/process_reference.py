#!/usr/bin/env python3
"""
Script to process and clean up the reference.md file for better integration
with the Strudel MCP documentation system.
"""

import re
from pathlib import Path

def parse_function_entry(lines, start_idx):
    """Parse a single function entry from the reference file."""
    
    # Function name is on the first line
    func_name = lines[start_idx].strip()
    
    current_idx = start_idx + 1
    synonyms = []
    description = []
    parameters = []
    examples = []
    
    # Parse synonyms if they exist
    if current_idx < len(lines) and lines[current_idx].startswith("Synonyms:"):
        synonyms_line = lines[current_idx].replace("Synonyms:", "").strip()
        synonyms = [s.strip() for s in synonyms_line.split(",")]
        current_idx += 1
    
    # Skip empty line
    if current_idx < len(lines) and lines[current_idx].strip() == "":
        current_idx += 1
    
    # Parse description and parameters
    while current_idx < len(lines):
        line = lines[current_idx].strip()
        
        # Stop if we hit the next function (starts with a letter and no spaces)
        if line and re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', line):
            break
            
        # Empty line - might be separator
        if not line:
            current_idx += 1
            continue
            
        # Parameter line (starts with parameter name and colon)
        if ":" in line and line.split(":")[0].strip() in ["time", "amount", "gain", "name", "dictionary", "range", "bank", "alias", "func", "start", "end"]:
            parameters.append(line)
        # Code example (no leading text, likely JavaScript)
        elif line and not line[0].isupper() and not line.startswith("//"):
            examples.append(line)
        # Comment in code
        elif line.startswith("//"):
            examples.append(line)
        # Regular description text
        else:
            description.append(line)
            
        current_idx += 1
    
    return {
        "name": func_name,
        "synonyms": synonyms,
        "description": " ".join(description),
        "parameters": parameters,
        "examples": examples
    }, current_idx

def process_reference_file(input_file, output_file):
    """Process the reference.md file and create a cleaned version."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Remove the header lines
    content_start = 0
    for i, line in enumerate(lines):
        if line.strip() == "API Reference":
            content_start = i + 2  # Skip header and description
            break
    
    lines = [line.rstrip() for line in lines[content_start:]]
    
    functions = []
    current_idx = 0
    
    while current_idx < len(lines):
        line = lines[current_idx].strip()
        
        # Look for function names (start with letter, no spaces)
        if line and re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', line):
            func_data, next_idx = parse_function_entry(lines, current_idx)
            functions.append(func_data)
            current_idx = next_idx
        else:
            current_idx += 1
    
    # Generate the cleaned markdown
    output_content = ["# Strudel Functions Reference", ""]
    output_content.append("This is a comprehensive reference of all Strudel functions. Each function includes its description, parameters, and example usage.")
    output_content.append("")
    
    # Group functions by first letter
    current_letter = ""
    
    for func in sorted(functions, key=lambda x: x["name"].lower()):
        first_letter = func["name"][0].upper()
        
        if first_letter != current_letter:
            current_letter = first_letter
            output_content.append(f"## {current_letter}")
            output_content.append("")
        
        # Function name
        output_content.append(f"### {func['name']}")
        
        # Synonyms
        if func["synonyms"]:
            synonyms_text = ", ".join(func["synonyms"])
            output_content.append(f"*Synonyms: {synonyms_text}*")
            output_content.append("")
        
        # Description
        if func["description"]:
            output_content.append(func["description"])
            output_content.append("")
        
        # Parameters
        if func["parameters"]:
            output_content.append("**Parameters:**")
            for param in func["parameters"]:
                output_content.append(f"- `{param}`")
            output_content.append("")
        
        # Examples
        if func["examples"]:
            output_content.append("```javascript")
            for example in func["examples"]:
                output_content.append(example)
            output_content.append("```")
            output_content.append("")
    
    # Write the output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_content))
    
    print(f"Processed {len(functions)} functions")
    print(f"Output written to: {output_file}")

if __name__ == "__main__":
    input_file = Path("docs_processed/reference.md")
    output_file = Path("docs_processed/functions-reference-clean.md")
    
    process_reference_file(input_file, output_file)