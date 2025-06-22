# Strudel Drum Machines Reference

This is a comprehensive reference of all classic drum machine samples available in Strudel. These are authentic samples from legendary drum machines that shaped electronic music history.

## Summary

- **Total Drum Machines**: 84
- **Total Drum Samples**: 1355
- **Total Variations**: 4826

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

### Roland TR Series (Classic)

#### Roland TR-808
*13 drum types, 122 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `tr808_bd` | Bass Drum/Kick | 25 | `s("tr808_bd")` or `s("tr808_bd:0 tr808_bd:24")` |
| `tr808_cp` | Clap | 5 | `s("tr808_cp")` or `s("tr808_cp:0 tr808_cp:4")` |
| `tr808_cb` | Cowbell | 2 | `s("tr808_cb")` or `s("tr808_cb:0 tr808_cb:1")` |
| `tr808_cr` | Crash Cymbal | 25 | `s("tr808_cr")` or `s("tr808_cr:0 tr808_cr:24")` |
| `tr808_hh` | Hi-Hat (Closed) | 1 | `s("tr808_hh")` |
| `tr808_oh` | Hi-Hat (Open) | 5 | `s("tr808_oh")` or `s("tr808_oh:0 tr808_oh:4")` |
| `tr808_ht` | High Tom | 5 | `s("tr808_ht")` or `s("tr808_ht:0 tr808_ht:4")` |
| `tr808_lt` | Low Tom | 5 | `s("tr808_lt")` or `s("tr808_lt:0 tr808_lt:4")` |
| `tr808_mt` | Mid Tom | 5 | `s("tr808_mt")` or `s("tr808_mt:0 tr808_mt:4")` |
| `tr808_perc` | Percussion | 16 | `s("tr808_perc")` or `s("tr808_perc:0 tr808_perc:15")` |
| `tr808_rim` | Rimshot | 1 | `s("tr808_rim")` |
| `tr808_sh` | Shaker | 2 | `s("tr808_sh")` or `s("tr808_sh:0 tr808_sh:1")` |
| `tr808_sd` | Snare Drum | 25 | `s("tr808_sd")` or `s("tr808_sd:0 tr808_sd:24")` |

#### Roland TR-909
*11 drum types, 74 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `tr909_bd` | Bass Drum/Kick | 4 | `s("tr909_bd")` or `s("tr909_bd:0 tr909_bd:3")` |
| `tr909_cp` | Clap | 5 | `s("tr909_cp")` or `s("tr909_cp:0 tr909_cp:4")` |
| `tr909_cr` | Crash Cymbal | 5 | `s("tr909_cr")` or `s("tr909_cr:0 tr909_cr:4")` |
| `tr909_hh` | Hi-Hat (Closed) | 4 | `s("tr909_hh")` or `s("tr909_hh:0 tr909_hh:3")` |
| `tr909_oh` | Hi-Hat (Open) | 5 | `s("tr909_oh")` or `s("tr909_oh:0 tr909_oh:4")` |
| `tr909_ht` | High Tom | 9 | `s("tr909_ht")` or `s("tr909_ht:0 tr909_ht:8")` |
| `tr909_lt` | Low Tom | 9 | `s("tr909_lt")` or `s("tr909_lt:0 tr909_lt:8")` |
| `tr909_mt` | Mid Tom | 9 | `s("tr909_mt")` or `s("tr909_mt:0 tr909_mt:8")` |
| `tr909_rd` | Ride Cymbal | 5 | `s("tr909_rd")` or `s("tr909_rd:0 tr909_rd:4")` |
| `tr909_rim` | Rimshot | 3 | `s("tr909_rim")` or `s("tr909_rim:0 tr909_rim:2")` |
| `tr909_sd` | Snare Drum | 16 | `s("tr909_sd")` or `s("tr909_sd:0 tr909_sd:15")` |

#### Roland TR-707
*12 drum types, 14 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `tr707_bd` | Bass Drum/Kick | 2 | `s("tr707_bd")` or `s("tr707_bd:0 tr707_bd:1")` |
| `tr707_cp` | Clap | 1 | `s("tr707_cp")` |
| `tr707_cb` | Cowbell | 1 | `s("tr707_cb")` |
| `tr707_cr` | Crash Cymbal | 1 | `s("tr707_cr")` |
| `tr707_hh` | Hi-Hat (Closed) | 1 | `s("tr707_hh")` |
| `tr707_oh` | Hi-Hat (Open) | 1 | `s("tr707_oh")` |
| `tr707_ht` | High Tom | 1 | `s("tr707_ht")` |
| `tr707_lt` | Low Tom | 1 | `s("tr707_lt")` |
| `tr707_mt` | Mid Tom | 1 | `s("tr707_mt")` |
| `tr707_rim` | Rimshot | 1 | `s("tr707_rim")` |
| `tr707_sd` | Snare Drum | 2 | `s("tr707_sd")` or `s("tr707_sd:0 tr707_sd:1")` |
| `tr707_tb` | Tambourine | 1 | `s("tr707_tb")` |

#### Roland TR-727
*2 drum types, 12 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `tr727_perc` | Percussion | 10 | `s("tr727_perc")` or `s("tr727_perc:0 tr727_perc:9")` |
| `tr727_sh` | Shaker | 2 | `s("tr727_sh")` or `s("tr727_sh:0 tr727_sh:1")` |

#### Roland TR-606
*7 drum types, 7 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `tr606_bd` | Bass Drum/Kick | 1 | `s("tr606_bd")` |
| `tr606_cr` | Crash Cymbal | 1 | `s("tr606_cr")` |
| `tr606_hh` | Hi-Hat (Closed) | 1 | `s("tr606_hh")` |
| `tr606_oh` | Hi-Hat (Open) | 1 | `s("tr606_oh")` |
| `tr606_ht` | High Tom | 1 | `s("tr606_ht")` |
| `tr606_lt` | Low Tom | 1 | `s("tr606_lt")` |
| `tr606_sd` | Snare Drum | 1 | `s("tr606_sd")` |

#### Roland TR-626
*15 drum types, 30 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `tr626_bd` | Bass Drum/Kick | 2 | `s("tr626_bd")` or `s("tr626_bd:0 tr626_bd:1")` |
| `tr626_cp` | Clap | 1 | `s("tr626_cp")` |
| `tr626_cb` | Cowbell | 1 | `s("tr626_cb")` |
| `tr626_cr` | Crash Cymbal | 2 | `s("tr626_cr")` or `s("tr626_cr:0 tr626_cr:1")` |
| `tr626_hh` | Hi-Hat (Closed) | 1 | `s("tr626_hh")` |
| `tr626_oh` | Hi-Hat (Open) | 1 | `s("tr626_oh")` |
| `tr626_ht` | High Tom | 2 | `s("tr626_ht")` or `s("tr626_ht:0 tr626_ht:1")` |
| `tr626_lt` | Low Tom | 2 | `s("tr626_lt")` or `s("tr626_lt:0 tr626_lt:1")` |
| `tr626_mt` | Mid Tom | 2 | `s("tr626_mt")` or `s("tr626_mt:0 tr626_mt:1")` |
| `tr626_perc` | Percussion | 8 | `s("tr626_perc")` or `s("tr626_perc:0 tr626_perc:7")` |
| `tr626_rd` | Ride Cymbal | 2 | `s("tr626_rd")` or `s("tr626_rd:0 tr626_rd:1")` |
| `tr626_rim` | Rimshot | 1 | `s("tr626_rim")` |
| `tr626_sh` | Shaker | 1 | `s("tr626_sh")` |
| `tr626_sd` | Snare Drum | 3 | `s("tr626_sd")` or `s("tr626_sd:0 tr626_sd:2")` |
| `tr626_tb` | Tambourine | 1 | `s("tr626_tb")` |

#### Roland TR-505
*13 drum types, 16 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `tr505_bd` | Bass Drum/Kick | 1 | `s("tr505_bd")` |
| `tr505_cp` | Clap | 1 | `s("tr505_cp")` |
| `tr505_cb` | Cowbell | 2 | `s("tr505_cb")` or `s("tr505_cb:0 tr505_cb:1")` |
| `tr505_cr` | Crash Cymbal | 1 | `s("tr505_cr")` |
| `tr505_hh` | Hi-Hat (Closed) | 1 | `s("tr505_hh")` |
| `tr505_oh` | Hi-Hat (Open) | 1 | `s("tr505_oh")` |
| `tr505_ht` | High Tom | 1 | `s("tr505_ht")` |
| `tr505_lt` | Low Tom | 1 | `s("tr505_lt")` |
| `tr505_mt` | Mid Tom | 1 | `s("tr505_mt")` |
| `tr505_perc` | Percussion | 3 | `s("tr505_perc")` or `s("tr505_perc:0 tr505_perc:2")` |
| `tr505_rd` | Ride Cymbal | 1 | `s("tr505_rd")` |
| `tr505_rim` | Rimshot | 1 | `s("tr505_rim")` |
| `tr505_sd` | Snare Drum | 1 | `s("tr505_sd")` |

### Roland CR Series

#### Roland CompuRhythm CR-78
*8 drum types, 20 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `compurhythm78_bd` | Bass Drum/Kick | 1 | `s("compurhythm78_bd")` |
| `compurhythm78_cb` | Cowbell | 1 | `s("compurhythm78_cb")` |
| `compurhythm78_hh` | Hi-Hat (Closed) | 2 | `s("compurhythm78_hh")` or `s("compurhythm78_hh:0 compurhythm78_hh:1")` |
| `compurhythm78_oh` | Hi-Hat (Open) | 2 | `s("compurhythm78_oh")` or `s("compurhythm78_oh:0 compurhythm78_oh:1")` |
| `compurhythm78_misc` | Miscellaneous | 4 | `s("compurhythm78_misc")` or `s("compurhythm78_misc:0 compurhythm78_misc:3")` |
| `compurhythm78_perc` | Percussion | 8 | `s("compurhythm78_perc")` or `s("compurhythm78_perc:0 compurhythm78_perc:7")` |
| `compurhythm78_sd` | Snare Drum | 1 | `s("compurhythm78_sd")` |
| `compurhythm78_tb` | Tambourine | 1 | `s("compurhythm78_tb")` |

#### Roland CompuRhythm CR-1000
*13 drum types, 15 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `compurhythm1000_bd` | Bass Drum/Kick | 1 | `s("compurhythm1000_bd")` |
| `compurhythm1000_cp` | Clap | 1 | `s("compurhythm1000_cp")` |
| `compurhythm1000_cb` | Cowbell | 1 | `s("compurhythm1000_cb")` |
| `compurhythm1000_cr` | Crash Cymbal | 1 | `s("compurhythm1000_cr")` |
| `compurhythm1000_hh` | Hi-Hat (Closed) | 1 | `s("compurhythm1000_hh")` |
| `compurhythm1000_oh` | Hi-Hat (Open) | 1 | `s("compurhythm1000_oh")` |
| `compurhythm1000_ht` | High Tom | 1 | `s("compurhythm1000_ht")` |
| `compurhythm1000_lt` | Low Tom | 1 | `s("compurhythm1000_lt")` |
| `compurhythm1000_mt` | Mid Tom | 1 | `s("compurhythm1000_mt")` |
| `compurhythm1000_perc` | Percussion | 3 | `s("compurhythm1000_perc")` or `s("compurhythm1000_perc:0 compurhythm1000_perc:2")` |
| `compurhythm1000_rd` | Ride Cymbal | 1 | `s("compurhythm1000_rd")` |
| `compurhythm1000_rim` | Rimshot | 1 | `s("compurhythm1000_rim")` |
| `compurhythm1000_sd` | Snare Drum | 1 | `s("compurhythm1000_sd")` |

#### Roland CompuRhythm CR-8000
*12 drum types, 13 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `compurhythm8000_bd` | Bass Drum/Kick | 1 | `s("compurhythm8000_bd")` |
| `compurhythm8000_cp` | Clap | 1 | `s("compurhythm8000_cp")` |
| `compurhythm8000_cb` | Cowbell | 1 | `s("compurhythm8000_cb")` |
| `compurhythm8000_cr` | Crash Cymbal | 1 | `s("compurhythm8000_cr")` |
| `compurhythm8000_hh` | Hi-Hat (Closed) | 1 | `s("compurhythm8000_hh")` |
| `compurhythm8000_oh` | Hi-Hat (Open) | 1 | `s("compurhythm8000_oh")` |
| `compurhythm8000_ht` | High Tom | 1 | `s("compurhythm8000_ht")` |
| `compurhythm8000_lt` | Low Tom | 1 | `s("compurhythm8000_lt")` |
| `compurhythm8000_mt` | Mid Tom | 1 | `s("compurhythm8000_mt")` |
| `compurhythm8000_perc` | Percussion | 2 | `s("compurhythm8000_perc")` or `s("compurhythm8000_perc:0 compurhythm8000_perc:1")` |
| `compurhythm8000_rim` | Rimshot | 1 | `s("compurhythm8000_rim")` |
| `compurhythm8000_sd` | Snare Drum | 1 | `s("compurhythm8000_sd")` |

#### Roland CR-78 (Ace Tone)
*7 drum types, 16 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `ace_bd` | Bass Drum/Kick | 3 | `s("ace_bd")` or `s("ace_bd:0 ace_bd:2")` |
| `ace_hh` | Hi-Hat (Closed) | 1 | `s("ace_hh")` |
| `ace_oh` | Hi-Hat (Open) | 1 | `s("ace_oh")` |
| `ace_ht` | High Tom | 1 | `s("ace_ht")` |
| `ace_lt` | Low Tom | 1 | `s("ace_lt")` |
| `ace_perc` | Percussion | 6 | `s("ace_perc")` or `s("ace_perc:0 ace_perc:5")` |
| `ace_sd` | Snare Drum | 3 | `s("ace_sd")` or `s("ace_sd:0 ace_sd:2")` |

### Roland DR/R Series

#### Roland DR-55
*20 drum types, 60 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `dr550_bd` | Bass Drum/Kick | 5 | `s("dr550_bd")` or `s("dr550_bd:0 dr550_bd:4")` |
| `dr55_bd` | Bass Drum/Kick | 2 | `s("dr55_bd")` or `s("dr55_bd:0 dr55_bd:1")` |
| `dr550_cp` | Clap | 1 | `s("dr550_cp")` |
| `dr550_cb` | Cowbell | 2 | `s("dr550_cb")` or `s("dr550_cb:0 dr550_cb:1")` |
| `dr550_cr` | Crash Cymbal | 1 | `s("dr550_cr")` |
| `dr550_hh` | Hi-Hat (Closed) | 2 | `s("dr550_hh")` or `s("dr550_hh:0 dr550_hh:1")` |
| `dr55_hh` | Hi-Hat (Closed) | 2 | `s("dr55_hh")` or `s("dr55_hh:0 dr55_hh:1")` |
| `dr550_oh` | Hi-Hat (Open) | 2 | `s("dr550_oh")` or `s("dr550_oh:0 dr550_oh:1")` |
| `dr550_ht` | High Tom | 3 | `s("dr550_ht")` or `s("dr550_ht:0 dr550_ht:2")` |
| `dr550_lt` | Low Tom | 3 | `s("dr550_lt")` or `s("dr550_lt:0 dr550_lt:2")` |
| `dr550_mt` | Mid Tom | 2 | `s("dr550_mt")` or `s("dr550_mt:0 dr550_mt:1")` |
| `dr550_misc` | Miscellaneous | 3 | `s("dr550_misc")` or `s("dr550_misc:0 dr550_misc:2")` |
| `dr550_perc` | Percussion | 11 | `s("dr550_perc")` or `s("dr550_perc:0 dr550_perc:10")` |
| `dr550_rd` | Ride Cymbal | 2 | `s("dr550_rd")` or `s("dr550_rd:0 dr550_rd:1")` |
| `dr550_rim` | Rimshot | 1 | `s("dr550_rim")` |
| `dr55_rim` | Rimshot | 1 | `s("dr55_rim")` |
| `dr550_sh` | Shaker | 2 | `s("dr550_sh")` or `s("dr550_sh:0 dr550_sh:1")` |
| `dr550_sd` | Snare Drum | 6 | `s("dr550_sd")` or `s("dr550_sd:0 dr550_sd:5")` |
| `dr55_sd` | Snare Drum | 8 | `s("dr55_sd")` or `s("dr55_sd:0 dr55_sd:7")` |
| `dr550_tb` | Tambourine | 1 | `s("dr550_tb")` |

#### Roland DR-110
*7 drum types, 7 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `dr110_bd` | Bass Drum/Kick | 1 | `s("dr110_bd")` |
| `dr110_cp` | Clap | 1 | `s("dr110_cp")` |
| `dr110_cr` | Crash Cymbal | 1 | `s("dr110_cr")` |
| `dr110_hh` | Hi-Hat (Closed) | 1 | `s("dr110_hh")` |
| `dr110_oh` | Hi-Hat (Open) | 1 | `s("dr110_oh")` |
| `dr110_rd` | Ride Cymbal | 1 | `s("dr110_rd")` |
| `dr110_sd` | Snare Drum | 1 | `s("dr110_sd")` |

#### Roland DR-220
*11 drum types, 11 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `dr220_bd` | Bass Drum/Kick | 1 | `s("dr220_bd")` |
| `dr220_cp` | Clap | 1 | `s("dr220_cp")` |
| `dr220_cr` | Crash Cymbal | 1 | `s("dr220_cr")` |
| `dr220_hh` | Hi-Hat (Closed) | 1 | `s("dr220_hh")` |
| `dr220_oh` | Hi-Hat (Open) | 1 | `s("dr220_oh")` |
| `dr220_ht` | High Tom | 1 | `s("dr220_ht")` |
| `dr220_lt` | Low Tom | 1 | `s("dr220_lt")` |
| `dr220_mt` | Mid Tom | 1 | `s("dr220_mt")` |
| `dr220_perc` | Percussion | 1 | `s("dr220_perc")` |
| `dr220_rd` | Ride Cymbal | 1 | `s("dr220_rd")` |
| `dr220_sd` | Snare Drum | 1 | `s("dr220_sd")` |

#### Roland R-8
*20 drum types, 58 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `r88_bd` | Bass Drum/Kick | 1 | `s("r88_bd")` |
| `r8_bd` | Bass Drum/Kick | 7 | `s("r8_bd")` or `s("r8_bd:0 r8_bd:6")` |
| `r8_cp` | Clap | 1 | `s("r8_cp")` |
| `r8_cb` | Cowbell | 1 | `s("r8_cb")` |
| `r88_cr` | Crash Cymbal | 1 | `s("r88_cr")` |
| `r8_cr` | Crash Cymbal | 1 | `s("r8_cr")` |
| `r88_hh` | Hi-Hat (Closed) | 1 | `s("r88_hh")` |
| `r8_hh` | Hi-Hat (Closed) | 2 | `s("r8_hh")` or `s("r8_hh:0 r8_hh:1")` |
| `r88_oh` | Hi-Hat (Open) | 1 | `s("r88_oh")` |
| `r8_oh` | Hi-Hat (Open) | 1 | `s("r8_oh")` |
| `r8_ht` | High Tom | 4 | `s("r8_ht")` or `s("r8_ht:0 r8_ht:3")` |
| `r8_lt` | Low Tom | 4 | `s("r8_lt")` or `s("r8_lt:0 r8_lt:3")` |
| `r8_mt` | Mid Tom | 4 | `s("r8_mt")` or `s("r8_mt:0 r8_mt:3")` |
| `r8_perc` | Percussion | 8 | `s("r8_perc")` or `s("r8_perc:0 r8_perc:7")` |
| `r8_rd` | Ride Cymbal | 2 | `s("r8_rd")` or `s("r8_rd:0 r8_rd:1")` |
| `r8_rim` | Rimshot | 2 | `s("r8_rim")` or `s("r8_rim:0 r8_rim:1")` |
| `r8_sh` | Shaker | 2 | `s("r8_sh")` or `s("r8_sh:0 r8_sh:1")` |
| `r88_sd` | Snare Drum | 2 | `s("r88_sd")` or `s("r88_sd:0 r88_sd:1")` |
| `r8_sd` | Snare Drum | 12 | `s("r8_sd")` or `s("r8_sd:0 r8_sd:11")` |
| `r8_tb` | Tambourine | 1 | `s("r8_tb")` |

#### Roland DDR-30
*4 drum types, 24 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `ddr30_bd` | Bass Drum/Kick | 8 | `s("ddr30_bd")` or `s("ddr30_bd:0 ddr30_bd:7")` |
| `ddr30_ht` | High Tom | 4 | `s("ddr30_ht")` or `s("ddr30_ht:0 ddr30_ht:3")` |
| `ddr30_lt` | Low Tom | 4 | `s("ddr30_lt")` or `s("ddr30_lt:0 ddr30_lt:3")` |
| `ddr30_sd` | Snare Drum | 8 | `s("ddr30_sd")` or `s("ddr30_sd:0 ddr30_sd:7")` |

### Linn Electronics

