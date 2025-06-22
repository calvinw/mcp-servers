#!/usr/bin/env python3
"""
Script to parse and format the Strudel synths and drum machines lists.
"""

import re
from collections import defaultdict

def parse_drum_machines_file(file_path):
    """Parse the drum-machines.txt file to extract GM instruments and synths."""
    
    with open(file_path, 'r') as f:
        content = f.read().strip()
    
    # Split by spaces to get individual items
    items = content.split()
    
    synths = []
    gm_instruments = []
    
    for item in items:
        # Check if it has count in parentheses
        match = re.match(r'([^(]+)\((\d+)\)', item)
        if match:
            name, count = match.groups()
            if name.startswith('gm_'):
                gm_instruments.append({
                    'name': name,
                    'display_name': name.replace('gm_', '').replace('_', ' ').title(),
                    'count': int(count),
                    'category': categorize_gm_instrument(name)
                })
            else:
                # Non-GM instrument with count
                synths.append({
                    'name': name,
                    'count': int(count),
                    'category': categorize_synth(name)
                })
        else:
            # Items without count (basic synths/waveforms)
            synths.append({
                'name': item,
                'count': 1,
                'category': categorize_synth(item)
            })
    
    return synths, gm_instruments

def categorize_synth(name):
    """Categorize synth by type."""
    
    waveforms = ['sine', 'sawtooth', 'square', 'triangle', 'supersaw', 'pulse']
    noise_types = ['white', 'pink', 'brown', 'crackle']
    digital = ['bytebeat', 'zzfx']
    algorithmic = ['z_noise', 'z_sawtooth', 'z_sine', 'z_square', 'z_tan', 'z_triangle']
    
    if name in waveforms:
        return 'Basic Waveforms'
    elif name in noise_types:
        return 'Noise Generators'
    elif name in digital:
        return 'Digital/8-bit'
    elif name.startswith('z_'):
        return 'Algorithmic Synths'
    else:
        return 'Other Synths'

def categorize_gm_instrument(name):
    """Categorize GM instrument by family."""
    
    categories = {
        'Keyboards': [
            'gm_piano', 'gm_epiano1', 'gm_epiano2', 'gm_harpsichord', 'gm_clavinet',
            'gm_celesta', 'gm_glockenspiel', 'gm_music_box', 'gm_vibraphone',
            'gm_marimba', 'gm_xylophone', 'gm_tubular_bells', 'gm_dulcimer'
        ],
        'Organs': [
            'gm_drawbar_organ', 'gm_percussive_organ', 'gm_rock_organ', 'gm_church_organ',
            'gm_reed_organ', 'gm_accordion', 'gm_harmonica', 'gm_bandoneon'
        ],
        'Guitars': [
            'gm_acoustic_guitar_nylon', 'gm_acoustic_guitar_steel', 'gm_electric_guitar_jazz',
            'gm_electric_guitar_clean', 'gm_electric_guitar_muted', 'gm_overdriven_guitar',
            'gm_distortion_guitar', 'gm_guitar_harmonics', 'gm_guitar_fret_noise'
        ],
        'Bass': [
            'gm_acoustic_bass', 'gm_electric_bass_finger', 'gm_electric_bass_pick',
            'gm_fretless_bass', 'gm_slap_bass_1', 'gm_slap_bass_2', 'gm_synth_bass_1',
            'gm_synth_bass_2'
        ],
        'Strings': [
            'gm_violin', 'gm_viola', 'gm_cello', 'gm_contrabass', 'gm_tremolo_strings',
            'gm_pizzicato_strings', 'gm_orchestral_harp', 'gm_timpani', 'gm_string_ensemble_1',
            'gm_string_ensemble_2', 'gm_synth_strings_1', 'gm_synth_strings_2'
        ],
        'Brass': [
            'gm_trumpet', 'gm_trombone', 'gm_tuba', 'gm_muted_trumpet', 'gm_french_horn',
            'gm_brass_section', 'gm_synth_brass_1', 'gm_synth_brass_2'
        ],
        'Woodwinds': [
            'gm_soprano_sax', 'gm_alto_sax', 'gm_tenor_sax', 'gm_baritone_sax',
            'gm_oboe', 'gm_english_horn', 'gm_bassoon', 'gm_clarinet', 'gm_piccolo',
            'gm_flute', 'gm_recorder', 'gm_pan_flute', 'gm_blown_bottle', 'gm_shakuhachi',
            'gm_whistle', 'gm_ocarina'
        ],
        'Vocals': [
            'gm_choir_aahs', 'gm_voice_oohs', 'gm_synth_choir'
        ],
        'Ethnic': [
            'gm_sitar', 'gm_banjo', 'gm_shamisen', 'gm_koto', 'gm_kalimba',
            'gm_bagpipe', 'gm_fiddle', 'gm_shanai', 'gm_steel_drums', 'gm_taiko_drum'
        ],
        'Percussion': [
            'gm_agogo', 'gm_woodblock', 'gm_melodic_tom', 'gm_synth_drum',
            'gm_reverse_cymbal', 'gm_tinkle_bell'
        ],
        'Synth Leads': [
            'gm_lead_1_square', 'gm_lead_2_sawtooth', 'gm_lead_3_calliope',
            'gm_lead_4_chiff', 'gm_lead_5_charang', 'gm_lead_6_voice',
            'gm_lead_7_fifths', 'gm_lead_8_bass_lead'
        ],
        'Synth Pads': [
            'gm_pad_new_age', 'gm_pad_warm', 'gm_pad_poly', 'gm_pad_choir',
            'gm_pad_bowed', 'gm_pad_metallic', 'gm_pad_halo', 'gm_pad_sweep'
        ],
        'Sound Effects': [
            'gm_fx_rain', 'gm_fx_soundtrack', 'gm_fx_crystal', 'gm_fx_atmosphere',
            'gm_fx_brightness', 'gm_fx_goblins', 'gm_fx_echoes', 'gm_fx_sci_fi',
            'gm_bird_tweet', 'gm_telephone', 'gm_helicopter', 'gm_applause',
            'gm_gunshot', 'gm_seashore', 'gm_breath_noise', 'gm_orchestra_hit'
        ]
    }
    
    for category, instruments in categories.items():
        if name in instruments:
            return category
    
    return 'Other'

