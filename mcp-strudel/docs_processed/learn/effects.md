# Audio Effects

Whether you're using a synth or a sample, you can apply any of the following built-in audio effects.
As you might suspect, the effects can be chained together, and they accept a pattern string as their argument.

# Filters

Filters are an essential building block of [subtractive synthesis](https://en.wikipedia.org/wiki/Subtractive_synthesis).
Strudel comes with 3 types of filters:

- low-pass filter: low frequencies may _pass_, high frequencies are cut off
- high-pass filter: high frequencies may _pass_, low frequencies are cut off
- band-pass filters: only a frequency band may _pass_, low and high frequencies around are cut off

Each filter has 2 parameters:

- cutoff: the frequency at which the filter starts to work. e.g. a low-pass filter with a cutoff of 1000Hz allows frequencies below 1000Hz to pass.
- q-value: Controls the resonance of the filter. Higher values sound more aggressive. Also see [Q-Factor](https://en.wikipedia.org/wiki/Q_factor)

## lpf

##lpf##

*Function documentation for `lpf`*

## lpq

##lpq##

*Function documentation for `lpq`*

## hpf

##hpf##

*Function documentation for `hpf`*

## hpq

##hpq##

*Function documentation for `hpq`*

## bpf

##bpf##

*Function documentation for `bpf`*

## bpq

##bpq##

*Function documentation for `bpq`*

## ftype

##ftype##

*Function documentation for `ftype`*

## vowel

##vowel##

*Function documentation for `vowel`*

# Amplitude Envelope

The amplitude [envelope](<https://en.wikipedia.org/wiki/Envelope_(music)>) controls the dynamic contour of a sound.
Strudel uses ADSR envelopes, which are probably the most common way to describe an envelope:

![ADSR](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/ADSR_parameter.svg/1920px-ADSR_parameter.svg.png)

[image link](https://commons.wikimedia.org/wiki/File:ADSR_parameter.svg)

## attack

##attack##

*Function documentation for `attack`*

## decay

##decay##

*Function documentation for `decay`*

## sustain

##sustain##

*Function documentation for `sustain`*

## release

##release##

*Function documentation for `release`*

## adsr

##adsr##

*Function documentation for `adsr`*

# Filter Envelope

Each filter can receive an additional filter envelope controlling the cutoff value dynamically. It uses an ADSR envelope similar to the one used for amplitude. There is an additional parameter to control the depth of the filter modulation: `lpenv`|`hpenv`|`bpenv`. This allows you to play subtle or huge filter modulations just the same by only increasing or decreasing the depth.

```javascript
note("[c eb g <f bb>](3,8,<0 1>)".sub(12))
  .s("<sawtooth>/64")
  .lpf(sine.range(300,2000).slow(16))
  .lpa(0.005)
  .lpd(perlin.range(.02,.2))
  .lps(perlin.range(0,.5).slow(3))
  .lpq(sine.range(2,10).slow(32))
  .release(.5)
  .lpenv(perlin.range(1,8).slow(2))
  .ftype('24db')
  .room(1)
  .juxBy(.5,rev)
  .sometimes(add(note(12)))
  .stack(s("bd*2").bank('RolandTR909'))
  .gain(.5).fast(2)
```

There is one filter envelope for each filter type and thus one set of envelope filter parameters preceded either by `lp`, `hp` or `bp`:

- `lpattack`, `lpdecay`, `lpsustain`, `lprelease`, `lpenv`: filter envelope for the lowpass filter.
  - alternatively: `lpa`, `lpd`, `lps`, `lpr` and `lpe`.
- `hpattack`, `hpdecay`, `hpsustain`, `hprelease`, `hpenv`: filter envelope for the highpass filter.
  - alternatively: `hpa`, `hpd`, `hps`, `hpr` and `hpe`.
- `bpattack`, `bpdecay`, `bpsustain`, `bprelease`, `bpenv`: filter envelope for the bandpass filter.
  - alternatively: `bpa`, `bpd`, `bps`, `bpr` and `bpe`.

## lpattack

##lpattack##

*Function documentation for `lpattack`*

## lpdecay

##lpdecay##

*Function documentation for `lpdecay`*

## lpsustain

##lpsustain##

*Function documentation for `lpsustain`*

## lprelease

##lprelease##

*Function documentation for `lprelease`*

## lpenv

##lpenv##

*Function documentation for `lpenv`*

# Pitch Envelope

You can also control the pitch with envelopes!
Pitch envelopes can breathe life into static sounds:

```javascript
n("<-4,0 5 2 1>*<2!3 4>")
  .scale("<C F>/8:pentatonic")
  .s("gm_electric_guitar_jazz")
  .penv("<.5 0 7 -2>*2").vib("4:.1")
  .phaser(2).delay(.25).room(.3)
  .size(4).fast(1.5)
```

You also create some lovely chiptune-style sounds:

```javascript
n(run("<4 8>/16")).jux(rev)
.chord("<C^7 <Db^7 Fm7>>")
.dict('ireal')
.voicing().add(note("<0 1>/8"))
.dec(.1).room(.2)
.segment("<4 [2 8]>")
.penv("<0 <2 -2>>").patt(.02).fast(2)
```

Let's break down all pitch envelope controls:

## pattack

##pattack##

*Function documentation for `pattack`*

## pdecay

##pdecay##

*Function documentation for `pdecay`*

## prelease

##prelease##

*Function documentation for `prelease`*

## penv

##penv##

*Function documentation for `penv`*

## pcurve

##pcurve##

*Function documentation for `pcurve`*

## panchor

##panchor##

*Function documentation for `panchor`*

# Dynamics

## gain

##gain##

*Function documentation for `gain`*

## velocity

##velocity##

*Function documentation for `velocity`*

## compressor

##compressor##

*Function documentation for `compressor`*

## postgain

##postgain##

*Function documentation for `postgain`*

## xfade

##xfade##

*Function documentation for `xfade`*

# Panning

## jux

##jux##

*Function documentation for `jux`*

## juxBy

##juxBy##

*Function documentation for `juxBy`*

## pan

##pan##

*Function documentation for `pan`*

# Waveshaping

## coarse

##coarse##

*Function documentation for `coarse`*

## crush

##crush##

*Function documentation for `crush`*

## distort

##distort##

*Function documentation for `distort`*

# Global Effects

## Local vs Global Effects

While the above listed "local" effects will always create a separate effects chain for each event,
global effects use the same chain for all events of the same orbit:

## orbit

##orbit##

*Function documentation for `orbit`*

## Delay

### delay

##delay##

*Function documentation for `delay`*

### delaytime

##delaytime##

*Function documentation for `delaytime`*

### delayfeedback

##delayfeedback##

*Function documentation for `delayfeedback`*

## Reverb

### room

##room##

*Function documentation for `room`*

### roomsize

##roomsize##

*Function documentation for `roomsize`*

### roomfade

##roomfade##

*Function documentation for `roomfade`*

### roomlp

##roomlp##

*Function documentation for `roomlp`*

### roomdim

##roomdim##

*Function documentation for `roomdim`*

### iresponse

##iresponse##

*Function documentation for `iresponse`*

## Phaser

### phaser

##phaser##

*Function documentation for `phaser`*

### phaserdepth

##phaserdepth##

*Function documentation for `phaserdepth`*

### phasercenter

##phasercenter##

*Function documentation for `phasercenter`*

### phasersweep

##phasersweep##

*Function documentation for `phasersweep`*

Next, we'll look at input / output via [MIDI, OSC and other methods](/learn/input-output).