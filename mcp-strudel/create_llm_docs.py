#!/usr/bin/env python3
"""
Create LLM-optimized documentation packages from processed Strudel docs.
Provides both single-file and indexed retrieval approaches.
"""

import json
import glob
from pathlib import Path
from typing import Dict, List, Tuple
import re

class LLMDocPackager:
    def __init__(self, docs_dir: str = "/home/calvinw/develop/mcp-servers/mcp-strudel/docs_processed"):
        self.docs_dir = Path(docs_dir)
        self.metadata = self.load_metadata()
    
    def load_metadata(self) -> dict:
        """Load the metadata created during conversion."""
        metadata_file = self.docs_dir / "metadata.json"
        if metadata_file.exists():
            with open(metadata_file, 'r') as f:
                return json.load(f)
        return {}
    
    def create_single_file_docs(self) -> str:
        """Create a single consolidated documentation file."""
        
        content = """# Strudel Complete Documentation

This is a comprehensive guide to Strudel, a web-based live coding environment for algorithmic pattern music.

## Overview

Strudel is a JavaScript implementation of Tidal Cycles, allowing you to create complex musical patterns using code.
Key concepts: patterns, functions, cycles, samples, synths, effects.

## Quick Reference

### Essential Functions
"""
        
        # Add top functions from metadata
        if 'functions' in self.metadata:
            essential_functions = [
                's', 'note', 'freq', 'stack', 'seq', 'slow', 'fast', 'rev', 'add', 'mul',
                'lpf', 'hpf', 'delay', 'reverb', 'gain', 'pan', 'cut', 'begin', 'end'
            ]
            
            for func in essential_functions:
                if func in self.metadata['functions']:
                    content += f"- `{func}` - Core Strudel function\n"
        
        content += "\n## Complete Documentation\n\n"
        
        # Add documentation by category in logical order
        categories = [
            ('learn', 'Learning Strudel'),
            ('workshop', 'Workshop Exercises'), 
            ('recipes', 'Pattern Recipes'),
            ('functions', 'Function Reference'),
            ('technical-manual', 'Technical Details'),
            ('understand', 'Advanced Concepts')
        ]
        
        for category_dir, category_title in categories:
            category_path = self.docs_dir / category_dir
            if not category_path.exists():
                continue
                
            content += f"# {category_title}\n\n"
            
            # Get all markdown files in category
            md_files = sorted(category_path.glob("*.md"))
            
            for md_file in md_files:
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                    
                    # Add file as section
                    content += f"## {md_file.stem.replace('-', ' ').title()}\n\n"
                    content += file_content + "\n\n---\n\n"
                    
                except Exception as e:
                    print(f"Error reading {md_file}: {e}")
        
        return content
    
    def create_indexed_system(self) -> Dict[str, any]:
        """Create an indexed retrieval system with search capabilities."""
        
        index = {
            'overview': {
                'total_docs': 0,
                'total_functions': len(self.metadata.get('functions', [])),
                'total_samples': self.metadata.get('code_samples_count', 0),
                'categories': []
            },
            'categories': {},
            'functions': {},
            'search_index': {},
            'quick_start': '',
            'common_patterns': []
        }
        
        # Build category index
        for category_path in self.docs_dir.iterdir():
            if not category_path.is_dir() or category_path.name in ['__pycache__']:
                continue
                
            category_name = category_path.name
            category_files = []
            
            for md_file in category_path.glob("*.md"):
                file_info = {
                    'name': md_file.stem,
                    'title': md_file.stem.replace('-', ' ').title(),
                    'path': str(md_file.relative_to(self.docs_dir)),
                    'size': md_file.stat().st_size,
                    'preview': self.get_file_preview(md_file)
                }
                category_files.append(file_info)
                index['overview']['total_docs'] += 1
            
            if category_files:
                index['categories'][category_name] = {
                    'title': category_name.replace('-', ' ').title(),
                    'files': category_files,
                    'count': len(category_files)
                }
                index['overview']['categories'].append(category_name)
        
        # Build function index
        if 'function_locations' in self.metadata:
            for func, locations in self.metadata['function_locations'].items():
                # Clean function name
                clean_func = re.sub(r'[<>"`]', '', func)
                if len(clean_func) > 1 and clean_func.isalnum():
                    index['functions'][clean_func] = {
                        'name': clean_func,
                        'locations': locations,
                        'category': self.categorize_function(clean_func)
                    }
        
        # Create search index (keywords -> documents)
        index['search_index'] = self.build_search_index()
        
        # Add quick start content
        getting_started_path = self.docs_dir / 'learn' / 'getting-started.md'
        if getting_started_path.exists():
            index['quick_start'] = self.get_file_content(getting_started_path)[:2000] + "..."
        
        # Extract common patterns
        index['common_patterns'] = self.extract_common_patterns()
        
        return index
    
    def get_file_preview(self, file_path: Path, max_chars: int = 300) -> str:
        """Get a preview of the file content."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove markdown headers and get clean preview
            lines = content.split('\n')
            preview_lines = []
            char_count = 0
            
            for line in lines:
                if line.startswith('#'):
                    continue
                if line.strip():
                    preview_lines.append(line.strip())
                    char_count += len(line)
                    if char_count > max_chars:
                        break
            
            preview = ' '.join(preview_lines)
            return preview[:max_chars] + "..." if len(preview) > max_chars else preview
            
        except Exception:
            return "Preview unavailable"
    
    def get_file_content(self, file_path: Path) -> str:
        """Get full file content."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception:
            return ""
    
    def categorize_function(self, func_name: str) -> str:
        """Categorize a function based on its name."""
        patterns = {
            'sound': ['s', 'note', 'freq', 'oct', 'pitch'],
            'time': ['slow', 'fast', 'rev', 'jux', 'every', 'whenmod'],
            'effects': ['lpf', 'hpf', 'delay', 'reverb', 'gain', 'pan', 'cut'],
            'pattern': ['stack', 'seq', 'cat', 'superimpose', 'layer'],
            'math': ['add', 'mul', 'sub', 'div', 'mod', 'range'],
            'control': ['sometimes', 'often', 'rarely', 'never', 'always']
        }
        
        func_lower = func_name.lower()
        for category, keywords in patterns.items():
            if any(keyword in func_lower for keyword in keywords):
                return category
        return 'misc'
    
    def build_search_index(self) -> Dict[str, List[str]]:
        """Build a keyword search index."""
        search_index = {}
        
        for category_path in self.docs_dir.iterdir():
            if not category_path.is_dir():
                continue
                
            for md_file in category_path.glob("*.md"):
                try:
                    content = self.get_file_content(md_file).lower()
                    words = re.findall(r'\b\w+\b', content)
                    
                    # Index significant words
                    for word in set(words):
                        if len(word) > 3 and word not in ['the', 'and', 'for', 'with', 'this', 'that']:
                            if word not in search_index:
                                search_index[word] = []
                            file_ref = f"{category_path.name}/{md_file.stem}"
                            if file_ref not in search_index[word]:
                                search_index[word].append(file_ref)
                                
                except Exception:
                    continue
        
        return search_index
    
    def extract_common_patterns(self) -> List[Dict[str, str]]:
        """Extract common Strudel patterns from code samples."""
        patterns = []
        
        code_samples_file = self.docs_dir / "code-samples.md"
        if code_samples_file.exists():
            content = self.get_file_content(code_samples_file)
            
            # Extract code blocks
            code_blocks = re.findall(r'```javascript\n(.*?)\n```', content, re.DOTALL)
            
            # Common pattern types
            pattern_types = {
                'basic_drums': r's\(".*?(bd|kick|drum).*?"\)',
                'chord_progressions': r'note\(".*?[a-g].*?"\)',
                'effects_chain': r'\.(?:lpf|hpf|delay|reverb)',
                'timing_patterns': r'\.(?:slow|fast|every)'
            }
            
            for i, code in enumerate(code_blocks[:20]):  # Limit to first 20
                code_clean = code.strip()
                if len(code_clean) > 10:  # Skip very short snippets
                    pattern_info = {
                        'id': i,
                        'code': code_clean,
                        'type': 'general',
                        'description': f"Pattern example {i+1}"
                    }
                    
                    # Categorize pattern
                    for pattern_type, regex in pattern_types.items():
                        if re.search(regex, code_clean, re.IGNORECASE):
                            pattern_info['type'] = pattern_type
                            break
                    
                    patterns.append(pattern_info)
        
        return patterns
    
    def create_mcp_tools_integration(self) -> str:
        """Create MCP server tool integration code."""
        
        return '''
# Add these tools to your MCP server (server.py)

@mcp.tool()
def get_strudel_docs(query: str = "", category: str = "", function_name: str = "") -> str:
    """
    Get Strudel documentation. Can search by query, category, or function name.
    
    Args:
        query: Search term to find relevant documentation
        category: Specific category (learn, workshop, recipes, etc.)  
        function_name: Specific Strudel function to look up
    """
    docs_system = StrudelDocsSystem()
    
    if function_name:
        return docs_system.get_function_docs(function_name)
    elif category:
        return docs_system.get_category_docs(category)
    elif query:
        return docs_system.search_docs(query)
    else:
        return docs_system.get_overview()

@mcp.tool()
def get_strudel_examples(pattern_type: str = "all") -> str:
    """
    Get Strudel code examples by pattern type.
    
    Args:
        pattern_type: Type of pattern (drums, chords, effects, etc.)
    """
    docs_system = StrudelDocsSystem()
    return docs_system.get_examples(pattern_type)

@mcp.tool()
def search_strudel_functions(search_term: str) -> str:
    """
    Search for Strudel functions by name or description.
    
    Args:
        search_term: Function name or related keyword
    """
    docs_system = StrudelDocsSystem()
    return docs_system.search_functions(search_term)
'''