def generate_synths_markdown(synths):
    """Generate markdown documentation for synths."""
    
    # Group by category
    by_category = defaultdict(list)
    for synth in synths:
        by_category[synth['category']].append(synth)
    
    # Sort categories and synths
    sorted_categories = sorted(by_category.keys())
    for category in sorted_categories:
        by_category[category].sort(key=lambda x: x['name'])
    
    total_synths = len(synths)
    
    markdown = f"""# Strudel Synthesizers Reference

This is a comprehensive reference of all available synthesizers and sound generators in Strudel.

## Summary

- **Total Synthesizers**: {total_synths}
- **Categories**: {len(sorted_categories)}

## Usage

Use these synths with the `sound()` or `s()` function:
```javascript
note("c d e f").sound("sawtooth")  // Basic waveform
note("c d e f").s("sine")          // Alternative syntax
sound("white pink brown")          // Noise generators
```

For synths with variations, use the `n` parameter:
```javascript
note("c d e f").sound("sawtooth").n("<1 2 4 8>")  // Harmonic partials
```

## Categories

"""
    
    for category in sorted_categories:
        synths_in_category = by_category[category]
        
        markdown += f"### {category}\n\n"
        markdown += f"*{len(synths_in_category)} synthesizers*\n\n"
        
        if category == 'Basic Waveforms':
            markdown += """These are the fundamental waveforms available in Strudel:

| Synth Name | Description | Usage Example |
|------------|-------------|---------------|
"""
            waveform_descriptions = {
                'sine': 'Pure sine wave - smooth, fundamental tone',
                'sawtooth': 'Bright, buzzy sawtooth wave - rich in harmonics', 
                'square': 'Hollow square wave - classic digital sound',
                'triangle': 'Soft triangle wave - default for notes',
                'pulse': 'Variable pulse width wave',
                'supersaw': 'Multiple detuned sawtooth waves - thick lead sound'
            }
            
            for synth in synths_in_category:
                desc = waveform_descriptions.get(synth['name'], 'Basic waveform')
                markdown += f"| `{synth['name']}` | {desc} | `note(\"c d e f\").sound(\"{synth['name']}\")` |\n"
        
        elif category == 'Noise Generators':
            markdown += """Different types of noise for percussion and textures:

| Synth Name | Description | Usage Example |
|------------|-------------|---------------|
"""
            noise_descriptions = {
                'white': 'White noise - equal energy across all frequencies',
                'pink': 'Pink noise - softer, more natural than white',
                'brown': 'Brown noise - deepest, smoothest noise',
                'crackle': 'Subtle noise crackles - use with density parameter'
            }
            
            for synth in synths_in_category:
                desc = noise_descriptions.get(synth['name'], 'Noise generator')
                markdown += f"| `{synth['name']}` | {desc} | `sound(\"{synth['name']}\").decay(0.1)` |\n"
        
        else:
            markdown += "| Synth Name | Usage Example |\n"
            markdown += "|------------|---------------|\n"
            
            for synth in synths_in_category:
                example = f'`sound("{synth["name"]}")`'
                markdown += f"| `{synth['name']}` | {example} |\n"
        
        markdown += "\n"
    
    markdown += """## Examples

### Basic Synthesis
```javascript
// Classic analog-style lead
note("c4 d4 e4 f4 g4").sound("sawtooth").lpf(800).resonance(5)

// Warm pad
note("c3 e3 g3").sound("triangle").attack(0.5).release(2).gain(0.3)

// Percussive noise hits
sound("white pink brown").decay(0.1).lpf("<400 800 1200>")
```

### Advanced Techniques
```javascript
// FM synthesis
note("c d e f").sound("sine").fm(2).fmh(0.5)

// Additive synthesis - limiting harmonics
note("c2 e2 g2").sound("sawtooth").n("<1 2 4 8 16>")

// Noise with filtering
sound("crackle*8").density(0.1).lpf(2000).hpf(100)
```

### Sound Design
```javascript
// Ambient texture
stack(
  note("c2").sound("triangle").slow(8).attack(2).release(4),
  sound("pink").gain(0.1).lpf(200).slow(4)
)

// Digital chaos
sound("bytebeat zzfx").fast(4).distort(0.3).delay(0.125)
```

## Synthesis Parameters

Strudel synths can be modified with various parameters:

- **Envelope**: `attack`, `decay`, `sustain`, `release`
- **Filter**: `lpf`, `hpf`, `resonance`, `cutoff`
- **Modulation**: `fm`, `fmh`, `vib`, `vibmod`
- **Effects**: `distort`, `delay`, `reverb`, `chorus`
- **Harmonics**: `n` (for additive synthesis)

For more synthesis techniques, see the [Synths Tutorial](/learn/synths).
"""
    
    return markdown