#### LinnDrum
*67 drum types, 101 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `linn9000_bd` | Bass Drum/Kick | 1 | `s("linn9000_bd")` |
| `linn_bd` | Bass Drum/Kick | 1 | `s("linn_bd")` |
| `linndrum_bd` | Bass Drum/Kick | 1 | `s("linndrum_bd")` |
| `linnlm1_bd` | Bass Drum/Kick | 4 | `s("linnlm1_bd")` or `s("linnlm1_bd:0 linnlm1_bd:3")` |
| `linnlm2_bd` | Bass Drum/Kick | 4 | `s("linnlm2_bd")` or `s("linnlm2_bd:0 linnlm2_bd:3")` |
| `linn_cp` | Clap | 1 | `s("linn_cp")` |
| `linndrum_cp` | Clap | 1 | `s("linndrum_cp")` |
| `linnlm1_cp` | Clap | 1 | `s("linnlm1_cp")` |
| `linnlm2_cp` | Clap | 1 | `s("linnlm2_cp")` |
| `linn9000_cb` | Cowbell | 2 | `s("linn9000_cb")` or `s("linn9000_cb:0 linn9000_cb:1")` |
| `linn_cb` | Cowbell | 1 | `s("linn_cb")` |
| `linndrum_cb` | Cowbell | 1 | `s("linndrum_cb")` |
| `linnlm1_cb` | Cowbell | 1 | `s("linnlm1_cb")` |
| `linnlm2_cb` | Cowbell | 1 | `s("linnlm2_cb")` |
| `linn9000_cr` | Crash Cymbal | 2 | `s("linn9000_cr")` or `s("linn9000_cr:0 linn9000_cr:1")` |
| `linn_cr` | Crash Cymbal | 1 | `s("linn_cr")` |
| `linndrum_cr` | Crash Cymbal | 1 | `s("linndrum_cr")` |
| `linnlm2_cr` | Crash Cymbal | 1 | `s("linnlm2_cr")` |
| `linn9000_hh` | Hi-Hat (Closed) | 1 | `s("linn9000_hh")` |
| `linn_hh` | Hi-Hat (Closed) | 1 | `s("linn_hh")` |
| `linndrum_hh` | Hi-Hat (Closed) | 3 | `s("linndrum_hh")` or `s("linndrum_hh:0 linndrum_hh:2")` |
| `linnlm1_hh` | Hi-Hat (Closed) | 1 | `s("linnlm1_hh")` |
| `linnlm2_hh` | Hi-Hat (Closed) | 2 | `s("linnlm2_hh")` or `s("linnlm2_hh:0 linnlm2_hh:1")` |
| `linn9000_oh` | Hi-Hat (Open) | 1 | `s("linn9000_oh")` |
| `linn_oh` | Hi-Hat (Open) | 1 | `s("linn_oh")` |
| `linndrum_oh` | Hi-Hat (Open) | 1 | `s("linndrum_oh")` |
| `linnlm1_oh` | Hi-Hat (Open) | 1 | `s("linnlm1_oh")` |
| `linnlm2_oh` | Hi-Hat (Open) | 2 | `s("linnlm2_oh")` or `s("linnlm2_oh:0 linnlm2_oh:1")` |
| `linn9000_ht` | High Tom | 2 | `s("linn9000_ht")` or `s("linn9000_ht:0 linn9000_ht:1")` |
| `linn_ht` | High Tom | 1 | `s("linn_ht")` |
| `linndrum_ht` | High Tom | 2 | `s("linndrum_ht")` or `s("linndrum_ht:0 linndrum_ht:1")` |
| `linnlm1_ht` | High Tom | 1 | `s("linnlm1_ht")` |
| `linnlm2_ht` | High Tom | 1 | `s("linnlm2_ht")` |
| `linn9000_lt` | Low Tom | 2 | `s("linn9000_lt")` or `s("linn9000_lt:0 linn9000_lt:1")` |
| `linn_lt` | Low Tom | 1 | `s("linn_lt")` |
| `linndrum_lt` | Low Tom | 2 | `s("linndrum_lt")` or `s("linndrum_lt:0 linndrum_lt:1")` |
| `linnlm1_lt` | Low Tom | 1 | `s("linnlm1_lt")` |
| `linnlm2_lt` | Low Tom | 1 | `s("linnlm2_lt")` |
| `linn9000_mt` | Mid Tom | 1 | `s("linn9000_mt")` |
| `linn_mt` | Mid Tom | 1 | `s("linn_mt")` |
| `linndrum_mt` | Mid Tom | 1 | `s("linndrum_mt")` |
| `linnlm2_mt` | Mid Tom | 1 | `s("linnlm2_mt")` |
| `linn9000_perc` | Percussion | 3 | `s("linn9000_perc")` or `s("linn9000_perc:0 linn9000_perc:2")` |
| `linndrum_perc` | Percussion | 6 | `s("linndrum_perc")` or `s("linndrum_perc:0 linndrum_perc:5")` |
| `linnlm1_perc` | Percussion | 3 | `s("linnlm1_perc")` or `s("linnlm1_perc:0 linnlm1_perc:2")` |
| `linn9000_rd` | Ride Cymbal | 2 | `s("linn9000_rd")` or `s("linn9000_rd:0 linn9000_rd:1")` |
| `linn_rd` | Ride Cymbal | 1 | `s("linn_rd")` |
| `linndrum_rd` | Ride Cymbal | 1 | `s("linndrum_rd")` |
| `linnlm2_rd` | Ride Cymbal | 1 | `s("linnlm2_rd")` |
| `linn9000_rim` | Rimshot | 1 | `s("linn9000_rim")` |
| `linndrum_rim` | Rimshot | 3 | `s("linndrum_rim")` or `s("linndrum_rim:0 linndrum_rim:2")` |
| `linnlm1_rim` | Rimshot | 1 | `s("linnlm1_rim")` |
| `linnlm2_rim` | Rimshot | 2 | `s("linnlm2_rim")` or `s("linnlm2_rim:0 linnlm2_rim:1")` |
| `linn_sh` | Shaker | 1 | `s("linn_sh")` |
| `linndrum_sh` | Shaker | 1 | `s("linndrum_sh")` |
| `linnlm1_sh` | Shaker | 1 | `s("linnlm1_sh")` |
| `linnlm2_sh` | Shaker | 1 | `s("linnlm2_sh")` |
| `linn9000_sd` | Snare Drum | 1 | `s("linn9000_sd")` |
| `linn_sd` | Snare Drum | 1 | `s("linn_sd")` |
| `linndrum_sd` | Snare Drum | 3 | `s("linndrum_sd")` or `s("linndrum_sd:0 linndrum_sd:2")` |
| `linnlm1_sd` | Snare Drum | 1 | `s("linnlm1_sd")` |
| `linnlm2_sd` | Snare Drum | 4 | `s("linnlm2_sd")` or `s("linnlm2_sd:0 linnlm2_sd:3")` |
| `linn9000_tb` | Tambourine | 1 | `s("linn9000_tb")` |
| `linn_tb` | Tambourine | 1 | `s("linn_tb")` |
| `linndrum_tb` | Tambourine | 1 | `s("linndrum_tb")` |
| `linnlm1_tb` | Tambourine | 1 | `s("linnlm1_tb")` |
| `linnlm2_tb` | Tambourine | 1 | `s("linnlm2_tb")` |

#### Linn LM-1
*12 drum types, 17 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `lm1_bd` | Bass Drum/Kick | 4 | `s("lm1_bd")` or `s("lm1_bd:0 lm1_bd:3")` |
| `lm1_cp` | Clap | 1 | `s("lm1_cp")` |
| `lm1_cb` | Cowbell | 1 | `s("lm1_cb")` |
| `lm1_hh` | Hi-Hat (Closed) | 1 | `s("lm1_hh")` |
| `lm1_oh` | Hi-Hat (Open) | 1 | `s("lm1_oh")` |
| `lm1_ht` | High Tom | 1 | `s("lm1_ht")` |
| `lm1_lt` | Low Tom | 1 | `s("lm1_lt")` |
| `lm1_perc` | Percussion | 3 | `s("lm1_perc")` or `s("lm1_perc:0 lm1_perc:2")` |
| `lm1_rim` | Rimshot | 1 | `s("lm1_rim")` |
| `lm1_sh` | Shaker | 1 | `s("lm1_sh")` |
| `lm1_sd` | Snare Drum | 1 | `s("lm1_sd")` |
| `lm1_tb` | Tambourine | 1 | `s("lm1_tb")` |

#### Linn LM-2
*14 drum types, 23 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `lm2_bd` | Bass Drum/Kick | 4 | `s("lm2_bd")` or `s("lm2_bd:0 lm2_bd:3")` |
| `lm2_cp` | Clap | 1 | `s("lm2_cp")` |
| `lm2_cb` | Cowbell | 1 | `s("lm2_cb")` |
| `lm2_cr` | Crash Cymbal | 1 | `s("lm2_cr")` |
| `lm2_hh` | Hi-Hat (Closed) | 2 | `s("lm2_hh")` or `s("lm2_hh:0 lm2_hh:1")` |
| `lm2_oh` | Hi-Hat (Open) | 2 | `s("lm2_oh")` or `s("lm2_oh:0 lm2_oh:1")` |
| `lm2_ht` | High Tom | 1 | `s("lm2_ht")` |
| `lm2_lt` | Low Tom | 1 | `s("lm2_lt")` |
| `lm2_mt` | Mid Tom | 1 | `s("lm2_mt")` |
| `lm2_rd` | Ride Cymbal | 1 | `s("lm2_rd")` |
| `lm2_rim` | Rimshot | 2 | `s("lm2_rim")` or `s("lm2_rim:0 lm2_rim:1")` |
| `lm2_sh` | Shaker | 1 | `s("lm2_sh")` |
| `lm2_sd` | Snare Drum | 4 | `s("lm2_sd")` or `s("lm2_sd:0 lm2_sd:3")` |
| `lm2_tb` | Tambourine | 1 | `s("lm2_tb")` |

#### Linn 9000
*13 drum types, 20 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `9000_bd` | Bass Drum/Kick | 1 | `s("9000_bd")` |
| `9000_cb` | Cowbell | 2 | `s("9000_cb")` or `s("9000_cb:0 9000_cb:1")` |
| `9000_cr` | Crash Cymbal | 2 | `s("9000_cr")` or `s("9000_cr:0 9000_cr:1")` |
| `9000_hh` | Hi-Hat (Closed) | 1 | `s("9000_hh")` |
| `9000_oh` | Hi-Hat (Open) | 1 | `s("9000_oh")` |
| `9000_ht` | High Tom | 2 | `s("9000_ht")` or `s("9000_ht:0 9000_ht:1")` |
| `9000_lt` | Low Tom | 2 | `s("9000_lt")` or `s("9000_lt:0 9000_lt:1")` |
| `9000_mt` | Mid Tom | 1 | `s("9000_mt")` |
| `9000_perc` | Percussion | 3 | `s("9000_perc")` or `s("9000_perc:0 9000_perc:2")` |
| `9000_rd` | Ride Cymbal | 2 | `s("9000_rd")` or `s("9000_rd:0 9000_rd:1")` |
| `9000_rim` | Rimshot | 1 | `s("9000_rim")` |
| `9000_sd` | Snare Drum | 1 | `s("9000_sd")` |
| `9000_tb` | Tambourine | 1 | `s("9000_tb")` |

### Oberheim

#### Oberheim DMX
*27 drum types, 37 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `oberheimdmx_` |  | 3 | `s("oberheimdmx_")` or `s("oberheimdmx_:0 oberheimdmx_:2")` |
| `dmx_bd` | Bass Drum/Kick | 3 | `s("dmx_bd")` or `s("dmx_bd:0 dmx_bd:2")` |
| `oberheimdmx_bd` | Bass Drum/Kick | 3 | `s("oberheimdmx_bd")` or `s("oberheimdmx_bd:0 oberheimdmx_bd:2")` |
| `dmx_cp` | Clap | 1 | `s("dmx_cp")` |
| `oberheimdmx_cp` | Clap | 1 | `s("oberheimdmx_cp")` |
| `dmx_cr` | Crash Cymbal | 1 | `s("dmx_cr")` |
| `oberheimdmx_cr` | Crash Cymbal | 1 | `s("oberheimdmx_cr")` |
| `dmx_hh` | Hi-Hat (Closed) | 1 | `s("dmx_hh")` |
| `oberheimdmx_hh` | Hi-Hat (Closed) | 1 | `s("oberheimdmx_hh")` |
| `dmx_oh` | Hi-Hat (Open) | 1 | `s("dmx_oh")` |
| `oberheimdmx_oh` | Hi-Hat (Open) | 1 | `s("oberheimdmx_oh")` |
| `dmx_ht` | High Tom | 1 | `s("dmx_ht")` |
| `oberheimdmx_ht` | High Tom | 1 | `s("oberheimdmx_ht")` |
| `dmx_lt` | Low Tom | 1 | `s("dmx_lt")` |
| `oberheimdmx_lt` | Low Tom | 1 | `s("oberheimdmx_lt")` |
| `dmx_mt` | Mid Tom | 1 | `s("dmx_mt")` |
| `oberheimdmx_mt` | Mid Tom | 1 | `s("oberheimdmx_mt")` |
| `dmx_rd` | Ride Cymbal | 1 | `s("dmx_rd")` |
| `oberheimdmx_rd` | Ride Cymbal | 1 | `s("oberheimdmx_rd")` |
| `dmx_rim` | Rimshot | 1 | `s("dmx_rim")` |
| `oberheimdmx_rim` | Rimshot | 1 | `s("oberheimdmx_rim")` |
| `dmx_sh` | Shaker | 1 | `s("dmx_sh")` |
| `oberheimdmx_sh` | Shaker | 1 | `s("oberheimdmx_sh")` |
| `dmx_sd` | Snare Drum | 3 | `s("dmx_sd")` or `s("dmx_sd:0 dmx_sd:2")` |
| `oberheimdmx_sd` | Snare Drum | 3 | `s("oberheimdmx_sd")` or `s("oberheimdmx_sd:0 oberheimdmx_sd:2")` |
| `dmx_tb` | Tambourine | 1 | `s("dmx_tb")` |
| `oberheimdmx_tb` | Tambourine | 1 | `s("oberheimdmx_tb")` |

### E-mu

#### E-mu Drumulator
*24 drum types, 24 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `drumulator_bd` | Bass Drum/Kick | 1 | `s("drumulator_bd")` |
| `emudrumulator_bd` | Bass Drum/Kick | 1 | `s("emudrumulator_bd")` |
| `drumulator_cp` | Clap | 1 | `s("drumulator_cp")` |
| `emudrumulator_cp` | Clap | 1 | `s("emudrumulator_cp")` |
| `drumulator_cb` | Cowbell | 1 | `s("drumulator_cb")` |
| `emudrumulator_cb` | Cowbell | 1 | `s("emudrumulator_cb")` |
| `drumulator_cr` | Crash Cymbal | 1 | `s("drumulator_cr")` |
| `emudrumulator_cr` | Crash Cymbal | 1 | `s("emudrumulator_cr")` |
| `drumulator_hh` | Hi-Hat (Closed) | 1 | `s("drumulator_hh")` |
| `emudrumulator_hh` | Hi-Hat (Closed) | 1 | `s("emudrumulator_hh")` |
| `drumulator_oh` | Hi-Hat (Open) | 1 | `s("drumulator_oh")` |
| `emudrumulator_oh` | Hi-Hat (Open) | 1 | `s("emudrumulator_oh")` |
| `drumulator_ht` | High Tom | 1 | `s("drumulator_ht")` |
| `emudrumulator_ht` | High Tom | 1 | `s("emudrumulator_ht")` |
| `drumulator_lt` | Low Tom | 1 | `s("drumulator_lt")` |
| `emudrumulator_lt` | Low Tom | 1 | `s("emudrumulator_lt")` |
| `drumulator_mt` | Mid Tom | 1 | `s("drumulator_mt")` |
| `emudrumulator_mt` | Mid Tom | 1 | `s("emudrumulator_mt")` |
| `drumulator_perc` | Percussion | 1 | `s("drumulator_perc")` |
| `emudrumulator_perc` | Percussion | 1 | `s("emudrumulator_perc")` |
| `drumulator_rim` | Rimshot | 1 | `s("drumulator_rim")` |
| `emudrumulator_rim` | Rimshot | 1 | `s("emudrumulator_rim")` |
| `drumulator_sd` | Snare Drum | 1 | `s("drumulator_sd")` |
| `emudrumulator_sd` | Snare Drum | 1 | `s("emudrumulator_sd")` |

#### E-mu SP-12
*28 drum types, 136 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `emusp12_bd` | Bass Drum/Kick | 14 | `s("emusp12_bd")` or `s("emusp12_bd:0 emusp12_bd:13")` |
| `sp12_bd` | Bass Drum/Kick | 14 | `s("sp12_bd")` or `s("sp12_bd:0 sp12_bd:13")` |
| `emusp12_cp` | Clap | 1 | `s("emusp12_cp")` |
| `sp12_cp` | Clap | 1 | `s("sp12_cp")` |
| `emusp12_cb` | Cowbell | 1 | `s("emusp12_cb")` |
| `sp12_cb` | Cowbell | 1 | `s("sp12_cb")` |
| `emusp12_cr` | Crash Cymbal | 1 | `s("emusp12_cr")` |
| `sp12_cr` | Crash Cymbal | 1 | `s("sp12_cr")` |
| `emusp12_hh` | Hi-Hat (Closed) | 2 | `s("emusp12_hh")` or `s("emusp12_hh:0 emusp12_hh:1")` |
| `sp12_hh` | Hi-Hat (Closed) | 2 | `s("sp12_hh")` or `s("sp12_hh:0 sp12_hh:1")` |
| `emusp12_oh` | Hi-Hat (Open) | 1 | `s("emusp12_oh")` |
| `sp12_oh` | Hi-Hat (Open) | 1 | `s("sp12_oh")` |
| `emusp12_ht` | High Tom | 6 | `s("emusp12_ht")` or `s("emusp12_ht:0 emusp12_ht:5")` |
| `sp12_ht` | High Tom | 6 | `s("sp12_ht")` or `s("sp12_ht:0 sp12_ht:5")` |
| `emusp12_lt` | Low Tom | 6 | `s("emusp12_lt")` or `s("emusp12_lt:0 emusp12_lt:5")` |
| `sp12_lt` | Low Tom | 6 | `s("sp12_lt")` or `s("sp12_lt:0 sp12_lt:5")` |
| `emusp12_mt` | Mid Tom | 4 | `s("emusp12_mt")` or `s("emusp12_mt:0 emusp12_mt:3")` |
| `sp12_mt` | Mid Tom | 4 | `s("sp12_mt")` or `s("sp12_mt:0 sp12_mt:3")` |
| `emusp12_misc` | Miscellaneous | 7 | `s("emusp12_misc")` or `s("emusp12_misc:0 emusp12_misc:6")` |
| `sp12_misc` | Miscellaneous | 7 | `s("sp12_misc")` or `s("sp12_misc:0 sp12_misc:6")` |
| `emusp12_perc` | Percussion | 1 | `s("emusp12_perc")` |
| `sp12_perc` | Percussion | 1 | `s("sp12_perc")` |
| `emusp12_rd` | Ride Cymbal | 1 | `s("emusp12_rd")` |
| `sp12_rd` | Ride Cymbal | 1 | `s("sp12_rd")` |
| `emusp12_rim` | Rimshot | 2 | `s("emusp12_rim")` or `s("emusp12_rim:0 emusp12_rim:1")` |
| `sp12_rim` | Rimshot | 2 | `s("sp12_rim")` or `s("sp12_rim:0 sp12_rim:1")` |
| `emusp12_sd` | Snare Drum | 21 | `s("emusp12_sd")` or `s("emusp12_sd:0 emusp12_sd:20")` |
| `sp12_sd` | Snare Drum | 21 | `s("sp12_sd")` or `s("sp12_sd:0 sp12_sd:20")` |

### Akai

