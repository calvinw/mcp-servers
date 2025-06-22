import json
from pathlib import Path
from typing import List, Dict, Optional
import re

class StrudelDocsSystemV2:
    """
    Faithful documentation system that mirrors the Strudel website structure
    and adds value through curation, not reinterpretation.
    """
    
    def __init__(self, docs_dir: str = None):
        # Auto-detect docs directory location
        if docs_dir is None:
            # Try to find docs_processed relative to this file or current working directory
            possible_paths = [
                Path(__file__).parent.parent / "docs_processed",  # ../docs_processed from llm_docs/
                Path.cwd() / "docs_processed",  # ./docs_processed from current working directory
                Path("/app/docs_processed"),  # Docker container path
                Path("/home/calvinw/develop/mcp-servers/mcp-strudel/docs_processed"),  # Development path
            ]
            
            for path in possible_paths:
                if path.exists() and path.is_dir():
                    docs_dir = str(path)
                    break
            
            if docs_dir is None:
                raise ValueError(f"Could not find docs_processed directory. Tried: {[str(p) for p in possible_paths]}")
        
        self.docs_dir = Path(docs_dir)
        self.index_file = Path(__file__).parent / "strudel_docs_index.json"
        self.index = self.load_index()
        self.site_structure = self._build_site_structure()
        self.all_examples = self._extract_all_examples()
    
    def load_index(self) -> dict:
        """Load the documentation index."""
        if self.index_file.exists():
            with open(self.index_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _build_site_structure(self) -> dict:
        """Build the complete site structure from the docs directory."""
        structure = {}
        
        if not self.docs_dir.exists():
            return structure
        
        for category_dir in self.docs_dir.iterdir():
            if category_dir.is_dir() and category_dir.name != '__pycache__':
                category_name = category_dir.name
                structure[category_name] = []
                
                for file_path in category_dir.glob("*.md"):
                    if file_path.name != 'README.md':
                        page_name = file_path.stem
                        structure[category_name].append({
                            'name': page_name,
                            'path': f"{category_name}/{page_name}",
                            'title': self._get_page_title(file_path),
                            'file_path': file_path
                        })
        
        return structure
    
    def _get_page_title(self, file_path: Path) -> str:
        """Extract the title from a markdown file."""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                # Look for first H1 heading
                lines = content.split('\n')
                for line in lines[:10]:  # Check first 10 lines
                    if line.startswith('# '):
                        return line[2:].strip()
                # Fallback to filename
                return file_path.stem.replace('-', ' ').title()
        except:
            return file_path.stem.replace('-', ' ').title()
    
    def _extract_all_examples(self) -> List[Dict]:
        """Extract all code examples from all pages."""
        examples = []
        
        for category in self.site_structure.values():
            for page in category:
                page_examples = self._extract_page_examples(page['file_path'], page['path'])
                examples.extend(page_examples)
        
        return examples
    
    def _extract_page_examples(self, file_path: Path, page_path: str) -> List[Dict]:
        """Extract code examples from a specific page."""
        examples = []
        
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                
            # Find JavaScript code blocks
            code_blocks = re.findall(r'```(?:javascript|js)\n(.*?)\n```', content, re.DOTALL)
            
            for i, code in enumerate(code_blocks):
                # Try to find context around the code block
                code_start = content.find(f'```javascript\n{code}')
                if code_start == -1:
                    code_start = content.find(f'```js\n{code}')
                
                context = ""
                if code_start > -1:
                    # Look backwards for a heading or description
                    before_code = content[:code_start]
                    lines_before = before_code.split('\n')
                    for line in reversed(lines_before[-10:]):  # Last 10 lines before code
                        if line.startswith('#') or (line.strip() and not line.startswith('```')):
                            context = line.strip()
                            break
                
                examples.append({
                    'code': code.strip(),
                    'context': context,
                    'page': page_path,
                    'page_title': self._get_page_title(file_path),
                    'category': page_path.split('/')[0] if '/' in page_path else 'misc'
                })
        
        except Exception as e:
            pass  # Skip files that can't be read
        
        return examples
    
    def get_site_outline(self, category: str = "") -> str:
        """Get the complete site structure outline."""
        if category and category in self.site_structure:
            # Return specific category outline
            pages = self.site_structure[category]
            result = f"# Strudel Documentation: {category.title()} Section\n\n"
            result += f"**{len(pages)} pages in this section:**\n\n"
            
            for page in pages:
                result += f"## {page['title']}\n"
                result += f"**Path**: `{page['path']}`\n"
                result += f"**Read**: `get_strudel_docs(page=\"{page['path']}\")` to read this page\n\n"
            
            return result
        
        # Return complete site outline - filter out empty categories
        non_empty_categories = {k: v for k, v in self.site_structure.items() if len(v) > 0}
        total_pages = sum(len(pages) for pages in non_empty_categories.values())
        
        result = "# Complete Strudel Documentation Outline\n\n"
        result += f"**Total categories:** {len(non_empty_categories)}\n"
        result += f"**Total pages:** {total_pages}\n\n"
        
        result += "## Function Reference (399 functions)\n\n"
        result += "- **Complete API Reference** (`functions`)\n"
        result += "  - All 399 Strudel functions with descriptions, parameters, and examples\n"
        result += "  - Read with: `get_strudel_docs(page=\"functions\")`\n\n"
        
        result += "## Instrument Samples Reference (139 instruments, 2032 variations)\n\n"
        result += "- **VCSL Instrument Samples** (`instruments`)\n"
        result += "  - Complete catalog of available instrument samples\n"
        result += "  - Organized by categories: Percussion, Keyboards, Strings, Wind, etc.\n"
        result += "  - Read with: `get_strudel_docs(page=\"instruments\")`\n\n"
        
        result += "## Synthesizers Reference (18 synthesizers)\n\n"
        result += "- **Built-in Synthesizers** (`synths`)\n"
        result += "  - Basic waveforms: sine, sawtooth, square, triangle\n"
        result += "  - Noise generators: white, pink, brown, crackle\n"
        result += "  - Algorithmic synths: z_sine, z_sawtooth, etc.\n"
        result += "  - Read with: `get_strudel_docs(page=\"synths\")`\n\n"
        
        result += "## General MIDI Instruments (125 instruments, 871 variations)\n\n"
        result += "- **GM Instrument Collection** (`gm`)\n"
        result += "  - Complete General MIDI standard instruments\n"
        result += "  - Categories: Keyboards, Strings, Brass, Woodwinds, etc.\n"
        result += "  - High-quality sampled instruments\n"
        result += "  - Read with: `get_strudel_docs(page=\"gm\")`\n\n"
        
        result += "## Classic Drum Machines (84 machines, 1355 samples, 4826 variations)\n\n"
        result += "- **Legendary Drum Machines** (`drums`)\n"
        result += "  - TR-808, TR-909, LinnDrum, Oberheim DMX, and many more\n"
        result += "  - Authentic samples from classic hardware\n"
        result += "  - Hip-hop, house, pop, and electronic music history\n"
        result += "  - Read with: `get_strudel_docs(page=\"drums\")`\n\n"
        
        for category_name, pages in non_empty_categories.items():
            result += f"## {category_name.title()} ({len(pages)} pages)\n\n"
            
            for page in pages:
                result += f"- **{page['title']}** (`{page['path']}`)\n"
            
            result += f"\n**Usage:**\n"
            result += f"- `get_strudel_docs(page=\"{category_name}/page_name\")` to read any page\n"
            result += f"- `get_strudel_docs(outline=\"{category_name}\")` to see just this section\n\n"
        
        return result
    
    def get_complete_page(self, page_path: str) -> str:
        """Get a complete page exactly as written."""
        # Clean the page path
        page_path = page_path.strip().strip('"').strip("'")
        
        # Special handling for function reference
        if page_path in ["functions", "function-reference", "functions-reference", "api-reference", "reference"]:
            func_ref_path = self.docs_dir / "functions-reference-clean.md"
            if func_ref_path.exists():
                try:
                    with open(func_ref_path, 'r') as f:
                        content = f.read()
                    return f"# Function Reference\n*Complete Strudel API reference with 399 functions*\n\n---\n\n{content}"
                except Exception as e:
                    pass  # Fall through to normal handling
        
        # Special handling for instrument samples reference
        if page_path in ["instruments", "instrument-samples", "samples-reference", "vcsl", "instrument-reference"]:
            samples_ref_path = self.docs_dir / "instrument-samples.md"
            if samples_ref_path.exists():
                try:
                    with open(samples_ref_path, 'r') as f:
                        content = f.read()
                    return f"# Instrument Samples Reference\n*Complete VCSL instrument samples with 139 instruments, 2032 variations*\n\n---\n\n{content}"
                except Exception as e:
                    pass  # Fall through to normal handling
        
        # Special handling for synths reference
        if page_path in ["synths", "synths-reference", "synthesizers", "waveforms"]:
            synths_ref_path = self.docs_dir / "synths-reference.md"
            if synths_ref_path.exists():
                try:
                    with open(synths_ref_path, 'r') as f:
                        content = f.read()
                    return f"# Synthesizers Reference\n*Complete synths and waveforms with 18 synthesizers*\n\n---\n\n{content}"
                except Exception as e:
                    pass  # Fall through to normal handling
        
        # Special handling for GM instruments reference
        if page_path in ["gm", "gm-instruments", "general-midi", "midi-instruments"]:
            gm_ref_path = self.docs_dir / "gm-instruments-reference.md"
            if gm_ref_path.exists():
                try:
                    with open(gm_ref_path, 'r') as f:
                        content = f.read()
                    return f"# General MIDI Instruments Reference\n*Complete GM instruments with 125 instruments, 871 variations*\n\n---\n\n{content}"
                except Exception as e:
                    pass  # Fall through to normal handling
        
        # Special handling for drum machines reference
        if page_path in ["drums", "drum-machines", "drum-machines-reference", "classic-drums"]:
            drums_ref_path = self.docs_dir / "drum-machines-reference.md"
            if drums_ref_path.exists():
                try:
                    with open(drums_ref_path, 'r') as f:
                        content = f.read()
                    return f"# Drum Machines Reference\n*Classic drum machines with 84 machines, 1355 samples, 4826 variations*\n\n---\n\n{content}"
                except Exception as e:
                    pass  # Fall through to normal handling
        
        # Handle different input formats
        if not page_path.endswith('.md'):
            page_path = page_path + '.md'
        
        file_path = self.docs_dir / page_path
        
        if not file_path.exists():
            # Try to find the page in any category
            page_name = Path(page_path).stem
            for category, pages in self.site_structure.items():
                for page in pages:
                    if page['name'] == page_name:
                        file_path = page['file_path']
                        break
                if file_path.exists():
                    break
        
        if not file_path.exists():
            available_pages = []
            for category, pages in self.site_structure.items():
                for page in pages:
                    available_pages.append(page['path'])
            
            return f"Page '{page_path}' not found.\n\nAvailable pages:\n" + "\n".join(f"- {p}" for p in available_pages[:20])
        
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Add metadata header
            relative_path = file_path.relative_to(self.docs_dir)
            result = f"# {relative_path}\n"
            result += f"*Complete page from Strudel documentation*\n\n"
            result += "---\n\n"
            result += content
            
            return result
            
        except Exception as e:
            return f"Error reading page '{page_path}': {str(e)}"
    
    def search_functions(self, query: str, limit: int = 10) -> str:
        """Search for functions by name or description."""
        func_ref_path = self.docs_dir / "functions-reference-clean.md"
        if not func_ref_path.exists():
            return "Function reference not available."
        
        try:
            with open(func_ref_path, 'r') as f:
                content = f.read()
            
            results = []
            current_function = None
            current_content = []
            
            lines = content.split('\n')
            for line in lines:
                if line.startswith('### '):
                    # Save previous function if it matches
                    if current_function and self._matches_query(current_function, '\n'.join(current_content), query):
                        results.append({
                            'name': current_function,
                            'content': '\n'.join(current_content[:10])  # First 10 lines
                        })
                    
                    # Start new function
                    current_function = line[4:].strip()
                    current_content = [line]
                elif current_function:
                    current_content.append(line)
            
            # Check last function
            if current_function and self._matches_query(current_function, '\n'.join(current_content), query):
                results.append({
                    'name': current_function,
                    'content': '\n'.join(current_content[:10])
                })
            
            if not results:
                return f"No functions found matching '{query}'. Try searching for function names, keywords, or concepts."
            
            # Limit results
            results = results[:limit]
            
            result_text = f"# Function Search Results for '{query}'\n\n"
            result_text += f"Found {len(results)} function(s):\n\n"
            
            for result in results:
                result_text += f"## {result['name']}\n\n"
                result_text += result['content'] + "\n\n---\n\n"
            
            if len(results) == limit:
                result_text += f"*Showing first {limit} results. Use get_strudel_docs(page=\"functions\") for complete reference.*"
            
            return result_text
            
        except Exception as e:
            return f"Error searching functions: {str(e)}"
    
    def _matches_query(self, function_name: str, content: str, query: str) -> bool:
        """Check if a function matches the search query."""
        query_lower = query.lower()
        
        # Check function name
        if query_lower in function_name.lower():
            return True
        
        # Check content (description, parameters, examples)
        if query_lower in content.lower():
            return True
        
        return False
    
    def search_instrument_samples(self, query: str, limit: int = 15) -> str:
        """Search for instrument samples by name or category."""
        samples_ref_path = self.docs_dir / "instrument-samples.md"
        if not samples_ref_path.exists():
            return "Instrument samples reference not available."
        
        try:
            with open(samples_ref_path, 'r') as f:
                content = f.read()
            
            results = []
            lines = content.split('\n')
            current_category = None
            
            for line in lines:
                if line.startswith('### ') and not line.startswith('### Summary'):
                    current_category = line[4:].strip()
                elif line.startswith('| `') and '|' in line:
                    # Parse table row: | `sample_name` | variations | usage |
                    parts = line.split('|')
                    if len(parts) >= 4:
                        sample_name = parts[1].strip().strip('`').strip()
                        variations = parts[2].strip()
                        usage = parts[3].strip()
                        
                        if sample_name and sample_name != 'Sample Name':
                            # Check if query matches
                            query_lower = query.lower()
                            if (query_lower in sample_name.lower() or 
                                (current_category and query_lower in current_category.lower())):
                                results.append({
                                    'name': sample_name,
                                    'category': current_category or 'Unknown',
                                    'variations': variations,
                                    'usage': usage
                                })
            
            if not results:
                return f"No instrument samples found matching '{query}'. Try searching for instrument names, categories, or keywords like 'piano', 'percussion', 'wind', etc."
            
            # Limit results
            results = results[:limit]
            
            result_text = f"# Instrument Sample Search Results for '{query}'\n\n"
            result_text += f"Found {len(results)} instrument(s):\n\n"
            
            current_cat = None
            for result in results:
                if result['category'] != current_cat:
                    current_cat = result['category']
                    result_text += f"## {current_cat}\n\n"
                
                result_text += f"### {result['name']}\n"
                result_text += f"- **Variations**: {result['variations']}\n"
                result_text += f"- **Usage**: {result['usage']}\n\n"
            
            if len(results) == limit:
                result_text += f"*Showing first {limit} results. Use get_strudel_docs(page=\"instruments\") for complete reference.*"
            
            return result_text
            
        except Exception as e:
            return f"Error searching instrument samples: {str(e)}"
    
    def search_synths(self, query: str, limit: int = 10) -> str:
        """Search for synthesizers by name or category."""
        synths_ref_path = self.docs_dir / "synths-reference.md"
        if not synths_ref_path.exists():
            return "Synthesizers reference not available."
        
        try:
            with open(synths_ref_path, 'r') as f:
                content = f.read()
            
            results = []
            lines = content.split('\n')
            current_category = None
            
            for line in lines:
                if line.startswith('### ') and line != '### Summary':
                    current_category = line[4:].strip()
                elif line.startswith('| `') and '|' in line and 'Usage Example' not in line:
                    # Parse table row: | `synth_name` | description | usage |
                    parts = line.split('|')
                    if len(parts) >= 3:
                        synth_name = parts[1].strip().strip('`').strip()
                        description = parts[2].strip() if len(parts) > 2 else ''
                        usage = parts[3].strip() if len(parts) > 3 else ''
                        
                        if synth_name and synth_name != 'Synth Name':
                            # Check if query matches
                            query_lower = query.lower()
                            if (query_lower in synth_name.lower() or 
                                (current_category and query_lower in current_category.lower()) or
                                query_lower in description.lower()):
                                results.append({
                                    'name': synth_name,
                                    'category': current_category or 'Unknown',
                                    'description': description,
                                    'usage': usage
                                })
            
            if not results:
                return f"No synthesizers found matching '{query}'. Try searching for synth names, categories like 'waveform', 'noise', or keywords like 'sine', 'sawtooth', etc."
            
            # Limit results
            results = results[:limit]
            
            result_text = f"# Synthesizer Search Results for '{query}'\n\n"
            result_text += f"Found {len(results)} synthesizer(s):\n\n"
            
            current_cat = None
            for result in results:
                if result['category'] != current_cat:
                    current_cat = result['category']
                    result_text += f"## {current_cat}\n\n"
                
                result_text += f"### {result['name']}\n"
                if result['description']:
                    result_text += f"- **Description**: {result['description']}\n"
                if result['usage']:
                    result_text += f"- **Usage**: {result['usage']}\n"
                result_text += "\n"
            
            if len(results) == limit:
                result_text += f"*Showing first {limit} results. Use get_strudel_docs(page=\"synths\") for complete reference.*"
            
            return result_text
            
        except Exception as e:
            return f"Error searching synthesizers: {str(e)}"
    
    def search_gm_instruments(self, query: str, limit: int = 15) -> str:
        """Search for GM instruments by name or category."""
        gm_ref_path = self.docs_dir / "gm-instruments-reference.md"
        if not gm_ref_path.exists():
            return "GM instruments reference not available."
        
        try:
            with open(gm_ref_path, 'r') as f:
                content = f.read()
            
            results = []
            lines = content.split('\n')
            current_category = None
            
            for line in lines:
                if line.startswith('### ') and line != '### Summary':
                    current_category = line[4:].strip()
                elif line.startswith('| `gm_') and '|' in line:
                    # Parse table row: | `gm_instrument` | variations | display_name | usage |
                    parts = line.split('|')
                    if len(parts) >= 5:
                        instrument_name = parts[1].strip().strip('`').strip()
                        variations = parts[2].strip()
                        display_name = parts[3].strip()
                        usage = parts[4].strip()
                        
                        if instrument_name and instrument_name != 'Instrument':
                            # Check if query matches
                            query_lower = query.lower()
                            if (query_lower in instrument_name.lower() or 
                                (current_category and query_lower in current_category.lower()) or
                                query_lower in display_name.lower()):
                                results.append({
                                    'name': instrument_name,
                                    'category': current_category or 'Unknown',
                                    'variations': variations,
                                    'display_name': display_name,
                                    'usage': usage
                                })
            
            if not results:
                return f"No GM instruments found matching '{query}'. Try searching for instrument names, categories like 'brass', 'strings', or keywords like 'piano', 'guitar', etc."
            
            # Limit results
            results = results[:limit]
            
            result_text = f"# GM Instrument Search Results for '{query}'\n\n"
            result_text += f"Found {len(results)} instrument(s):\n\n"
            
            current_cat = None
            for result in results:
                if result['category'] != current_cat:
                    current_cat = result['category']
                    result_text += f"## {current_cat}\n\n"
                
                result_text += f"### {result['display_name']} (`{result['name']}`)\n"
                result_text += f"- **Variations**: {result['variations']}\n"
                result_text += f"- **Usage**: {result['usage']}\n\n"
            
            if len(results) == limit:
                result_text += f"*Showing first {limit} results. Use get_strudel_docs(page=\"gm\") for complete reference.*"
            
            return result_text
            
        except Exception as e:
            return f"Error searching GM instruments: {str(e)}"
    
    def search_drum_machines(self, query: str, limit: int = 15) -> str:
        """Search for drum machines by name, machine model, or drum type."""
        drums_ref_path = self.docs_dir / "drum-machines-reference.md"
        if not drums_ref_path.exists():
            return "Drum machines reference not available."
        
        try:
            with open(drums_ref_path, 'r') as f:
                content = f.read()
            
            results = []
            lines = content.split('\n')
            current_category = None
            current_machine = None
            
            for line in lines:
                if line.startswith('### ') and line != '### Summary':
                    current_category = line[4:].strip()
                elif line.startswith('#### '):
                    current_machine = line[5:].strip()
                elif line.startswith('| `') and '|' in line and 'Usage Example' not in line:
                    # Parse table row: | `sample_name` | type | variations | usage |
                    parts = line.split('|')
                    if len(parts) >= 5:
                        sample_name = parts[1].strip().strip('`').strip()
                        drum_type = parts[2].strip()
                        variations = parts[3].strip()
                        usage = parts[4].strip()
                        
                        if sample_name and sample_name != 'Sample Name':
                            # Check if query matches
                            query_lower = query.lower()
                            if (query_lower in sample_name.lower() or 
                                (current_machine and query_lower in current_machine.lower()) or
                                (current_category and query_lower in current_category.lower()) or
                                query_lower in drum_type.lower()):
                                results.append({
                                    'name': sample_name,
                                    'machine': current_machine or 'Unknown',
                                    'category': current_category or 'Unknown',
                                    'drum_type': drum_type,
                                    'variations': variations,
                                    'usage': usage
                                })
            
            if not results:
                return f"No drum machines found matching '{query}'. Try searching for machine names like 'tr808', 'tr909', 'linndrum', drum types like 'kick', 'snare', or categories like 'roland'."
            
            # Limit results
            results = results[:limit]
            
            result_text = f"# Drum Machine Search Results for '{query}'\n\n"
            result_text += f"Found {len(results)} sample(s):\n\n"
            
            current_machine = None
            for result in results:
                if result['machine'] != current_machine:
                    current_machine = result['machine']
                    result_text += f"## {current_machine}\n\n"
                
                result_text += f"### {result['name']}\n"
                result_text += f"- **Type**: {result['drum_type']}\n"
                result_text += f"- **Variations**: {result['variations']}\n"
                result_text += f"- **Usage**: {result['usage']}\n\n"
            
            if len(results) == limit:
                result_text += f"*Showing first {limit} results. Use get_strudel_docs(page=\"drums\") for complete reference.*"
            
            return result_text
            
        except Exception as e:
            return f"Error searching drum machines: {str(e)}"
    
    def get_all_pages_concatenated(self) -> str:
        """Get all documentation pages concatenated in logical order."""
        result = "# Complete Strudel Documentation\n"
        result += "*All pages concatenated in reading order*\n\n"
        
        # Define logical reading order
        reading_order = ['intro', 'learn', 'understand', 'workshop', 'recipes', 'technical-manual', 'functions']
        
        for category_name in reading_order:
            if category_name in self.site_structure:
                result += f"\n\n# {category_name.upper()} SECTION\n\n"
                
                for page in self.site_structure[category_name]:
                    try:
                        with open(page['file_path'], 'r') as f:
                            content = f.read()
                        
                        result += f"## {page['title']} ({page['path']})\n\n"
                        result += content + "\n\n"
                        result += "---\n\n"
                    
                    except Exception:
                        continue
        
        # Add any remaining categories
        for category_name, pages in self.site_structure.items():
            if category_name not in reading_order:
                result += f"\n\n# {category_name.upper()} SECTION\n\n"
                
                for page in pages:
                    try:
                        with open(page['file_path'], 'r') as f:
                            content = f.read()
                        
                        result += f"## {page['title']} ({page['path']})\n\n"
                        result += content + "\n\n"
                        result += "---\n\n"
                    
                    except Exception:
                        continue
        
        return result
    
    def get_curated_examples(self, 
                           example_type: str = "all", 
                           function: str = "", 
                           concept: str = "",
                           difficulty: str = "") -> str:
        """Curate examples across all pages - this is the MCP's value-add."""
        
        if function:
            return self._get_function_examples(function)
        elif concept:
            return self._get_concept_examples(concept)
        elif difficulty:
            return self._get_difficulty_examples(difficulty)
        elif example_type != "all":
            return self._get_typed_examples(example_type)
        else:
            return self._get_all_examples_overview()
    
    def _get_function_examples(self, function: str) -> str:
        """Get all examples that use a specific function."""
        matching_examples = []
        
        for example in self.all_examples:
            if function in example['code']:
                matching_examples.append(example)
        
        if not matching_examples:
            return f"No examples found using function '{function}'."
        
        result = f"# Examples using `{function}` function\n\n"
        result += f"Found {len(matching_examples)} examples across {len(set(ex['page'] for ex in matching_examples))} pages:\n\n"
        
        for i, example in enumerate(matching_examples):
            result += f"## Example {i+1}: {example['context'] or 'Code Example'}\n"
            result += f"*From: {example['page_title']} ({example['page']})*\n\n"
            result += f"```javascript\n{example['code']}\n```\n\n"
        
        return result
    
    def _get_concept_examples(self, concept: str) -> str:
        """Get examples related to a musical concept."""
        concept_keywords = {
            'drums': ['bd', 'sd', 'hh', 'cp', 'kick', 'snare', 'hihat'],
            'timing': ['slow', 'fast', 'euclid', 'swing', '*', '/'],
            'effects': ['lpf', 'hpf', 'delay', 'reverb', 'gain', 'pan'],
            'chords': ['chord', 'voicing', '[', ',', 'stack'],
            'patterns': ['seq', 'cat', 'stack', '<', '>', 'rev'],
            'bass': ['c2', 'g1', 'f1', 'bass', 'sub'],
            'melody': ['note', 'scale', 'c4', 'd4', 'e4']
        }
        
        keywords = concept_keywords.get(concept.lower(), [concept])
        matching_examples = []
        
        for example in self.all_examples:
            if any(keyword in example['code'].lower() for keyword in keywords):
                matching_examples.append(example)
        
        if not matching_examples:
            available_concepts = list(concept_keywords.keys())
            return f"No examples found for concept '{concept}'.\n\nAvailable concepts: {', '.join(available_concepts)}"
        
        result = f"# Examples for concept: {concept}\n\n"
        result += f"Found {len(matching_examples)} examples across {len(set(ex['page'] for ex in matching_examples))} pages:\n\n"
        
        for i, example in enumerate(matching_examples[:10]):  # Limit to top 10
            result += f"## {example['context'] or f'Example {i+1}'}\n"
            result += f"*From: {example['page_title']} ({example['page']})*\n\n"
            result += f"```javascript\n{example['code']}\n```\n\n"
        
        return result
    
    def _get_difficulty_examples(self, difficulty: str) -> str:
        """Get examples by difficulty level."""
        if difficulty.lower() == "beginner":
            # Simple patterns with basic functions
            matching_examples = []
            for example in self.all_examples:
                code = example['code']
                # Beginner: short code, basic functions, no complex chaining
                if (len(code) < 100 and 
                    code.count('.') <= 2 and 
                    not any(adv in code for adv in ['superimpose', 'chunk', 'when', 'euclid'])):
                    matching_examples.append(example)
        
        elif difficulty.lower() == "intermediate":
            # More complex patterns
            matching_examples = []
            for example in self.all_examples:
                code = example['code']
                if (50 < len(code) < 200 and 
                    2 < code.count('.') <= 5):
                    matching_examples.append(example)
        
        elif difficulty.lower() == "advanced":
            # Complex patterns with advanced functions
            matching_examples = []
            for example in self.all_examples:
                code = example['code']
                if (len(code) > 100 and 
                    (code.count('.') > 5 or 
                     any(adv in code for adv in ['superimpose', 'chunk', 'when', 'euclid', 'sometimes']))):
                    matching_examples.append(example)
        
        else:
            return f"Unknown difficulty '{difficulty}'. Use: beginner, intermediate, or advanced."
        
        result = f"# {difficulty.title()} Examples\n\n"
        result += f"Found {len(matching_examples)} {difficulty} examples:\n\n"
        
        for i, example in enumerate(matching_examples[:15]):
            result += f"## {example['context'] or f'Example {i+1}'}\n"
            result += f"*From: {example['page_title']} ({example['page']})*\n\n"
            result += f"```javascript\n{example['code']}\n```\n\n"
        
        return result
    
    def _get_typed_examples(self, example_type: str) -> str:
        """Get examples by type."""
        # Map types to search criteria
        type_criteria = {
            'drum_patterns': lambda ex: any(drum in ex['code'] for drum in ['bd', 'sd', 'hh', 'cp', 's(']),
            'melodies': lambda ex: 'note(' in ex['code'] and any(note in ex['code'] for note in ['c', 'd', 'e', 'f', 'g', 'a', 'b']),
            'effects_chains': lambda ex: ex['code'].count('.') >= 3,
            'basic_patterns': lambda ex: len(ex['code']) < 80,
            'polyrhythm': lambda ex: any(poly in ex['code'] for poly in ['euclid', '*', '/', 'off', 'superimpose'])
        }
        
        if example_type not in type_criteria:
            available_types = list(type_criteria.keys())
            return f"Unknown example type '{example_type}'.\n\nAvailable types: {', '.join(available_types)}"
        
        criteria_func = type_criteria[example_type]
        matching_examples = [ex for ex in self.all_examples if criteria_func(ex)]
        
        result = f"# {example_type.replace('_', ' ').title()} Examples\n\n"
        result += f"Found {len(matching_examples)} examples:\n\n"
        
        for i, example in enumerate(matching_examples[:12]):
            result += f"## {example['context'] or f'Example {i+1}'}\n"
            result += f"*From: {example['page_title']} ({example['page']})*\n\n"
            result += f"```javascript\n{example['code']}\n```\n\n"
        
        return result
    
    def _get_all_examples_overview(self) -> str:
        """Get an overview of all available examples."""
        result = f"# All Strudel Examples Overview\n\n"
        result += f"Total examples found: {len(self.all_examples)}\n"
        result += f"From {len(set(ex['page'] for ex in self.all_examples))} documentation pages\n\n"
        
        # Group by category
        by_category = {}
        for example in self.all_examples:
            cat = example['category']
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(example)
        
        result += "## Examples by Category\n\n"
        for category, examples in by_category.items():
            result += f"- **{category}**: {len(examples)} examples\n"
        
        result += "\n## How to Use\n"
        result += "- `get_strudel_examples(function=\"note\")` - All examples using 'note'\n"
        result += "- `get_strudel_examples(concept=\"drums\")` - All drum-related examples\n"
        result += "- `get_strudel_examples(difficulty=\"beginner\")` - Simple examples\n"
        result += "- `get_strudel_examples(example_type=\"drum_patterns\")` - Specific pattern types\n"
        
        return result
    
    def find_related_pages(self, topic: str) -> str:
        """Find pages related to a topic with URLs and descriptions."""
        related_pages = []
        
        for category, pages in self.site_structure.items():
            for page in pages:
                # Check if topic appears in page title or content preview
                if (topic.lower() in page['title'].lower() or 
                    topic.lower() in page['name'].lower()):
                    
                    # Get brief preview
                    try:
                        with open(page['file_path'], 'r') as f:
                            content = f.read()
                        preview = content[:200].replace('\n', ' ').strip()
                        
                        related_pages.append({
                            'title': page['title'],
                            'path': page['path'],
                            'preview': preview + "..."
                        })
                    except:
                        related_pages.append({
                            'title': page['title'],
                            'path': page['path'],
                            'preview': "Documentation page"
                        })
        
        if not related_pages:
            return f"No pages found directly related to '{topic}'.\n\nUse `get_strudel_docs(outline=True)` to see all available pages."
        
        result = f"# Pages related to '{topic}'\n\n"
        
        for page in related_pages:
            result += f"## {page['title']}\n"
            result += f"**Path**: `{page['path']}`\n"
            result += f"**Preview**: {page['preview']}\n"
            result += f"**Read**: `get_strudel_docs(page=\"{page['path']}\")`\n\n"
        
        return result