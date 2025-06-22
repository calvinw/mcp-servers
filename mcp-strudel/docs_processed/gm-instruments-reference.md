# General MIDI Instruments Reference

This is a comprehensive reference of all General MIDI instruments available in Strudel. These are high-quality sampled instruments that follow the GM standard.

## Summary

- **Total Instruments**: 125
- **Total Variations**: 871
- **Categories**: 13

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

### Bass

*8 instruments, 40 variations*

| Instrument | Variations | Display Name | Usage Example |
|------------|------------|--------------|---------------|
| `gm_acoustic_bass` | 4 | Acoustic Bass | `s("gm_acoustic_bass")` or `s("gm_acoustic_bass:0 gm_acoustic_bass:3")` |
| `gm_electric_bass_finger` | 4 | Electric Bass Finger | `s("gm_electric_bass_finger")` or `s("gm_electric_bass_finger:0 gm_electric_bass_finger:3")` |
| `gm_electric_bass_pick` | 5 | Electric Bass Pick | `s("gm_electric_bass_pick")` or `s("gm_electric_bass_pick:0 gm_electric_bass_pick:4")` |
| `gm_fretless_bass` | 2 | Fretless Bass | `s("gm_fretless_bass")` or `s("gm_fretless_bass:0 gm_fretless_bass:1")` |
| `gm_slap_bass_1` | 4 | Slap Bass 1 | `s("gm_slap_bass_1")` or `s("gm_slap_bass_1:0 gm_slap_bass_1:3")` |
| `gm_slap_bass_2` | 4 | Slap Bass 2 | `s("gm_slap_bass_2")` or `s("gm_slap_bass_2:0 gm_slap_bass_2:3")` |
| `gm_synth_bass_1` | 10 | Synth Bass 1 | `s("gm_synth_bass_1")` or `s("gm_synth_bass_1:0 gm_synth_bass_1:9")` |
| `gm_synth_bass_2` | 7 | Synth Bass 2 | `s("gm_synth_bass_2")` or `s("gm_synth_bass_2:0 gm_synth_bass_2:6")` |

### Brass

*8 instruments, 39 variations*

| Instrument | Variations | Display Name | Usage Example |
|------------|------------|--------------|---------------|
| `gm_brass_section` | 5 | Brass Section | `s("gm_brass_section")` or `s("gm_brass_section:0 gm_brass_section:4")` |
| `gm_french_horn` | 5 | French Horn | `s("gm_french_horn")` or `s("gm_french_horn:0 gm_french_horn:4")` |
| `gm_muted_trumpet` | 5 | Muted Trumpet | `s("gm_muted_trumpet")` or `s("gm_muted_trumpet:0 gm_muted_trumpet:4")` |
| `gm_synth_brass_1` | 4 | Synth Brass 1 | `s("gm_synth_brass_1")` or `s("gm_synth_brass_1:0 gm_synth_brass_1:3")` |
| `gm_synth_brass_2` | 7 | Synth Brass 2 | `s("gm_synth_brass_2")` or `s("gm_synth_brass_2:0 gm_synth_brass_2:6")` |
| `gm_trombone` | 5 | Trombone | `s("gm_trombone")` or `s("gm_trombone:0 gm_trombone:4")` |
| `gm_trumpet` | 4 | Trumpet | `s("gm_trumpet")` or `s("gm_trumpet:0 gm_trumpet:3")` |
| `gm_tuba` | 4 | Tuba | `s("gm_tuba")` or `s("gm_tuba:0 gm_tuba:3")` |

### Ethnic

*10 instruments, 65 variations*