#### Akai MPC60
*26 drum types, 42 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `akaimpc60_bd` | Bass Drum/Kick | 2 | `s("akaimpc60_bd")` or `s("akaimpc60_bd:0 akaimpc60_bd:1")` |
| `mpc60_bd` | Bass Drum/Kick | 2 | `s("mpc60_bd")` or `s("mpc60_bd:0 mpc60_bd:1")` |
| `akaimpc60_cp` | Clap | 1 | `s("akaimpc60_cp")` |
| `mpc60_cp` | Clap | 1 | `s("mpc60_cp")` |
| `akaimpc60_cr` | Crash Cymbal | 1 | `s("akaimpc60_cr")` |
| `mpc60_cr` | Crash Cymbal | 1 | `s("mpc60_cr")` |
| `akaimpc60_hh` | Hi-Hat (Closed) | 1 | `s("akaimpc60_hh")` |
| `mpc60_hh` | Hi-Hat (Closed) | 1 | `s("mpc60_hh")` |
| `akaimpc60_oh` | Hi-Hat (Open) | 1 | `s("akaimpc60_oh")` |
| `mpc60_oh` | Hi-Hat (Open) | 1 | `s("mpc60_oh")` |
| `akaimpc60_ht` | High Tom | 1 | `s("akaimpc60_ht")` |
| `mpc60_ht` | High Tom | 1 | `s("mpc60_ht")` |
| `akaimpc60_lt` | Low Tom | 1 | `s("akaimpc60_lt")` |
| `mpc60_lt` | Low Tom | 1 | `s("mpc60_lt")` |
| `akaimpc60_mt` | Mid Tom | 1 | `s("akaimpc60_mt")` |
| `mpc60_mt` | Mid Tom | 1 | `s("mpc60_mt")` |
| `akaimpc60_misc` | Miscellaneous | 2 | `s("akaimpc60_misc")` or `s("akaimpc60_misc:0 akaimpc60_misc:1")` |
| `mpc60_misc` | Miscellaneous | 2 | `s("mpc60_misc")` or `s("mpc60_misc:0 mpc60_misc:1")` |
| `akaimpc60_perc` | Percussion | 5 | `s("akaimpc60_perc")` or `s("akaimpc60_perc:0 akaimpc60_perc:4")` |
| `mpc60_perc` | Percussion | 5 | `s("mpc60_perc")` or `s("mpc60_perc:0 mpc60_perc:4")` |
| `akaimpc60_rd` | Ride Cymbal | 1 | `s("akaimpc60_rd")` |
| `mpc60_rd` | Ride Cymbal | 1 | `s("mpc60_rd")` |
| `akaimpc60_rim` | Rimshot | 1 | `s("akaimpc60_rim")` |
| `mpc60_rim` | Rimshot | 1 | `s("mpc60_rim")` |
| `akaimpc60_sd` | Snare Drum | 3 | `s("akaimpc60_sd")` or `s("akaimpc60_sd:0 akaimpc60_sd:2")` |
| `mpc60_sd` | Snare Drum | 3 | `s("mpc60_sd")` or `s("mpc60_sd:0 mpc60_sd:2")` |

#### Akai MPC1000
*7 drum types, 17 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `mpc1000_bd` | Bass Drum/Kick | 5 | `s("mpc1000_bd")` or `s("mpc1000_bd:0 mpc1000_bd:4")` |
| `mpc1000_cp` | Clap | 1 | `s("mpc1000_cp")` |
| `mpc1000_hh` | Hi-Hat (Closed) | 4 | `s("mpc1000_hh")` or `s("mpc1000_hh:0 mpc1000_hh:3")` |
| `mpc1000_oh` | Hi-Hat (Open) | 1 | `s("mpc1000_oh")` |
| `mpc1000_perc` | Percussion | 1 | `s("mpc1000_perc")` |
| `mpc1000_sh` | Shaker | 1 | `s("mpc1000_sh")` |
| `mpc1000_sd` | Snare Drum | 4 | `s("mpc1000_sd")` or `s("mpc1000_sd:0 mpc1000_sd:3")` |

#### Akai XR10
*32 drum types, 114 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `akaixr10_bd` | Bass Drum/Kick | 10 | `s("akaixr10_bd")` or `s("akaixr10_bd:0 akaixr10_bd:9")` |
| `xr10_bd` | Bass Drum/Kick | 10 | `s("xr10_bd")` or `s("xr10_bd:0 xr10_bd:9")` |
| `akaixr10_cp` | Clap | 1 | `s("akaixr10_cp")` |
| `xr10_cp` | Clap | 1 | `s("xr10_cp")` |
| `akaixr10_cb` | Cowbell | 1 | `s("akaixr10_cb")` |
| `xr10_cb` | Cowbell | 1 | `s("xr10_cb")` |
| `akaixr10_cr` | Crash Cymbal | 3 | `s("akaixr10_cr")` or `s("akaixr10_cr:0 akaixr10_cr:2")` |
| `xr10_cr` | Crash Cymbal | 3 | `s("xr10_cr")` or `s("xr10_cr:0 xr10_cr:2")` |
| `akaixr10_hh` | Hi-Hat (Closed) | 2 | `s("akaixr10_hh")` or `s("akaixr10_hh:0 akaixr10_hh:1")` |
| `xr10_hh` | Hi-Hat (Closed) | 2 | `s("xr10_hh")` or `s("xr10_hh:0 xr10_hh:1")` |
| `akaixr10_oh` | Hi-Hat (Open) | 1 | `s("akaixr10_oh")` |
| `xr10_oh` | Hi-Hat (Open) | 1 | `s("xr10_oh")` |
| `akaixr10_ht` | High Tom | 1 | `s("akaixr10_ht")` |
| `xr10_ht` | High Tom | 1 | `s("xr10_ht")` |
| `akaixr10_lt` | Low Tom | 2 | `s("akaixr10_lt")` or `s("akaixr10_lt:0 akaixr10_lt:1")` |
| `xr10_lt` | Low Tom | 2 | `s("xr10_lt")` or `s("xr10_lt:0 xr10_lt:1")` |
| `akaixr10_mt` | Mid Tom | 2 | `s("akaixr10_mt")` or `s("akaixr10_mt:0 akaixr10_mt:1")` |
| `xr10_mt` | Mid Tom | 2 | `s("xr10_mt")` or `s("xr10_mt:0 xr10_mt:1")` |
| `akaixr10_misc` | Miscellaneous | 4 | `s("akaixr10_misc")` or `s("akaixr10_misc:0 akaixr10_misc:3")` |
| `xr10_misc` | Miscellaneous | 4 | `s("xr10_misc")` or `s("xr10_misc:0 xr10_misc:3")` |
| `akaixr10_perc` | Percussion | 15 | `s("akaixr10_perc")` or `s("akaixr10_perc:0 akaixr10_perc:14")` |
| `xr10_perc` | Percussion | 15 | `s("xr10_perc")` or `s("xr10_perc:0 xr10_perc:14")` |
| `akaixr10_rd` | Ride Cymbal | 1 | `s("akaixr10_rd")` |
| `xr10_rd` | Ride Cymbal | 1 | `s("xr10_rd")` |
| `akaixr10_rim` | Rimshot | 2 | `s("akaixr10_rim")` or `s("akaixr10_rim:0 akaixr10_rim:1")` |
| `xr10_rim` | Rimshot | 2 | `s("xr10_rim")` or `s("xr10_rim:0 xr10_rim:1")` |
| `akaixr10_sh` | Shaker | 1 | `s("akaixr10_sh")` |
| `xr10_sh` | Shaker | 1 | `s("xr10_sh")` |
| `akaixr10_sd` | Snare Drum | 10 | `s("akaixr10_sd")` or `s("akaixr10_sd:0 akaixr10_sd:9")` |
| `xr10_sd` | Snare Drum | 10 | `s("xr10_sd")` or `s("xr10_sd:0 xr10_sd:9")` |
| `akaixr10_tb` | Tambourine | 1 | `s("akaixr10_tb")` |
| `xr10_tb` | Tambourine | 1 | `s("xr10_tb")` |

### Alesis

#### Alesis HR-16
*20 drum types, 38 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `alesishr16_bd` | Bass Drum/Kick | 1 | `s("alesishr16_bd")` |
| `hr16_bd` | Bass Drum/Kick | 1 | `s("hr16_bd")` |
| `alesishr16_cp` | Clap | 1 | `s("alesishr16_cp")` |
| `hr16_cp` | Clap | 1 | `s("hr16_cp")` |
| `alesishr16_hh` | Hi-Hat (Closed) | 1 | `s("alesishr16_hh")` |
| `hr16_hh` | Hi-Hat (Closed) | 1 | `s("hr16_hh")` |
| `alesishr16_oh` | Hi-Hat (Open) | 1 | `s("alesishr16_oh")` |
| `hr16_oh` | Hi-Hat (Open) | 1 | `s("hr16_oh")` |
| `alesishr16_ht` | High Tom | 1 | `s("alesishr16_ht")` |
| `hr16_ht` | High Tom | 1 | `s("hr16_ht")` |
| `alesishr16_lt` | Low Tom | 1 | `s("alesishr16_lt")` |
| `hr16_lt` | Low Tom | 1 | `s("hr16_lt")` |
| `alesishr16_perc` | Percussion | 8 | `s("alesishr16_perc")` or `s("alesishr16_perc:0 alesishr16_perc:7")` |
| `hr16_perc` | Percussion | 8 | `s("hr16_perc")` or `s("hr16_perc:0 hr16_perc:7")` |
| `alesishr16_rim` | Rimshot | 1 | `s("alesishr16_rim")` |
| `hr16_rim` | Rimshot | 1 | `s("hr16_rim")` |
| `alesishr16_sh` | Shaker | 3 | `s("alesishr16_sh")` or `s("alesishr16_sh:0 alesishr16_sh:2")` |
| `hr16_sh` | Shaker | 3 | `s("hr16_sh")` or `s("hr16_sh:0 hr16_sh:2")` |
| `alesishr16_sd` | Snare Drum | 1 | `s("alesishr16_sd")` |
| `hr16_sd` | Snare Drum | 1 | `s("hr16_sd")` |

#### Alesis SR-16
*26 drum types, 104 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `alesissr16_bd` | Bass Drum/Kick | 13 | `s("alesissr16_bd")` or `s("alesissr16_bd:0 alesissr16_bd:12")` |
| `sr16_bd` | Bass Drum/Kick | 13 | `s("sr16_bd")` or `s("sr16_bd:0 sr16_bd:12")` |
| `alesissr16_cp` | Clap | 1 | `s("alesissr16_cp")` |
| `sr16_cp` | Clap | 1 | `s("sr16_cp")` |
| `alesissr16_cb` | Cowbell | 1 | `s("alesissr16_cb")` |
| `sr16_cb` | Cowbell | 1 | `s("sr16_cb")` |
| `alesissr16_cr` | Crash Cymbal | 2 | `s("alesissr16_cr")` or `s("alesissr16_cr:0 alesissr16_cr:1")` |
| `sr16_cr` | Crash Cymbal | 2 | `s("sr16_cr")` or `s("sr16_cr:0 sr16_cr:1")` |
| `alesissr16_hh` | Hi-Hat (Closed) | 3 | `s("alesissr16_hh")` or `s("alesissr16_hh:0 alesissr16_hh:2")` |
| `sr16_hh` | Hi-Hat (Closed) | 3 | `s("sr16_hh")` or `s("sr16_hh:0 sr16_hh:2")` |
| `alesissr16_oh` | Hi-Hat (Open) | 4 | `s("alesissr16_oh")` or `s("alesissr16_oh:0 alesissr16_oh:3")` |
| `sr16_oh` | Hi-Hat (Open) | 4 | `s("sr16_oh")` or `s("sr16_oh:0 sr16_oh:3")` |
| `alesissr16_misc` | Miscellaneous | 3 | `s("alesissr16_misc")` or `s("alesissr16_misc:0 alesissr16_misc:2")` |
| `sr16_misc` | Miscellaneous | 3 | `s("sr16_misc")` or `s("sr16_misc:0 sr16_misc:2")` |
| `alesissr16_perc` | Percussion | 7 | `s("alesissr16_perc")` or `s("alesissr16_perc:0 alesissr16_perc:6")` |
| `sr16_perc` | Percussion | 7 | `s("sr16_perc")` or `s("sr16_perc:0 sr16_perc:6")` |
| `alesissr16_rd` | Ride Cymbal | 3 | `s("alesissr16_rd")` or `s("alesissr16_rd:0 alesissr16_rd:2")` |
| `sr16_rd` | Ride Cymbal | 3 | `s("sr16_rd")` or `s("sr16_rd:0 sr16_rd:2")` |
| `alesissr16_rim` | Rimshot | 1 | `s("alesissr16_rim")` |
| `sr16_rim` | Rimshot | 1 | `s("sr16_rim")` |
| `alesissr16_sh` | Shaker | 1 | `s("alesissr16_sh")` |
| `sr16_sh` | Shaker | 1 | `s("sr16_sh")` |
| `alesissr16_sd` | Snare Drum | 12 | `s("alesissr16_sd")` or `s("alesissr16_sd:0 alesissr16_sd:11")` |
| `sr16_sd` | Snare Drum | 12 | `s("sr16_sd")` or `s("sr16_sd:0 sr16_sd:11")` |
| `alesissr16_tb` | Tambourine | 1 | `s("alesissr16_tb")` |
| `sr16_tb` | Tambourine | 1 | `s("sr16_tb")` |

### Yamaha

#### Yamaha RX5
*10 drum types, 13 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `rx5_bd` | Bass Drum/Kick | 2 | `s("rx5_bd")` or `s("rx5_bd:0 rx5_bd:1")` |
| `rx5_cb` | Cowbell | 1 | `s("rx5_cb")` |
| `rx5_fx` | Effects | 1 | `s("rx5_fx")` |
| `rx5_hh` | Hi-Hat (Closed) | 1 | `s("rx5_hh")` |
| `rx5_oh` | Hi-Hat (Open) | 1 | `s("rx5_oh")` |
| `rx5_lt` | Low Tom | 1 | `s("rx5_lt")` |
| `rx5_rim` | Rimshot | 1 | `s("rx5_rim")` |
| `rx5_sh` | Shaker | 1 | `s("rx5_sh")` |
| `rx5_sd` | Snare Drum | 3 | `s("rx5_sd")` or `s("rx5_sd:0 rx5_sd:2")` |
| `rx5_tb` | Tambourine | 1 | `s("rx5_tb")` |

#### Yamaha RX21
*9 drum types, 9 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `rx21_bd` | Bass Drum/Kick | 1 | `s("rx21_bd")` |
| `rx21_cp` | Clap | 1 | `s("rx21_cp")` |
| `rx21_cr` | Crash Cymbal | 1 | `s("rx21_cr")` |
| `rx21_hh` | Hi-Hat (Closed) | 1 | `s("rx21_hh")` |
| `rx21_oh` | Hi-Hat (Open) | 1 | `s("rx21_oh")` |
| `rx21_ht` | High Tom | 1 | `s("rx21_ht")` |
| `rx21_lt` | Low Tom | 1 | `s("rx21_lt")` |
| `rx21_mt` | Mid Tom | 1 | `s("rx21_mt")` |
| `rx21_sd` | Snare Drum | 1 | `s("rx21_sd")` |

#### Yamaha RY30
*16 drum types, 84 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `ry30_bd` | Bass Drum/Kick | 13 | `s("ry30_bd")` or `s("ry30_bd:0 ry30_bd:12")` |
| `ry30_cp` | Clap | 1 | `s("ry30_cp")` |
| `ry30_cb` | Cowbell | 2 | `s("ry30_cb")` or `s("ry30_cb:0 ry30_cb:1")` |
| `ry30_cr` | Crash Cymbal | 2 | `s("ry30_cr")` or `s("ry30_cr:0 ry30_cr:1")` |
| `ry30_hh` | Hi-Hat (Closed) | 4 | `s("ry30_hh")` or `s("ry30_hh:0 ry30_hh:3")` |
| `ry30_oh` | Hi-Hat (Open) | 4 | `s("ry30_oh")` or `s("ry30_oh:0 ry30_oh:3")` |
| `ry30_ht` | High Tom | 3 | `s("ry30_ht")` or `s("ry30_ht:0 ry30_ht:2")` |
| `ry30_lt` | Low Tom | 3 | `s("ry30_lt")` or `s("ry30_lt:0 ry30_lt:2")` |
| `ry30_mt` | Mid Tom | 2 | `s("ry30_mt")` or `s("ry30_mt:0 ry30_mt:1")` |
| `ry30_misc` | Miscellaneous | 8 | `s("ry30_misc")` or `s("ry30_misc:0 ry30_misc:7")` |
| `ry30_perc` | Percussion | 13 | `s("ry30_perc")` or `s("ry30_perc:0 ry30_perc:12")` |
| `ry30_rd` | Ride Cymbal | 3 | `s("ry30_rd")` or `s("ry30_rd:0 ry30_rd:2")` |
| `ry30_rim` | Rimshot | 2 | `s("ry30_rim")` or `s("ry30_rim:0 ry30_rim:1")` |
| `ry30_sh` | Shaker | 2 | `s("ry30_sh")` or `s("ry30_sh:0 ry30_sh:1")` |
| `ry30_sd` | Snare Drum | 21 | `s("ry30_sd")` or `s("ry30_sd:0 ry30_sd:20")` |
| `ry30_tb` | Tambourine | 1 | `s("ry30_tb")` |

#### Yamaha TG33
*16 drum types, 51 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `tg33_bd` | Bass Drum/Kick | 4 | `s("tg33_bd")` or `s("tg33_bd:0 tg33_bd:3")` |
| `tg33_cp` | Clap | 1 | `s("tg33_cp")` |
| `tg33_cb` | Cowbell | 3 | `s("tg33_cb")` or `s("tg33_cb:0 tg33_cb:2")` |
| `tg33_cr` | Crash Cymbal | 3 | `s("tg33_cr")` or `s("tg33_cr:0 tg33_cr:2")` |
| `tg33_fx` | Effects | 1 | `s("tg33_fx")` |
| `tg33_oh` | Hi-Hat (Open) | 1 | `s("tg33_oh")` |
| `tg33_ht` | High Tom | 2 | `s("tg33_ht")` or `s("tg33_ht:0 tg33_ht:1")` |
| `tg33_lt` | Low Tom | 2 | `s("tg33_lt")` or `s("tg33_lt:0 tg33_lt:1")` |
| `tg33_mt` | Mid Tom | 2 | `s("tg33_mt")` or `s("tg33_mt:0 tg33_mt:1")` |
| `tg33_misc` | Miscellaneous | 10 | `s("tg33_misc")` or `s("tg33_misc:0 tg33_misc:9")` |
| `tg33_perc` | Percussion | 12 | `s("tg33_perc")` or `s("tg33_perc:0 tg33_perc:11")` |
| `tg33_rd` | Ride Cymbal | 2 | `s("tg33_rd")` or `s("tg33_rd:0 tg33_rd:1")` |
| `tg33_rim` | Rimshot | 1 | `s("tg33_rim")` |
| `tg33_sh` | Shaker | 1 | `s("tg33_sh")` |
| `tg33_sd` | Snare Drum | 5 | `s("tg33_sd")` or `s("tg33_sd:0 tg33_sd:4")` |
| `tg33_tb` | Tambourine | 1 | `s("tg33_tb")` |

#### Yamaha RM50
*15 drum types, 485 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `rm50_bd` | Bass Drum/Kick | 103 | `s("rm50_bd")` or `s("rm50_bd:0 rm50_bd:102")` |
| `rm50_cp` | Clap | 2 | `s("rm50_cp")` or `s("rm50_cp:0 rm50_cp:1")` |
| `rm50_cb` | Cowbell | 6 | `s("rm50_cb")` or `s("rm50_cb:0 rm50_cb:5")` |
| `rm50_cr` | Crash Cymbal | 22 | `s("rm50_cr")` or `s("rm50_cr:0 rm50_cr:21")` |
| `rm50_hh` | Hi-Hat (Closed) | 18 | `s("rm50_hh")` or `s("rm50_hh:0 rm50_hh:17")` |
| `rm50_oh` | Hi-Hat (Open) | 12 | `s("rm50_oh")` or `s("rm50_oh:0 rm50_oh:11")` |
| `rm50_ht` | High Tom | 25 | `s("rm50_ht")` or `s("rm50_ht:0 rm50_ht:24")` |
| `rm50_lt` | Low Tom | 49 | `s("rm50_lt")` or `s("rm50_lt:0 rm50_lt:48")` |
| `rm50_mt` | Mid Tom | 34 | `s("rm50_mt")` or `s("rm50_mt:0 rm50_mt:33")` |
| `rm50_misc` | Miscellaneous | 28 | `s("rm50_misc")` or `s("rm50_misc:0 rm50_misc:27")` |
| `rm50_perc` | Percussion | 56 | `s("rm50_perc")` or `s("rm50_perc:0 rm50_perc:55")` |
| `rm50_rd` | Ride Cymbal | 13 | `s("rm50_rd")` or `s("rm50_rd:0 rm50_rd:12")` |
| `rm50_sh` | Shaker | 6 | `s("rm50_sh")` or `s("rm50_sh:0 rm50_sh:5")` |
| `rm50_sd` | Snare Drum | 108 | `s("rm50_sd")` or `s("rm50_sd:0 rm50_sd:107")` |
| `rm50_tb` | Tambourine | 3 | `s("rm50_tb")` or `s("rm50_tb:0 rm50_tb:2")` |

### Korg

#### Korg DDM-110
*9 drum types, 11 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `ddm110_bd` | Bass Drum/Kick | 1 | `s("ddm110_bd")` |
| `ddm110_cp` | Clap | 1 | `s("ddm110_cp")` |
| `ddm110_cr` | Crash Cymbal | 1 | `s("ddm110_cr")` |
| `ddm110_hh` | Hi-Hat (Closed) | 1 | `s("ddm110_hh")` |
| `ddm110_oh` | Hi-Hat (Open) | 1 | `s("ddm110_oh")` |
| `ddm110_ht` | High Tom | 2 | `s("ddm110_ht")` or `s("ddm110_ht:0 ddm110_ht:1")` |
| `ddm110_lt` | Low Tom | 2 | `s("ddm110_lt")` or `s("ddm110_lt:0 ddm110_lt:1")` |
| `ddm110_rim` | Rimshot | 1 | `s("ddm110_rim")` |
| `ddm110_sd` | Snare Drum | 1 | `s("ddm110_sd")` |