def main():
    """Create both single-file and indexed documentation packages."""
    
    packager = LLMDocPackager()
    output_dir = Path("/home/calvinw/develop/mcp-servers/mcp-strudel/llm_docs")
    output_dir.mkdir(exist_ok=True)
    
    print("Creating LLM documentation packages...")
    
    # Create single consolidated file
    print("1. Creating single consolidated file...")
    single_file_content = packager.create_single_file_docs()
    
    with open(output_dir / "strudel_complete_docs.md", 'w', encoding='utf-8') as f:
        f.write(single_file_content)
    
    print(f"   ✓ Single file: {len(single_file_content)} characters")
    
    # Create indexed system
    print("2. Creating indexed retrieval system...")
    index_system = packager.create_indexed_system()
    
    with open(output_dir / "strudel_docs_index.json", 'w', encoding='utf-8') as f:
        json.dump(index_system, f, indent=2)
    
    print(f"   ✓ Index system: {len(index_system['categories'])} categories")
    
    # Create MCP integration code
    print("3. Creating MCP server integration...")
    integration_code = packager.create_mcp_tools_integration()
    
    with open(output_dir / "mcp_integration.py", 'w', encoding='utf-8') as f:
        f.write(integration_code)
    
    # Create documentation system class
    create_docs_system_class(output_dir)
    
    print(f"""
LLM Documentation packages created in: {output_dir}

Files created:
- strudel_complete_docs.md ({len(single_file_content):,} chars) - Single consolidated file
- strudel_docs_index.json - Indexed retrieval system
- mcp_integration.py - MCP server tools
- strudel_docs_system.py - Documentation system class

Recommended approach:
- Use indexed system for real-time queries (better performance)
- Use single file for comprehensive context (may hit token limits)
""")

