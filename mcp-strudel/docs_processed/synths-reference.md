# Strudel Synthesizers Reference

This is a comprehensive reference of all available synthesizers and sound generators in Strudel.

## Summary

- **Total Synthesizers**: 18
- **Categories**: 4

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

### Algorithmic Synths

*6 synthesizers*

| Synth Name | Usage Example |
|------------|---------------|
| `z_noise` | `sound("z_noise")` |
| `z_sawtooth` | `sound("z_sawtooth")` |
| `z_sine` | `sound("z_sine")` |
| `z_square` | `sound("z_square")` |
| `z_tan` | `sound("z_tan")` |
| `z_triangle` | `sound("z_triangle")` |

### Basic Waveforms

*6 synthesizers*

These are the fundamental waveforms available in Strudel:

| Synth Name | Description | Usage Example |
|------------|-------------|---------------|
| `pulse` | Variable pulse width wave | `note("c d e f").sound("pulse")` |
| `sawtooth` | Bright, buzzy sawtooth wave - rich in harmonics | `note("c d e f").sound("sawtooth")` |
| `sine` | Pure sine wave - smooth, fundamental tone | `note("c d e f").sound("sine")` |
| `square` | Hollow square wave - classic digital sound | `note("c d e f").sound("square")` |
| `supersaw` | Multiple detuned sawtooth waves - thick lead sound | `note("c d e f").sound("supersaw")` |
| `triangle` | Soft triangle wave - default for notes | `note("c d e f").sound("triangle")` |

### Digital/8-bit

*2 synthesizers*

| Synth Name | Usage Example |
|------------|---------------|
| `bytebeat` | `sound("bytebeat")` |
| `zzfx` | `sound("zzfx")` |

### Noise Generators

*4 synthesizers*

Different types of noise for percussion and textures:

| Synth Name | Description | Usage Example |
|------------|-------------|---------------|
| `brown` | Brown noise - deepest, smoothest noise | `sound("brown").decay(0.1)` |
| `crackle` | Subtle noise crackles - use with density parameter | `sound("crackle").decay(0.1)` |
| `pink` | Pink noise - softer, more natural than white | `sound("pink").decay(0.1)` |
| `white` | White noise - equal energy across all frequencies | `sound("white").decay(0.1)` |

## Examples

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