#### Korg KPR-77
*5 drum types, 5 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `kpr77_bd` | Bass Drum/Kick | 1 | `s("kpr77_bd")` |
| `kpr77_cp` | Clap | 1 | `s("kpr77_cp")` |
| `kpr77_hh` | Hi-Hat (Closed) | 1 | `s("kpr77_hh")` |
| `kpr77_oh` | Hi-Hat (Open) | 1 | `s("kpr77_oh")` |
| `kpr77_sd` | Snare Drum | 1 | `s("kpr77_sd")` |

#### Korg KR-55
*9 drum types, 10 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `kr55_bd` | Bass Drum/Kick | 1 | `s("kr55_bd")` |
| `kr55_cb` | Cowbell | 1 | `s("kr55_cb")` |
| `kr55_cr` | Crash Cymbal | 1 | `s("kr55_cr")` |
| `kr55_hh` | Hi-Hat (Closed) | 1 | `s("kr55_hh")` |
| `kr55_oh` | Hi-Hat (Open) | 1 | `s("kr55_oh")` |
| `kr55_ht` | High Tom | 1 | `s("kr55_ht")` |
| `kr55_perc` | Percussion | 2 | `s("kr55_perc")` or `s("kr55_perc:0 kr55_perc:1")` |
| `kr55_rim` | Rimshot | 1 | `s("kr55_rim")` |
| `kr55_sd` | Snare Drum | 1 | `s("kr55_sd")` |

#### Korg M1
*15 drum types, 44 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `m1_bd` | Bass Drum/Kick | 3 | `s("m1_bd")` or `s("m1_bd:0 m1_bd:2")` |
| `m1_cp` | Clap | 1 | `s("m1_cp")` |
| `m1_cb` | Cowbell | 1 | `s("m1_cb")` |
| `m1_cr` | Crash Cymbal | 1 | `s("m1_cr")` |
| `m1_hh` | Hi-Hat (Closed) | 2 | `s("m1_hh")` or `s("m1_hh:0 m1_hh:1")` |
| `m1_oh` | Hi-Hat (Open) | 2 | `s("m1_oh")` or `s("m1_oh:0 m1_oh:1")` |
| `m1_ht` | High Tom | 2 | `s("m1_ht")` or `s("m1_ht:0 m1_ht:1")` |
| `m1_mt` | Mid Tom | 1 | `s("m1_mt")` |
| `m1_misc` | Miscellaneous | 16 | `s("m1_misc")` or `s("m1_misc:0 m1_misc:15")` |
| `m1_perc` | Percussion | 7 | `s("m1_perc")` or `s("m1_perc:0 m1_perc:6")` |
| `m1_rd` | Ride Cymbal | 1 | `s("m1_rd")` |
| `m1_rim` | Rimshot | 1 | `s("m1_rim")` |
| `m1_sh` | Shaker | 1 | `s("m1_sh")` |
| `m1_sd` | Snare Drum | 4 | `s("m1_sd")` or `s("m1_sd:0 m1_sd:3")` |
| `m1_tb` | Tambourine | 1 | `s("m1_tb")` |

#### Korg Mini Pops
*5 drum types, 32 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `minipops_bd` | Bass Drum/Kick | 7 | `s("minipops_bd")` or `s("minipops_bd:0 minipops_bd:6")` |
| `minipops_hh` | Hi-Hat (Closed) | 4 | `s("minipops_hh")` or `s("minipops_hh:0 minipops_hh:3")` |
| `minipops_oh` | Hi-Hat (Open) | 4 | `s("minipops_oh")` or `s("minipops_oh:0 minipops_oh:3")` |
| `minipops_misc` | Miscellaneous | 4 | `s("minipops_misc")` or `s("minipops_misc:0 minipops_misc:3")` |
| `minipops_sd` | Snare Drum | 13 | `s("minipops_sd")` or `s("minipops_sd:0 minipops_sd:12")` |

#### Korg Poly-800
*1 drum types, 4 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `poly800_bd` | Bass Drum/Kick | 4 | `s("poly800_bd")` or `s("poly800_bd:0 poly800_bd:3")` |

#### Korg T3
*9 drum types, 27 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `t3_bd` | Bass Drum/Kick | 5 | `s("t3_bd")` or `s("t3_bd:0 t3_bd:4")` |
| `t3_cp` | Clap | 1 | `s("t3_cp")` |
| `t3_hh` | Hi-Hat (Closed) | 2 | `s("t3_hh")` or `s("t3_hh:0 t3_hh:1")` |
| `t3_oh` | Hi-Hat (Open) | 2 | `s("t3_oh")` or `s("t3_oh:0 t3_oh:1")` |
| `t3_misc` | Miscellaneous | 4 | `s("t3_misc")` or `s("t3_misc:0 t3_misc:3")` |
| `t3_perc` | Percussion | 4 | `s("t3_perc")` or `s("t3_perc:0 t3_perc:3")` |
| `t3_rim` | Rimshot | 1 | `s("t3_rim")` |
| `t3_sh` | Shaker | 3 | `s("t3_sh")` or `s("t3_sh:0 t3_sh:2")` |
| `t3_sd` | Snare Drum | 5 | `s("t3_sd")` or `s("t3_sd:0 t3_sd:4")` |

### Casio

#### Casio RZ-1
*22 drum types, 24 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `casiorz1_bd` | Bass Drum/Kick | 1 | `s("casiorz1_bd")` |
| `rz1_bd` | Bass Drum/Kick | 1 | `s("rz1_bd")` |
| `casiorz1_cp` | Clap | 1 | `s("casiorz1_cp")` |
| `rz1_cp` | Clap | 1 | `s("rz1_cp")` |
| `casiorz1_cb` | Cowbell | 1 | `s("casiorz1_cb")` |
| `rz1_cb` | Cowbell | 1 | `s("rz1_cb")` |
| `casiorz1_cr` | Crash Cymbal | 1 | `s("casiorz1_cr")` |
| `rz1_cr` | Crash Cymbal | 1 | `s("rz1_cr")` |
| `casiorz1_hh` | Hi-Hat (Closed) | 1 | `s("casiorz1_hh")` |
| `rz1_hh` | Hi-Hat (Closed) | 1 | `s("rz1_hh")` |
| `casiorz1_ht` | High Tom | 1 | `s("casiorz1_ht")` |
| `rz1_ht` | High Tom | 1 | `s("rz1_ht")` |
| `casiorz1_lt` | Low Tom | 1 | `s("casiorz1_lt")` |
| `rz1_lt` | Low Tom | 1 | `s("rz1_lt")` |
| `casiorz1_mt` | Mid Tom | 1 | `s("casiorz1_mt")` |
| `rz1_mt` | Mid Tom | 1 | `s("rz1_mt")` |
| `casiorz1_rd` | Ride Cymbal | 2 | `s("casiorz1_rd")` or `s("casiorz1_rd:0 casiorz1_rd:1")` |
| `rz1_rd` | Ride Cymbal | 2 | `s("rz1_rd")` or `s("rz1_rd:0 rz1_rd:1")` |
| `casiorz1_rim` | Rimshot | 1 | `s("casiorz1_rim")` |
| `rz1_rim` | Rimshot | 1 | `s("rz1_rim")` |
| `casiorz1_sd` | Snare Drum | 1 | `s("casiorz1_sd")` |
| `rz1_sd` | Snare Drum | 1 | `s("rz1_sd")` |

#### Casio SK-1
*12 drum types, 12 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `casiosk1_bd` | Bass Drum/Kick | 1 | `s("casiosk1_bd")` |
| `sk1_bd` | Bass Drum/Kick | 1 | `s("sk1_bd")` |
| `casiosk1_hh` | Hi-Hat (Closed) | 1 | `s("casiosk1_hh")` |
| `sk1_hh` | Hi-Hat (Closed) | 1 | `s("sk1_hh")` |
| `casiosk1_oh` | Hi-Hat (Open) | 1 | `s("casiosk1_oh")` |
| `sk1_oh` | Hi-Hat (Open) | 1 | `s("sk1_oh")` |
| `casiosk1_ht` | High Tom | 1 | `s("casiosk1_ht")` |
| `sk1_ht` | High Tom | 1 | `s("sk1_ht")` |
| `casiosk1_mt` | Mid Tom | 1 | `s("casiosk1_mt")` |
| `sk1_mt` | Mid Tom | 1 | `s("sk1_mt")` |
| `casiosk1_sd` | Snare Drum | 1 | `s("casiosk1_sd")` |
| `sk1_sd` | Snare Drum | 1 | `s("sk1_sd")` |

#### Casio VL-1
*6 drum types, 6 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `casiovl1_bd` | Bass Drum/Kick | 1 | `s("casiovl1_bd")` |
| `vl1_bd` | Bass Drum/Kick | 1 | `s("vl1_bd")` |
| `casiovl1_hh` | Hi-Hat (Closed) | 1 | `s("casiovl1_hh")` |
| `vl1_hh` | Hi-Hat (Closed) | 1 | `s("vl1_hh")` |
| `casiovl1_sd` | Snare Drum | 1 | `s("casiovl1_sd")` |
| `vl1_sd` | Snare Drum | 1 | `s("vl1_sd")` |

### Boss

#### Boss DR-55
*20 drum types, 60 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `bossdr550_bd` | Bass Drum/Kick | 5 | `s("bossdr550_bd")` or `s("bossdr550_bd:0 bossdr550_bd:4")` |
| `bossdr55_bd` | Bass Drum/Kick | 2 | `s("bossdr55_bd")` or `s("bossdr55_bd:0 bossdr55_bd:1")` |
| `bossdr550_cp` | Clap | 1 | `s("bossdr550_cp")` |
| `bossdr550_cb` | Cowbell | 2 | `s("bossdr550_cb")` or `s("bossdr550_cb:0 bossdr550_cb:1")` |
| `bossdr550_cr` | Crash Cymbal | 1 | `s("bossdr550_cr")` |
| `bossdr550_hh` | Hi-Hat (Closed) | 2 | `s("bossdr550_hh")` or `s("bossdr550_hh:0 bossdr550_hh:1")` |
| `bossdr55_hh` | Hi-Hat (Closed) | 2 | `s("bossdr55_hh")` or `s("bossdr55_hh:0 bossdr55_hh:1")` |
| `bossdr550_oh` | Hi-Hat (Open) | 2 | `s("bossdr550_oh")` or `s("bossdr550_oh:0 bossdr550_oh:1")` |
| `bossdr550_ht` | High Tom | 3 | `s("bossdr550_ht")` or `s("bossdr550_ht:0 bossdr550_ht:2")` |
| `bossdr550_lt` | Low Tom | 3 | `s("bossdr550_lt")` or `s("bossdr550_lt:0 bossdr550_lt:2")` |
| `bossdr550_mt` | Mid Tom | 2 | `s("bossdr550_mt")` or `s("bossdr550_mt:0 bossdr550_mt:1")` |
| `bossdr550_misc` | Miscellaneous | 3 | `s("bossdr550_misc")` or `s("bossdr550_misc:0 bossdr550_misc:2")` |
| `bossdr550_perc` | Percussion | 11 | `s("bossdr550_perc")` or `s("bossdr550_perc:0 bossdr550_perc:10")` |
| `bossdr550_rd` | Ride Cymbal | 2 | `s("bossdr550_rd")` or `s("bossdr550_rd:0 bossdr550_rd:1")` |
| `bossdr550_rim` | Rimshot | 1 | `s("bossdr550_rim")` |
| `bossdr55_rim` | Rimshot | 1 | `s("bossdr55_rim")` |
| `bossdr550_sh` | Shaker | 2 | `s("bossdr550_sh")` or `s("bossdr550_sh:0 bossdr550_sh:1")` |
| `bossdr550_sd` | Snare Drum | 6 | `s("bossdr550_sd")` or `s("bossdr550_sd:0 bossdr550_sd:5")` |
| `bossdr55_sd` | Snare Drum | 8 | `s("bossdr55_sd")` or `s("bossdr55_sd:0 bossdr55_sd:7")` |
| `bossdr550_tb` | Tambourine | 1 | `s("bossdr550_tb")` |

#### Boss DR-110
*7 drum types, 7 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `bossdr110_bd` | Bass Drum/Kick | 1 | `s("bossdr110_bd")` |
| `bossdr110_cp` | Clap | 1 | `s("bossdr110_cp")` |
| `bossdr110_cr` | Crash Cymbal | 1 | `s("bossdr110_cr")` |
| `bossdr110_hh` | Hi-Hat (Closed) | 1 | `s("bossdr110_hh")` |
| `bossdr110_oh` | Hi-Hat (Open) | 1 | `s("bossdr110_oh")` |
| `bossdr110_rd` | Ride Cymbal | 1 | `s("bossdr110_rd")` |
| `bossdr110_sd` | Snare Drum | 1 | `s("bossdr110_sd")` |

#### Boss DR-220
*11 drum types, 11 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `bossdr220_bd` | Bass Drum/Kick | 1 | `s("bossdr220_bd")` |
| `bossdr220_cp` | Clap | 1 | `s("bossdr220_cp")` |
| `bossdr220_cr` | Crash Cymbal | 1 | `s("bossdr220_cr")` |
| `bossdr220_hh` | Hi-Hat (Closed) | 1 | `s("bossdr220_hh")` |
| `bossdr220_oh` | Hi-Hat (Open) | 1 | `s("bossdr220_oh")` |
| `bossdr220_ht` | High Tom | 1 | `s("bossdr220_ht")` |
| `bossdr220_lt` | Low Tom | 1 | `s("bossdr220_lt")` |
| `bossdr220_mt` | Mid Tom | 1 | `s("bossdr220_mt")` |
| `bossdr220_perc` | Percussion | 1 | `s("bossdr220_perc")` |
| `bossdr220_rd` | Ride Cymbal | 1 | `s("bossdr220_rd")` |
| `bossdr220_sd` | Snare Drum | 1 | `s("bossdr220_sd")` |

### Simmons

#### Simmons SDS-5
*8 drum types, 64 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `sds5_bd` | Bass Drum/Kick | 12 | `s("sds5_bd")` or `s("sds5_bd:0 sds5_bd:11")` |
| `sds5_hh` | Hi-Hat (Closed) | 5 | `s("sds5_hh")` or `s("sds5_hh:0 sds5_hh:4")` |
| `sds5_oh` | Hi-Hat (Open) | 2 | `s("sds5_oh")` or `s("sds5_oh:0 sds5_oh:1")` |
| `sds5_ht` | High Tom | 3 | `s("sds5_ht")` or `s("sds5_ht:0 sds5_ht:2")` |
| `sds5_lt` | Low Tom | 8 | `s("sds5_lt")` or `s("sds5_lt:0 sds5_lt:7")` |
| `sds5_mt` | Mid Tom | 6 | `s("sds5_mt")` or `s("sds5_mt:0 sds5_mt:5")` |
| `sds5_rim` | Rimshot | 7 | `s("sds5_rim")` or `s("sds5_rim:0 sds5_rim:6")` |
| `sds5_sd` | Snare Drum | 21 | `s("sds5_sd")` or `s("sds5_sd:0 sds5_sd:20")` |

#### Simmons SDS-400
*4 drum types, 20 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `sds400_ht` | High Tom | 3 | `s("sds400_ht")` or `s("sds400_ht:0 sds400_ht:2")` |
| `sds400_lt` | Low Tom | 6 | `s("sds400_lt")` or `s("sds400_lt:0 sds400_lt:5")` |
| `sds400_mt` | Mid Tom | 8 | `s("sds400_mt")` or `s("sds400_mt:0 sds400_mt:7")` |
| `sds400_sd` | Snare Drum | 3 | `s("sds400_sd")` or `s("sds400_sd:0 sds400_sd:2")` |

### Other Classics

#### AJK Percusyn
*8 drum types, 10 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `ajkpercusyn_bd` | Bass Drum/Kick | 1 | `s("ajkpercusyn_bd")` |
| `percysyn_bd` | Bass Drum/Kick | 1 | `s("percysyn_bd")` |
| `ajkpercusyn_cb` | Cowbell | 2 | `s("ajkpercusyn_cb")` or `s("ajkpercusyn_cb:0 ajkpercusyn_cb:1")` |
| `percysyn_cb` | Cowbell | 2 | `s("percysyn_cb")` or `s("percysyn_cb:0 percysyn_cb:1")` |
| `ajkpercusyn_ht` | High Tom | 1 | `s("ajkpercusyn_ht")` |
| `percysyn_ht` | High Tom | 1 | `s("percysyn_ht")` |
| `ajkpercusyn_sd` | Snare Drum | 1 | `s("ajkpercusyn_sd")` |
| `percysyn_sd` | Snare Drum | 1 | `s("percysyn_sd")` |

#### Ace Tone Rhythm Ace
*7 drum types, 16 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `rhythmace_bd` | Bass Drum/Kick | 3 | `s("rhythmace_bd")` or `s("rhythmace_bd:0 rhythmace_bd:2")` |
| `rhythmace_hh` | Hi-Hat (Closed) | 1 | `s("rhythmace_hh")` |
| `rhythmace_oh` | Hi-Hat (Open) | 1 | `s("rhythmace_oh")` |
| `rhythmace_ht` | High Tom | 1 | `s("rhythmace_ht")` |
| `rhythmace_lt` | Low Tom | 1 | `s("rhythmace_lt")` |
| `rhythmace_perc` | Percussion | 6 | `s("rhythmace_perc")` or `s("rhythmace_perc:0 rhythmace_perc:5")` |
| `rhythmace_sd` | Snare Drum | 3 | `s("rhythmace_sd")` or `s("rhythmace_sd:0 rhythmace_sd:2")` |

#### Akai Linn
*13 drum types, 13 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `akailinn_bd` | Bass Drum/Kick | 1 | `s("akailinn_bd")` |
| `akailinn_cp` | Clap | 1 | `s("akailinn_cp")` |
| `akailinn_cb` | Cowbell | 1 | `s("akailinn_cb")` |
| `akailinn_cr` | Crash Cymbal | 1 | `s("akailinn_cr")` |
| `akailinn_hh` | Hi-Hat (Closed) | 1 | `s("akailinn_hh")` |
| `akailinn_oh` | Hi-Hat (Open) | 1 | `s("akailinn_oh")` |
| `akailinn_ht` | High Tom | 1 | `s("akailinn_ht")` |
| `akailinn_lt` | Low Tom | 1 | `s("akailinn_lt")` |
| `akailinn_mt` | Mid Tom | 1 | `s("akailinn_mt")` |
| `akailinn_rd` | Ride Cymbal | 1 | `s("akailinn_rd")` |
| `akailinn_sh` | Shaker | 1 | `s("akailinn_sh")` |
| `akailinn_sd` | Snare Drum | 1 | `s("akailinn_sd")` |
| `akailinn_tb` | Tambourine | 1 | `s("akailinn_tb")` |

#### Doepfer MS-404
*10 drum types, 12 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `doepferms404_bd` | Bass Drum/Kick | 2 | `s("doepferms404_bd")` or `s("doepferms404_bd:0 doepferms404_bd:1")` |
| `ms404_bd` | Bass Drum/Kick | 2 | `s("ms404_bd")` or `s("ms404_bd:0 ms404_bd:1")` |
| `doepferms404_hh` | Hi-Hat (Closed) | 1 | `s("doepferms404_hh")` |
| `ms404_hh` | Hi-Hat (Closed) | 1 | `s("ms404_hh")` |
| `doepferms404_oh` | Hi-Hat (Open) | 1 | `s("doepferms404_oh")` |
| `ms404_oh` | Hi-Hat (Open) | 1 | `s("ms404_oh")` |
| `doepferms404_lt` | Low Tom | 1 | `s("doepferms404_lt")` |
| `ms404_lt` | Low Tom | 1 | `s("ms404_lt")` |
| `doepferms404_sd` | Snare Drum | 1 | `s("doepferms404_sd")` |
| `ms404_sd` | Snare Drum | 1 | `s("ms404_sd")` |

#### E-mu Modular
*3 drum types, 5 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `emumodular_bd` | Bass Drum/Kick | 2 | `s("emumodular_bd")` or `s("emumodular_bd:0 emumodular_bd:1")` |
| `emumodular_misc` | Miscellaneous | 1 | `s("emumodular_misc")` |
| `emumodular_perc` | Percussion | 2 | `s("emumodular_perc")` or `s("emumodular_perc:0 emumodular_perc:1")` |

