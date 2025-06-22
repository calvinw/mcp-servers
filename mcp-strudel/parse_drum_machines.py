#!/usr/bin/env python3
"""
Script to parse and format the Strudel drum machines list.
"""

import re
from collections import defaultdict

def parse_drum_machines_file(file_path):
    """Parse the drum-machines.txt file to extract drum machine models and sounds."""
    
    with open(file_path, 'r') as f:
        content = f.read().strip()
    
    # Split by spaces to get individual items
    items = content.split()
    
    drum_machines = []
    
    for item in items:
        # Check if it has count in parentheses
        match = re.match(r'([^(]+)\((\d+)\)', item)
        if match:
            name, count = match.groups()
            drum_machines.append({
                'name': name,
                'count': int(count),
                'machine': extract_machine_name(name),
                'drum_type': extract_drum_type(name)
            })
        else:
            # Items without count - basic drum types
            drum_machines.append({
                'name': item,
                'count': 1,
                'machine': extract_machine_name(item),
                'drum_type': extract_drum_type(item)
            })
    
    return drum_machines

def extract_machine_name(name):
    """Extract the drum machine model from the sample name."""
    
    # Common prefixes/machine names
    machines = {
        '9000': 'Linn 9000',
        'ace': 'Roland CR-78 (Ace Tone)',
        'ajkpercusyn': 'AJK Percusyn',
        'akailinn': 'Akai Linn',
        'akaimpc60': 'Akai MPC60',
        'akaixr10': 'Akai XR10',
        'alesishr16': 'Alesis HR-16',
        'alesissr16': 'Alesis SR-16',
        'bossdr110': 'Boss DR-110',
        'bossdr220': 'Boss DR-220',
        'bossdr55': 'Boss DR-55',
        'bossdr550': 'Boss DR-550',
        'casiorz1': 'Casio RZ-1',
        'casiosk1': 'Casio SK-1',
        'casiovl1': 'Casio VL-1',
        'circuitsdrumtracks': 'Sequential Circuits Drum Tracks',
        'circuitstom': 'Sequential Circuits Tom',
        'compurhythm1000': 'Roland CompuRhythm CR-1000',
        'compurhythm78': 'Roland CompuRhythm CR-78',
        'compurhythm8000': 'Roland CompuRhythm CR-8000',
        'concertmatemg1': 'Moog Concertmate MG-1',
        'd110': 'Roland D-110',
        'd70': 'Roland D-70',
        'ddm110': 'Korg DDM-110',
        'ddr30': 'Roland DDR-30',
        'dmx': 'Oberheim DMX',
        'doepferms404': 'Doepfer MS-404',
        'dpm48': 'Sakata DPM-48',
        'dr110': 'Roland DR-110',
        'dr220': 'Roland DR-220',
        'dr55': 'Roland DR-55',
        'dr550': 'Roland DR-550',
        'drumulator': 'E-mu Drumulator',
        'emudrumulator': 'E-mu Drumulator',
        'emumodular': 'E-mu Modular',
        'emusp12': 'E-mu SP-12',
        'hr16': 'Alesis HR-16',
        'jd990': 'Roland JD-990',
        'korg': 'Korg',
        'kpr77': 'Korg KPR-77',
        'kr55': 'Korg KR-55',
        'krz': 'Korg Krz',
        'linn': 'LinnDrum',
        'linn9000': 'Linn 9000',
        'linndrum': 'LinnDrum',
        'linnlm1': 'Linn LM-1',
        'linnlm2': 'Linn LM-2',
        'lm1': 'Linn LM-1',
        'lm2': 'Linn LM-2',
        'lm8953': 'Linn LM-8953',
        'm1': 'Korg M1',
        'mc202': 'Roland MC-202',
        'mc303': 'Roland MC-303',
        'mfb512': 'MFB-512',
        'microrhythmer12': 'Univox MicroRhythmer 12',
        'minipops': 'Korg Mini Pops',
        'moogconcertmatemg1': 'Moog Concertmate MG-1',
        'mpc1000': 'Akai MPC1000',
        'mpc60': 'Akai MPC60',
        'mridangam': 'Mridangam (Indian percussion)',
        'ms404': 'Doepfer MS-404',
        'mt32': 'Roland MT-32',
        'oberheim': 'Oberheim',
        'oberheimdmx': 'Oberheim DMX',
        'percysyn': 'AJK Percusyn',
        'polaris': 'Rhodes Polaris',
        'poly800': 'Korg Poly-800',
        'r8': 'Roland R-8',
        'r88': 'SoundMaster SR-88',
        'rhodespolaris': 'Rhodes Polaris',
        'rhythmace': 'Ace Tone Rhythm Ace',
        'rm50': 'Yamaha RM50',
        'roland': 'Roland',
        'rx21': 'Yamaha RX21',
        'rx5': 'Yamaha RX5',
        'ry30': 'Yamaha RY30',
        'rz1': 'Casio RZ-1',
        's50': 'Roland S-50',
        'sakata': 'Sakata',
        'sds400': 'Simmons SDS-400',
        'sds5': 'Simmons SDS-5',
        'sergemodular': 'Serge Modular',
        'sh09': 'Roland SH-09',
        'simmons': 'Simmons',
        'sk1': 'Casio SK-1',
        'soundmaster': 'SoundMaster',
        'sp12': 'E-mu SP-12',
        'spacedrum': 'Visco Space Drum',
        'sr16': 'Alesis SR-16',
        'system100': 'Roland System-100',
        't3': 'Korg T3',
        'tg33': 'Yamaha TG33',
        'tr505': 'Roland TR-505',
        'tr606': 'Roland TR-606',
        'tr626': 'Roland TR-626',
        'tr707': 'Roland TR-707',
        'tr727': 'Roland TR-727',
        'tr808': 'Roland TR-808',
        'tr909': 'Roland TR-909',
        'univox': 'Univox',
        'visco': 'Visco',
        'vl1': 'Casio VL-1',
        'xdrum': 'X-Drum',
        'xr10': 'Akai XR10',
        'yamaha': 'Yamaha'
    }
    
    # Find the longest matching prefix
    best_match = 'Unknown'
    for prefix, machine in machines.items():
        if name.lower().startswith(prefix.lower()):
            if len(prefix) > len(best_match) or best_match == 'Unknown':
                best_match = machine
    
    return best_match