| Instrument | Variations | Display Name | Usage Example |
|------------|------------|--------------|---------------|
| `gm_bagpipe` | 1 | Bagpipe | `s("gm_bagpipe")` |
| `gm_banjo` | 6 | Banjo | `s("gm_banjo")` or `s("gm_banjo:0 gm_banjo:5")` |
| `gm_fiddle` | 9 | Fiddle | `s("gm_fiddle")` or `s("gm_fiddle:0 gm_fiddle:8")` |
| `gm_kalimba` | 5 | Kalimba | `s("gm_kalimba")` or `s("gm_kalimba:0 gm_kalimba:4")` |
| `gm_koto` | 9 | Koto | `s("gm_koto")` or `s("gm_koto:0 gm_koto:8")` |
| `gm_shamisen` | 7 | Shamisen | `s("gm_shamisen")` or `s("gm_shamisen:0 gm_shamisen:6")` |
| `gm_shanai` | 5 | Shanai | `s("gm_shanai")` or `s("gm_shanai:0 gm_shanai:4")` |
| `gm_sitar` | 7 | Sitar | `s("gm_sitar")` or `s("gm_sitar:0 gm_sitar:6")` |
| `gm_steel_drums` | 6 | Steel Drums | `s("gm_steel_drums")` or `s("gm_steel_drums:0 gm_steel_drums:5")` |
| `gm_taiko_drum` | 10 | Taiko Drum | `s("gm_taiko_drum")` or `s("gm_taiko_drum:0 gm_taiko_drum:9")` |

### Guitars

*9 instruments, 75 variations*

| Instrument | Variations | Display Name | Usage Example |
|------------|------------|--------------|---------------|
| `gm_acoustic_guitar_nylon` | 9 | Acoustic Guitar Nylon | `s("gm_acoustic_guitar_nylon")` or `s("gm_acoustic_guitar_nylon:0 gm_acoustic_guitar_nylon:8")` |
| `gm_acoustic_guitar_steel` | 10 | Acoustic Guitar Steel | `s("gm_acoustic_guitar_steel")` or `s("gm_acoustic_guitar_steel:0 gm_acoustic_guitar_steel:9")` |
| `gm_distortion_guitar` | 7 | Distortion Guitar | `s("gm_distortion_guitar")` or `s("gm_distortion_guitar:0 gm_distortion_guitar:6")` |
| `gm_electric_guitar_clean` | 9 | Electric Guitar Clean | `s("gm_electric_guitar_clean")` or `s("gm_electric_guitar_clean:0 gm_electric_guitar_clean:8")` |
| `gm_electric_guitar_jazz` | 9 | Electric Guitar Jazz | `s("gm_electric_guitar_jazz")` or `s("gm_electric_guitar_jazz:0 gm_electric_guitar_jazz:8")` |
| `gm_electric_guitar_muted` | 10 | Electric Guitar Muted | `s("gm_electric_guitar_muted")` or `s("gm_electric_guitar_muted:0 gm_electric_guitar_muted:9")` |
| `gm_guitar_fret_noise` | 8 | Guitar Fret Noise | `s("gm_guitar_fret_noise")` or `s("gm_guitar_fret_noise:0 gm_guitar_fret_noise:7")` |
| `gm_guitar_harmonics` | 3 | Guitar Harmonics | `s("gm_guitar_harmonics")` or `s("gm_guitar_harmonics:0 gm_guitar_harmonics:2")` |
| `gm_overdriven_guitar` | 10 | Overdriven Guitar | `s("gm_overdriven_guitar")` or `s("gm_overdriven_guitar:0 gm_overdriven_guitar:9")` |

### Keyboards

*13 instruments, 110 variations*