#### Korg
*63 drum types, 145 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `korgddm110_bd` | Bass Drum/Kick | 1 | `s("korgddm110_bd")` |
| `korgkpr77_bd` | Bass Drum/Kick | 1 | `s("korgkpr77_bd")` |
| `korgkr55_bd` | Bass Drum/Kick | 1 | `s("korgkr55_bd")` |
| `korgkrz_bd` | Bass Drum/Kick | 1 | `s("korgkrz_bd")` |
| `korgm1_bd` | Bass Drum/Kick | 3 | `s("korgm1_bd")` or `s("korgm1_bd:0 korgm1_bd:2")` |
| `korgminipops_bd` | Bass Drum/Kick | 7 | `s("korgminipops_bd")` or `s("korgminipops_bd:0 korgminipops_bd:6")` |
| `korgpoly800_bd` | Bass Drum/Kick | 4 | `s("korgpoly800_bd")` or `s("korgpoly800_bd:0 korgpoly800_bd:3")` |
| `korgt3_bd` | Bass Drum/Kick | 5 | `s("korgt3_bd")` or `s("korgt3_bd:0 korgt3_bd:4")` |
| `korgddm110_cp` | Clap | 1 | `s("korgddm110_cp")` |
| `korgkpr77_cp` | Clap | 1 | `s("korgkpr77_cp")` |
| `korgm1_cp` | Clap | 1 | `s("korgm1_cp")` |
| `korgt3_cp` | Clap | 1 | `s("korgt3_cp")` |
| `korgkr55_cb` | Cowbell | 1 | `s("korgkr55_cb")` |
| `korgm1_cb` | Cowbell | 1 | `s("korgm1_cb")` |
| `korgddm110_cr` | Crash Cymbal | 1 | `s("korgddm110_cr")` |
| `korgkr55_cr` | Crash Cymbal | 1 | `s("korgkr55_cr")` |
| `korgkrz_cr` | Crash Cymbal | 1 | `s("korgkrz_cr")` |
| `korgm1_cr` | Crash Cymbal | 1 | `s("korgm1_cr")` |
| `korgkrz_fx` | Effects | 2 | `s("korgkrz_fx")` or `s("korgkrz_fx:0 korgkrz_fx:1")` |
| `korgddm110_hh` | Hi-Hat (Closed) | 1 | `s("korgddm110_hh")` |
| `korgkpr77_hh` | Hi-Hat (Closed) | 1 | `s("korgkpr77_hh")` |
| `korgkr55_hh` | Hi-Hat (Closed) | 1 | `s("korgkr55_hh")` |
| `korgkrz_hh` | Hi-Hat (Closed) | 1 | `s("korgkrz_hh")` |
| `korgm1_hh` | Hi-Hat (Closed) | 2 | `s("korgm1_hh")` or `s("korgm1_hh:0 korgm1_hh:1")` |
| `korgminipops_hh` | Hi-Hat (Closed) | 4 | `s("korgminipops_hh")` or `s("korgminipops_hh:0 korgminipops_hh:3")` |
| `korgt3_hh` | Hi-Hat (Closed) | 2 | `s("korgt3_hh")` or `s("korgt3_hh:0 korgt3_hh:1")` |
| `korgddm110_oh` | Hi-Hat (Open) | 1 | `s("korgddm110_oh")` |
| `korgkpr77_oh` | Hi-Hat (Open) | 1 | `s("korgkpr77_oh")` |
| `korgkr55_oh` | Hi-Hat (Open) | 1 | `s("korgkr55_oh")` |
| `korgkrz_oh` | Hi-Hat (Open) | 1 | `s("korgkrz_oh")` |
| `korgm1_oh` | Hi-Hat (Open) | 2 | `s("korgm1_oh")` or `s("korgm1_oh:0 korgm1_oh:1")` |
| `korgminipops_oh` | Hi-Hat (Open) | 4 | `s("korgminipops_oh")` or `s("korgminipops_oh:0 korgminipops_oh:3")` |
| `korgt3_oh` | Hi-Hat (Open) | 2 | `s("korgt3_oh")` or `s("korgt3_oh:0 korgt3_oh:1")` |
| `korgddm110_ht` | High Tom | 2 | `s("korgddm110_ht")` or `s("korgddm110_ht:0 korgddm110_ht:1")` |
| `korgkr55_ht` | High Tom | 1 | `s("korgkr55_ht")` |
| `korgkrz_ht` | High Tom | 1 | `s("korgkrz_ht")` |
| `korgm1_ht` | High Tom | 2 | `s("korgm1_ht")` or `s("korgm1_ht:0 korgm1_ht:1")` |
| `korgddm110_lt` | Low Tom | 2 | `s("korgddm110_lt")` or `s("korgddm110_lt:0 korgddm110_lt:1")` |
| `korgkrz_lt` | Low Tom | 1 | `s("korgkrz_lt")` |
| `korgm1_mt` | Mid Tom | 1 | `s("korgm1_mt")` |
| `korgkrz_misc` | Miscellaneous | 1 | `s("korgkrz_misc")` |
| `korgm1_misc` | Miscellaneous | 16 | `s("korgm1_misc")` or `s("korgm1_misc:0 korgm1_misc:15")` |
| `korgminipops_misc` | Miscellaneous | 4 | `s("korgminipops_misc")` or `s("korgminipops_misc:0 korgminipops_misc:3")` |
| `korgt3_misc` | Miscellaneous | 4 | `s("korgt3_misc")` or `s("korgt3_misc:0 korgt3_misc:3")` |
| `korgkr55_perc` | Percussion | 2 | `s("korgkr55_perc")` or `s("korgkr55_perc:0 korgkr55_perc:1")` |
| `korgm1_perc` | Percussion | 7 | `s("korgm1_perc")` or `s("korgm1_perc:0 korgm1_perc:6")` |
| `korgt3_perc` | Percussion | 4 | `s("korgt3_perc")` or `s("korgt3_perc:0 korgt3_perc:3")` |
| `korgkrz_rd` | Ride Cymbal | 1 | `s("korgkrz_rd")` |
| `korgm1_rd` | Ride Cymbal | 1 | `s("korgm1_rd")` |
| `korgddm110_rim` | Rimshot | 1 | `s("korgddm110_rim")` |
| `korgkr55_rim` | Rimshot | 1 | `s("korgkr55_rim")` |
| `korgm1_rim` | Rimshot | 1 | `s("korgm1_rim")` |
| `korgt3_rim` | Rimshot | 1 | `s("korgt3_rim")` |
| `korgm1_sh` | Shaker | 1 | `s("korgm1_sh")` |
| `korgt3_sh` | Shaker | 3 | `s("korgt3_sh")` or `s("korgt3_sh:0 korgt3_sh:2")` |
| `korgddm110_sd` | Snare Drum | 1 | `s("korgddm110_sd")` |
| `korgkpr77_sd` | Snare Drum | 1 | `s("korgkpr77_sd")` |
| `korgkr55_sd` | Snare Drum | 1 | `s("korgkr55_sd")` |
| `korgkrz_sd` | Snare Drum | 2 | `s("korgkrz_sd")` or `s("korgkrz_sd:0 korgkrz_sd:1")` |
| `korgm1_sd` | Snare Drum | 4 | `s("korgm1_sd")` or `s("korgm1_sd:0 korgm1_sd:3")` |
| `korgminipops_sd` | Snare Drum | 13 | `s("korgminipops_sd")` or `s("korgminipops_sd:0 korgminipops_sd:12")` |
| `korgt3_sd` | Snare Drum | 5 | `s("korgt3_sd")` or `s("korgt3_sd:0 korgt3_sd:4")` |
| `korgm1_tb` | Tambourine | 1 | `s("korgm1_tb")` |

#### Korg Krz
*10 drum types, 12 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `krz_bd` | Bass Drum/Kick | 1 | `s("krz_bd")` |
| `krz_cr` | Crash Cymbal | 1 | `s("krz_cr")` |
| `krz_fx` | Effects | 2 | `s("krz_fx")` or `s("krz_fx:0 krz_fx:1")` |
| `krz_hh` | Hi-Hat (Closed) | 1 | `s("krz_hh")` |
| `krz_oh` | Hi-Hat (Open) | 1 | `s("krz_oh")` |
| `krz_ht` | High Tom | 1 | `s("krz_ht")` |
| `krz_lt` | Low Tom | 1 | `s("krz_lt")` |
| `krz_misc` | Miscellaneous | 1 | `s("krz_misc")` |
| `krz_rd` | Ride Cymbal | 1 | `s("krz_rd")` |
| `krz_sd` | Snare Drum | 2 | `s("krz_sd")` or `s("krz_sd:0 krz_sd:1")` |

#### Linn LM-8953
*11 drum types, 22 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `lm8953_bd` | Bass Drum/Kick | 3 | `s("lm8953_bd")` or `s("lm8953_bd:0 lm8953_bd:2")` |
| `lm8953_cr` | Crash Cymbal | 1 | `s("lm8953_cr")` |
| `lm8953_hh` | Hi-Hat (Closed) | 2 | `s("lm8953_hh")` or `s("lm8953_hh:0 lm8953_hh:1")` |
| `lm8953_oh` | Hi-Hat (Open) | 1 | `s("lm8953_oh")` |
| `lm8953_ht` | High Tom | 2 | `s("lm8953_ht")` or `s("lm8953_ht:0 lm8953_ht:1")` |
| `lm8953_lt` | Low Tom | 2 | `s("lm8953_lt")` or `s("lm8953_lt:0 lm8953_lt:1")` |
| `lm8953_mt` | Mid Tom | 2 | `s("lm8953_mt")` or `s("lm8953_mt:0 lm8953_mt:1")` |
| `lm8953_rd` | Ride Cymbal | 1 | `s("lm8953_rd")` |
| `lm8953_rim` | Rimshot | 2 | `s("lm8953_rim")` or `s("lm8953_rim:0 lm8953_rim:1")` |
| `lm8953_sd` | Snare Drum | 5 | `s("lm8953_sd")` or `s("lm8953_sd:0 lm8953_sd:4")` |
| `lm8953_tb` | Tambourine | 1 | `s("lm8953_tb")` |

#### MFB-512
*9 drum types, 9 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `mfb512_bd` | Bass Drum/Kick | 1 | `s("mfb512_bd")` |
| `mfb512_cp` | Clap | 1 | `s("mfb512_cp")` |
| `mfb512_cr` | Crash Cymbal | 1 | `s("mfb512_cr")` |
| `mfb512_hh` | Hi-Hat (Closed) | 1 | `s("mfb512_hh")` |
| `mfb512_oh` | Hi-Hat (Open) | 1 | `s("mfb512_oh")` |
| `mfb512_ht` | High Tom | 1 | `s("mfb512_ht")` |
| `mfb512_lt` | Low Tom | 1 | `s("mfb512_lt")` |
| `mfb512_mt` | Mid Tom | 1 | `s("mfb512_mt")` |
| `mfb512_sd` | Snare Drum | 1 | `s("mfb512_sd")` |

#### Moog Concertmate MG-1
*4 drum types, 10 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `concertmatemg1_bd` | Bass Drum/Kick | 3 | `s("concertmatemg1_bd")` or `s("concertmatemg1_bd:0 concertmatemg1_bd:2")` |
| `moogconcertmatemg1_bd` | Bass Drum/Kick | 3 | `s("moogconcertmatemg1_bd")` or `s("moogconcertmatemg1_bd:0 moogconcertmatemg1_bd:2")` |
| `concertmatemg1_sd` | Snare Drum | 2 | `s("concertmatemg1_sd")` or `s("concertmatemg1_sd:0 concertmatemg1_sd:1")` |
| `moogconcertmatemg1_sd` | Snare Drum | 2 | `s("moogconcertmatemg1_sd")` or `s("moogconcertmatemg1_sd:0 moogconcertmatemg1_sd:1")` |

#### Mridangam (Indian percussion)
*13 drum types, 131 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `mridangam_ardha` | Ardha | 20 | `s("mridangam_ardha")` or `s("mridangam_ardha:0 mridangam_ardha:19")` |
| `mridangam_chaapu` | Chaapu | 13 | `s("mridangam_chaapu")` or `s("mridangam_chaapu:0 mridangam_chaapu:12")` |
| `mridangam_dhi` | Dhi | 7 | `s("mridangam_dhi")` or `s("mridangam_dhi:0 mridangam_dhi:6")` |
| `mridangam_dhin` | Dhin | 8 | `s("mridangam_dhin")` or `s("mridangam_dhin:0 mridangam_dhin:7")` |
| `mridangam_dhum` | Dhum | 7 | `s("mridangam_dhum")` or `s("mridangam_dhum:0 mridangam_dhum:6")` |
| `mridangam_gumki` | Gumki | 14 | `s("mridangam_gumki")` or `s("mridangam_gumki:0 mridangam_gumki:13")` |
| `mridangam_ka` | Ka | 12 | `s("mridangam_ka")` or `s("mridangam_ka:0 mridangam_ka:11")` |
| `mridangam_ki` | Ki | 7 | `s("mridangam_ki")` or `s("mridangam_ki:0 mridangam_ki:6")` |
| `mridangam_na` | Na | 12 | `s("mridangam_na")` or `s("mridangam_na:0 mridangam_na:11")` |
| `mridangam_nam` | Nam | 8 | `s("mridangam_nam")` or `s("mridangam_nam:0 mridangam_nam:7")` |
| `mridangam_ta` | Ta | 9 | `s("mridangam_ta")` or `s("mridangam_ta:0 mridangam_ta:8")` |
| `mridangam_tha` | Tha | 7 | `s("mridangam_tha")` or `s("mridangam_tha:0 mridangam_tha:6")` |
| `mridangam_thom` | Thom | 7 | `s("mridangam_thom")` or `s("mridangam_thom:0 mridangam_thom:6")` |

#### Rhodes Polaris
*6 drum types, 24 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `polaris_bd` | Bass Drum/Kick | 4 | `s("polaris_bd")` or `s("polaris_bd:0 polaris_bd:3")` |
| `rhodespolaris_bd` | Bass Drum/Kick | 4 | `s("rhodespolaris_bd")` or `s("rhodespolaris_bd:0 rhodespolaris_bd:3")` |
| `polaris_misc` | Miscellaneous | 4 | `s("polaris_misc")` or `s("polaris_misc:0 polaris_misc:3")` |
| `rhodespolaris_misc` | Miscellaneous | 4 | `s("rhodespolaris_misc")` or `s("rhodespolaris_misc:0 rhodespolaris_misc:3")` |
| `polaris_sd` | Snare Drum | 4 | `s("polaris_sd")` or `s("polaris_sd:0 polaris_sd:3")` |
| `rhodespolaris_sd` | Snare Drum | 4 | `s("rhodespolaris_sd")` or `s("rhodespolaris_sd:0 rhodespolaris_sd:3")` |

