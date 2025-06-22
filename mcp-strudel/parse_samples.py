#!/usr/bin/env python3
"""
Script to parse and format the comprehensive Strudel samples list.
"""

import re
from collections import defaultdict

def parse_samples_list(samples_text):
    """Parse the samples list into structured data."""
    
    # Extract sample entries with pattern: name(count)
    pattern = r'(\w+)\((\d+)\)'
    matches = re.findall(pattern, samples_text)
    
    samples = []
    for name, count in matches:
        samples.append({
            'name': name,
            'count': int(count),
            'category': categorize_sample(name)
        })
    
    return samples

def categorize_sample(name):
    """Categorize samples by instrument type."""
    
    # Define categories based on instrument families
    categories = {
        'Percussion': [
            'agogo', 'anvil', 'ballwhistle', 'bassdrum1', 'bassdrum2', 'belltree', 'bongo', 
            'brakedrum', 'cabasa', 'cajon', 'clap', 'clash', 'clash2', 'clave', 'conga', 
            'cowbell', 'darbuka', 'fingercymbal', 'flexatone', 'framedrum', 'gong', 'gong2', 
            'guiro', 'handbells', 'handchimes', 'marktrees', 'ratchet', 'shaker_large', 
            'shaker_small', 'siren', 'slapstick', 'sleighbells', 'slitdrum', 'snare_hi', 
            'snare_low', 'snare_modern', 'snare_rim', 'sus_cymbal', 'sus_cymbal2', 'tambourine', 
            'tambourine2', 'timpani', 'timpani_roll', 'timpani2', 'tom_mallet', 'tom_rim', 
            'tom_stick', 'tom2_mallet', 'tom2_rim', 'tom2_stick', 'trainwhistle', 'triangles', 
            'tubularbells', 'tubularbells2', 'vibraslap', 'woodblock'
        ],
        'Mallet Instruments': [
            'balafon', 'balafon_hard', 'balafon_soft', 'glockenspiel', 'kalimba', 'kalimba2', 
            'kalimba3', 'kalimba4', 'kalimba5', 'marimba', 'vibraphone', 'vibraphone_bowed', 
            'vibraphone_soft', 'xylophone_hard_ff', 'xylophone_hard_pp', 'xylophone_medium_ff', 
            'xylophone_medium_pp', 'xylophone_soft_ff', 'xylophone_soft_pp'
        ],
        'Keyboards': [
            'casio', 'clavisynth', 'fmpiano', 'kawai', 'piano', 'piano1', 'steinway'
        ],
        'Organs': [
            'organ_4inch', 'organ_8inch', 'organ_full', 'pipeorgan_loud', 'pipeorgan_loud_pedal', 
            'pipeorgan_quiet', 'pipeorgan_quiet_pedal'
        ],
        'Strings': [
            'folkharp', 'harp', 'psaltery_bow', 'psaltery_pluck', 'psaltery_spiccato', 'strumstick'
        ],
        'Wind Instruments': [
            'didgeridoo', 'harmonica', 'harmonica_soft', 'harmonica_vib', 'ocarina', 'ocarina_small', 
            'ocarina_small_stacc', 'ocarina_vib', 'recorder_alto_stacc', 'recorder_alto_sus', 
            'recorder_alto_vib', 'recorder_bass_stacc', 'recorder_bass_sus', 'recorder_bass_vib', 
            'recorder_soprano_stacc', 'recorder_soprano_sus', 'recorder_tenor_stacc', 
            'recorder_tenor_sus', 'recorder_tenor_vib', 'sax', 'sax_stacc', 'sax_vib', 'saxello', 
            'saxello_stacc', 'saxello_vib'
        ],
        'Ethnic/World': [
            'dantranh', 'dantranh_tremolo', 'dantranh_vibrato', 'east'
        ],
        'Electronic/Synth': [
            'super64', 'super64_acc', 'super64_vib'
        ],
        'Sound Effects': [
            'crow', 'insect', 'oceandrum', 'space', 'wind', 'wineglass', 'wineglass_slow'
        ],
        'Drum Kit': [
            'hihat'
        ],
        'Misc': [
            'jazz', 'metal', 'num', 'numbers'
        ]
    }
    
    # Find which category the sample belongs to
    for category, sample_list in categories.items():
        if name in sample_list:
            return category
    
    return 'Uncategorized'

