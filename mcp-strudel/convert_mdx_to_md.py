#!/usr/bin/env python3
"""
Script to convert Strudel MDX documentation files to clean Markdown for LLM consumption.
Enhanced to extract code samples and function references.
"""

import os
import re
import json
import glob
from pathlib import Path
from typing import Dict, List, Tuple, Set
from collections import defaultdict

class StrudelDocConverter:
    def __init__(self):
        self.functions_found = set()
        self.code_samples = []
        self.function_locations = defaultdict(list)
    
    def extract_frontmatter(self, content: str) -> Tuple[Dict[str, str], str]:
        """Extract YAML frontmatter from MDX content."""
        frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(frontmatter_pattern, content, re.DOTALL)
        
        if not match:
            return {}, content
        
        # Extract frontmatter
        frontmatter_content = match.group(1)
        remaining_content = content[match.end():]
        
        # Parse simple YAML (title and layout)
        frontmatter = {}
        for line in frontmatter_content.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip()
        
        return frontmatter, remaining_content

    def remove_imports(self, content: str) -> str:
        """Remove import statements from MDX content."""
        # Remove import lines
        import_pattern = r'^import\s+.*?from\s+.*?;?\s*$'
        content = re.sub(import_pattern, '', content, flags=re.MULTILINE)
        
        # Remove empty lines left by imports
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        return content.strip()

    def extract_code_samples(self, content: str, source_file: str) -> str:
        """Extract code samples from MiniRepl components and convert to markdown."""
        
        # Pattern to match MiniRepl components with various attributes
        minirepl_pattern = r'<MiniRepl\s+([^>]*?)(?:tune=\{`([^`]+)`\})?([^>]*?)/>'
        
        def replace_minirepl(match):
            attrs_before = match.group(1) if match.group(1) else ""
            code = match.group(2) if match.group(2) else ""
            attrs_after = match.group(3) if match.group(3) else ""
            
            # Extract additional attributes for context
            all_attrs = attrs_before + attrs_after
            punchcard = 'punchcard' in all_attrs
            client_idle = 'client:idle' in all_attrs
            
            if code:
                # Store code sample for analysis
                sample_info = {
                    'code': code,
                    'source_file': source_file,
                    'has_punchcard': punchcard,
                    'client_idle': client_idle
                }
                self.code_samples.append(sample_info)
                
                # Extract function calls from the code
                self.extract_functions_from_code(code, source_file)
                
                # Create enhanced markdown code block
                markdown = f'```javascript\n{code}\n```'
                
                # Add context if available
                if punchcard:
                    markdown += '\n*This example includes visual pattern representation*'
                
                return markdown
            else:
                return '<!-- MiniRepl component without code -->'
        
        return re.sub(minirepl_pattern, replace_minirepl, content, flags=re.DOTALL)

    def extract_functions_from_code(self, code: str, source_file: str):
        """Extract Strudel function calls from code samples."""
        # Common Strudel function patterns
        function_patterns = [
            r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(',  # Function calls
            r'\.([a-zA-Z_][a-zA-Z0-9_]*)\s*\(',  # Method calls
            r'\bs\s*\(\s*["\']([^"\']+)["\']',    # s() function with sound names
        ]
        
        for pattern in function_patterns:
            matches = re.findall(pattern, code)
            for match in matches:
                if isinstance(match, tuple):
                    func_name = match[0] if match[0] else match[1]
                else:
                    func_name = match
                
                # Filter out common JS keywords and short names
                if (len(func_name) > 1 and 
                    func_name not in ['if', 'for', 'var', 'let', 'const', 'return', 'function']):
                    self.functions_found.add(func_name)
                    self.function_locations[func_name].append(source_file)

    def convert_jsx_components(self, content: str, source_file: str) -> str:
        """Convert JSX components to markdown equivalents."""
        
        # First extract code samples from MiniRepl
        content = self.extract_code_samples(content, source_file)
        
        # Convert JsDoc components to function references with enhanced info
        jsdoc_pattern = r'<JsDoc[^>]*?name="([^"]+)"[^>]*?(?:h=\{(\d+)\})?[^>]*?/>'
        def replace_jsdoc(match):
            name = match.group(1)
            heading_level = match.group(2) if match.group(2) else "2"
            
            # Track this function
            self.functions_found.add(name)
            self.function_locations[name].append(source_file)
            
            # Create appropriate markdown heading
            heading_prefix = "#" * int(heading_level) if heading_level != "0" else "**"
            heading_suffix = "" if heading_level != "0" else "**"
            
            return f'{heading_prefix}{heading_suffix}{name}{heading_suffix}{heading_prefix}\n\n*Function documentation for `{name}`*'
        
        content = re.sub(jsdoc_pattern, replace_jsdoc, content)
        
        # Remove other JSX components that don't have content
        jsx_pattern = r'<[A-Z][^>]*?/>'
        content = re.sub(jsx_pattern, '', content)
        
        # Remove JSX component tags with content (but keep the content)
        jsx_with_content_pattern = r'<([A-Z][^>]*?)>(.*?)</\1>'
        def replace_jsx_with_content(match):
            return match.group(2)  # Just return the content
        
        content = re.sub(jsx_with_content_pattern, replace_jsx_with_content, content, flags=re.DOTALL)
        
        return content

    def clean_markdown(self, content: str) -> str:
        """Clean up the markdown content."""
        # Remove excess whitespace
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # Remove HTML comments
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        
        # Clean up remaining whitespace
        content = content.strip()
        
        return content

    def convert_mdx_to_md(self, mdx_content: str, source_file: str, title: str = None) -> str:
        """Convert MDX content to clean Markdown."""
        
        # Extract frontmatter
        frontmatter, content = self.extract_frontmatter(mdx_content)
        
        # Get title from frontmatter if not provided
        if not title:
            title = frontmatter.get('title', 'Untitled')
        
        # Remove imports
        content = self.remove_imports(content)
        
        # Convert JSX components (this will also extract functions and code)
        content = self.convert_jsx_components(content, source_file)
        
        # Clean up markdown
        content = self.clean_markdown(content)
        
        # Add title if it's not already a top-level header
        if not content.startswith('# '):
            content = f'# {title}\n\n{content}'
        
        return content

    def get_category_from_path(self, file_path: str) -> str:
        """Extract category from file path."""
        path_parts = Path(file_path).parts
        
        # Find the category based on path structure
        if 'learn' in path_parts:
            return 'learn'
        elif 'workshop' in path_parts:
            return 'workshop'
        elif 'recipes' in path_parts:
            return 'recipes'
        elif 'technical-manual' in path_parts:
            return 'technical-manual'
        elif 'understand' in path_parts:
            return 'understand'
        elif 'functions' in path_parts:
            return 'functions'
        elif 'intro' in path_parts:
            return 'intro'
        elif 'blog' in path_parts:
            return 'blog'
        else:
            return 'misc'

    def create_function_index(self, output_dir: Path):
        """Create a comprehensive function index."""
        
        # Sort functions alphabetically
        sorted_functions = sorted(self.functions_found)
        
        index_content = """# Strudel Function Reference

This is a comprehensive index of all Strudel functions found in the documentation.

## Function List

"""
        
        for func in sorted_functions:
            locations = self.function_locations[func]
            index_content += f"### `{func}`\n\n"
            
            if locations:
                index_content += "Found in:\n"
                for loc in set(locations):  # Remove duplicates
                    category = self.get_category_from_path(loc)
                    filename = Path(loc).stem
                    index_content += f"- [{filename}]({category}/{filename}.md)\n"
            
            index_content += "\n"
        
        # Write function index
        with open(output_dir / 'function-index.md', 'w', encoding='utf-8') as f:
            f.write(index_content)

    def create_code_samples_index(self, output_dir: Path):
        """Create an index of all code samples."""
        
        index_content = """# Strudel Code Samples

This is a collection of all code samples found in the documentation.

"""
        
        for i, sample in enumerate(self.code_samples):
            category = self.get_category_from_path(sample['source_file'])
            filename = Path(sample['source_file']).stem
            
            index_content += f"## Sample {i+1} - from [{filename}]({category}/{filename}.md)\n\n"
            index_content += f"```javascript\n{sample['code']}\n```\n\n"
            
            if sample['has_punchcard']:
                index_content += "*Includes visual pattern representation*\n\n"
        
        # Write code samples index
        with open(output_dir / 'code-samples.md', 'w', encoding='utf-8') as f:
            f.write(index_content)

    def create_index_file(self, output_dir: Path, converted_files: List[Tuple[str, Path]]):
        """Create an index file listing all converted documentation."""
        
        index_content = f"""# Strudel Documentation Index

This directory contains Strudel documentation converted from MDX to Markdown for LLM consumption.

## Statistics

- **Total Documents**: {len(converted_files)}
- **Functions Found**: {len(self.functions_found)}
- **Code Samples**: {len(self.code_samples)}

## Special Indexes

- [Function Reference](function-index.md) - Complete list of all Strudel functions
- [Code Samples](code-samples.md) - All code examples from the documentation

## Categories

"""
        
        # Group files by category
        categories = {}
        for original_path, output_path in converted_files:
            category = output_path.parent.name
            if category not in categories:
                categories[category] = []
            categories[category].append(output_path.name)
        
        # Add category sections
        for category, files in sorted(categories.items()):
            index_content += f"### {category.replace('-', ' ').title()}\n\n"
            for file in sorted(files):
                filename = file.replace('.md', '')
                index_content += f"- [{filename}]({category}/{file})\n"
            index_content += "\n"
        
        # Write index file
        with open(output_dir / 'README.md', 'w', encoding='utf-8') as f:
            f.write(index_content)

    def save_metadata(self, output_dir: Path):
        """Save extracted metadata as JSON for programmatic access."""
        metadata = {
            'functions': list(self.functions_found),
            'function_locations': dict(self.function_locations),
            'code_samples_count': len(self.code_samples),
            'total_functions': len(self.functions_found)
        }
        
        with open(output_dir / 'metadata.json', 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)

    def convert_all(self):
        """Main function to convert all MDX files."""
        
        # Create output directory structure
        output_dir = Path('/home/calvinw/develop/mcp-servers/mcp-strudel/docs_processed')
        output_dir.mkdir(exist_ok=True)
        
        # Categories to organize documentation
        categories = ['learn', 'workshop', 'recipes', 'technical-manual', 'understand', 'functions', 'intro', 'blog', 'misc']
        
        for category in categories:
            (output_dir / category).mkdir(exist_ok=True)
        
        # Find all MDX files
        mdx_files = glob.glob('/home/calvinw/develop/mcp-servers/mcp-strudel/docs/strudel/**/*.mdx', recursive=True)
        
        # Filter to documentation files (exclude blog posts for now)
        doc_files = [f for f in mdx_files if '/pages/' in f and '/blog/' not in f]
        
        converted_files = []
        
        print(f"Found {len(doc_files)} documentation files to convert...")
        
        for mdx_file in doc_files:
            try:
                # Read MDX file
                with open(mdx_file, 'r', encoding='utf-8') as f:
                    mdx_content = f.read()
                
                # Convert to markdown
                md_content = self.convert_mdx_to_md(mdx_content, mdx_file)
                
                # Determine output category and filename
                category = self.get_category_from_path(mdx_file)
                filename = Path(mdx_file).stem + '.md'
                
                # Write to output directory
                output_file = output_dir / category / filename
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(md_content)
                
                converted_files.append((mdx_file, output_file))
                print(f"✓ Converted: {Path(mdx_file).name}")
                
            except Exception as e:
                print(f"✗ Error converting {mdx_file}: {e}")
        
        # Create comprehensive indexes
        print("\nCreating indexes...")
        self.create_index_file(output_dir, converted_files)
        self.create_function_index(output_dir)
        self.create_code_samples_index(output_dir)
        self.save_metadata(output_dir)
        
        print(f"""
Conversion complete!
- Processed: {len(converted_files)} files
- Functions found: {len(self.functions_found)}
- Code samples: {len(self.code_samples)}
- Output directory: {output_dir}
""")

def main():
    converter = StrudelDocConverter()
    converter.convert_all()

if __name__ == '__main__':
    main()