#### Roland
*219 drum types, 834 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `rolandcompurhythm1000_bd` | Bass Drum/Kick | 1 | `s("rolandcompurhythm1000_bd")` |
| `rolandcompurhythm78_bd` | Bass Drum/Kick | 1 | `s("rolandcompurhythm78_bd")` |
| `rolandcompurhythm8000_bd` | Bass Drum/Kick | 1 | `s("rolandcompurhythm8000_bd")` |
| `rolandd110_bd` | Bass Drum/Kick | 1 | `s("rolandd110_bd")` |
| `rolandd70_bd` | Bass Drum/Kick | 4 | `s("rolandd70_bd")` or `s("rolandd70_bd:0 rolandd70_bd:3")` |
| `rolandddr30_bd` | Bass Drum/Kick | 8 | `s("rolandddr30_bd")` or `s("rolandddr30_bd:0 rolandddr30_bd:7")` |
| `rolandjd990_bd` | Bass Drum/Kick | 10 | `s("rolandjd990_bd")` or `s("rolandjd990_bd:0 rolandjd990_bd:9")` |
| `rolandmc202_bd` | Bass Drum/Kick | 5 | `s("rolandmc202_bd")` or `s("rolandmc202_bd:0 rolandmc202_bd:4")` |
| `rolandmc303_bd` | Bass Drum/Kick | 16 | `s("rolandmc303_bd")` or `s("rolandmc303_bd:0 rolandmc303_bd:15")` |
| `rolandmt32_bd` | Bass Drum/Kick | 1 | `s("rolandmt32_bd")` |
| `rolandr8_bd` | Bass Drum/Kick | 7 | `s("rolandr8_bd")` or `s("rolandr8_bd:0 rolandr8_bd:6")` |
| `rolands50_bd` | Bass Drum/Kick | 4 | `s("rolands50_bd")` or `s("rolands50_bd:0 rolands50_bd:3")` |
| `rolandsh09_bd` | Bass Drum/Kick | 43 | `s("rolandsh09_bd")` or `s("rolandsh09_bd:0 rolandsh09_bd:42")` |
| `rolandsystem100_bd` | Bass Drum/Kick | 15 | `s("rolandsystem100_bd")` or `s("rolandsystem100_bd:0 rolandsystem100_bd:14")` |
| `rolandtr505_bd` | Bass Drum/Kick | 1 | `s("rolandtr505_bd")` |
| `rolandtr606_bd` | Bass Drum/Kick | 1 | `s("rolandtr606_bd")` |
| `rolandtr626_bd` | Bass Drum/Kick | 2 | `s("rolandtr626_bd")` or `s("rolandtr626_bd:0 rolandtr626_bd:1")` |
| `rolandtr707_bd` | Bass Drum/Kick | 2 | `s("rolandtr707_bd")` or `s("rolandtr707_bd:0 rolandtr707_bd:1")` |
| `rolandtr808_bd` | Bass Drum/Kick | 25 | `s("rolandtr808_bd")` or `s("rolandtr808_bd:0 rolandtr808_bd:24")` |
| `rolandtr909_bd` | Bass Drum/Kick | 4 | `s("rolandtr909_bd")` or `s("rolandtr909_bd:0 rolandtr909_bd:3")` |
| `rolandcompurhythm1000_cp` | Clap | 1 | `s("rolandcompurhythm1000_cp")` |
| `rolandcompurhythm8000_cp` | Clap | 1 | `s("rolandcompurhythm8000_cp")` |
| `rolandd70_cp` | Clap | 1 | `s("rolandd70_cp")` |
| `rolandjd990_cp` | Clap | 1 | `s("rolandjd990_cp")` |
| `rolandmc303_cp` | Clap | 8 | `s("rolandmc303_cp")` or `s("rolandmc303_cp:0 rolandmc303_cp:7")` |
| `rolandmt32_cp` | Clap | 1 | `s("rolandmt32_cp")` |
| `rolandr8_cp` | Clap | 1 | `s("rolandr8_cp")` |
| `rolands50_cp` | Clap | 1 | `s("rolands50_cp")` |
| `rolandtr505_cp` | Clap | 1 | `s("rolandtr505_cp")` |
| `rolandtr626_cp` | Clap | 1 | `s("rolandtr626_cp")` |
| `rolandtr707_cp` | Clap | 1 | `s("rolandtr707_cp")` |
| `rolandtr808_cp` | Clap | 5 | `s("rolandtr808_cp")` or `s("rolandtr808_cp:0 rolandtr808_cp:4")` |
| `rolandtr909_cp` | Clap | 5 | `s("rolandtr909_cp")` or `s("rolandtr909_cp:0 rolandtr909_cp:4")` |
| `rolandcompurhythm1000_cb` | Cowbell | 1 | `s("rolandcompurhythm1000_cb")` |
| `rolandcompurhythm78_cb` | Cowbell | 1 | `s("rolandcompurhythm78_cb")` |
| `rolandcompurhythm8000_cb` | Cowbell | 1 | `s("rolandcompurhythm8000_cb")` |
| `rolandd110_cb` | Cowbell | 2 | `s("rolandd110_cb")` or `s("rolandd110_cb:0 rolandd110_cb:1")` |
| `rolandd70_cb` | Cowbell | 1 | `s("rolandd70_cb")` |
| `rolandjd990_cb` | Cowbell | 1 | `s("rolandjd990_cb")` |
| `rolandmc303_cb` | Cowbell | 2 | `s("rolandmc303_cb")` or `s("rolandmc303_cb:0 rolandmc303_cb:1")` |
| `rolandmt32_cb` | Cowbell | 1 | `s("rolandmt32_cb")` |
| `rolandr8_cb` | Cowbell | 1 | `s("rolandr8_cb")` |
| `rolands50_cb` | Cowbell | 1 | `s("rolands50_cb")` |
| `rolandtr505_cb` | Cowbell | 2 | `s("rolandtr505_cb")` or `s("rolandtr505_cb:0 rolandtr505_cb:1")` |
| `rolandtr626_cb` | Cowbell | 1 | `s("rolandtr626_cb")` |
| `rolandtr707_cb` | Cowbell | 1 | `s("rolandtr707_cb")` |
| `rolandtr808_cb` | Cowbell | 2 | `s("rolandtr808_cb")` or `s("rolandtr808_cb:0 rolandtr808_cb:1")` |
| `rolandcompurhythm1000_cr` | Crash Cymbal | 1 | `s("rolandcompurhythm1000_cr")` |
| `rolandcompurhythm8000_cr` | Crash Cymbal | 1 | `s("rolandcompurhythm8000_cr")` |
| `rolandd110_cr` | Crash Cymbal | 1 | `s("rolandd110_cr")` |
| `rolandd70_cr` | Crash Cymbal | 1 | `s("rolandd70_cr")` |
| `rolandjd990_cr` | Crash Cymbal | 1 | `s("rolandjd990_cr")` |
| `rolandmt32_cr` | Crash Cymbal | 1 | `s("rolandmt32_cr")` |
| `rolandr8_cr` | Crash Cymbal | 1 | `s("rolandr8_cr")` |
| `rolands50_cr` | Crash Cymbal | 2 | `s("rolands50_cr")` or `s("rolands50_cr:0 rolands50_cr:1")` |
| `rolandtr505_cr` | Crash Cymbal | 1 | `s("rolandtr505_cr")` |
| `rolandtr606_cr` | Crash Cymbal | 1 | `s("rolandtr606_cr")` |
| `rolandtr626_cr` | Crash Cymbal | 2 | `s("rolandtr626_cr")` or `s("rolandtr626_cr:0 rolandtr626_cr:1")` |
| `rolandtr707_cr` | Crash Cymbal | 1 | `s("rolandtr707_cr")` |
| `rolandtr808_cr` | Crash Cymbal | 25 | `s("rolandtr808_cr")` or `s("rolandtr808_cr:0 rolandtr808_cr:24")` |
| `rolandtr909_cr` | Crash Cymbal | 5 | `s("rolandtr909_cr")` or `s("rolandtr909_cr:0 rolandtr909_cr:4")` |
| `rolandmc303_fx` | Effects | 2 | `s("rolandmc303_fx")` or `s("rolandmc303_fx:0 rolandmc303_fx:1")` |
| `rolandcompurhythm1000_hh` | Hi-Hat (Closed) | 1 | `s("rolandcompurhythm1000_hh")` |
| `rolandcompurhythm78_hh` | Hi-Hat (Closed) | 2 | `s("rolandcompurhythm78_hh")` or `s("rolandcompurhythm78_hh:0 rolandcompurhythm78_hh:1")` |
| `rolandcompurhythm8000_hh` | Hi-Hat (Closed) | 1 | `s("rolandcompurhythm8000_hh")` |
| `rolandd110_hh` | Hi-Hat (Closed) | 1 | `s("rolandd110_hh")` |
| `rolandd70_hh` | Hi-Hat (Closed) | 1 | `s("rolandd70_hh")` |
| `rolandjd990_hh` | Hi-Hat (Closed) | 4 | `s("rolandjd990_hh")` or `s("rolandjd990_hh:0 rolandjd990_hh:3")` |
| `rolandmc303_hh` | Hi-Hat (Closed) | 6 | `s("rolandmc303_hh")` or `s("rolandmc303_hh:0 rolandmc303_hh:5")` |
| `rolandmt32_hh` | Hi-Hat (Closed) | 1 | `s("rolandmt32_hh")` |
| `rolandr8_hh` | Hi-Hat (Closed) | 2 | `s("rolandr8_hh")` or `s("rolandr8_hh:0 rolandr8_hh:1")` |
| `rolandsystem100_hh` | Hi-Hat (Closed) | 2 | `s("rolandsystem100_hh")` or `s("rolandsystem100_hh:0 rolandsystem100_hh:1")` |
| `rolandtr505_hh` | Hi-Hat (Closed) | 1 | `s("rolandtr505_hh")` |
| `rolandtr606_hh` | Hi-Hat (Closed) | 1 | `s("rolandtr606_hh")` |
| `rolandtr626_hh` | Hi-Hat (Closed) | 1 | `s("rolandtr626_hh")` |
| `rolandtr707_hh` | Hi-Hat (Closed) | 1 | `s("rolandtr707_hh")` |
| `rolandtr808_hh` | Hi-Hat (Closed) | 1 | `s("rolandtr808_hh")` |
| `rolandtr909_hh` | Hi-Hat (Closed) | 4 | `s("rolandtr909_hh")` or `s("rolandtr909_hh:0 rolandtr909_hh:3")` |
| `rolandcompurhythm1000_oh` | Hi-Hat (Open) | 1 | `s("rolandcompurhythm1000_oh")` |
| `rolandcompurhythm78_oh` | Hi-Hat (Open) | 2 | `s("rolandcompurhythm78_oh")` or `s("rolandcompurhythm78_oh:0 rolandcompurhythm78_oh:1")` |
| `rolandcompurhythm8000_oh` | Hi-Hat (Open) | 1 | `s("rolandcompurhythm8000_oh")` |
| `rolandd110_oh` | Hi-Hat (Open) | 2 | `s("rolandd110_oh")` or `s("rolandd110_oh:0 rolandd110_oh:1")` |
| `rolandd70_oh` | Hi-Hat (Open) | 1 | `s("rolandd70_oh")` |
| `rolandjd990_oh` | Hi-Hat (Open) | 2 | `s("rolandjd990_oh")` or `s("rolandjd990_oh:0 rolandjd990_oh:1")` |
| `rolandmc303_oh` | Hi-Hat (Open) | 5 | `s("rolandmc303_oh")` or `s("rolandmc303_oh:0 rolandmc303_oh:4")` |
| `rolandmt32_oh` | Hi-Hat (Open) | 2 | `s("rolandmt32_oh")` or `s("rolandmt32_oh:0 rolandmt32_oh:1")` |
| `rolandr8_oh` | Hi-Hat (Open) | 1 | `s("rolandr8_oh")` |
| `rolands50_oh` | Hi-Hat (Open) | 1 | `s("rolands50_oh")` |
| `rolandsystem100_oh` | Hi-Hat (Open) | 3 | `s("rolandsystem100_oh")` or `s("rolandsystem100_oh:0 rolandsystem100_oh:2")` |
| `rolandtr505_oh` | Hi-Hat (Open) | 1 | `s("rolandtr505_oh")` |
| `rolandtr606_oh` | Hi-Hat (Open) | 1 | `s("rolandtr606_oh")` |
| `rolandtr626_oh` | Hi-Hat (Open) | 1 | `s("rolandtr626_oh")` |
| `rolandtr707_oh` | Hi-Hat (Open) | 1 | `s("rolandtr707_oh")` |
| `rolandtr808_oh` | Hi-Hat (Open) | 5 | `s("rolandtr808_oh")` or `s("rolandtr808_oh:0 rolandtr808_oh:4")` |
| `rolandtr909_oh` | Hi-Hat (Open) | 5 | `s("rolandtr909_oh")` or `s("rolandtr909_oh:0 rolandtr909_oh:4")` |
| `rolandcompurhythm1000_ht` | High Tom | 1 | `s("rolandcompurhythm1000_ht")` |
| `rolandcompurhythm8000_ht` | High Tom | 1 | `s("rolandcompurhythm8000_ht")` |
| `rolandddr30_ht` | High Tom | 4 | `s("rolandddr30_ht")` or `s("rolandddr30_ht:0 rolandddr30_ht:3")` |
| `rolandjd990_ht` | High Tom | 1 | `s("rolandjd990_ht")` |
| `rolandmc202_ht` | High Tom | 3 | `s("rolandmc202_ht")` or `s("rolandmc202_ht:0 rolandmc202_ht:2")` |
| `rolandmc303_ht` | High Tom | 5 | `s("rolandmc303_ht")` or `s("rolandmc303_ht:0 rolandmc303_ht:4")` |
| `rolandmt32_ht` | High Tom | 1 | `s("rolandmt32_ht")` |
| `rolandr8_ht` | High Tom | 4 | `s("rolandr8_ht")` or `s("rolandr8_ht:0 rolandr8_ht:3")` |
| `rolands50_ht` | High Tom | 1 | `s("rolands50_ht")` |
| `rolandtr505_ht` | High Tom | 1 | `s("rolandtr505_ht")` |
| `rolandtr606_ht` | High Tom | 1 | `s("rolandtr606_ht")` |
| `rolandtr626_ht` | High Tom | 2 | `s("rolandtr626_ht")` or `s("rolandtr626_ht:0 rolandtr626_ht:1")` |
| `rolandtr707_ht` | High Tom | 1 | `s("rolandtr707_ht")` |
| `rolandtr808_ht` | High Tom | 5 | `s("rolandtr808_ht")` or `s("rolandtr808_ht:0 rolandtr808_ht:4")` |
| `rolandtr909_ht` | High Tom | 9 | `s("rolandtr909_ht")` or `s("rolandtr909_ht:0 rolandtr909_ht:8")` |
| `rolandcompurhythm1000_lt` | Low Tom | 1 | `s("rolandcompurhythm1000_lt")` |
| `rolandcompurhythm8000_lt` | Low Tom | 1 | `s("rolandcompurhythm8000_lt")` |
| `rolandd110_lt` | Low Tom | 1 | `s("rolandd110_lt")` |
| `rolandd70_lt` | Low Tom | 1 | `s("rolandd70_lt")` |
| `rolandddr30_lt` | Low Tom | 4 | `s("rolandddr30_lt")` or `s("rolandddr30_lt:0 rolandddr30_lt:3")` |
| `rolandjd990_lt` | Low Tom | 5 | `s("rolandjd990_lt")` or `s("rolandjd990_lt:0 rolandjd990_lt:4")` |
| `rolandmc303_lt` | Low Tom | 5 | `s("rolandmc303_lt")` or `s("rolandmc303_lt:0 rolandmc303_lt:4")` |
| `rolandmt32_lt` | Low Tom | 1 | `s("rolandmt32_lt")` |
| `rolandr8_lt` | Low Tom | 4 | `s("rolandr8_lt")` or `s("rolandr8_lt:0 rolandr8_lt:3")` |
| `rolands50_lt` | Low Tom | 2 | `s("rolands50_lt")` or `s("rolands50_lt:0 rolands50_lt:1")` |
| `rolandtr505_lt` | Low Tom | 1 | `s("rolandtr505_lt")` |
| `rolandtr606_lt` | Low Tom | 1 | `s("rolandtr606_lt")` |
| `rolandtr626_lt` | Low Tom | 2 | `s("rolandtr626_lt")` or `s("rolandtr626_lt:0 rolandtr626_lt:1")` |
| `rolandtr707_lt` | Low Tom | 1 | `s("rolandtr707_lt")` |
| `rolandtr808_lt` | Low Tom | 5 | `s("rolandtr808_lt")` or `s("rolandtr808_lt:0 rolandtr808_lt:4")` |
| `rolandtr909_lt` | Low Tom | 9 | `s("rolandtr909_lt")` or `s("rolandtr909_lt:0 rolandtr909_lt:8")` |
| `rolandcompurhythm1000_mt` | Mid Tom | 1 | `s("rolandcompurhythm1000_mt")` |
| `rolandcompurhythm8000_mt` | Mid Tom | 1 | `s("rolandcompurhythm8000_mt")` |
| `rolandd70_mt` | Mid Tom | 1 | `s("rolandd70_mt")` |
| `rolandjd990_mt` | Mid Tom | 2 | `s("rolandjd990_mt")` or `s("rolandjd990_mt:0 rolandjd990_mt:1")` |
| `rolandmc303_mt` | Mid Tom | 6 | `s("rolandmc303_mt")` or `s("rolandmc303_mt:0 rolandmc303_mt:5")` |
| `rolandmt32_mt` | Mid Tom | 1 | `s("rolandmt32_mt")` |
| `rolandr8_mt` | Mid Tom | 4 | `s("rolandr8_mt")` or `s("rolandr8_mt:0 rolandr8_mt:3")` |
| `rolands50_mt` | Mid Tom | 1 | `s("rolands50_mt")` |
| `rolandtr505_mt` | Mid Tom | 1 | `s("rolandtr505_mt")` |
| `rolandtr626_mt` | Mid Tom | 2 | `s("rolandtr626_mt")` or `s("rolandtr626_mt:0 rolandtr626_mt:1")` |
| `rolandtr707_mt` | Mid Tom | 1 | `s("rolandtr707_mt")` |
| `rolandtr808_mt` | Mid Tom | 5 | `s("rolandtr808_mt")` or `s("rolandtr808_mt:0 rolandtr808_mt:4")` |
| `rolandtr909_mt` | Mid Tom | 9 | `s("rolandtr909_mt")` or `s("rolandtr909_mt:0 rolandtr909_mt:8")` |
| `rolandcompurhythm78_misc` | Miscellaneous | 4 | `s("rolandcompurhythm78_misc")` or `s("rolandcompurhythm78_misc:0 rolandcompurhythm78_misc:3")` |
| `rolandjd990_misc` | Miscellaneous | 12 | `s("rolandjd990_misc")` or `s("rolandjd990_misc:0 rolandjd990_misc:11")` |
| `rolandmc303_misc` | Miscellaneous | 8 | `s("rolandmc303_misc")` or `s("rolandmc303_misc:0 rolandmc303_misc:7")` |
| `rolands50_misc` | Miscellaneous | 6 | `s("rolands50_misc")` or `s("rolands50_misc:0 rolands50_misc:5")` |
| `rolandsystem100_misc` | Miscellaneous | 2 | `s("rolandsystem100_misc")` or `s("rolandsystem100_misc:0 rolandsystem100_misc:1")` |
| `rolandcompurhythm1000_perc` | Percussion | 3 | `s("rolandcompurhythm1000_perc")` or `s("rolandcompurhythm1000_perc:0 rolandcompurhythm1000_perc:2")` |
| `rolandcompurhythm78_perc` | Percussion | 8 | `s("rolandcompurhythm78_perc")` or `s("rolandcompurhythm78_perc:0 rolandcompurhythm78_perc:7")` |
| `rolandcompurhythm8000_perc` | Percussion | 2 | `s("rolandcompurhythm8000_perc")` or `s("rolandcompurhythm8000_perc:0 rolandcompurhythm8000_perc:1")` |
| `rolandd110_perc` | Percussion | 3 | `s("rolandd110_perc")` or `s("rolandd110_perc:0 rolandd110_perc:2")` |
| `rolandd70_perc` | Percussion | 1 | `s("rolandd70_perc")` |
| `rolandjd990_perc` | Percussion | 6 | `s("rolandjd990_perc")` or `s("rolandjd990_perc:0 rolandjd990_perc:5")` |
| `rolandmc202_perc` | Percussion | 1 | `s("rolandmc202_perc")` |
| `rolandmc303_perc` | Percussion | 39 | `s("rolandmc303_perc")` or `s("rolandmc303_perc:0 rolandmc303_perc:38")` |
| `rolandmt32_perc` | Percussion | 13 | `s("rolandmt32_perc")` or `s("rolandmt32_perc:0 rolandmt32_perc:12")` |
| `rolandr8_perc` | Percussion | 8 | `s("rolandr8_perc")` or `s("rolandr8_perc:0 rolandr8_perc:7")` |
| `rolands50_perc` | Percussion | 14 | `s("rolands50_perc")` or `s("rolands50_perc:0 rolands50_perc:13")` |
| `rolandsystem100_perc` | Percussion | 19 | `s("rolandsystem100_perc")` or `s("rolandsystem100_perc:0 rolandsystem100_perc:18")` |
| `rolandtr505_perc` | Percussion | 3 | `s("rolandtr505_perc")` or `s("rolandtr505_perc:0 rolandtr505_perc:2")` |
| `rolandtr626_perc` | Percussion | 8 | `s("rolandtr626_perc")` or `s("rolandtr626_perc:0 rolandtr626_perc:7")` |
| `rolandtr727_perc` | Percussion | 10 | `s("rolandtr727_perc")` or `s("rolandtr727_perc:0 rolandtr727_perc:9")` |
| `rolandtr808_perc` | Percussion | 16 | `s("rolandtr808_perc")` or `s("rolandtr808_perc:0 rolandtr808_perc:15")` |
| `rolandcompurhythm1000_rd` | Ride Cymbal | 1 | `s("rolandcompurhythm1000_rd")` |
| `rolandd110_rd` | Ride Cymbal | 1 | `s("rolandd110_rd")` |
| `rolandd70_rd` | Ride Cymbal | 1 | `s("rolandd70_rd")` |
| `rolandjd990_rd` | Ride Cymbal | 1 | `s("rolandjd990_rd")` |
| `rolandmc303_rd` | Ride Cymbal | 2 | `s("rolandmc303_rd")` or `s("rolandmc303_rd:0 rolandmc303_rd:1")` |
| `rolandmt32_rd` | Ride Cymbal | 1 | `s("rolandmt32_rd")` |
| `rolandr8_rd` | Ride Cymbal | 2 | `s("rolandr8_rd")` or `s("rolandr8_rd:0 rolandr8_rd:1")` |
| `rolands50_rd` | Ride Cymbal | 1 | `s("rolands50_rd")` |
| `rolandtr505_rd` | Ride Cymbal | 1 | `s("rolandtr505_rd")` |
| `rolandtr626_rd` | Ride Cymbal | 2 | `s("rolandtr626_rd")` or `s("rolandtr626_rd:0 rolandtr626_rd:1")` |
| `rolandtr909_rd` | Ride Cymbal | 5 | `s("rolandtr909_rd")` or `s("rolandtr909_rd:0 rolandtr909_rd:4")` |
| `rolandcompurhythm1000_rim` | Rimshot | 1 | `s("rolandcompurhythm1000_rim")` |
| `rolandcompurhythm8000_rim` | Rimshot | 1 | `s("rolandcompurhythm8000_rim")` |
| `rolandd110_rim` | Rimshot | 1 | `s("rolandd110_rim")` |
| `rolandd70_rim` | Rimshot | 1 | `s("rolandd70_rim")` |
| `rolandmc303_rim` | Rimshot | 6 | `s("rolandmc303_rim")` or `s("rolandmc303_rim:0 rolandmc303_rim:5")` |
| `rolandmt32_rim` | Rimshot | 1 | `s("rolandmt32_rim")` |
| `rolandr8_rim` | Rimshot | 2 | `s("rolandr8_rim")` or `s("rolandr8_rim:0 rolandr8_rim:1")` |
| `rolandtr505_rim` | Rimshot | 1 | `s("rolandtr505_rim")` |
| `rolandtr626_rim` | Rimshot | 1 | `s("rolandtr626_rim")` |
| `rolandtr707_rim` | Rimshot | 1 | `s("rolandtr707_rim")` |
| `rolandtr808_rim` | Rimshot | 1 | `s("rolandtr808_rim")` |
| `rolandtr909_rim` | Rimshot | 3 | `s("rolandtr909_rim")` or `s("rolandtr909_rim:0 rolandtr909_rim:2")` |
| `rolandd110_sh` | Shaker | 1 | `s("rolandd110_sh")` |
| `rolandd70_sh` | Shaker | 1 | `s("rolandd70_sh")` |
| `rolandmc303_sh` | Shaker | 7 | `s("rolandmc303_sh")` or `s("rolandmc303_sh:0 rolandmc303_sh:6")` |
| `rolandmt32_sh` | Shaker | 2 | `s("rolandmt32_sh")` or `s("rolandmt32_sh:0 rolandmt32_sh:1")` |
| `rolandr8_sh` | Shaker | 2 | `s("rolandr8_sh")` or `s("rolandr8_sh:0 rolandr8_sh:1")` |
| `rolands50_sh` | Shaker | 4 | `s("rolands50_sh")` or `s("rolands50_sh:0 rolands50_sh:3")` |
| `rolandtr626_sh` | Shaker | 1 | `s("rolandtr626_sh")` |
| `rolandtr727_sh` | Shaker | 2 | `s("rolandtr727_sh")` or `s("rolandtr727_sh:0 rolandtr727_sh:1")` |
| `rolandtr808_sh` | Shaker | 2 | `s("rolandtr808_sh")` or `s("rolandtr808_sh:0 rolandtr808_sh:1")` |
| `rolandcompurhythm1000_sd` | Snare Drum | 1 | `s("rolandcompurhythm1000_sd")` |
| `rolandcompurhythm78_sd` | Snare Drum | 1 | `s("rolandcompurhythm78_sd")` |
| `rolandcompurhythm8000_sd` | Snare Drum | 1 | `s("rolandcompurhythm8000_sd")` |
| `rolandd110_sd` | Snare Drum | 3 | `s("rolandd110_sd")` or `s("rolandd110_sd:0 rolandd110_sd:2")` |
| `rolandd70_sd` | Snare Drum | 5 | `s("rolandd70_sd")` or `s("rolandd70_sd:0 rolandd70_sd:4")` |
| `rolandddr30_sd` | Snare Drum | 8 | `s("rolandddr30_sd")` or `s("rolandddr30_sd:0 rolandddr30_sd:7")` |
| `rolandjd990_sd` | Snare Drum | 15 | `s("rolandjd990_sd")` or `s("rolandjd990_sd:0 rolandjd990_sd:14")` |
| `rolandmc303_sd` | Snare Drum | 26 | `s("rolandmc303_sd")` or `s("rolandmc303_sd:0 rolandmc303_sd:25")` |
| `rolandmt32_sd` | Snare Drum | 2 | `s("rolandmt32_sd")` or `s("rolandmt32_sd:0 rolandmt32_sd:1")` |
| `rolandr8_sd` | Snare Drum | 12 | `s("rolandr8_sd")` or `s("rolandr8_sd:0 rolandr8_sd:11")` |
| `rolands50_sd` | Snare Drum | 3 | `s("rolands50_sd")` or `s("rolands50_sd:0 rolands50_sd:2")` |
| `rolandsystem100_sd` | Snare Drum | 21 | `s("rolandsystem100_sd")` or `s("rolandsystem100_sd:0 rolandsystem100_sd:20")` |
| `rolandtr505_sd` | Snare Drum | 1 | `s("rolandtr505_sd")` |
| `rolandtr606_sd` | Snare Drum | 1 | `s("rolandtr606_sd")` |
| `rolandtr626_sd` | Snare Drum | 3 | `s("rolandtr626_sd")` or `s("rolandtr626_sd:0 rolandtr626_sd:2")` |
| `rolandtr707_sd` | Snare Drum | 2 | `s("rolandtr707_sd")` or `s("rolandtr707_sd:0 rolandtr707_sd:1")` |
| `rolandtr808_sd` | Snare Drum | 25 | `s("rolandtr808_sd")` or `s("rolandtr808_sd:0 rolandtr808_sd:24")` |
| `rolandtr909_sd` | Snare Drum | 16 | `s("rolandtr909_sd")` or `s("rolandtr909_sd:0 rolandtr909_sd:15")` |
| `rolandcompurhythm78_tb` | Tambourine | 1 | `s("rolandcompurhythm78_tb")` |
| `rolandd110_tb` | Tambourine | 1 | `s("rolandd110_tb")` |
| `rolandjd990_tb` | Tambourine | 1 | `s("rolandjd990_tb")` |
| `rolandmc303_tb` | Tambourine | 5 | `s("rolandmc303_tb")` or `s("rolandmc303_tb:0 rolandmc303_tb:4")` |
| `rolandmt32_tb` | Tambourine | 1 | `s("rolandmt32_tb")` |
| `rolandr8_tb` | Tambourine | 1 | `s("rolandr8_tb")` |
| `rolands50_tb` | Tambourine | 2 | `s("rolands50_tb")` or `s("rolands50_tb:0 rolands50_tb:1")` |
| `rolandtr626_tb` | Tambourine | 1 | `s("rolandtr626_tb")` |
| `rolandtr707_tb` | Tambourine | 1 | `s("rolandtr707_tb")` |