def generate_gm_instruments_markdown(gm_instruments):
    """Generate markdown documentation for GM instruments."""
    
    # Group by category
    by_category = defaultdict(list)
    for instrument in gm_instruments:
        by_category[instrument['category']].append(instrument)
    
    # Sort categories and instruments
    sorted_categories = sorted(by_category.keys())
    for category in sorted_categories:
        by_category[category].sort(key=lambda x: x['display_name'])
    
    total_instruments = len(gm_instruments)
    total_variations = sum(instr['count'] for instr in gm_instruments)
    
    markdown = f"""# General MIDI Instruments Reference

This is a comprehensive reference of all General MIDI instruments available in Strudel. These are high-quality sampled instruments that follow the GM standard.

## Summary

- **Total Instruments**: {total_instruments}
- **Total Variations**: {total_variations}
- **Categories**: {len(sorted_categories)}

## Usage

Use these instruments with the `sound()` or `s()` function:
```javascript
note("c d e f").sound("gm_piano")      // GM Piano
note("c d e f").s("gm_violin")        // GM Violin
note("c d e f").sound("gm_trumpet:0") // Specific variation
```

Select variations with the colon notation:
```javascript
s("gm_piano:0 gm_piano:15 gm_piano:31")  // Different piano samples
```

## Categories

"""
    
    for category in sorted_categories:
        instruments_in_category = by_category[category]
        category_variations = sum(instr['count'] for instr in instruments_in_category)
        
        markdown += f"### {category}\n\n"
        markdown += f"*{len(instruments_in_category)} instruments, {category_variations} variations*\n\n"
        markdown += "| Instrument | Variations | Display Name | Usage Example |\n"
        markdown += "|------------|------------|--------------|---------------|\n"
        
        for instrument in instruments_in_category:
            example = f'`s("{instrument["name"]}")`'
            if instrument['count'] > 1:
                example += f' or `s("{instrument["name"]}:0 {instrument["name"]}:{instrument["count"]-1}")`'
            
            markdown += f"| `{instrument['name']}` | {instrument['count']} | {instrument['display_name']} | {example} |\n"
        
        markdown += "\n"
    
    markdown += """## Examples

### Classical Orchestra
```javascript
stack(
  note("c4 d4 e4 f4").sound("gm_violin").gain(0.6),
  note("g3 a3 b3 c4").sound("gm_viola").gain(0.5),
  note("c3 d3 e3 f3").sound("gm_cello").gain(0.7),
  note("c2 g2").sound("gm_contrabass").slow(2)
)
```

### Jazz Ensemble
```javascript
stack(
  note("c4 e4 g4 bb4").sound("gm_piano").slow(2),
  note("c2 g2").sound("gm_acoustic_bass").slow(2),
  note("c5 d5 eb5").sound("gm_alto_sax"),
  s("~ gm_brush_snare ~ gm_brush_snare").gain(0.4)
)
```

### Ethnic Instruments
```javascript
stack(
  note("c d e g a").sound("gm_sitar").slow(3),
  note("c5 d5 e5").sound("gm_kalimba"),
  s("gm_taiko_drum ~ ~ gm_taiko_drum:5").slow(2)
)
```

### Electronic Sounds
```javascript
stack(
  note("c2 e2 g2").sound("gm_synth_bass_1"),
  note("c4 e4 g4").sound("gm_lead_2_sawtooth").gain(0.6),
  note("c3 e3 g3 c4").sound("gm_pad_new_age").slow(4).gain(0.3)
)
```

### Sound Effects
```javascript
// Atmospheric soundscape
stack(
  s("gm_seashore").slow(8).gain(0.2),
  s("gm_fx_atmosphere").slow(6).gain(0.3),
  s("~ ~ gm_bird_tweet ~").slow(4).gain(0.5)
)
```

## Instrument Families

The General MIDI specification organizes instruments into families:

- **Keyboards**: Pianos, electric pianos, harpsichords, organs
- **Guitars**: Acoustic and electric guitars with various techniques
- **Bass**: Acoustic and electric bass instruments
- **Strings**: Orchestral strings and ensembles
- **Brass**: Trumpets, trombones, french horns, brass sections
- **Woodwinds**: Saxophones, flutes, clarinets, oboes
- **Vocals**: Choir sounds and voice effects
- **Ethnic**: Traditional instruments from various cultures
- **Synth Leads**: Electronic lead synthesizers
- **Synth Pads**: Electronic pad and atmosphere sounds
- **Sound Effects**: Nature sounds, mechanical sounds, special effects

For more information about using samples and instruments, see the [Samples Tutorial](/learn/samples).
"""
    
    return markdown

def main():
    file_path = "docs_processed/drum-machines.txt"
    
    # Parse the file
    synths, gm_instruments = parse_drum_machines_file(file_path)
    
    # Generate synths documentation
    synths_markdown = generate_synths_markdown(synths)
    with open("docs_processed/synths-reference.md", 'w') as f:
        f.write(synths_markdown)
    
    # Generate GM instruments documentation  
    gm_markdown = generate_gm_instruments_markdown(gm_instruments)
    with open("docs_processed/gm-instruments-reference.md", 'w') as f:
        f.write(gm_markdown)
    
    print(f"Generated synths documentation: docs_processed/synths-reference.md")
    print(f"Total synths: {len(synths)}")
    print(f"Generated GM instruments documentation: docs_processed/gm-instruments-reference.md") 
    print(f"Total GM instruments: {len(gm_instruments)}")
    print(f"Total GM variations: {sum(instr['count'] for instr in gm_instruments)}")

if __name__ == "__main__":
    main()