def extract_drum_type(name):
    """Extract the drum type from the sample name."""
    
    # Extract the suffix (drum type)
    parts = name.split('_')
    if len(parts) > 1:
        drum_suffix = parts[-1]
    else:
        drum_suffix = name
    
    # Map common drum abbreviations
    drum_types = {
        'bd': 'Bass Drum/Kick',
        'sd': 'Snare Drum',
        'hh': 'Hi-Hat (Closed)',
        'oh': 'Hi-Hat (Open)',
        'cp': 'Clap',
        'cr': 'Crash Cymbal',
        'rd': 'Ride Cymbal',
        'ht': 'High Tom',
        'mt': 'Mid Tom',
        'lt': 'Low Tom',
        'cb': 'Cowbell',
        'rim': 'Rimshot',
        'sh': 'Shaker',
        'tb': 'Tambourine',
        'perc': 'Percussion',
        'misc': 'Miscellaneous',
        'fx': 'Effects'
    }
    
    return drum_types.get(drum_suffix.lower(), drum_suffix.title())

def generate_drum_machines_markdown(drum_machines):
    """Generate markdown documentation for drum machines."""
    
    # Group by machine
    by_machine = defaultdict(list)
    for drum in drum_machines:
        by_machine[drum['machine']].append(drum)
    
    # Sort machines and drums within each machine
    sorted_machines = sorted(by_machine.keys())
    for machine in sorted_machines:
        by_machine[machine].sort(key=lambda x: (x['drum_type'], x['name']))
    
    total_drums = len(drum_machines)
    total_variations = sum(drum['count'] for drum in drum_machines)
    total_machines = len(sorted_machines)
    
    markdown = f"""# Strudel Drum Machines Reference

This is a comprehensive reference of all classic drum machine samples available in Strudel. These are authentic samples from legendary drum machines that shaped electronic music history.

## Summary

- **Total Drum Machines**: {total_machines}
- **Total Drum Samples**: {total_drums}
- **Total Variations**: {total_variations}

## Usage

Use these drum machine samples with the `s()` function:
```javascript
s("tr808_bd tr808_sd tr808_hh tr808_oh")  // Classic TR-808 pattern
s("tr909_bd tr909_sd tr909_hh")          // TR-909 house beat
s("linndrum_bd:0 linndrum_sd:2")         // Specific LinnDrum variations
```

Access specific variations with colon notation:
```javascript
s("tr808_bd:0 tr808_bd:12 tr808_bd:24")  // Different TR-808 bass drums
```

Use with `.bank()` for cleaner notation:
```javascript
s("bd sd hh oh").bank("tr808")           // Equivalent to tr808_bd tr808_sd etc.
```

## Classic Drum Machines

"""
    
    # Group machines by era/manufacturer for better organization
    machine_categories = {
        'Roland TR Series (Classic)': [
            'Roland TR-808', 'Roland TR-909', 'Roland TR-707', 'Roland TR-727',
            'Roland TR-606', 'Roland TR-626', 'Roland TR-505'
        ],
        'Roland CR Series': [
            'Roland CompuRhythm CR-78', 'Roland CompuRhythm CR-1000', 
            'Roland CompuRhythm CR-8000', 'Roland CR-78 (Ace Tone)'
        ],
        'Roland DR/R Series': [
            'Roland DR-55', 'Roland DR-110', 'Roland DR-220', 'Roland DR-550',
            'Roland R-8', 'Roland DDR-30'
        ],
        'Linn Electronics': [
            'LinnDrum', 'Linn LM-1', 'Linn LM-2', 'Linn 9000'
        ],
        'Oberheim': [
            'Oberheim DMX'
        ],
        'E-mu': [
            'E-mu Drumulator', 'E-mu SP-12'
        ],
        'Akai': [
            'Akai MPC60', 'Akai MPC1000', 'Akai XR10'
        ],
        'Alesis': [
            'Alesis HR-16', 'Alesis SR-16'
        ],
        'Yamaha': [
            'Yamaha RX5', 'Yamaha RX21', 'Yamaha RY30', 'Yamaha TG33', 'Yamaha RM50'
        ],
        'Korg': [
            'Korg DDM-110', 'Korg KPR-77', 'Korg KR-55', 'Korg M1', 'Korg Mini Pops',
            'Korg Poly-800', 'Korg T3'
        ],
        'Casio': [
            'Casio RZ-1', 'Casio SK-1', 'Casio VL-1'
        ],
        'Boss': [
            'Boss DR-55', 'Boss DR-110', 'Boss DR-220', 'Boss DR-550'
        ],
        'Simmons': [
            'Simmons SDS-5', 'Simmons SDS-400'
        ],
    }
    
    # Add any machines not in the above categories to "Other Classics"
    categorized_machines = set()
    for cat_machines in machine_categories.values():
        categorized_machines.update(cat_machines)
    
    other_machines = [machine for machine in sorted_machines 
                     if machine not in categorized_machines]
    
    if other_machines:
        machine_categories['Other Classics'] = other_machines
    
    for category, category_machines in machine_categories.items():
        if not category_machines:
            continue
            
        # Filter to only machines we actually have
        available_machines = [m for m in category_machines if m in by_machine]
        if not available_machines:
            continue
            
        markdown += f"### {category}\n\n"
        
        for machine in available_machines:
            drums_in_machine = by_machine[machine]
            machine_variations = sum(drum['count'] for drum in drums_in_machine)
            
            markdown += f"#### {machine}\n"
            markdown += f"*{len(drums_in_machine)} drum types, {machine_variations} variations*\n\n"
            markdown += "| Sample Name | Type | Variations | Usage Example |\n"
            markdown += "|-------------|------|------------|---------------|\n"
            
            for drum in drums_in_machine:
                example = f'`s("{drum["name"]}")`'
                if drum['count'] > 1:
                    example += f' or `s("{drum["name"]}:0 {drum["name"]}:{drum["count"]-1}")`'
                
                markdown += f"| `{drum['name']}` | {drum['drum_type']} | {drum['count']} | {example} |\n"
            
            markdown += "\n"
    
    markdown += """## Classic Patterns

### TR-808 Hip-Hop Beat
```javascript
stack(
  s("tr808_bd ~ tr808_bd ~"),
  s("~ tr808_sd ~ tr808_sd"),
  s("tr808_hh*8").gain(0.6)
)
```

### TR-909 House Pattern  
```javascript
stack(
  s("tr909_bd*4"),
  s("~ tr909_sd ~ tr909_sd"),
  s("tr909_hh*16").gain(0.4),
  s("~ ~ ~ tr909_oh").slow(2)
)
```

### LinnDrum Pop Beat
```javascript
stack(
  s("linndrum_bd ~ ~ linndrum_bd"),
  s("~ linndrum_sd ~ linndrum_sd"),
  s("linndrum_hh*8").gain(0.5)
)
```

### Oberheim DMX Electro
```javascript
stack(
  s("dmx_bd ~ dmx_bd ~"),
  s("~ dmx_sd ~ dmx_cp"),
  s("dmx_hh*4").gain(0.7)
)
```

## Drum Machine History

**Roland TR-808** (1980): The legendary bass-heavy drum machine that defined hip-hop, rap, and electronic music. Famous for its distinctive analog kick drum and crisp hi-hats.

**Roland TR-909** (1983): The house music standard with punchy kicks, snappy snares, and sizzling hi-hats. Combined analog and digital sounds.

**LinnDrum** (1982): Used digital samples for realistic drum sounds. Dominated 80s pop and R&B productions.

**Oberheim DMX** (1981): Early digital drum machine with distinctive gritty character, popular in early hip-hop and electro.

**E-mu SP-12** (1985): Sampler/sequencer that allowed custom sounds while maintaining the classic drum machine workflow.

For more about using drum samples and patterns, see the [Samples Tutorial](/learn/samples).
"""
    
    return markdown

def main():
    file_path = "docs_processed/drum-machines.txt"
    
    # Parse the file
    drum_machines = parse_drum_machines_file(file_path)
    
    # Generate drum machines documentation
    markdown = generate_drum_machines_markdown(drum_machines)
    with open("docs_processed/drum-machines-reference.md", 'w') as f:
        f.write(markdown)
    
    print(f"Generated drum machines documentation: docs_processed/drum-machines-reference.md")
    print(f"Total drum samples: {len(drum_machines)}")
    print(f"Total variations: {sum(drum['count'] for drum in drum_machines)}")
    print(f"Total machines: {len(set(drum['machine'] for drum in drum_machines))}")

if __name__ == "__main__":
    main()