#### Roland D-110
*12 drum types, 18 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `d110_bd` | Bass Drum/Kick | 1 | `s("d110_bd")` |
| `d110_cb` | Cowbell | 2 | `s("d110_cb")` or `s("d110_cb:0 d110_cb:1")` |
| `d110_cr` | Crash Cymbal | 1 | `s("d110_cr")` |
| `d110_hh` | Hi-Hat (Closed) | 1 | `s("d110_hh")` |
| `d110_oh` | Hi-Hat (Open) | 2 | `s("d110_oh")` or `s("d110_oh:0 d110_oh:1")` |
| `d110_lt` | Low Tom | 1 | `s("d110_lt")` |
| `d110_perc` | Percussion | 3 | `s("d110_perc")` or `s("d110_perc:0 d110_perc:2")` |
| `d110_rd` | Ride Cymbal | 1 | `s("d110_rd")` |
| `d110_rim` | Rimshot | 1 | `s("d110_rim")` |
| `d110_sh` | Shaker | 1 | `s("d110_sh")` |
| `d110_sd` | Snare Drum | 3 | `s("d110_sd")` or `s("d110_sd:0 d110_sd:2")` |
| `d110_tb` | Tambourine | 1 | `s("d110_tb")` |

#### Roland D-70
*13 drum types, 20 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `d70_bd` | Bass Drum/Kick | 4 | `s("d70_bd")` or `s("d70_bd:0 d70_bd:3")` |
| `d70_cp` | Clap | 1 | `s("d70_cp")` |
| `d70_cb` | Cowbell | 1 | `s("d70_cb")` |
| `d70_cr` | Crash Cymbal | 1 | `s("d70_cr")` |
| `d70_hh` | Hi-Hat (Closed) | 1 | `s("d70_hh")` |
| `d70_oh` | Hi-Hat (Open) | 1 | `s("d70_oh")` |
| `d70_lt` | Low Tom | 1 | `s("d70_lt")` |
| `d70_mt` | Mid Tom | 1 | `s("d70_mt")` |
| `d70_perc` | Percussion | 1 | `s("d70_perc")` |
| `d70_rd` | Ride Cymbal | 1 | `s("d70_rd")` |
| `d70_rim` | Rimshot | 1 | `s("d70_rim")` |
| `d70_sh` | Shaker | 1 | `s("d70_sh")` |
| `d70_sd` | Snare Drum | 5 | `s("d70_sd")` or `s("d70_sd:0 d70_sd:4")` |

#### Roland JD-990
*14 drum types, 62 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `jd990_bd` | Bass Drum/Kick | 10 | `s("jd990_bd")` or `s("jd990_bd:0 jd990_bd:9")` |
| `jd990_cp` | Clap | 1 | `s("jd990_cp")` |
| `jd990_cb` | Cowbell | 1 | `s("jd990_cb")` |
| `jd990_cr` | Crash Cymbal | 1 | `s("jd990_cr")` |
| `jd990_hh` | Hi-Hat (Closed) | 4 | `s("jd990_hh")` or `s("jd990_hh:0 jd990_hh:3")` |
| `jd990_oh` | Hi-Hat (Open) | 2 | `s("jd990_oh")` or `s("jd990_oh:0 jd990_oh:1")` |
| `jd990_ht` | High Tom | 1 | `s("jd990_ht")` |
| `jd990_lt` | Low Tom | 5 | `s("jd990_lt")` or `s("jd990_lt:0 jd990_lt:4")` |
| `jd990_mt` | Mid Tom | 2 | `s("jd990_mt")` or `s("jd990_mt:0 jd990_mt:1")` |
| `jd990_misc` | Miscellaneous | 12 | `s("jd990_misc")` or `s("jd990_misc:0 jd990_misc:11")` |
| `jd990_perc` | Percussion | 6 | `s("jd990_perc")` or `s("jd990_perc:0 jd990_perc:5")` |
| `jd990_rd` | Ride Cymbal | 1 | `s("jd990_rd")` |
| `jd990_sd` | Snare Drum | 15 | `s("jd990_sd")` or `s("jd990_sd:0 jd990_sd:14")` |
| `jd990_tb` | Tambourine | 1 | `s("jd990_tb")` |

#### Roland MC-202
*3 drum types, 9 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `mc202_bd` | Bass Drum/Kick | 5 | `s("mc202_bd")` or `s("mc202_bd:0 mc202_bd:4")` |
| `mc202_ht` | High Tom | 3 | `s("mc202_ht")` or `s("mc202_ht:0 mc202_ht:2")` |
| `mc202_perc` | Percussion | 1 | `s("mc202_perc")` |

#### Roland MC-303
*16 drum types, 148 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `mc303_bd` | Bass Drum/Kick | 16 | `s("mc303_bd")` or `s("mc303_bd:0 mc303_bd:15")` |
| `mc303_cp` | Clap | 8 | `s("mc303_cp")` or `s("mc303_cp:0 mc303_cp:7")` |
| `mc303_cb` | Cowbell | 2 | `s("mc303_cb")` or `s("mc303_cb:0 mc303_cb:1")` |
| `mc303_fx` | Effects | 2 | `s("mc303_fx")` or `s("mc303_fx:0 mc303_fx:1")` |
| `mc303_hh` | Hi-Hat (Closed) | 6 | `s("mc303_hh")` or `s("mc303_hh:0 mc303_hh:5")` |
| `mc303_oh` | Hi-Hat (Open) | 5 | `s("mc303_oh")` or `s("mc303_oh:0 mc303_oh:4")` |
| `mc303_ht` | High Tom | 5 | `s("mc303_ht")` or `s("mc303_ht:0 mc303_ht:4")` |
| `mc303_lt` | Low Tom | 5 | `s("mc303_lt")` or `s("mc303_lt:0 mc303_lt:4")` |
| `mc303_mt` | Mid Tom | 6 | `s("mc303_mt")` or `s("mc303_mt:0 mc303_mt:5")` |
| `mc303_misc` | Miscellaneous | 8 | `s("mc303_misc")` or `s("mc303_misc:0 mc303_misc:7")` |
| `mc303_perc` | Percussion | 39 | `s("mc303_perc")` or `s("mc303_perc:0 mc303_perc:38")` |
| `mc303_rd` | Ride Cymbal | 2 | `s("mc303_rd")` or `s("mc303_rd:0 mc303_rd:1")` |
| `mc303_rim` | Rimshot | 6 | `s("mc303_rim")` or `s("mc303_rim:0 mc303_rim:5")` |
| `mc303_sh` | Shaker | 7 | `s("mc303_sh")` or `s("mc303_sh:0 mc303_sh:6")` |
| `mc303_sd` | Snare Drum | 26 | `s("mc303_sd")` or `s("mc303_sd:0 mc303_sd:25")` |
| `mc303_tb` | Tambourine | 5 | `s("mc303_tb")` or `s("mc303_tb:0 mc303_tb:4")` |

#### Roland MT-32
*15 drum types, 30 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `mt32_bd` | Bass Drum/Kick | 1 | `s("mt32_bd")` |
| `mt32_cp` | Clap | 1 | `s("mt32_cp")` |
| `mt32_cb` | Cowbell | 1 | `s("mt32_cb")` |
| `mt32_cr` | Crash Cymbal | 1 | `s("mt32_cr")` |
| `mt32_hh` | Hi-Hat (Closed) | 1 | `s("mt32_hh")` |
| `mt32_oh` | Hi-Hat (Open) | 2 | `s("mt32_oh")` or `s("mt32_oh:0 mt32_oh:1")` |
| `mt32_ht` | High Tom | 1 | `s("mt32_ht")` |
| `mt32_lt` | Low Tom | 1 | `s("mt32_lt")` |
| `mt32_mt` | Mid Tom | 1 | `s("mt32_mt")` |
| `mt32_perc` | Percussion | 13 | `s("mt32_perc")` or `s("mt32_perc:0 mt32_perc:12")` |
| `mt32_rd` | Ride Cymbal | 1 | `s("mt32_rd")` |
| `mt32_rim` | Rimshot | 1 | `s("mt32_rim")` |
| `mt32_sh` | Shaker | 2 | `s("mt32_sh")` or `s("mt32_sh:0 mt32_sh:1")` |
| `mt32_sd` | Snare Drum | 2 | `s("mt32_sd")` or `s("mt32_sd:0 mt32_sd:1")` |
| `mt32_tb` | Tambourine | 1 | `s("mt32_tb")` |

#### Roland S-50
*14 drum types, 43 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `s50_bd` | Bass Drum/Kick | 4 | `s("s50_bd")` or `s("s50_bd:0 s50_bd:3")` |
| `s50_cp` | Clap | 1 | `s("s50_cp")` |
| `s50_cb` | Cowbell | 1 | `s("s50_cb")` |
| `s50_cr` | Crash Cymbal | 2 | `s("s50_cr")` or `s("s50_cr:0 s50_cr:1")` |
| `s50_oh` | Hi-Hat (Open) | 1 | `s("s50_oh")` |
| `s50_ht` | High Tom | 1 | `s("s50_ht")` |
| `s50_lt` | Low Tom | 2 | `s("s50_lt")` or `s("s50_lt:0 s50_lt:1")` |
| `s50_mt` | Mid Tom | 1 | `s("s50_mt")` |
| `s50_misc` | Miscellaneous | 6 | `s("s50_misc")` or `s("s50_misc:0 s50_misc:5")` |
| `s50_perc` | Percussion | 14 | `s("s50_perc")` or `s("s50_perc:0 s50_perc:13")` |
| `s50_rd` | Ride Cymbal | 1 | `s("s50_rd")` |
| `s50_sh` | Shaker | 4 | `s("s50_sh")` or `s("s50_sh:0 s50_sh:3")` |
| `s50_sd` | Snare Drum | 3 | `s("s50_sd")` or `s("s50_sd:0 s50_sd:2")` |
| `s50_tb` | Tambourine | 2 | `s("s50_tb")` or `s("s50_tb:0 s50_tb:1")` |

#### Roland SH-09
*1 drum types, 43 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `sh09_bd` | Bass Drum/Kick | 43 | `s("sh09_bd")` or `s("sh09_bd:0 sh09_bd:42")` |

#### Roland System-100
*6 drum types, 62 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `system100_bd` | Bass Drum/Kick | 15 | `s("system100_bd")` or `s("system100_bd:0 system100_bd:14")` |
| `system100_hh` | Hi-Hat (Closed) | 2 | `s("system100_hh")` or `s("system100_hh:0 system100_hh:1")` |
| `system100_oh` | Hi-Hat (Open) | 3 | `s("system100_oh")` or `s("system100_oh:0 system100_oh:2")` |
| `system100_misc` | Miscellaneous | 2 | `s("system100_misc")` or `s("system100_misc:0 system100_misc:1")` |
| `system100_perc` | Percussion | 19 | `s("system100_perc")` or `s("system100_perc:0 system100_perc:18")` |
| `system100_sd` | Snare Drum | 21 | `s("system100_sd")` or `s("system100_sd:0 system100_sd:20")` |

#### Sakata
*13 drum types, 20 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `sakatadpm48_bd` | Bass Drum/Kick | 3 | `s("sakatadpm48_bd")` or `s("sakatadpm48_bd:0 sakatadpm48_bd:2")` |
| `sakatadpm48_cp` | Clap | 1 | `s("sakatadpm48_cp")` |
| `sakatadpm48_cr` | Crash Cymbal | 1 | `s("sakatadpm48_cr")` |
| `sakatadpm48_hh` | Hi-Hat (Closed) | 2 | `s("sakatadpm48_hh")` or `s("sakatadpm48_hh:0 sakatadpm48_hh:1")` |
| `sakatadpm48_oh` | Hi-Hat (Open) | 1 | `s("sakatadpm48_oh")` |
| `sakatadpm48_ht` | High Tom | 1 | `s("sakatadpm48_ht")` |
| `sakatadpm48_lt` | Low Tom | 2 | `s("sakatadpm48_lt")` or `s("sakatadpm48_lt:0 sakatadpm48_lt:1")` |
| `sakatadpm48_mt` | Mid Tom | 1 | `s("sakatadpm48_mt")` |
| `sakatadpm48_perc` | Percussion | 2 | `s("sakatadpm48_perc")` or `s("sakatadpm48_perc:0 sakatadpm48_perc:1")` |
| `sakatadpm48_rd` | Ride Cymbal | 1 | `s("sakatadpm48_rd")` |
| `sakatadpm48_rim` | Rimshot | 1 | `s("sakatadpm48_rim")` |
| `sakatadpm48_sh` | Shaker | 2 | `s("sakatadpm48_sh")` or `s("sakatadpm48_sh:0 sakatadpm48_sh:1")` |
| `sakatadpm48_sd` | Snare Drum | 2 | `s("sakatadpm48_sd")` or `s("sakatadpm48_sd:0 sakatadpm48_sd:1")` |

#### Sakata DPM-48
*13 drum types, 20 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `dpm48_bd` | Bass Drum/Kick | 3 | `s("dpm48_bd")` or `s("dpm48_bd:0 dpm48_bd:2")` |
| `dpm48_cp` | Clap | 1 | `s("dpm48_cp")` |
| `dpm48_cr` | Crash Cymbal | 1 | `s("dpm48_cr")` |
| `dpm48_hh` | Hi-Hat (Closed) | 2 | `s("dpm48_hh")` or `s("dpm48_hh:0 dpm48_hh:1")` |
| `dpm48_oh` | Hi-Hat (Open) | 1 | `s("dpm48_oh")` |
| `dpm48_ht` | High Tom | 1 | `s("dpm48_ht")` |
| `dpm48_lt` | Low Tom | 2 | `s("dpm48_lt")` or `s("dpm48_lt:0 dpm48_lt:1")` |
| `dpm48_mt` | Mid Tom | 1 | `s("dpm48_mt")` |
| `dpm48_perc` | Percussion | 2 | `s("dpm48_perc")` or `s("dpm48_perc:0 dpm48_perc:1")` |
| `dpm48_rd` | Ride Cymbal | 1 | `s("dpm48_rd")` |
| `dpm48_rim` | Rimshot | 1 | `s("dpm48_rim")` |
| `dpm48_sh` | Shaker | 2 | `s("dpm48_sh")` or `s("dpm48_sh:0 dpm48_sh:1")` |
| `dpm48_sd` | Snare Drum | 2 | `s("dpm48_sd")` or `s("dpm48_sd:0 dpm48_sd:1")` |

#### Sequential Circuits Drum Tracks
*12 drum types, 12 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `circuitsdrumtracks_bd` | Bass Drum/Kick | 1 | `s("circuitsdrumtracks_bd")` |
| `circuitsdrumtracks_cp` | Clap | 1 | `s("circuitsdrumtracks_cp")` |
| `circuitsdrumtracks_cb` | Cowbell | 1 | `s("circuitsdrumtracks_cb")` |
| `circuitsdrumtracks_cr` | Crash Cymbal | 1 | `s("circuitsdrumtracks_cr")` |
| `circuitsdrumtracks_hh` | Hi-Hat (Closed) | 1 | `s("circuitsdrumtracks_hh")` |
| `circuitsdrumtracks_oh` | Hi-Hat (Open) | 1 | `s("circuitsdrumtracks_oh")` |
| `circuitsdrumtracks_ht` | High Tom | 1 | `s("circuitsdrumtracks_ht")` |
| `circuitsdrumtracks_rd` | Ride Cymbal | 1 | `s("circuitsdrumtracks_rd")` |
| `circuitsdrumtracks_rim` | Rimshot | 1 | `s("circuitsdrumtracks_rim")` |
| `circuitsdrumtracks_sh` | Shaker | 1 | `s("circuitsdrumtracks_sh")` |
| `circuitsdrumtracks_sd` | Snare Drum | 1 | `s("circuitsdrumtracks_sd")` |
| `circuitsdrumtracks_tb` | Tambourine | 1 | `s("circuitsdrumtracks_tb")` |

#### Sequential Circuits Tom
*7 drum types, 8 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `circuitstom_bd` | Bass Drum/Kick | 1 | `s("circuitstom_bd")` |
| `circuitstom_cp` | Clap | 1 | `s("circuitstom_cp")` |
| `circuitstom_cr` | Crash Cymbal | 1 | `s("circuitstom_cr")` |
| `circuitstom_hh` | Hi-Hat (Closed) | 1 | `s("circuitstom_hh")` |
| `circuitstom_oh` | Hi-Hat (Open) | 1 | `s("circuitstom_oh")` |
| `circuitstom_ht` | High Tom | 2 | `s("circuitstom_ht")` or `s("circuitstom_ht:0 circuitstom_ht:1")` |
| `circuitstom_sd` | Snare Drum | 1 | `s("circuitstom_sd")` |

#### Serge Modular
*3 drum types, 7 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `sergemodular_bd` | Bass Drum/Kick | 1 | `s("sergemodular_bd")` |
| `sergemodular_misc` | Miscellaneous | 1 | `s("sergemodular_misc")` |
| `sergemodular_perc` | Percussion | 5 | `s("sergemodular_perc")` or `s("sergemodular_perc:0 sergemodular_perc:4")` |

#### Simmons
*12 drum types, 84 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `simmonssds5_bd` | Bass Drum/Kick | 12 | `s("simmonssds5_bd")` or `s("simmonssds5_bd:0 simmonssds5_bd:11")` |
| `simmonssds5_hh` | Hi-Hat (Closed) | 5 | `s("simmonssds5_hh")` or `s("simmonssds5_hh:0 simmonssds5_hh:4")` |
| `simmonssds5_oh` | Hi-Hat (Open) | 2 | `s("simmonssds5_oh")` or `s("simmonssds5_oh:0 simmonssds5_oh:1")` |
| `simmonssds400_ht` | High Tom | 3 | `s("simmonssds400_ht")` or `s("simmonssds400_ht:0 simmonssds400_ht:2")` |
| `simmonssds5_ht` | High Tom | 3 | `s("simmonssds5_ht")` or `s("simmonssds5_ht:0 simmonssds5_ht:2")` |
| `simmonssds400_lt` | Low Tom | 6 | `s("simmonssds400_lt")` or `s("simmonssds400_lt:0 simmonssds400_lt:5")` |
| `simmonssds5_lt` | Low Tom | 8 | `s("simmonssds5_lt")` or `s("simmonssds5_lt:0 simmonssds5_lt:7")` |
| `simmonssds400_mt` | Mid Tom | 8 | `s("simmonssds400_mt")` or `s("simmonssds400_mt:0 simmonssds400_mt:7")` |
| `simmonssds5_mt` | Mid Tom | 6 | `s("simmonssds5_mt")` or `s("simmonssds5_mt:0 simmonssds5_mt:5")` |
| `simmonssds5_rim` | Rimshot | 7 | `s("simmonssds5_rim")` or `s("simmonssds5_rim:0 simmonssds5_rim:6")` |
| `simmonssds400_sd` | Snare Drum | 3 | `s("simmonssds400_sd")` or `s("simmonssds400_sd:0 simmonssds400_sd:2")` |
| `simmonssds5_sd` | Snare Drum | 21 | `s("simmonssds5_sd")` or `s("simmonssds5_sd:0 simmonssds5_sd:20")` |