| Instrument | Variations | Display Name | Usage Example |
|------------|------------|--------------|---------------|
| `gm_celesta` | 6 | Celesta | `s("gm_celesta")` or `s("gm_celesta:0 gm_celesta:5")` |
| `gm_clavinet` | 4 | Clavinet | `s("gm_clavinet")` or `s("gm_clavinet:0 gm_clavinet:3")` |
| `gm_dulcimer` | 5 | Dulcimer | `s("gm_dulcimer")` or `s("gm_dulcimer:0 gm_dulcimer:4")` |
| `gm_epiano1` | 11 | Epiano1 | `s("gm_epiano1")` or `s("gm_epiano1:0 gm_epiano1:10")` |
| `gm_epiano2` | 9 | Epiano2 | `s("gm_epiano2")` or `s("gm_epiano2:0 gm_epiano2:8")` |
| `gm_glockenspiel` | 5 | Glockenspiel | `s("gm_glockenspiel")` or `s("gm_glockenspiel:0 gm_glockenspiel:4")` |
| `gm_harpsichord` | 8 | Harpsichord | `s("gm_harpsichord")` or `s("gm_harpsichord:0 gm_harpsichord:7")` |
| `gm_marimba` | 7 | Marimba | `s("gm_marimba")` or `s("gm_marimba:0 gm_marimba:6")` |
| `gm_music_box` | 5 | Music Box | `s("gm_music_box")` or `s("gm_music_box:0 gm_music_box:4")` |
| `gm_piano` | 32 | Piano | `s("gm_piano")` or `s("gm_piano:0 gm_piano:31")` |
| `gm_tubular_bells` | 6 | Tubular Bells | `s("gm_tubular_bells")` or `s("gm_tubular_bells:0 gm_tubular_bells:5")` |
| `gm_vibraphone` | 6 | Vibraphone | `s("gm_vibraphone")` or `s("gm_vibraphone:0 gm_vibraphone:5")` |
| `gm_xylophone` | 6 | Xylophone | `s("gm_xylophone")` or `s("gm_xylophone:0 gm_xylophone:5")` |

### Organs

*8 instruments, 54 variations*

| Instrument | Variations | Display Name | Usage Example |
|------------|------------|--------------|---------------|
| `gm_accordion` | 7 | Accordion | `s("gm_accordion")` or `s("gm_accordion:0 gm_accordion:6")` |
| `gm_bandoneon` | 10 | Bandoneon | `s("gm_bandoneon")` or `s("gm_bandoneon:0 gm_bandoneon:9")` |
| `gm_church_organ` | 5 | Church Organ | `s("gm_church_organ")` or `s("gm_church_organ:0 gm_church_organ:4")` |
| `gm_drawbar_organ` | 7 | Drawbar Organ | `s("gm_drawbar_organ")` or `s("gm_drawbar_organ:0 gm_drawbar_organ:6")` |
| `gm_harmonica` | 6 | Harmonica | `s("gm_harmonica")` or `s("gm_harmonica:0 gm_harmonica:5")` |
| `gm_percussive_organ` | 6 | Percussive Organ | `s("gm_percussive_organ")` or `s("gm_percussive_organ:0 gm_percussive_organ:5")` |
| `gm_reed_organ` | 8 | Reed Organ | `s("gm_reed_organ")` or `s("gm_reed_organ:0 gm_reed_organ:7")` |
| `gm_rock_organ` | 5 | Rock Organ | `s("gm_rock_organ")` or `s("gm_rock_organ:0 gm_rock_organ:4")` |

### Percussion

*6 instruments, 41 variations*

| Instrument | Variations | Display Name | Usage Example |
|------------|------------|--------------|---------------|
| `gm_agogo` | 6 | Agogo | `s("gm_agogo")` or `s("gm_agogo:0 gm_agogo:5")` |
| `gm_melodic_tom` | 9 | Melodic Tom | `s("gm_melodic_tom")` or `s("gm_melodic_tom:0 gm_melodic_tom:8")` |
| `gm_reverse_cymbal` | 9 | Reverse Cymbal | `s("gm_reverse_cymbal")` or `s("gm_reverse_cymbal:0 gm_reverse_cymbal:8")` |
| `gm_synth_drum` | 7 | Synth Drum | `s("gm_synth_drum")` or `s("gm_synth_drum:0 gm_synth_drum:6")` |
| `gm_tinkle_bell` | 1 | Tinkle Bell | `s("gm_tinkle_bell")` |
| `gm_woodblock` | 9 | Woodblock | `s("gm_woodblock")` or `s("gm_woodblock:0 gm_woodblock:8")` |