def generate_samples_markdown(samples):
    """Generate markdown documentation for the samples."""
    
    # Group samples by category
    by_category = defaultdict(list)
    for sample in samples:
        by_category[sample['category']].append(sample)
    
    # Sort categories and samples within each category
    sorted_categories = sorted(by_category.keys())
    for category in sorted_categories:
        by_category[category].sort(key=lambda x: x['name'])
    
    total_samples = len(samples)
    total_variations = sum(sample['count'] for sample in samples)
    
    markdown = f"""# Strudel Instrument Samples Reference

This is a comprehensive reference of all available instrument samples in Strudel. These samples are from the VCSL (Virtual Community Sample Library) collection.

## Summary

- **Total Instruments**: {total_samples}
- **Total Sample Variations**: {total_variations}
- **Categories**: {len(sorted_categories)}

## Usage

Use these samples with the `s()` function:
```javascript
s("piano harp sax")  // Play different instruments
s("piano:0 piano:5 piano:10")  // Select specific variations
```

## Categories

"""
    
    for category in sorted_categories:
        samples_in_category = by_category[category]
        category_variations = sum(sample['count'] for sample in samples_in_category)
        
        markdown += f"### {category}\n\n"
        markdown += f"*{len(samples_in_category)} instruments, {category_variations} variations*\n\n"
        markdown += "| Sample Name | Variations | Usage Example |\n"
        markdown += "|-------------|------------|---------------|\n"
        
        for sample in samples_in_category:
            example = f'`s("{sample["name"]}")`'
            if sample['count'] > 1:
                example += f' or `s("{sample["name"]}:0 {sample["name"]}:{sample["count"]-1}")`'
            
            markdown += f"| `{sample['name']}` | {sample['count']} | {example} |\n"
        
        markdown += "\n"
    
    markdown += """## Examples

### Basic Instrument Patterns
```javascript
// Piano melody
note("c d e f g").s("piano")

// Harp arpeggios  
note("c e g c5").s("harp").slow(2)

// Saxophone improvisation
note("c d eb f g").s("sax").gain(0.7)
```

### Percussion Ensemble
```javascript
// Traditional percussion
stack(
  s("bongo conga"),
  s("~ tambourine ~ tambourine"), 
  s("~ ~ shaker_small ~").fast(2)
)
```

### Mallet Instruments
```javascript
// Gamelan-style patterns
stack(
  note("c e g").s("glockenspiel").slow(3),
  note("c2 g2").s("marimba").slow(2),
  note("c4 d4 e4 g4").s("kalimba")
)
```

### World Music
```javascript
// Asian instruments
stack(
  note("c d e g a").s("dantranh"),
  s("~ gong ~ gong2").slow(2)
)
```

## Loading and Availability

These samples are loaded by default when using Strudel. They are part of the VCSL collection and don't require additional loading with the `samples()` function.

For more information about samples in Strudel, see the [Samples Tutorial](/learn/samples).
"""
    
    return markdown

def main():
    # Input samples list
    samples_text = """agogo(5) anvil(9) balafon(6) balafon_hard(6) balafon_soft(6) ballwhistle(2) bassdrum1(8) bassdrum2(30) belltree(6) bongo(28) brakedrum(17) cabasa(6) cajon(18) casio(3) clap(10) clash(10) clash2(5) clave(6) clavisynth(19) conga(34) cowbell(13) crow(4) dantranh(17) dantranh_tremolo(16) dantranh_vibrato(16) darbuka(20) didgeridoo(12) east(9) fingercymbal(1) flexatone(8) fmpiano(22) folkharp(29) framedrum(18) glockenspiel(7) gong(7) gong2(6) guiro(5) handbells(3) handchimes(19) harmonica(9) harmonica_soft(10) harmonica_vib(10) harp(23) hihat(15) insect(3) jazz(8) kalimba(11) kalimba2(25) kalimba3(22) kalimba4(22) kalimba5(14) kawai(37) marimba(10) marktrees(6) metal(10) num(21) numbers(9) ocarina(11) ocarina_small(10) ocarina_small_stacc(13) ocarina_vib(10) oceandrum(3) organ_4inch(27) organ_8inch(27) organ_full(27) piano(29) piano1(22) pipeorgan_loud(21) pipeorgan_loud_pedal(11) pipeorgan_quiet(21) pipeorgan_quiet_pedal(11) psaltery_bow(11) psaltery_pluck(11) psaltery_spiccato(11) ratchet(8) recorder_alto_stacc(12) recorder_alto_sus(12) recorder_alto_vib(12) recorder_bass_stacc(15) recorder_bass_sus(12) recorder_bass_vib(14) recorder_soprano_stacc(12) recorder_soprano_sus(13) recorder_tenor_stacc(12) recorder_tenor_sus(13) recorder_tenor_vib(14) sax(23) sax_stacc(23) sax_vib(19) saxello(8) saxello_stacc(8) saxello_vib(8) shaker_large(6) shaker_small(16) siren(5) slapstick(5) sleighbells(6) slitdrum(6) snare_hi(8) snare_low(20) snare_modern(72) snare_rim(4) space(18) steinway(42) strumstick(19) super64(13) super64_acc(13) super64_vib(13) sus_cymbal(25) sus_cymbal2(23) tambourine(7) tambourine2(7) timpani(30) timpani_roll(10) timpani2(204) tom_mallet(8) tom_rim(6) tom_stick(8) tom2_mallet(8) tom2_rim(6) tom2_stick(8) trainwhistle(6) triangles(37) tubularbells(9) tubularbells2(11) vibraphone(11) vibraphone_bowed(6) vibraphone_soft(11) vibraslap(4) wind(10) wineglass(4) wineglass_slow(4) woodblock(10) xylophone_hard_ff(8) xylophone_hard_pp(8) xylophone_medium_ff(8) xylophone_medium_pp(8) xylophone_soft_ff(8) xylophone_soft_pp(8)"""
    
    # Parse samples
    samples = parse_samples_list(samples_text)
    
    # Generate markdown
    markdown = generate_samples_markdown(samples)
    
    # Write to file
    output_file = "docs_processed/instrument-samples.md"
    with open(output_file, 'w') as f:
        f.write(markdown)
    
    print(f"Generated instrument samples documentation: {output_file}")
    print(f"Total instruments: {len(samples)}")
    print(f"Total variations: {sum(sample['count'] for sample in samples)}")

if __name__ == "__main__":
    main()