#### SoundMaster
*5 drum types, 6 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `soundmastersr88_bd` | Bass Drum/Kick | 1 | `s("soundmastersr88_bd")` |
| `soundmastersr88_cr` | Crash Cymbal | 1 | `s("soundmastersr88_cr")` |
| `soundmastersr88_hh` | Hi-Hat (Closed) | 1 | `s("soundmastersr88_hh")` |
| `soundmastersr88_oh` | Hi-Hat (Open) | 1 | `s("soundmastersr88_oh")` |
| `soundmastersr88_sd` | Snare Drum | 2 | `s("soundmastersr88_sd")` or `s("soundmastersr88_sd:0 soundmastersr88_sd:1")` |

#### Univox
*4 drum types, 4 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `univoxmicrorhythmer12_bd` | Bass Drum/Kick | 1 | `s("univoxmicrorhythmer12_bd")` |
| `univoxmicrorhythmer12_hh` | Hi-Hat (Closed) | 1 | `s("univoxmicrorhythmer12_hh")` |
| `univoxmicrorhythmer12_oh` | Hi-Hat (Open) | 1 | `s("univoxmicrorhythmer12_oh")` |
| `univoxmicrorhythmer12_sd` | Snare Drum | 1 | `s("univoxmicrorhythmer12_sd")` |

#### Univox MicroRhythmer 12
*4 drum types, 4 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `microrhythmer12_bd` | Bass Drum/Kick | 1 | `s("microrhythmer12_bd")` |
| `microrhythmer12_hh` | Hi-Hat (Closed) | 1 | `s("microrhythmer12_hh")` |
| `microrhythmer12_oh` | Hi-Hat (Open) | 1 | `s("microrhythmer12_oh")` |
| `microrhythmer12_sd` | Snare Drum | 1 | `s("microrhythmer12_sd")` |

#### Unknown
*33 drum types, 88 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `bd` | Bass Drum/Kick | 14 | `s("bd")` or `s("bd:0 bd:13")` |
| `sequentialcircuitsdrumtracks_bd` | Bass Drum/Kick | 1 | `s("sequentialcircuitsdrumtracks_bd")` |
| `sequentialcircuitstom_bd` | Bass Drum/Kick | 1 | `s("sequentialcircuitstom_bd")` |
| `cp` | Clap | 1 | `s("cp")` |
| `sequentialcircuitsdrumtracks_cp` | Clap | 1 | `s("sequentialcircuitsdrumtracks_cp")` |
| `sequentialcircuitstom_cp` | Clap | 1 | `s("sequentialcircuitstom_cp")` |
| `cb` | Cowbell | 1 | `s("cb")` |
| `sequentialcircuitsdrumtracks_cb` | Cowbell | 1 | `s("sequentialcircuitsdrumtracks_cb")` |
| `cr` | Crash Cymbal | 1 | `s("cr")` |
| `sequentialcircuitsdrumtracks_cr` | Crash Cymbal | 1 | `s("sequentialcircuitsdrumtracks_cr")` |
| `sequentialcircuitstom_cr` | Crash Cymbal | 1 | `s("sequentialcircuitstom_cr")` |
| `hh` | Hi-Hat (Closed) | 2 | `s("hh")` or `s("hh:0 hh:1")` |
| `sequentialcircuitsdrumtracks_hh` | Hi-Hat (Closed) | 1 | `s("sequentialcircuitsdrumtracks_hh")` |
| `sequentialcircuitstom_hh` | Hi-Hat (Closed) | 1 | `s("sequentialcircuitstom_hh")` |
| `oh` | Hi-Hat (Open) | 1 | `s("oh")` |
| `sequentialcircuitsdrumtracks_oh` | Hi-Hat (Open) | 1 | `s("sequentialcircuitsdrumtracks_oh")` |
| `sequentialcircuitstom_oh` | Hi-Hat (Open) | 1 | `s("sequentialcircuitstom_oh")` |
| `ht` | High Tom | 6 | `s("ht")` or `s("ht:0 ht:5")` |
| `sequentialcircuitsdrumtracks_ht` | High Tom | 1 | `s("sequentialcircuitsdrumtracks_ht")` |
| `sequentialcircuitstom_ht` | High Tom | 2 | `s("sequentialcircuitstom_ht")` or `s("sequentialcircuitstom_ht:0 sequentialcircuitstom_ht:1")` |
| `lt` | Low Tom | 6 | `s("lt")` or `s("lt:0 lt:5")` |
| `mt` | Mid Tom | 4 | `s("mt")` or `s("mt:0 mt:3")` |
| `misc` | Miscellaneous | 7 | `s("misc")` or `s("misc:0 misc:6")` |
| `perc` | Percussion | 1 | `s("perc")` |
| `rd` | Ride Cymbal | 1 | `s("rd")` |
| `sequentialcircuitsdrumtracks_rd` | Ride Cymbal | 1 | `s("sequentialcircuitsdrumtracks_rd")` |
| `rim` | Rimshot | 2 | `s("rim")` or `s("rim:0 rim:1")` |
| `sequentialcircuitsdrumtracks_rim` | Rimshot | 1 | `s("sequentialcircuitsdrumtracks_rim")` |
| `sequentialcircuitsdrumtracks_sh` | Shaker | 1 | `s("sequentialcircuitsdrumtracks_sh")` |
| `sd` | Snare Drum | 21 | `s("sd")` or `s("sd:0 sd:20")` |
| `sequentialcircuitsdrumtracks_sd` | Snare Drum | 1 | `s("sequentialcircuitsdrumtracks_sd")` |
| `sequentialcircuitstom_sd` | Snare Drum | 1 | `s("sequentialcircuitstom_sd")` |
| `sequentialcircuitsdrumtracks_tb` | Tambourine | 1 | `s("sequentialcircuitsdrumtracks_tb")` |

#### Visco
*11 drum types, 40 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `viscospacedrum_bd` | Bass Drum/Kick | 11 | `s("viscospacedrum_bd")` or `s("viscospacedrum_bd:0 viscospacedrum_bd:10")` |
| `viscospacedrum_cb` | Cowbell | 1 | `s("viscospacedrum_cb")` |
| `viscospacedrum_hh` | Hi-Hat (Closed) | 6 | `s("viscospacedrum_hh")` or `s("viscospacedrum_hh:0 viscospacedrum_hh:5")` |
| `viscospacedrum_oh` | Hi-Hat (Open) | 3 | `s("viscospacedrum_oh")` or `s("viscospacedrum_oh:0 viscospacedrum_oh:2")` |
| `viscospacedrum_ht` | High Tom | 7 | `s("viscospacedrum_ht")` or `s("viscospacedrum_ht:0 viscospacedrum_ht:6")` |
| `viscospacedrum_lt` | Low Tom | 2 | `s("viscospacedrum_lt")` or `s("viscospacedrum_lt:0 viscospacedrum_lt:1")` |
| `viscospacedrum_mt` | Mid Tom | 2 | `s("viscospacedrum_mt")` or `s("viscospacedrum_mt:0 viscospacedrum_mt:1")` |
| `viscospacedrum_misc` | Miscellaneous | 2 | `s("viscospacedrum_misc")` or `s("viscospacedrum_misc:0 viscospacedrum_misc:1")` |
| `viscospacedrum_perc` | Percussion | 2 | `s("viscospacedrum_perc")` or `s("viscospacedrum_perc:0 viscospacedrum_perc:1")` |
| `viscospacedrum_rim` | Rimshot | 1 | `s("viscospacedrum_rim")` |
| `viscospacedrum_sd` | Snare Drum | 3 | `s("viscospacedrum_sd")` or `s("viscospacedrum_sd:0 viscospacedrum_sd:2")` |

#### Visco Space Drum
*11 drum types, 40 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `spacedrum_bd` | Bass Drum/Kick | 11 | `s("spacedrum_bd")` or `s("spacedrum_bd:0 spacedrum_bd:10")` |
| `spacedrum_cb` | Cowbell | 1 | `s("spacedrum_cb")` |
| `spacedrum_hh` | Hi-Hat (Closed) | 6 | `s("spacedrum_hh")` or `s("spacedrum_hh:0 spacedrum_hh:5")` |
| `spacedrum_oh` | Hi-Hat (Open) | 3 | `s("spacedrum_oh")` or `s("spacedrum_oh:0 spacedrum_oh:2")` |
| `spacedrum_ht` | High Tom | 7 | `s("spacedrum_ht")` or `s("spacedrum_ht:0 spacedrum_ht:6")` |
| `spacedrum_lt` | Low Tom | 2 | `s("spacedrum_lt")` or `s("spacedrum_lt:0 spacedrum_lt:1")` |
| `spacedrum_mt` | Mid Tom | 2 | `s("spacedrum_mt")` or `s("spacedrum_mt:0 spacedrum_mt:1")` |
| `spacedrum_misc` | Miscellaneous | 2 | `s("spacedrum_misc")` or `s("spacedrum_misc:0 spacedrum_misc:1")` |
| `spacedrum_perc` | Percussion | 2 | `s("spacedrum_perc")` or `s("spacedrum_perc:0 spacedrum_perc:1")` |
| `spacedrum_rim` | Rimshot | 1 | `s("spacedrum_rim")` |
| `spacedrum_sd` | Snare Drum | 3 | `s("spacedrum_sd")` or `s("spacedrum_sd:0 spacedrum_sd:2")` |

#### X-Drum
*11 drum types, 22 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `xdrumlm8953_bd` | Bass Drum/Kick | 3 | `s("xdrumlm8953_bd")` or `s("xdrumlm8953_bd:0 xdrumlm8953_bd:2")` |
| `xdrumlm8953_cr` | Crash Cymbal | 1 | `s("xdrumlm8953_cr")` |
| `xdrumlm8953_hh` | Hi-Hat (Closed) | 2 | `s("xdrumlm8953_hh")` or `s("xdrumlm8953_hh:0 xdrumlm8953_hh:1")` |
| `xdrumlm8953_oh` | Hi-Hat (Open) | 1 | `s("xdrumlm8953_oh")` |
| `xdrumlm8953_ht` | High Tom | 2 | `s("xdrumlm8953_ht")` or `s("xdrumlm8953_ht:0 xdrumlm8953_ht:1")` |
| `xdrumlm8953_lt` | Low Tom | 2 | `s("xdrumlm8953_lt")` or `s("xdrumlm8953_lt:0 xdrumlm8953_lt:1")` |
| `xdrumlm8953_mt` | Mid Tom | 2 | `s("xdrumlm8953_mt")` or `s("xdrumlm8953_mt:0 xdrumlm8953_mt:1")` |
| `xdrumlm8953_rd` | Ride Cymbal | 1 | `s("xdrumlm8953_rd")` |
| `xdrumlm8953_rim` | Rimshot | 2 | `s("xdrumlm8953_rim")` or `s("xdrumlm8953_rim:0 xdrumlm8953_rim:1")` |
| `xdrumlm8953_sd` | Snare Drum | 5 | `s("xdrumlm8953_sd")` or `s("xdrumlm8953_sd:0 xdrumlm8953_sd:4")` |
| `xdrumlm8953_tb` | Tambourine | 1 | `s("xdrumlm8953_tb")` |

#### Yamaha
*66 drum types, 642 variations*

| Sample Name | Type | Variations | Usage Example |
|-------------|------|------------|---------------|
| `yamaharm50_bd` | Bass Drum/Kick | 103 | `s("yamaharm50_bd")` or `s("yamaharm50_bd:0 yamaharm50_bd:102")` |
| `yamaharx21_bd` | Bass Drum/Kick | 1 | `s("yamaharx21_bd")` |
| `yamaharx5_bd` | Bass Drum/Kick | 2 | `s("yamaharx5_bd")` or `s("yamaharx5_bd:0 yamaharx5_bd:1")` |
| `yamahary30_bd` | Bass Drum/Kick | 13 | `s("yamahary30_bd")` or `s("yamahary30_bd:0 yamahary30_bd:12")` |
| `yamahatg33_bd` | Bass Drum/Kick | 4 | `s("yamahatg33_bd")` or `s("yamahatg33_bd:0 yamahatg33_bd:3")` |
| `yamaharm50_cp` | Clap | 2 | `s("yamaharm50_cp")` or `s("yamaharm50_cp:0 yamaharm50_cp:1")` |
| `yamaharx21_cp` | Clap | 1 | `s("yamaharx21_cp")` |
| `yamahary30_cp` | Clap | 1 | `s("yamahary30_cp")` |
| `yamahatg33_cp` | Clap | 1 | `s("yamahatg33_cp")` |
| `yamaharm50_cb` | Cowbell | 6 | `s("yamaharm50_cb")` or `s("yamaharm50_cb:0 yamaharm50_cb:5")` |
| `yamaharx5_cb` | Cowbell | 1 | `s("yamaharx5_cb")` |
| `yamahary30_cb` | Cowbell | 2 | `s("yamahary30_cb")` or `s("yamahary30_cb:0 yamahary30_cb:1")` |
| `yamahatg33_cb` | Cowbell | 3 | `s("yamahatg33_cb")` or `s("yamahatg33_cb:0 yamahatg33_cb:2")` |
| `yamaharm50_cr` | Crash Cymbal | 22 | `s("yamaharm50_cr")` or `s("yamaharm50_cr:0 yamaharm50_cr:21")` |
| `yamaharx21_cr` | Crash Cymbal | 1 | `s("yamaharx21_cr")` |
| `yamahary30_cr` | Crash Cymbal | 2 | `s("yamahary30_cr")` or `s("yamahary30_cr:0 yamahary30_cr:1")` |
| `yamahatg33_cr` | Crash Cymbal | 3 | `s("yamahatg33_cr")` or `s("yamahatg33_cr:0 yamahatg33_cr:2")` |
| `yamaharx5_fx` | Effects | 1 | `s("yamaharx5_fx")` |
| `yamahatg33_fx` | Effects | 1 | `s("yamahatg33_fx")` |
| `yamaharm50_hh` | Hi-Hat (Closed) | 18 | `s("yamaharm50_hh")` or `s("yamaharm50_hh:0 yamaharm50_hh:17")` |
| `yamaharx21_hh` | Hi-Hat (Closed) | 1 | `s("yamaharx21_hh")` |
| `yamaharx5_hh` | Hi-Hat (Closed) | 1 | `s("yamaharx5_hh")` |
| `yamahary30_hh` | Hi-Hat (Closed) | 4 | `s("yamahary30_hh")` or `s("yamahary30_hh:0 yamahary30_hh:3")` |
| `yamaharm50_oh` | Hi-Hat (Open) | 12 | `s("yamaharm50_oh")` or `s("yamaharm50_oh:0 yamaharm50_oh:11")` |
| `yamaharx21_oh` | Hi-Hat (Open) | 1 | `s("yamaharx21_oh")` |
| `yamaharx5_oh` | Hi-Hat (Open) | 1 | `s("yamaharx5_oh")` |
| `yamahary30_oh` | Hi-Hat (Open) | 4 | `s("yamahary30_oh")` or `s("yamahary30_oh:0 yamahary30_oh:3")` |
| `yamahatg33_oh` | Hi-Hat (Open) | 1 | `s("yamahatg33_oh")` |
| `yamaharm50_ht` | High Tom | 25 | `s("yamaharm50_ht")` or `s("yamaharm50_ht:0 yamaharm50_ht:24")` |
| `yamaharx21_ht` | High Tom | 1 | `s("yamaharx21_ht")` |
| `yamahary30_ht` | High Tom | 3 | `s("yamahary30_ht")` or `s("yamahary30_ht:0 yamahary30_ht:2")` |
| `yamahatg33_ht` | High Tom | 2 | `s("yamahatg33_ht")` or `s("yamahatg33_ht:0 yamahatg33_ht:1")` |
| `yamaharm50_lt` | Low Tom | 49 | `s("yamaharm50_lt")` or `s("yamaharm50_lt:0 yamaharm50_lt:48")` |
| `yamaharx21_lt` | Low Tom | 1 | `s("yamaharx21_lt")` |
| `yamaharx5_lt` | Low Tom | 1 | `s("yamaharx5_lt")` |
| `yamahary30_lt` | Low Tom | 3 | `s("yamahary30_lt")` or `s("yamahary30_lt:0 yamahary30_lt:2")` |
| `yamahatg33_lt` | Low Tom | 2 | `s("yamahatg33_lt")` or `s("yamahatg33_lt:0 yamahatg33_lt:1")` |
| `yamaharm50_mt` | Mid Tom | 34 | `s("yamaharm50_mt")` or `s("yamaharm50_mt:0 yamaharm50_mt:33")` |
| `yamaharx21_mt` | Mid Tom | 1 | `s("yamaharx21_mt")` |
| `yamahary30_mt` | Mid Tom | 2 | `s("yamahary30_mt")` or `s("yamahary30_mt:0 yamahary30_mt:1")` |
| `yamahatg33_mt` | Mid Tom | 2 | `s("yamahatg33_mt")` or `s("yamahatg33_mt:0 yamahatg33_mt:1")` |
| `yamaharm50_misc` | Miscellaneous | 28 | `s("yamaharm50_misc")` or `s("yamaharm50_misc:0 yamaharm50_misc:27")` |
| `yamahary30_misc` | Miscellaneous | 8 | `s("yamahary30_misc")` or `s("yamahary30_misc:0 yamahary30_misc:7")` |
| `yamahatg33_misc` | Miscellaneous | 10 | `s("yamahatg33_misc")` or `s("yamahatg33_misc:0 yamahatg33_misc:9")` |
| `yamaharm50_perc` | Percussion | 56 | `s("yamaharm50_perc")` or `s("yamaharm50_perc:0 yamaharm50_perc:55")` |
| `yamahary30_perc` | Percussion | 13 | `s("yamahary30_perc")` or `s("yamahary30_perc:0 yamahary30_perc:12")` |
| `yamahatg33_perc` | Percussion | 12 | `s("yamahatg33_perc")` or `s("yamahatg33_perc:0 yamahatg33_perc:11")` |
| `yamaharm50_rd` | Ride Cymbal | 13 | `s("yamaharm50_rd")` or `s("yamaharm50_rd:0 yamaharm50_rd:12")` |
| `yamahary30_rd` | Ride Cymbal | 3 | `s("yamahary30_rd")` or `s("yamahary30_rd:0 yamahary30_rd:2")` |
| `yamahatg33_rd` | Ride Cymbal | 2 | `s("yamahatg33_rd")` or `s("yamahatg33_rd:0 yamahatg33_rd:1")` |
| `yamaharx5_rim` | Rimshot | 1 | `s("yamaharx5_rim")` |
| `yamahary30_rim` | Rimshot | 2 | `s("yamahary30_rim")` or `s("yamahary30_rim:0 yamahary30_rim:1")` |
| `yamahatg33_rim` | Rimshot | 1 | `s("yamahatg33_rim")` |
| `yamaharm50_sh` | Shaker | 6 | `s("yamaharm50_sh")` or `s("yamaharm50_sh:0 yamaharm50_sh:5")` |
| `yamaharx5_sh` | Shaker | 1 | `s("yamaharx5_sh")` |
| `yamahary30_sh` | Shaker | 2 | `s("yamahary30_sh")` or `s("yamahary30_sh:0 yamahary30_sh:1")` |
| `yamahatg33_sh` | Shaker | 1 | `s("yamahatg33_sh")` |
| `yamaharm50_sd` | Snare Drum | 108 | `s("yamaharm50_sd")` or `s("yamaharm50_sd:0 yamaharm50_sd:107")` |
| `yamaharx21_sd` | Snare Drum | 1 | `s("yamaharx21_sd")` |
| `yamaharx5_sd` | Snare Drum | 3 | `s("yamaharx5_sd")` or `s("yamaharx5_sd:0 yamaharx5_sd:2")` |
| `yamahary30_sd` | Snare Drum | 21 | `s("yamahary30_sd")` or `s("yamahary30_sd:0 yamahary30_sd:20")` |
| `yamahatg33_sd` | Snare Drum | 5 | `s("yamahatg33_sd")` or `s("yamahatg33_sd:0 yamahatg33_sd:4")` |
| `yamaharm50_tb` | Tambourine | 3 | `s("yamaharm50_tb")` or `s("yamaharm50_tb:0 yamaharm50_tb:2")` |
| `yamaharx5_tb` | Tambourine | 1 | `s("yamaharx5_tb")` |
| `yamahary30_tb` | Tambourine | 1 | `s("yamahary30_tb")` |
| `yamahatg33_tb` | Tambourine | 1 | `s("yamahatg33_tb")` |

## Classic Patterns

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