### Sound Effects

*16 instruments, 163 variations*

| Instrument | Variations | Display Name | Usage Example |
|------------|------------|--------------|---------------|
| `gm_applause` | 15 | Applause | `s("gm_applause")` or `s("gm_applause:0 gm_applause:14")` |
| `gm_bird_tweet` | 7 | Bird Tweet | `s("gm_bird_tweet")` or `s("gm_bird_tweet:0 gm_bird_tweet:6")` |
| `gm_breath_noise` | 8 | Breath Noise | `s("gm_breath_noise")` or `s("gm_breath_noise:0 gm_breath_noise:7")` |
| `gm_fx_atmosphere` | 13 | Fx Atmosphere | `s("gm_fx_atmosphere")` or `s("gm_fx_atmosphere:0 gm_fx_atmosphere:12")` |
| `gm_fx_brightness` | 12 | Fx Brightness | `s("gm_fx_brightness")` or `s("gm_fx_brightness:0 gm_fx_brightness:11")` |
| `gm_fx_crystal` | 10 | Fx Crystal | `s("gm_fx_crystal")` or `s("gm_fx_crystal:0 gm_fx_crystal:9")` |
| `gm_fx_echoes` | 10 | Fx Echoes | `s("gm_fx_echoes")` or `s("gm_fx_echoes:0 gm_fx_echoes:9")` |
| `gm_fx_goblins` | 9 | Fx Goblins | `s("gm_fx_goblins")` or `s("gm_fx_goblins:0 gm_fx_goblins:8")` |
| `gm_fx_rain` | 6 | Fx Rain | `s("gm_fx_rain")` or `s("gm_fx_rain:0 gm_fx_rain:5")` |
| `gm_fx_sci_fi` | 9 | Fx Sci Fi | `s("gm_fx_sci_fi")` or `s("gm_fx_sci_fi:0 gm_fx_sci_fi:8")` |
| `gm_fx_soundtrack` | 5 | Fx Soundtrack | `s("gm_fx_soundtrack")` or `s("gm_fx_soundtrack:0 gm_fx_soundtrack:4")` |
| `gm_gunshot` | 12 | Gunshot | `s("gm_gunshot")` or `s("gm_gunshot:0 gm_gunshot:11")` |
| `gm_helicopter` | 16 | Helicopter | `s("gm_helicopter")` or `s("gm_helicopter:0 gm_helicopter:15")` |
| `gm_orchestra_hit` | 5 | Orchestra Hit | `s("gm_orchestra_hit")` or `s("gm_orchestra_hit:0 gm_orchestra_hit:4")` |
| `gm_seashore` | 16 | Seashore | `s("gm_seashore")` or `s("gm_seashore:0 gm_seashore:15")` |
| `gm_telephone` | 10 | Telephone | `s("gm_telephone")` or `s("gm_telephone:0 gm_telephone:9")` |

### Strings

*12 instruments, 75 variations*

