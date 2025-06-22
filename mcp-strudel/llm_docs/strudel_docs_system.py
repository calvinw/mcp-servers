import json
from pathlib import Path
from typing import List, Dict, Optional

class StrudelDocsSystem:
    """Simplified documentation system for Strudel MCP server integration."""
    
    def __init__(self, docs_dir: str = "/home/calvinw/develop/mcp-servers/mcp-strudel/docs_processed"):
        self.docs_dir = Path(docs_dir)
        self.index_file = Path(__file__).parent / "strudel_docs_index.json"
        self.complete_docs_file = Path(__file__).parent / "strudel_complete_docs.md"
        self.index = self.load_index()
        self.complete_docs = self.load_complete_docs()
    
    def load_index(self) -> dict:
        """Load the documentation index."""
        if self.index_file.exists():
            with open(self.index_file, 'r') as f:
                return json.load(f)
        return {}
    
    def load_complete_docs(self) -> str:
        """Load the complete documentation content."""
        if self.complete_docs_file.exists():
            with open(self.complete_docs_file, 'r') as f:
                return f.read()
        return "Documentation not available."
    
    def get_overview(self) -> str:
        """Get documentation overview and categories."""
        overview = self.index.get('overview', {})
        
        result = f"""# Strudel Documentation Overview

Total Documents: {overview.get('total_docs', 0)}
Total Functions: {overview.get('total_functions', 0)}
Code Samples: {overview.get('total_samples', 0)}

## Available Categories:
"""
        
        categories = overview.get('categories', [])
        for category in categories:
            cat_info = self.index.get('categories', {}).get(category, {})
            result += f"- **{category}**: {cat_info.get('title', category)} ({cat_info.get('count', 0)} docs)\n"
        
        result += "\n## Quick Reference\n\n"
        
        # Extract and return the quick reference section from complete docs
        lines = self.complete_docs.split('\n')
        quick_ref_start = -1
        quick_ref_end = -1
        
        for i, line in enumerate(lines):
            if '## Quick Reference' in line:
                quick_ref_start = i
            elif quick_ref_start > -1 and line.startswith('## ') and 'Quick Reference' not in line:
                quick_ref_end = i
                break
        
        if quick_ref_start > -1:
            end_idx = quick_ref_end if quick_ref_end > -1 else min(quick_ref_start + 30, len(lines))
            quick_ref = '\n'.join(lines[quick_ref_start+1:end_idx])
            result += quick_ref
        
        return result
    
    def get_category_docs(self, category: str) -> str:
        """Get documentation for a specific category."""
        if category not in self.index.get('categories', {}):
            available = list(self.index.get('categories', {}).keys())
            return f"Category '{category}' not found. Available categories: {', '.join(available)}\n\nUse the get_strudel_docs() function without parameters to see all documentation."
        
        # Extract the category section from the complete docs
        lines = self.complete_docs.split('\n')
        category_start = -1
        category_end = len(lines)
        
        # Look for the category header in the complete docs
        category_patterns = [
            f"# {category.title()}",
            f"## {category.title()}",
            f"# Learning {category.title()}",
            f"## Learning {category.title()}"
        ]
        
        for i, line in enumerate(lines):
            if any(pattern in line for pattern in category_patterns):
                category_start = i
                break
        
        if category_start == -1:
            # If we can't find the category, return the available categories and suggest using full docs
            cat_info = self.index['categories'][category]
            result = f"# {cat_info.get('title', category.title())} Documentation\n\n"
            
            # Return file previews from the index
            for file_info in cat_info.get('files', []):
                result += f"## {file_info['title']}\n\n"
                result += file_info['preview'] + "\n\n---\n\n"
            
            return result
        
        # Find the end of this category section
        for i in range(category_start + 1, len(lines)):
            if lines[i].startswith('# ') and not any(pattern in lines[i] for pattern in category_patterns):
                category_end = i
                break
        
        # Extract the category content
        category_content = '\n'.join(lines[category_start:category_end])
        
        return category_content
    
    def get_function_docs(self, function_name: str) -> str:
        """Get documentation for a specific function."""
        # Search for the function in the complete documentation
        lines = self.complete_docs.split('\n')
        function_sections = []
        
        # Look for function mentions in the complete docs
        for i, line in enumerate(lines):
            if function_name in line and ('##' in line or '`' in line or 'function' in line.lower()):
                # Extract context around the function mention
                start = max(0, i - 3)
                end = min(len(lines), i + 10)
                section = '\n'.join(lines[start:end])
                function_sections.append(section)
        
        if not function_sections:
            # Try fuzzy matching
            functions = self.index.get('functions', {})
            similar = [f for f in functions.keys() if function_name.lower() in f.lower()]
            if similar:
                return f"Function '{function_name}' not found directly. Similar functions: {', '.join(similar[:10])}\n\nTry using search_strudel_functions() or get_strudel_docs() for more comprehensive results."
            return f"Function '{function_name}' not found. Use search_strudel_functions() to find similar functions or get_strudel_docs() to browse all documentation."
        
        # Get function info from index if available
        func_info = self.index.get('functions', {}).get(function_name, {})
        
        result = f"# {function_name} Function Documentation\n\n"
        
        if func_info:
            result += f"**Category:** {func_info.get('category', 'unknown')}\n\n"
        
        # Add the found sections
        for i, section in enumerate(function_sections[:3]):  # Limit to first 3 matches
            result += f"## Context {i+1}\n\n"
            result += section + "\n\n---\n\n"
        
        return result
    
    def search_docs(self, query: str) -> str:
        """Search documentation by query with improved grouping and topic recognition."""
        if not query.strip():
            return "Please provide a search query. Use get_strudel_docs() without parameters to see all documentation."
        
        query_lower = query.lower()
        
        # Check for common topic searches and provide comprehensive answers
        topic_searches = {
            'samples': self._get_samples_info,
            'sample': self._get_samples_info,
            'drums': self._get_drums_info,
            'drum': self._get_drums_info,
            'effects': self._get_effects_info,
            'effect': self._get_effects_info,
            'synths': self._get_synths_info,
            'synth': self._get_synths_info,
            'timing': self._get_timing_info,
            'time': self._get_timing_info,
            'patterns': self._get_patterns_info,
            'pattern': self._get_patterns_info
        }
        
        if query_lower in topic_searches:
            return topic_searches[query_lower]()
        
        # Regular text search with better grouping
        lines = self.complete_docs.split('\n')
        matching_sections = []
        
        for i, line in enumerate(lines):
            if query_lower in line.lower():
                # Extract larger context for better coherence
                start = max(0, i - 8)
                end = min(len(lines), i + 20)
                
                # Find the best section title
                section_title = "Context"
                for j in range(i, max(0, i-15), -1):
                    if lines[j].startswith('#'):
                        section_title = lines[j].strip('# ')
                        break
                
                section = {
                    'title': section_title,
                    'content': '\n'.join(lines[start:end]),
                    'line_num': i,
                    'relevance': line.lower().count(query_lower)  # Count occurrences for relevance
                }
                matching_sections.append(section)
        
        if not matching_sections:
            return self._get_search_suggestions(query)
        
        # Group by section title and merge similar content
        grouped_sections = {}
        for section in matching_sections:
            title = section['title']
            if title not in grouped_sections:
                grouped_sections[title] = {
                    'title': title,
                    'content': section['content'],
                    'relevance': section['relevance'],
                    'count': 1
                }
            else:
                # Only add if significantly different content
                existing = grouped_sections[title]['content']
                new_content = section['content']
                if len(set(new_content.split()) - set(existing.split())) > 10:
                    grouped_sections[title]['content'] += f"\n\n### Additional Context:\n{new_content}"
                grouped_sections[title]['relevance'] += section['relevance']
                grouped_sections[title]['count'] += 1
        
        # Sort by relevance
        sorted_sections = sorted(grouped_sections.values(), 
                               key=lambda x: (x['relevance'], x['count']), 
                               reverse=True)
        
        result = f"# Search Results for '{query}'\n\n"
        result += f"Found {len(matching_sections)} matches in {len(grouped_sections)} sections:\n\n"
        
        # Show top sections with better formatting
        for section in sorted_sections[:4]:
            result += f"## {section['title']} (Relevance: {section['relevance']})\n\n"
            result += section['content'] + "\n\n---\n\n"
        
        return result
    
    def get_all_docs(self) -> str:
        """Return the complete documentation."""
        return f"# Complete Strudel Documentation\n\n{self.complete_docs}"
    
    def _get_samples_info(self) -> str:
        """Get comprehensive information about samples."""
        result = "# Strudel Samples - Complete Guide\n\n"
        
        # Extract sample-related content from docs
        lines = self.complete_docs.split('\n')
        sample_sections = []
        
        for i, line in enumerate(lines):
            if any(keyword in line.lower() for keyword in ['sample', 'bd', 'sd', 'hh', 'cp', 'roland', 'gm']):
                start = max(0, i - 3)
                end = min(len(lines), i + 10)
                sample_sections.append('\n'.join(lines[start:end]))
        
        # Add built-in drum samples
        result += """## Built-in Drum Samples

### Basic Drum Kit
- `bd` - Bass drum/kick drum  
- `sd` - Snare drum
- `hh` - Hi-hat
- `cp` - Clap
- `rim` - Rim shot
- `perc` - Percussion
- `tabla` - Tabla drums

### Usage Examples:
```javascript
s("bd sd hh cp")        // Basic drum pattern
s("bd*2 sd hh*4 cp")    // With timing variations  
s("bd ~ sd ~")          // With rests
```

"""
        
        # Add Roland and GM banks info
        result += """## Roland and GM Sound Banks

Access professional sample banks:
```javascript
s("RolandTR808:bd")     // Roland TR-808 bass drum
s("RolandTR909:sd")     // Roland TR-909 snare  
s("GM:AcousticGrandPiano") // General MIDI piano
```

"""
        
        # Add relevant sections from docs
        if sample_sections:
            result += "## From Documentation:\n\n"
            for section in sample_sections[:3]:
                result += section + "\n\n---\n\n"
        
        return result
    
    def _get_drums_info(self) -> str:
        """Get comprehensive drum programming information."""
        return """# Strudel Drums - Complete Guide

## Basic Drum Samples
- `bd` - Bass drum (kick)
- `sd` - Snare drum  
- `hh` - Hi-hat
- `cp` - Clap/handclap
- `rim` - Rim shot
- `perc` - General percussion

## Drum Pattern Examples

### Basic Patterns
```javascript
s("bd sd hh cp")              // 4/4 basic pattern
s("bd ~ sd ~")                // Kick-snare pattern with rests
s("bd bd sd hh")              // Double kick pattern
s("hh*8")                     // Continuous hi-hats
```

### Advanced Patterns  
```javascript
s("bd*2 sd hh*4 cp")          // Mixed timing
s("bd [sd sd] hh cp")         // Subdivisions
s("bd sd:2 hh cp:3")          // Different sample variations
```

## Roland Drum Machines
```javascript
s("RolandTR808:bd")           // Classic 808 kick
s("RolandTR909:sd")           // Classic 909 snare
s("RolandTR707:hh")           // 707 hi-hat
```

## Effects for Drums
```javascript
s("bd sd hh cp").gain(0.8)    // Volume control
s("bd sd hh cp").lpf(800)     // Low-pass filter
s("bd sd hh cp").room(0.3)    // Reverb
s("bd sd hh cp").delay(0.2)   // Echo
```
"""
    
    def _get_effects_info(self) -> str:
        """Get comprehensive effects information."""
        return """# Strudel Effects - Complete Guide

## Basic Effects

### Filters
- `.lpf(frequency)` - Low-pass filter (removes highs)
- `.hpf(frequency)` - High-pass filter (removes lows) 
- `.bpf(frequency)` - Band-pass filter

```javascript
note("c d e f").lpf(800)      // Muffled sound
note("c d e f").hpf(200)      // Bright sound
```

### Volume & Dynamics  
- `.gain(amount)` - Volume (0-1)
- `.amp(amount)` - Amplitude
- `.velocity(amount)` - Note velocity

```javascript
note("c d e f").gain(0.5)     // Half volume
note("c d e f").velocity(0.8) // Softer attack
```

### Spatial Effects
- `.pan(position)` - Stereo position (-1 to 1)
- `.room(amount)` - Reverb (0-1)
- `.size(amount)` - Room size

```javascript
note("c d e f").pan(0.5)      // Right side
note("c d e f").room(0.4)     // Some reverb
```

### Time-based Effects
- `.delay(time)` - Echo delay 
- `.delaytime(time)` - Delay time
- `.delayfeedback(amount)` - Echo feedback

```javascript
note("c d e f").delay(0.3)    // 300ms echo
```

## Chaining Effects
```javascript
note("c d e f")
  .lpf(800)
  .gain(0.7)
  .room(0.3)
  .delay(0.2)
```
"""
    
    def _get_synths_info(self) -> str:
        """Get comprehensive synthesizer information.""" 
        return """# Strudel Synthesizers - Complete Guide

## Basic Waveforms
- `sawtooth` - Bright, buzzy sound
- `square` - Hollow, digital sound  
- `triangle` - Soft, mellow sound
- `sine` - Pure, smooth tone

```javascript
note("c d e f").s("sawtooth")  // Saw wave
note("c d e f").s("square")    // Square wave
note("c d e f").s("triangle")  // Triangle wave
note("c d e f").s("sine")      // Sine wave
```

## Preset Synths
- `piano` - Acoustic piano sound
- `bass` - Bass synthesizer
- `lead` - Lead synthesizer
- `pad` - Atmospheric pad
- `organ` - Organ sound

```javascript
note("c d e f").s("piano")     // Piano
note("c2 eb2 g2").s("bass")    // Bass line
note("c4 e4 g4").s("pad")      // Ambient pad
```

## Synth Parameters
```javascript
note("c d e f")
  .s("sawtooth")
  .lpf(800)           // Filter frequency
  .gain(0.7)          // Volume
  .attack(0.1)        // Attack time
  .decay(0.3)         // Decay time
  .sustain(0.5)       // Sustain level
  .release(0.8)       // Release time
```

## Advanced Synthesis
```javascript
// FM synthesis
note("c d e f").s("fmsawtooth")

// Additive synthesis  
note("c d e f").s("additive")

// Granular synthesis
note("c d e f").s("granular")
```
"""
    
    def _get_timing_info(self) -> str:
        """Get comprehensive timing information."""
        return """# Strudel Timing - Complete Guide

## Basic Timing Functions
- `.slow(factor)` - Slow down by factor
- `.fast(factor)` - Speed up by factor
- `*factor` - Repeat pattern faster
- `/factor` - Play pattern slower

```javascript
note("c d e f").slow(2)        // Half speed
note("c d e f").fast(2)        // Double speed  
note("c d e f")*2              // Repeat twice per cycle
note("c d e f")/2              // Every other cycle
```

## Mini-notation Timing
- `"a b c d"` - 4 events per cycle
- `"a ~ b ~"` - Events with rests (~)
- `"a [b c] d"` - Subdivisions
- `"a*2 b c"` - Event repetition

```javascript
s("bd ~ sd ~")                 // Kick on 1&3, snare on 2&4
s("bd [sd sd] hh cp")          // Snare subdivision
s("hh*8")                      // 8 hi-hats per cycle
```

## Advanced Timing
```javascript
// Euclidean rhythms
s("bd").euclid(3, 8)           // 3 hits in 8 steps

// Time shifting
s("bd sd hh cp").early(0.1)    // Start early
s("bd sd hh cp").late(0.1)     // Start late

// Swing
s("bd sd hh cp").swing(0.1)    // Add groove
```

## Tempo Control
```javascript
// Global tempo (cycles per second)
setcps(0.6)                    // 0.6 cycles per second

// Pattern-specific timing
note("c d e f").cpm(120)       // 120 cycles per minute
```
"""
    
    def _get_patterns_info(self) -> str:
        """Get comprehensive pattern information."""
        return """# Strudel Patterns - Complete Guide

## Pattern Creation
- `seq(a, b, c)` - Sequence patterns
- `cat(a, b, c)` - Concatenate patterns  
- `stack(a, b, c)` - Layer patterns simultaneously
- `"<a b c>"` - Cycle through values

```javascript
seq("c", "d", "e")             // Sequence
cat("c d", "e f")              // Concatenation
stack("c e g", "c2")           // Chord + bass
note("<c d e f>")              // Cycling notes
```

## Pattern Manipulation
- `.rev()` - Reverse pattern
- `.ply(n)` - Repeat each element n times
- `.echo(n, time, feedback)` - Echo effect
- `.superimpose(fn)` - Layer with transformation

```javascript
note("c d e f").rev()          // f e d c
note("c d e f").ply(2)         // c c d d e e f f
note("c d e f").superimpose(x => x.add(7)) // Add harmony
```

## Conditional Patterns
- `.when(condition, function)` - Apply when condition met
- `.chunk(n, function)` - Apply to chunks
- `.sometimes(function)` - Apply randomly sometimes
- `.often(function)` - Apply randomly often

```javascript
note("c d e f").sometimes(x => x.add(12))  // Octave up sometimes
note("c d e f").when(x => x > 0.5, x => x.rev()) // Reverse sometimes
```

## Pattern Structure
```javascript
// 16-bar song structure
stack(
  note("c d e f").chunk(4, x => x.add(7)),    // Verse
  note("g a b c5").chunk(4, x => x.rev()),    // Chorus  
  s("bd ~ sd ~")*16                           // Drums throughout
)
```
"""
    
    def _get_search_suggestions(self, query: str) -> str:
        """Provide helpful suggestions when search fails."""
        suggestions = {
            'bass': ['samples', 'synths', 'note("c2")'],
            'melody': ['note', 'scale', 'chord'],  
            'chord': ['note("[c,e,g]")', 'voicing', 'harmony'],
            'tempo': ['slow', 'fast', 'cps', 'timing'],
            'loop': ['cycle', 'patterns', 'seq'],
            'sound': ['samples', 'synths', 's()'],
            'beat': ['drums', 'patterns', 's("bd sd")'],
            'filter': ['lpf', 'hpf', 'effects'],
            'volume': ['gain', 'amp', 'velocity'],
            'echo': ['delay', 'effects'],
            'reverb': ['room', 'effects']
        }
        
        result = f"No direct matches found for '{query}'.\n\n"
        
        # Find similar terms
        for term, related in suggestions.items():
            if term in query.lower() or any(r in query.lower() for r in related):
                result += f"**Try searching for:** {', '.join(related)}\n"
                break
        
        result += "\n**Common searches:**\n"
        result += "- `samples` - All about samples and drums\n"
        result += "- `effects` - Filters, reverb, delay, etc.\n" 
        result += "- `synths` - Synthesizers and waveforms\n"
        result += "- `timing` - Tempo, rhythm, mini-notation\n"
        result += "- `patterns` - Pattern creation and manipulation\n"
        result += "\n**Or use `get_strudel_docs()` without parameters to browse all documentation.**"
        
        return result
    
    def get_function_list(self) -> str:
        """Get a comprehensive list of all Strudel functions organized by category."""
        functions = self.index.get('functions', {})
        
        if not functions:
            return "Function index not available. Use get_strudel_docs() to browse documentation."
        
        # Group functions by category
        categories = {}
        for func_name, func_info in functions.items():
            category = func_info.get('category', 'misc')
            if category not in categories:
                categories[category] = []
            categories[category].append(func_name)
        
        result = "# Complete Strudel Function Reference\n\n"
        result += f"Total functions indexed: {len(functions)}\n\n"
        
        # Sort categories and functions
        for category in sorted(categories.keys()):
            func_list = sorted(categories[category])
            result += f"## {category.title()} Functions ({len(func_list)})\n\n"
            
            # Format in columns for readability
            for i in range(0, len(func_list), 4):
                row = func_list[i:i+4]
                result += "- " + " | ".join(f"`{func}`" for func in row) + "\n"
            
            result += "\n"
        
        result += "\n## Usage\n"
        result += "Use `get_strudel_docs(function_name=\"functionName\")` to get detailed docs for any function.\n"
        result += "Use `search_strudel_functions(\"keyword\")` to find functions by keyword.\n"
        
        return result
    
    def get_samples_list(self) -> str:
        """Get a comprehensive list of all available samples."""
        return """# Complete Strudel Samples Reference

## Basic Drum Kit
- `bd` - Bass drum (kick)
- `sd` - Snare drum  
- `hh` - Hi-hat (closed)
- `oh` - Open hi-hat
- `cp` - Clap/handclap
- `rim` - Rim shot
- `perc` - General percussion
- `tabla` - Tabla drums
- `kick` - Alternative kick drum
- `snare` - Alternative snare
- `hat` - Alternative hi-hat

## Extended Percussion  
- `crash` - Crash cymbal
- `ride` - Ride cymbal
- `tom` - Tom drums
- `cowbell` - Cowbell
- `shaker` - Shaker
- `tamb` - Tambourine
- `clave` - Clave
- `woodblock` - Woodblock

## Roland Drum Machines
Access with `s("RolandTR808:sample")` format:
- **TR-808**: bd, sd, hh, oh, cp, ma, cl, rs, cb
- **TR-909**: bd, sd, hh, oh, cp, crash, ride
- **TR-707**: bd, sd, hh, oh, cp, tom, crash

## General MIDI Instruments  
Access with `s("GM:InstrumentName")` format:
- **Piano**: AcousticGrandPiano, BrightAcousticPiano, ElectricGrandPiano
- **Organ**: DrawbarOrgan, PercussiveOrgan, RockOrgan, ChurchOrgan
- **Guitar**: AcousticGuitar, ElectricGuitar, OverdrivenGuitar, DistortionGuitar
- **Bass**: AcousticBass, ElectricBass, FretlessBass, SlapBass
- **Strings**: Violin, Viola, Cello, ContrabaBass, Orchestra
- **Brass**: Trumpet, Trombone, Tuba, FrenchHorn, BrassSection
- **Synths**: Lead1, Lead2, Lead3, Pad1, Pad2, Pad3

## Sample Loading from GitHub
```javascript
await samples('github:username/repository/path')
s("sample_name")  // Use after loading
```

## Usage Examples
```javascript
s("bd sd hh cp")                    // Basic pattern
s("RolandTR808:bd RolandTR909:sd")  // Roland samples  
s("GM:AcousticGrandPiano")          // GM instrument
s("bd:2 sd:3 hh:1")                // Sample variations
```
"""
    
    def get_examples(self, pattern_type: str = "all") -> str:
        """Get code examples by pattern type."""
        # Extract code examples from the complete documentation
        lines = self.complete_docs.split('\n')
        examples = []
        
        current_example = None
        in_code_block = False
        
        for line in lines:
            if line.strip().startswith('```javascript') or line.strip().startswith('```js'):
                in_code_block = True
                current_example = {"code": "", "context": ""}
                # Look back for context
                continue
            elif line.strip().startswith('```') and in_code_block:
                in_code_block = False
                if current_example and current_example["code"].strip():
                    examples.append(current_example)
                current_example = None
                continue
            elif in_code_block and current_example is not None:
                current_example["code"] += line + "\n"
        
        if not examples:
            # Fallback to patterns from index
            patterns = self.index.get('common_patterns', [])
            if patterns:
                result = f"# Strudel Examples - {pattern_type.title()}\n\n"
                for pattern in patterns[:10]:
                    result += f"## {pattern.get('description', 'Example')}\n\n"
                    result += f"```javascript\n{pattern['code']}\n```\n\n"
                return result
            else:
                return "No code examples found in documentation."
        
        result = f"# Strudel Code Examples\n\n"
        result += f"Found {len(examples)} code examples from the documentation:\n\n"
        
        # Show first 10 examples
        for i, example in enumerate(examples[:10]):
            result += f"## Example {i+1}\n\n"
            result += f"```javascript\n{example['code'].strip()}\n```\n\n"
        
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
            # Try a broader search in the complete docs
            lines = self.complete_docs.split('\n')
            function_mentions = []
            
            for line in lines:
                if search_lower in line.lower() and ('(' in line or 'function' in line.lower()):
                    function_mentions.append(line.strip())
            
            if function_mentions:
                result = f"# Functions related to '{search_term}'\n\n"
                result += f"No exact function matches, but found {len(function_mentions)} related mentions:\n\n"
                for mention in function_mentions[:10]:
                    result += f"- {mention}\n"
                result += "\nUse get_strudel_docs() with a query to search the full documentation."
                return result
            
            return f"No functions found matching '{search_term}'. Use get_strudel_docs() to browse all available functions."
        
        result = f"# Functions matching '{search_term}'\n\n"
        result += f"Found {len(matches)} matching functions:\n\n"
        
        for func_name, func_info in sorted(matches)[:15]:
            result += f"## {func_name}\n"
            result += f"**Category:** {func_info.get('category', 'unknown')}\n\n"
        
        return result