def create_docs_system_class(output_dir: Path):
    """Create the documentation system class for MCP integration."""
    
    system_code = '''import json
from pathlib import Path
from typing import List, Dict, Optional

class StrudelDocsSystem:
    """Documentation system for Strudel MCP server integration."""
    
    def __init__(self, docs_dir: str = "/home/calvinw/develop/mcp-servers/mcp-strudel/docs_processed"):
        self.docs_dir = Path(docs_dir)
        self.index_file = Path(__file__).parent / "strudel_docs_index.json"
        self.complete_docs_file = Path(__file__).parent / "strudel_complete_docs.md"
        self.index = self.load_index()
    
    def load_index(self) -> dict:
        """Load the documentation index."""
        if self.index_file.exists():
            with open(self.index_file, 'r') as f:
                return json.load(f)
        return {}
    
    def get_overview(self) -> str:
        """Get documentation overview."""
        overview = self.index.get('overview', {})
        
        result = f"""# Strudel Documentation Overview

Total Documents: {overview.get('total_docs', 0)}
Total Functions: {overview.get('total_functions', 0)}
Code Samples: {overview.get('total_samples', 0)}

## Categories Available:
"""
        
        for category in overview.get('categories', []):
            cat_info = self.index.get('categories', {}).get(category, {})
            result += f"- **{cat_info.get('title', category)}** ({cat_info.get('count', 0)} docs)\\n"
        
        # Add quick start
        if 'quick_start' in self.index:
            result += "\\n## Quick Start\\n\\n" + self.index['quick_start']
        
        return result
    
    def get_category_docs(self, category: str) -> str:
        """Get documentation for a specific category."""
        if category not in self.index.get('categories', {}):
            available = list(self.index.get('categories', {}).keys())
            return f"Category '{category}' not found. Available: {available}"
        
        cat_info = self.index['categories'][category]
        result = f"# {cat_info['title']}\\n\\n"
        
        for file_info in cat_info['files']:
            result += f"## {file_info['title']}\\n\\n"
            result += file_info['preview'] + "\\n\\n"
            
            # Load full content for small files
            if file_info['size'] < 10000:  # Less than 10KB
                file_path = self.docs_dir / file_info['path']
                if file_path.exists():
                    with open(file_path, 'r') as f:
                        content = f.read()
                    result += content + "\\n\\n---\\n\\n"
        
        return result
    
    def get_function_docs(self, function_name: str) -> str:
        """Get documentation for a specific function."""
        if function_name not in self.index.get('functions', {}):
            # Try fuzzy matching
            similar = [f for f in self.index.get('functions', {}).keys() 
                      if function_name.lower() in f.lower()]
            if similar:
                return f"Function '{function_name}' not found. Similar: {similar[:5]}"
            return f"Function '{function_name}' not found."
        
        func_info = self.index['functions'][function_name]
        result = f"# {function_name}\\n\\n"
        result += f"Category: {func_info.get('category', 'unknown')}\\n\\n"
        
        # Get documentation from source files
        for location in func_info.get('locations', [])[:3]:  # Limit to 3 sources
            file_path = self.docs_dir / location.replace('/', '/') 
            if file_path.exists():
                with open(file_path.with_suffix('.md'), 'r') as f:
                    content = f.read()
                
                # Extract relevant sections mentioning the function
                lines = content.split('\\n')
                relevant_lines = []
                context_range = 5
                
                for i, line in enumerate(lines):
                    if function_name in line:
                        start = max(0, i - context_range)
                        end = min(len(lines), i + context_range + 1)
                        relevant_lines.extend(lines[start:end])
                        relevant_lines.append("---")
                
                if relevant_lines:
                    result += f"\\n## From {location}\\n\\n"
                    result += '\\n'.join(relevant_lines)
        
        return result
    
    def search_docs(self, query: str) -> str:
        """Search documentation by query."""
        query_lower = query.lower()
        search_index = self.index.get('search_index', {})
        
        # Find matching documents
        matches = {}
        for word in query_lower.split():
            if word in search_index:
                for doc in search_index[word]:
                    matches[doc] = matches.get(doc, 0) + 1
        
        if not matches:
            return f"No matches found for '{query}'"
        
        # Sort by relevance
        sorted_matches = sorted(matches.items(), key=lambda x: x[1], reverse=True)
        
        result = f"# Search Results for '{query}'\\n\\n"
        
        for doc_path, score in sorted_matches[:5]:  # Top 5 results
            category, filename = doc_path.split('/')
            file_path = self.docs_dir / category / f"{filename}.md"
            
            if file_path.exists():
                with open(file_path, 'r') as f:
                    content = f.read()
                
                result += f"## {filename.replace('-', ' ').title()} (Score: {score})\\n\\n"
                result += content[:1000] + "...\\n\\n---\\n\\n"
        
        return result
    
    def get_examples(self, pattern_type: str = "all") -> str:
        """Get code examples by pattern type."""
        patterns = self.index.get('common_patterns', [])
        
        if pattern_type == "all":
            selected_patterns = patterns[:10]  # First 10
        else:
            selected_patterns = [p for p in patterns if p.get('type') == pattern_type]
        
        if not selected_patterns:
            available_types = list(set(p.get('type', 'general') for p in patterns))
            return f"No examples found for '{pattern_type}'. Available types: {available_types}"
        
        result = f"# Strudel Examples - {pattern_type.title()}\\n\\n"
        
        for pattern in selected_patterns:
            result += f"## {pattern.get('description', 'Example')}\\n\\n"
            result += f"```javascript\\n{pattern['code']}\\n```\\n\\n"
        
        return result
    
    def search_functions(self, search_term: str) -> str:
        """Search for functions by name or keyword."""
        functions = self.index.get('functions', {})
        search_lower = search_term.lower()
        
        matches = []
        for func_name, func_info in functions.items():
            if (search_lower in func_name.lower() or 
                search_lower in func_info.get('category', '').lower()):
                matches.append((func_name, func_info))
        
        if not matches:
            return f"No functions found matching '{search_term}'"
        
        result = f"# Functions matching '{search_term}'\\n\\n"
        
        for func_name, func_info in sorted(matches)[:10]:
            result += f"## {func_name}\\n"
            result += f"Category: {func_info.get('category', 'unknown')}\\n"
            result += f"Found in: {', '.join(func_info.get('locations', [])[:3])}\\n\\n"
        
        return result
'''
    
    with open(output_dir / "strudel_docs_system.py", 'w', encoding='utf-8') as f:
        f.write(system_code)

if __name__ == '__main__':
    main()