| Instrument | Variations | Display Name | Usage Example |
|------------|------------|--------------|---------------|
| `gm_cello` | 6 | Cello | `s("gm_cello")` or `s("gm_cello:0 gm_cello:5")` |
| `gm_contrabass` | 3 | Contrabass | `s("gm_contrabass")` or `s("gm_contrabass:0 gm_contrabass:2")` |
| `gm_orchestral_harp` | 5 | Orchestral Harp | `s("gm_orchestral_harp")` or `s("gm_orchestral_harp:0 gm_orchestral_harp:4")` |
| `gm_pizzicato_strings` | 6 | Pizzicato Strings | `s("gm_pizzicato_strings")` or `s("gm_pizzicato_strings:0 gm_pizzicato_strings:5")` |
| `gm_string_ensemble_1` | 11 | String Ensemble 1 | `s("gm_string_ensemble_1")` or `s("gm_string_ensemble_1:0 gm_string_ensemble_1:10")` |
| `gm_string_ensemble_2` | 7 | String Ensemble 2 | `s("gm_string_ensemble_2")` or `s("gm_string_ensemble_2:0 gm_string_ensemble_2:6")` |
| `gm_synth_strings_1` | 7 | Synth Strings 1 | `s("gm_synth_strings_1")` or `s("gm_synth_strings_1:0 gm_synth_strings_1:6")` |
| `gm_synth_strings_2` | 4 | Synth Strings 2 | `s("gm_synth_strings_2")` or `s("gm_synth_strings_2:0 gm_synth_strings_2:3")` |
| `gm_timpani` | 6 | Timpani | `s("gm_timpani")` or `s("gm_timpani:0 gm_timpani:5")` |
| `gm_tremolo_strings` | 6 | Tremolo Strings | `s("gm_tremolo_strings")` or `s("gm_tremolo_strings:0 gm_tremolo_strings:5")` |
| `gm_viola` | 5 | Viola | `s("gm_viola")` or `s("gm_viola:0 gm_viola:4")` |
| `gm_violin` | 9 | Violin | `s("gm_violin")` or `s("gm_violin:0 gm_violin:8")` |

### Synth Leads

*8 instruments, 49 variations*

| Instrument | Variations | Display Name | Usage Example |
|------------|------------|--------------|---------------|
| `gm_lead_1_square` | 3 | Lead 1 Square | `s("gm_lead_1_square")` or `s("gm_lead_1_square:0 gm_lead_1_square:2")` |
| `gm_lead_2_sawtooth` | 7 | Lead 2 Sawtooth | `s("gm_lead_2_sawtooth")` or `s("gm_lead_2_sawtooth:0 gm_lead_2_sawtooth:6")` |
| `gm_lead_3_calliope` | 7 | Lead 3 Calliope | `s("gm_lead_3_calliope")` or `s("gm_lead_3_calliope:0 gm_lead_3_calliope:6")` |
| `gm_lead_4_chiff` | 6 | Lead 4 Chiff | `s("gm_lead_4_chiff")` or `s("gm_lead_4_chiff:0 gm_lead_4_chiff:5")` |
| `gm_lead_5_charang` | 10 | Lead 5 Charang | `s("gm_lead_5_charang")` or `s("gm_lead_5_charang:0 gm_lead_5_charang:9")` |
| `gm_lead_6_voice` | 6 | Lead 6 Voice | `s("gm_lead_6_voice")` or `s("gm_lead_6_voice:0 gm_lead_6_voice:5")` |
| `gm_lead_7_fifths` | 5 | Lead 7 Fifths | `s("gm_lead_7_fifths")` or `s("gm_lead_7_fifths:0 gm_lead_7_fifths:4")` |
| `gm_lead_8_bass_lead` | 5 | Lead 8 Bass Lead | `s("gm_lead_8_bass_lead")` or `s("gm_lead_8_bass_lead:0 gm_lead_8_bass_lead:4")` |

### Synth Pads

*8 instruments, 59 variations*

| Instrument | Variations | Display Name | Usage Example |
|------------|------------|--------------|---------------|
| `gm_pad_bowed` | 5 | Pad Bowed | `s("gm_pad_bowed")` or `s("gm_pad_bowed:0 gm_pad_bowed:4")` |
| `gm_pad_choir` | 6 | Pad Choir | `s("gm_pad_choir")` or `s("gm_pad_choir:0 gm_pad_choir:5")` |
| `gm_pad_halo` | 8 | Pad Halo | `s("gm_pad_halo")` or `s("gm_pad_halo:0 gm_pad_halo:7")` |
| `gm_pad_metallic` | 7 | Pad Metallic | `s("gm_pad_metallic")` or `s("gm_pad_metallic:0 gm_pad_metallic:6")` |
| `gm_pad_new_age` | 12 | Pad New Age | `s("gm_pad_new_age")` or `s("gm_pad_new_age:0 gm_pad_new_age:11")` |
| `gm_pad_poly` | 7 | Pad Poly | `s("gm_pad_poly")` or `s("gm_pad_poly:0 gm_pad_poly:6")` |
| `gm_pad_sweep` | 7 | Pad Sweep | `s("gm_pad_sweep")` or `s("gm_pad_sweep:0 gm_pad_sweep:6")` |
| `gm_pad_warm` | 7 | Pad Warm | `s("gm_pad_warm")` or `s("gm_pad_warm:0 gm_pad_warm:6")` |

### Vocals

*3 instruments, 20 variations*

| Instrument | Variations | Display Name | Usage Example |
|------------|------------|--------------|---------------|
| `gm_choir_aahs` | 9 | Choir Aahs | `s("gm_choir_aahs")` or `s("gm_choir_aahs:0 gm_choir_aahs:8")` |
| `gm_synth_choir` | 5 | Synth Choir | `s("gm_synth_choir")` or `s("gm_synth_choir:0 gm_synth_choir:4")` |
| `gm_voice_oohs` | 6 | Voice Oohs | `s("gm_voice_oohs")` or `s("gm_voice_oohs:0 gm_voice_oohs:5")` |

### Woodwinds

*16 instruments, 81 variations*

| Instrument | Variations | Display Name | Usage Example |
|------------|------------|--------------|---------------|
| `gm_alto_sax` | 6 | Alto Sax | `s("gm_alto_sax")` or `s("gm_alto_sax:0 gm_alto_sax:5")` |
| `gm_baritone_sax` | 6 | Baritone Sax | `s("gm_baritone_sax")` or `s("gm_baritone_sax:0 gm_baritone_sax:5")` |
| `gm_bassoon` | 4 | Bassoon | `s("gm_bassoon")` or `s("gm_bassoon:0 gm_bassoon:3")` |
| `gm_blown_bottle` | 5 | Blown Bottle | `s("gm_blown_bottle")` or `s("gm_blown_bottle:0 gm_blown_bottle:4")` |
| `gm_clarinet` | 6 | Clarinet | `s("gm_clarinet")` or `s("gm_clarinet:0 gm_clarinet:5")` |
| `gm_english_horn` | 4 | English Horn | `s("gm_english_horn")` or `s("gm_english_horn:0 gm_english_horn:3")` |
| `gm_flute` | 5 | Flute | `s("gm_flute")` or `s("gm_flute:0 gm_flute:4")` |
| `gm_oboe` | 5 | Oboe | `s("gm_oboe")` or `s("gm_oboe:0 gm_oboe:4")` |
| `gm_ocarina` | 4 | Ocarina | `s("gm_ocarina")` or `s("gm_ocarina:0 gm_ocarina:3")` |
| `gm_pan_flute` | 8 | Pan Flute | `s("gm_pan_flute")` or `s("gm_pan_flute:0 gm_pan_flute:7")` |
| `gm_piccolo` | 5 | Piccolo | `s("gm_piccolo")` or `s("gm_piccolo:0 gm_piccolo:4")` |
| `gm_recorder` | 5 | Recorder | `s("gm_recorder")` or `s("gm_recorder:0 gm_recorder:4")` |
| `gm_shakuhachi` | 5 | Shakuhachi | `s("gm_shakuhachi")` or `s("gm_shakuhachi:0 gm_shakuhachi:4")` |
| `gm_soprano_sax` | 5 | Soprano Sax | `s("gm_soprano_sax")` or `s("gm_soprano_sax:0 gm_soprano_sax:4")` |
| `gm_tenor_sax` | 4 | Tenor Sax | `s("gm_tenor_sax")` or `s("gm_tenor_sax:0 gm_tenor_sax:3")` |
| `gm_whistle` | 4 | Whistle | `s("gm_whistle")` or `s("gm_whistle:0 gm_whistle:3")` |

## Examples

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
