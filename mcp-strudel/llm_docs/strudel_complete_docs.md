# Strudel Complete Documentation

This is a comprehensive guide to Strudel, a web-based live coding environment for algorithmic pattern music.

## Overview

Strudel is a JavaScript implementation of Tidal Cycles, allowing you to create complex musical patterns using code.
Key concepts: patterns, functions, cycles, samples, synths, effects.

## Quick Reference

### Essential Functions
- `note` - Core Strudel function
- `freq` - Core Strudel function
- `stack` - Core Strudel function
- `seq` - Core Strudel function
- `slow` - Core Strudel function
- `fast` - Core Strudel function
- `add` - Core Strudel function
- `lpf` - Core Strudel function
- `hpf` - Core Strudel function
- `delay` - Core Strudel function
- `gain` - Core Strudel function
- `pan` - Core Strudel function
- `cut` - Core Strudel function
- `end` - Core Strudel function

## Complete Documentation

# Learning Strudel

## Accumulation

# Accumulation Modifiers

## superimpose

##Pattern.superimpose##

*Function documentation for `Pattern.superimpose`*

## layer

##Pattern.layer##

*Function documentation for `Pattern.layer`*

## off

##Pattern.off##

*Function documentation for `Pattern.off`*

## echo

##Pattern.echo##

*Function documentation for `Pattern.echo`*

## echoWith

##echoWith##

*Function documentation for `echoWith`*

## stut

##stut##

*Function documentation for `stut`*

There are also [Tonal Functions](/learn/tonal).

---

## Code

# Coding Syntax

Let's take a step back and understand how the syntax in Strudel works.

Take a look at this simple example:



- We have a word `note` which is followed by some brackets `()` with some words/letters/numbers inside, surrounded by quotes `"c a f e"`
- Then we have a dot `.` followed by another similar piece of code `s("piano")`.
- We can also see these texts are _highlighted_ using colours: word `note` is purple, the brackets `()` are grey, and the content inside the `""` are green. (The colors could be different if you've changed the default theme)

What happens if we try to 'break' this pattern in different ways?







Ok, none of these seem to work...



This one does work, but now we only hear the first note...

So what is going on here?

# Functions, arguments and chaining

So far, we've seen the following syntax:

```
xxx("foo").yyy("bar")
```

Generally, `xxx` and `yyy` are called [_functions_](<https://en.wikipedia.org/wiki/Function_(computer_programming)>), while `foo` and `bar` are called function [_arguments_ or _parameters_](<https://en.wikipedia.org/wiki/Parameter_(computer_programming)>).
So far, we've used the functions to declare which aspect of the sound we want to control, and their arguments for the actual data.
The `yyy` function is called a [_chained_ function](https://en.wikipedia.org/wiki/Method_chaining), because it is appended with a dot (`.`).

Generally, the idea with chaining is that code such as `a("this").b("that").c("other")` allows `a`, `b` and `c` functions to happen in a specified order, without needing to write them as three separate lines of code.
You can think of this as being similar to chaining audio effects together using guitar pedals or digital audio effects.

Strudel makes heavy use of chained functions. Here is a more sophisticated example:



# Comments

The `//` in the example above is a line comment, resulting in the `delay` function being ignored.
It is a handy way to quickly turn code on and off.
Try uncommenting this line by deleting `//` and refreshing the pattern.
You can also use the keyboard shortcut `cmd-/` to toggle comments on and off.

You might noticed that some comments in the REPL samples include some words starting with a "@", like `@by` or `@license`.
Those are just a convention to define some information about the music. We will talk about it in the [Music metadata](/learn/metadata) section.

# Strings

Ok, so what about the content inside the quotes (e.g. `"c a f e"`)?
In JavaScript, as in most programming languages, this content is referred to as being a [_string_](<https://en.wikipedia.org/wiki/String_(computer_science)>).
A string is simply a sequence of individual characters.
In TidalCycles, double quoted strings are used to write _patterns_ using the mini-notation, and you may hear the phrase _pattern string_ from time to time.
If you want to create a regular string and not a pattern, you can use single quotes, e.g. `'C minor'` will not be parsed as Mini Notation.

The good news is, that this covers most of the JavaScript syntax needed for Strudel!

<br />

---

## Colors

# Colors

---

## Conditional Modifiers

# Conditional Modifiers

## lastOf

##Pattern.lastOf##

*Function documentation for `Pattern.lastOf`*

## firstOf

##Pattern.firstOf##

*Function documentation for `Pattern.firstOf`*

## when

##Pattern.when##

*Function documentation for `Pattern.when`*

## chunk

##Pattern.chunk##

*Function documentation for `Pattern.chunk`*

### chunkBack

##Pattern.chunkBack##

*Function documentation for `Pattern.chunkBack`*

### fastChunk

##Pattern.fastChunk##

*Function documentation for `Pattern.fastChunk`*

## arp

##Pattern#arp##

*Function documentation for `Pattern#arp`*

## arpWith 🧪

##Pattern#arpWith##

*Function documentation for `Pattern#arpWith`*

## struct

##Pattern#struct##

*Function documentation for `Pattern#struct`*

## mask

##Pattern#mask##

*Function documentation for `Pattern#mask`*

## reset

##Pattern#reset##

*Function documentation for `Pattern#reset`*

## restart

##Pattern#restart##

*Function documentation for `Pattern#restart`*

## hush

##hush##

*Function documentation for `hush`*

## invert

##invert##

*Function documentation for `invert`*

## pick

##pick##

*Function documentation for `pick`*

## pickmod

##pickmod##

*Function documentation for `pickmod`*

## pickF

##pickF##

*Function documentation for `pickF`*

## pickmodF

##pickmodF##

*Function documentation for `pickmodF`*

## pickRestart

##pickRestart##

*Function documentation for `pickRestart`*

## pickmodRestart

##pickmodRestart##

*Function documentation for `pickmodRestart`*

## pickReset

##pickReset##

*Function documentation for `pickReset`*

## pickmodReset

##pickmodReset##

*Function documentation for `pickmodReset`*

## inhabit

##inhabit##

*Function documentation for `inhabit`*

## inhabitmod

##inhabitmod##

*Function documentation for `inhabitmod`*

## squeeze

##squeeze##

*Function documentation for `squeeze`*

After Conditional Modifiers, let's see what [Accumulation Modifiers](/learn/accumulation) have to offer.

---

## Csound

# Using CSound with Strudel

🧪 Strudel has experimental support for csound, using [@csound/browser](https://www.npmjs.com/package/@csound/browser).

## Importing .orc files

To use existing csound instruments, you can load and use an orc file from an URL like this:



Note that the above url uses the `github:` shortcut, which resolves to the raw file on github, but you can use any URL you like.

The awesome [`livecode.orc by Steven Yi`](https://github.com/kunstmusik/csound-live-code) comes packed with many sounds ready for use:

```javascript
// livecode.orc by Steven Yi
await loadOrc('github:kunstmusik/csound-live-code/master/livecode.orc')
note("c a f e").csound(cat(
"Sub1", // 	Substractive Synth, 3osc
"Sub2", // 	Subtractive Synth, two saws, fifth freq apart
"Sub3", // 	Subtractive Synth, three detuned saws, swells in
"Sub4", // 	Subtractive Synth, detuned square/saw, stabby. Nice as a lead in octave 2, nicely grungy in octave -2, -1
"Sub5", // 	Subtractive Synth, detuned square/triangle
"Sub6", // 	Subtractive Synth, saw, K35 filters
"Sub7", // 	Subtractive Synth, saw + tri, K35 filters
"Sub8", // 	Subtractive Synth, square + saw + tri, diode ladder filter
"SynBrass", // 	SynthBrass subtractive synth
"SynHarp", // 	Synth Harp subtracitve Synth
"SSaw", // 	SuperSaw sound using 9 bandlimited saws (3 sets of detuned saws at octaves)
"Mode1", // 	Modal Synthesis Instrument: Percussive/organ-y sound
"Plk", // 	Pluck sound using impulses, noise, and waveguides
"Organ1", // 	Wavetable Organ sound using additive synthesis
"Organ2", // 	Organ sound based on M1 Organ 2 patch
"Organ3", // 	Wavetable Organ using Flute 8' and Flute 4', wavetable based on Claribel Flute http://www.pykett.org.uk/the\_tonal\_structure\_of\_organ\_flutes.htm
"Bass", // 	Subtractive Bass sound
"ms20_bass", // 	MS20-style Bass Sound
"VoxHumana", // 	VoxHumana Patch
"FM1", // 	FM 3:1 C:M ratio, 2->0.025 index, nice for bass
"Noi", // 	Filtered noise, exponential envelope
"Wobble", // 	Wobble patched based on Jacob Joaquin's "Tempo-Synced Wobble Bass"
"Sine", // 	Simple Sine-wave instrument with exponential envelope
"Square", // 	Simple Square-wave instrument with exponential envelope
"Saw", // 	Simple Sawtooth-wave instrument with exponential envelope
"Squine1", // 	Squinewave Synth, 2 osc
"Form1", // 	Formant Synth, buzz source, soprano ah formants
"Mono", // 	Monophone synth using sawtooth wave and 4pole lpf. Use "start("Mono") to run the monosynth, then use MonoNote instrument to play the instrument.
"MonoNote", // 	Note playing instrument for Mono synth. Be careful to use this and not try to create multiple Mono instruments!
"Click", // 	Bandpass-filtered impulse glitchy click sound. p4 = center frequency (e.g., 3000, 6000)
"NoiSaw", // 	Highpass-filtered noise+saw sound. Use NoiSaw.cut channel to adjust cutoff.
"Clap", // 	Modified clap instrument by Istvan Varga (clap1.orc)
"BD", // 	Bass Drum - From Iain McCurdy's TR-808.csd
"SD", // 	Snare Drum - From Iain McCurdy's TR-808.csd
"OHH", // 	Open High Hat - From Iain McCurdy's TR-808.csd
"CHH", // 	Closed High Hat - From Iain McCurdy's TR-808.csd
"HiTom", // 	High Tom - From Iain McCurdy's TR-808.csd
"MidTom", // 	Mid Tom - From Iain McCurdy's TR-808.csd
"LowTom", // 	Low Tom - From Iain McCurdy's TR-808.csd
"Cymbal", // 	Cymbal - From Iain McCurdy's TR-808.csd
"Rimshot", // 	Rimshot - From Iain McCurdy's TR-808.csd
"Claves", // 	Claves - From Iain McCurdy's TR-808.csd
"Cowbell", // 	Cowbell - From Iain McCurdy's TR-808.csd
"Maraca", // 	Maraca - from Iain McCurdy's TR-808.csd
"HiConga", // 	High Conga - From Iain McCurdy's TR-808.csd
"MidConga", // 	Mid Conga - From Iain McCurdy's TR-808.csd
"LowConga", // 	Low Conga - From Iain McCurdy's TR-808.csd
))
```

## Writing your own instruments

You can define your own instrument(s) with `loadCsound` like this:

<MiniRepl
  client:only="react"
tune={`await loadCsound\`
instr CoolSynth
    iduration = p3
    ifreq = p4
    igain = p5
    ioct = octcps(ifreq)

    kpwm = oscili(.05, 8)
    asig = vco2(igain, ifreq, 4, .5 + kpwm)
    asig += vco2(igain, ifreq * 2)

    idepth = 2
    acut = transegr:a(0, .005, 0, idepth, .06, -4.2, 0.001, .01, -4.2, 0) ; filter envelope
    asig = zdf_2pole(asig, cpsoct(ioct + acut + 2), 0.5)

    iattack = .01
    isustain = .5
    idecay = .1
    irelease = .1
    asig *= linsegr:a(0, iattack, 1, idecay, isustain, iduration, isustain, irelease, 0)

    out(asig, asig)

endin\`

"<0 2 [4 6](3,4,2) 3\*2>"
.off(1/4, add(2))
.off(1/2, add(6))
.scale('D minor')
.note()
.csound('CoolSynth')`}
/>

## Parameters

The `.csound` function sends the following p values:

|     |                                  |
| --- | -------------------------------- |
| p1  | instrument name e.g. `CoolSynth` |
| p2  | time offset, when it should play |
| p3  | the duration of the event / hap  |
| p4  | frequency in Hertz               |
| p5  | normalized `gain`, 0-1           |

There is an alternative `.csoundm` function with a different flavor:

|     |                                   |
| --- | --------------------------------- |
| p4  | midi key number, unrounded, 0-127 |
| p5  | midi velocity, 0-127              |

In both cases, p4 is derived from the value of `freq` or `note`.

## Limitations / Future Plans

Apart from the above listed p values, no other parameter can be patterned so far.
This also means that [audio effects](/learn/effects/) will not work.
In the future, the integration could be improved by passing all patterned control parameters to the csound instrument.
This could work by a unique [channel](https://kunstmusik.github.io/icsc2022-csound-web/tutorial2-interacting-with-csound/#step-4---writing-continuous-data-channels)
for each value. Channels could be read [like this](https://github.com/csound/csound/blob/master/Android/CsoundForAndroid/CsoundAndroidExamples/src/main/res/raw/multitouch_xy.csd).
Also, it might make sense to have a standard library of csound instruments for strudel's effects.

Now, let's dive into the [Functional JavaScript API](/functions/intro)

---

## Devicemotion

# Device Motion



---

## Effects

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

---

## Factories

# Creating Patterns

The following functions will return a pattern.
These are the equivalents used by the Mini Notation:

| function                       | mini             |
| ------------------------------ | ---------------- |
| `cat(x, y)`                    | `"<x y>"`        |
| `seq(x, y)`                    | `"x y"`          |
| `stack(x, y)`                  | `"x,y"`          |
| `stepcat([3,x],[2,y])`         | `"x@3 y@2"`      |
| `polymeter([a, b, c], [x, y])` | `"{a b c, x y}"` |
| `polymeterSteps(2, x, y, z)`   | `"{x y z}%2"`    |
| `silence`                      | `"~"`            |

## cat

##cat##

*Function documentation for `cat`*

## seq

##seq##

*Function documentation for `seq`*

## stack

##stack##

*Function documentation for `stack`*

## stepcat

##stepcat##

*Function documentation for `stepcat`*

## arrange

##arrange##

*Function documentation for `arrange`*

## polymeter

##polymeter##

*Function documentation for `polymeter`*

## polymeterSteps

##polymeterSteps##

*Function documentation for `polymeterSteps`*

## silence

##silence##

*Function documentation for `silence`*

## run

##run##

*Function documentation for `run`*

## binary

##binary##

*Function documentation for `binary`*

## binaryN

##binaryN##

*Function documentation for `binaryN`*

After Pattern Constructors, let's see what [Time Modifiers](/learn/time-modifiers) are available.

---

## Getting Started

# Welcome

Welcome to the Strudel documentation pages!

These pages will introduce you to [Strudel](https://strudel.cc/), a web-based [live coding](https://github.com/toplap/awesome-livecoding/) environment that implements the [Tidal Cycles](https://tidalcycles.org) algorithmic pattern language.

# What is Strudel?

[Strudel](https://strudel.cc/) is a version of [Tidal Cycles](https://tidalcycles.org) written in [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), initiated by [Alex McLean](https://slab.org) and [Felix Roos](https://froos.cc/) in 2022.
Tidal Cycles, also known as Tidal, is a language for [algorithmic pattern](https://algorithmicpattern.org), and though it is most commonly used for [making music](https://tidalcycles.org/docs/showcase), it can be used for any kind of pattern making activity, including [weaving](https://www.youtube.com/watch?v=TfEmEsusXjU).

Tidal was first implemented as a library written in the [Haskell](https://www.haskell.org/) functional programming language, and by itself it does not make any sound.
To make sound, it has to be connected to a sound engine, and by default this is a [SuperCollider](https://supercollider.github.io/) plugin called [SuperDirt](https://github.com/musikinformatik/SuperDirt/).
As such, it can be difficult for first-time users to install both Tidal Cycles and SuperDirt, as there are many small details to get right.
Strudel however runs directly in your web browser, does not require any custom software installation, and can make sound all by itself.

# Strudel REPL and MiniREPL

The main place to actually make music with Strudel is the [Strudel REPL](https://strudel.cc/) ([what is a REPL?](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)), but in these pages you will also encounter interactive "MiniREPLs" where you can listen to and edit Strudel patterns.
Try clicking the play icon below:



Then edit the text so it reads `s("bd sd cp hh")` and click the refresh icon.
Congratulations, you have now live coded your first Strudel pattern!

With Strudel, you can expressively write dynamic music pieces.
You don't need to know JavaScript or Tidal Cycles to make music with Strudel.
This interactive tutorial will guide you through the basics of Strudel.

# Show me some demos!

To see and hear what Strudel can do, visit the [Strudel REPL](https://strudel.cc/) and click the Shuffle icon in the top menu bar.
You can get a feel for Strudel by browsing and editing these examples and clicking the Refresh icon to update.

You can also browse through the examples [here](/examples).

Alternatively, you can get a taste of what Strudel can do by clicking play on this track:

```javascript
samples({
  bd: ['bd/BT0AADA.wav','bd/BT0AAD0.wav','bd/BT0A0DA.wav','bd/BT0A0D3.wav','bd/BT0A0D0.wav','bd/BT0A0A7.wav'],
  sd: ['sd/rytm-01-classic.wav','sd/rytm-00-hard.wav'],
  hh: ['hh27/000_hh27closedhh.wav','hh/000_hh3closedhh.wav'],
}, 'github:tidalcycles/dirt-samples');
stack(
s("bd,[~ <sd!3 sd(3,4,2)>],hh*8") // drums
.speed(perlin.range(.7,.9)) // random sample speed variation
,"<a1 b1\*2 a1(3,8) e2>" // bassline
.off(1/8,x=>x.add(12).degradeBy(.5)) // random octave jumps
.add(perlin.range(0,.5)) // random pitch variation
.superimpose(add(.05)) // add second, slightly detuned voice
.note() // wrap in "note"
.decay(.15).sustain(0) // make each note of equal length
.s('sawtooth') // waveform
.gain(.4) // turn down
.cutoff(sine.slow(7).range(300,5000)) // automate cutoff
,"<Am7!3 <Em7 E7b13 Em7 Ebm7b5>>".voicings('lefthand') // chords
.superimpose(x=>x.add(.04)) // add second, slightly detuned voice
.add(perlin.range(0,.5)) // random pitch variation
.note() // wrap in "note"
.s('sawtooth') // waveform
.gain(.16) // turn down
.cutoff(500) // fixed cutoff
.attack(1) // slowly fade in
)
.slow(3/2)
```

# Strudel is a work in progress 🚧

Please note that this project is still in its experimental state.
In the future, parts of it might change significantly.
This tutorial is also far from complete.
You can contribute to it clicking 'Edit this page' in the top right, or by visiting the [Strudel GitHub page](https://codeberg.org/uzu/strudel/).

# What's next?

Head on over to the [Notes](/learn/notes) page.

<br />

---

## Hydra

# Using Hydra inside Strudel

You can write [hydra](https://hydra.ojack.xyz/) code in strudel! All you have to do is to call `await initHydra()` at the top:

```javascript
await initHydra()
// licensed with CC BY-NC-SA 4.0 https://creativecommons.org/licenses/by-nc-sa/4.0/
// by Zach Krall
// http://zachkrall.online/

osc(10, 0.9, 300)
.color(0.9, 0.7, 0.8)
.diff(
osc(45, 0.3, 100)
.color(0.9, 0.9, 0.9)
.rotate(0.18)
.pixelate(12)
.kaleid()
)
.scrollX(10)
.colorama()
.luma()
.repeatX(4)
.repeatY(4)
.modulate(
osc(1, -0.9, 300)
)
.scale(2)
.out()

note("[a,c,e,<a4 ab4 g4 gb4>,b4]/2")
.s("sawtooth").vib(2)
.lpf(600).lpa(2).lpenv(6)

```

## H patterns

There is a special function `H` that allows you to use a pattern as an input to hydra:



## detectAudio

To use hydra audio capture, call `initHydra` with `{detectAudio:true}` configuration param:

```javascript
await initHydra({detectAudio:true})
let pattern = "<3 4 5 [6 7]*2>"
shape(H(pattern)).repeat()
  .scrollY(
    ()=> a.fft[0]*.25
  )
  .add(src(o0).color(.71 ).scrollX(.005),.95)
.out(o0)
n(pattern).scale("A:minor").piano().room(1)

```

You might now be able to see this properly here: [open in REPL](/#YXdhaXQgaW5pdEh5ZHJhKCkKbGV0IHBhdHRlcm4gPSAiMyA0IDUgWzYgN10qMiIKc2hhcGUoSChwYXR0ZXJuKSkub3V0KG8wKQpuKHBhdHRlcm4pLnNjYWxlKCJBOm1pbm9yIikucGlhbm8oKS5yb29tKDEpIA%3D%3D)

Similar to `detectAudio`, all the [available hydra options](https://github.com/hydra-synth/hydra-synth#api) can be passed to `initHydra`.

## feedStrudel

Using the `feedStrudel` option, you can transform strudel visualizations with hydra:

```javascript
await initHydra({feedStrudel:1})
//
src(s0).kaleid(H("<4 5 6>"))
  .diff(osc(1,0.5,5))
  .modulateScale(osc(2,-0.25,1))
  .out()
//

$: s("bd*4,[hh:0:<.5 1>]*8,~ rim").bank("RolandTR909").speed(.9)

$: note("[<g1!3 <bb1 <f1 d1>>>]\*3").s("sawtooth")

.room(.75).sometimes(add(note(12))).clip(.3)
.lpa(.05).lpenv(-4).lpf(2000).lpq(8).ftype('24db')

all(x=>x.fft(4).scope({pos:0,smear:.95}))
```

---

## Input Devices

# Input Devices

Strudel supports various input devices like Gamepads and MIDI controllers to manipulate patterns in real-time.

---

## Input Output

# MIDI, OSC and MQTT

Normally, Strudel is used to pattern sound, using its own '[web audio](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)'-based synthesiser called [SuperDough](https://codeberg.org/uzu/strudel/src/branch/main/packages/superdough).

It is also possible to pattern other things with Strudel, such as software and hardware synthesisers with MIDI, other software using Open Sound Control/OSC (including the [SuperDirt](https://github.com/musikinformatik/SuperDirt/) synthesiser commonly used with Strudel's sibling [TidalCycles](https://tidalcycles.org/)), or the MQTT 'internet of things' protocol.

# MIDI

Strudel supports MIDI without any additional software (thanks to [webmidi](https://npmjs.com/package/webmidi)), just by adding methods to your pattern:

## midiin(inputName?)

##midin##

*Function documentation for `midin`*

## midi(outputName?,options?)

Either connect a midi device or use the IAC Driver (Mac) or Midi Through Port (Linux) for internal midi messages.
If no outputName is given, it uses the first midi output it finds.

```javascript

$: chord("<C^7 A7 Dm7 G7>").voicing().midi('IAC Driver')

```

In the console, you will see a log of the available MIDI devices as soon as you run the code,
e.g.

```
 `Midi connected! Using "Midi Through Port-0".`
```

The `.midi()` function accepts an options object with the following properties:



<details>
<summary>Available Options</summary>

| Option       | Type          | Default   | Description                                                            |
| ------------ | ------------- | --------- | ---------------------------------------------------------------------- |
| isController | boolean       | false     | When true, disables sending note messages. Useful for MIDI controllers |
| latencyMs    | number        | 34        | Latency in milliseconds to align MIDI with audio engine                |
| noteOffsetMs | number        | 10        | Offset in milliseconds for note-off messages to prevent glitching      |
| midichannel  | number        | 1         | Default MIDI channel (1-16)                                            |
| velocity     | number        | 0.9       | Default note velocity (0-1)                                            |
| gain         | number        | 1         | Default gain multiplier for velocity (0-1)                             |
| midimap      | string        | 'default' | Name of MIDI mapping to use for control changes                        |
| midiport     | string/number | -         | MIDI device name or index                                              |

</details>

### midiport(outputName)

Selects the MIDI output device to use, pattern can be used to switch between devices.

```javascript
$: midiport('IAC Driver');
$: note('c a f e').midiport('<0 1 2 3>').midi();
```

##midiport##

*Function documentation for `midiport`*

## midichan(number)

Selects the MIDI channel to use. If not used, `.midi` will use channel 1 by default.

## midicmd(command)

`midicmd` sends MIDI system real-time messages to control timing and transport on MIDI devices.

It supports the following commands:

- `clock`/`midiClock` - Sends MIDI timing clock messages
- `start` - Sends MIDI start message
- `stop` - Sends MIDI stop message
- `continue` - Sends MIDI continue message

// You can control the clock with a pattern and ensure it starts in sync when the repl begins.
// Note: It might act unexpectedly if MIDI isn't set up initially.

```javascript
$:stack(
  midicmd("clock*48,<start stop>/2").midi('IAC Driver')
)
```

## control, ccn && ccv

- `control` sends MIDI control change messages to your MIDI device.
- `ccn` sets the cc number. Depends on your synths midi mapping
- `ccv` sets the cc value. normalized from 0 to 1.





In the above snippet, `ccn` is set to 74, which is the filter cutoff for many synths. `ccv` is controlled by a saw pattern.
Having everything in one pattern, the `ccv` pattern will be aligned to the note pattern, because the structure comes from the left by default.
But you can also control cc messages separately like this:



Instead of setting `ccn` and `ccv` directly, you can also create mappings with `midimaps`:

## midimaps

##midimaps##

*Function documentation for `midimaps`*

## defaultmidimap

##defaultmidimap##

*Function documentation for `defaultmidimap`*

## progNum (Program Change)

`progNum` sends MIDI program change messages to switch between different presets/patches on your MIDI device.
Program change values should be numbers between 0 and 127.

```javascript
// Switch between programs 0 and 1 every cycle
progNum("<0 1>").midi()

// Play notes while changing programs
note("c3 e3 g3").progNum("<0 1 2>").midi()
```

Program change messages are useful for switching between different instrument sounds or presets during a performance.
The exact sound that each program number maps to depends on your MIDI device's configuration.

## sysex, sysexid && sysexdata (System Exclusive Message)

`sysex` sends MIDI System Exclusive (SysEx) messages to your MIDI device.
ysEx messages are device-specific commands that allow deeper control over synthesizer parameters.
The value should be an array of numbers between 0-255 representing the SysEx data bytes.



The exact format of SysEx messages depends on your MIDI device's specification.
Consult your device's MIDI implementation guide for details on supported SysEx messages.

## midibend && miditouch

`midibend` sets MIDI pitch bend (-1 - 1)
`miditouch` sets MIDI key after touch (0-1)





# OSC/SuperDirt/StrudelDirt

In TidalCycles, sound is usually generated using [SuperDirt](https://github.com/musikinformatik/SuperDirt/), which runs inside SuperCollider. Strudel also supports using SuperDirt, although it requires installing some additional software.

There is also [StrudelDirt](https://github.com/daslyfe/StrudelDirt) which is SuperDirt with some optimisations for working with Strudel. (A longer term aim is to merge these optimisations back into mainline SuperDirt)

## Prequisites

To get SuperDirt to work with Strudel, you need to

1. install SuperCollider + sc3 plugins, see [Tidal Docs](https://tidalcycles.org/docs/) (Install Tidal) for more info.
2. install SuperDirt, or the [StrudelDirt](https://github.com/daslyfe/StrudelDirt) fork which is optimised for use with Strudel
3. install [node.js](https://nodejs.org/en/)
4. download [Strudel Repo](https://codeberg.org/uzu/strudel/) (or git clone, if you have git installed)
5. run `pnpm i` in the strudel directory
6. run `pnpm run osc` to start the osc server, which forwards OSC messages from Strudel REPL to SuperCollider

Now you're all set!

## Usage

1. Start SuperCollider, either using SuperCollider IDE or by running `sclang` in a terminal
2. Open the [Strudel REPL](https://strudel.cc/#cygiYmQgc2QiKS5vc2MoKQ%3D%3D)

...or test it here:



If you now hear sound, congratulations! If not, you can get help on the [#strudel channel in the TidalCycles discord](https://discord.com/invite/HGEdXmRkzT).

Note: if you have the 'Audio Engine Target' in settings set to 'OSC', you do not need to add .osc() to the end of your pattern.

### Pattern.osc

##Pattern.osc##

*Function documentation for `Pattern.osc`*

## SuperDirt Params

Please refer to [Tidal Docs](https://tidalcycles.org/) for more info.

<br />

But can we use Strudel [offline](/learn/pwa)?

# MQTT

MQTT is a lightweight network protocol, designed for 'internet of things' devices. For use with strudel, you will
need access to an MQTT server known as a 'broker' configured to accept secure 'websocket' connections. You could
run one yourself (e.g. by running [mosquitto](https://mosquitto.org/)), although getting an SSL certificate that
your web browser will trust might be a bit tricky for those without systems administration experience.
Alternatively, you can use [a public broker](https://www.hivemq.com/mqtt/public-mqtt-broker/).

Strudel does not yet support receiving messages over MQTT, only sending them.

## Usage

The following example shows how to send a pattern to an MQTT broker:



Other software can then receive the messages. For example using the [mosquitto](https://mosquitto.org/) commandline client tools:

```

> mosquitto_sub -h mqtt.eclipseprojects.io -p 1883 -t "/strudel-pattern"
> hello
> world
> hello
> world
> ...

```

Control patterns will be encoded as JSON, for example:



Will send messages like the following:

```

{"s":"sax","speed":2}
{"s":"sax","speed":2}
{"s":"sax","speed":3}
{"s":"sax","speed":2}
...

```

Libraries for receiving MQTT are available for many programming languages.

```

```

---

## Metadata

# Music metadata

You can optionally add some music metadata in your Strudel code, by using tags in code comments:

```js
// @title Hey Hoo
// @by Sam Tagada
// @license CC BY-NC-SA
```

Like other comments, those are ignored by Strudel, but it can be used by other tools to retrieve some information about the music.

## Alternative syntax

You can also use comment blocks:

```js
/*
@title Hey Hoo
@by Sam Tagada
@license CC BY-NC-SA
*/
```

Or define multiple tags in one line:

```js
// @title Hey Hoo @by Sam Tagada @license CC BY-NC-SA
```

The `title` tag has an alternative syntax using quotes (must be defined at the very begining):

```js
// "Hey Hoo" @by Sam Tagada
```

## Tags list

Available tags are:

- `@title`: music title
- `@by`: music author(s), separated by comma, eventually followed with a link in `<>` (ex: `@by John Doe <https://example.com>`)
- `@license`: music license(s), e.g. CC BY-NC-SA. Unsure? [Choose a creative commons license here](https://creativecommons.org/choose/)
- `@details`: some additional information about the music
- `@url`: web page(s) related to the music (git repo, soundcloud link, etc.)
- `@genre`: music genre(s) (pop, jazz, etc)
- `@album`: music album name

## Multiple values

Some of them accepts several values, using the comma or new line separator, or duplicating the tag:

```js
/*
@by Sam Tagada
    Jimmy
@genre pop, jazz
@url https://example.com
@url https://example.org
*/
```

You can also add optional prefixes and use tags where you want:

```js
/*
song @by Sam Tagada
samples @by Jimmy
*/
...
note("a3 c#4 e4 a4") // @by Sandy
```

## Multiline

If a tag doesn't accept a list, it can take multi-line values:

```js
/*
@details I wrote this song in February 19th, 2023.
         It was around midnight and I was lying on
         the sofa in the living room.
*/
```

---

## Mini Notation

# Mini-notation

Just like [Tidal Cycles](https://tidalcycles.org/), Strudel uses a so called "Mini-Notation", which is a custom language that is designed for writing rhythmic patterns using little amounts of text.

## Note

This page just explains the entirety of the Mini-Notation syntax.
If you are just getting started with Strudel, you can learn the basics of the Mini-Notation in a more practical manner in the [workshop](/workshop/first-sounds).
After that, you can come back here if you want to understand every little detail.

## Example

Before diving deeper into the details, here is a flavour of how the Mini-Notation looks like:

<MiniRepl
  client:idle
  tune={`note(\`<
[e5 [b4 c5] d5 [c5 b4]]
[a4 [a4 c5] e5 [d5 c5]]
[b4 [~ c5] d5 e5]
[c5 a4 a4 ~]
[[~ d5] [~ f5] a5 [g5 f5]]
[e5 [~ c5] e5 [d5 c5]]
[b4 [b4 c5] d5 e5]
[c5 a4 a4 ~]
,
[[e2 e3]*4]
[[a2 a3]*4]
[[g#2 g#3]*2 [e2 e3]*2]
[a2 a3 a2 a3 a2 a3 b1 c2]
[[d2 d3]*4]
[[c2 c3]*4]
[[b1 b2]*2 [e2 e3]*2]
[[a1 a2]*4]
>\`)`}
/>

## Mini Notation Format

The snippet above is enclosed in backticks (`), which allows you to write multi-line strings.

You can also use regular double quotes (`"`) for single line mini-notation, as we have done already.

If you do just want to get a regular string that is _not_ parsed as mini-notation, use single quotes (`'`).

## Sequences of events in a cycle

We can play more notes by separating them with spaces:



Here, those four notes are squashed into one cycle, so each note is a quarter second long.
Try adding or removing notes and notice how the tempo changes!



Note that the overall duration of time does not change, and instead each note length decreases.
This is a key idea, as it illustrates the 'Cycle' in TidalCycles!

Each space-separated note in this sequence is an _event_.
The time duration of each event is based on the speed or tempo of the cycle, and how many events are present.
Taking the two examples above, we have four and eight events respectively, and since they have the same cycle duration, they each have to fit their events inside the same amount of time.

This is perhaps counter-intuitive if you are used to adding notes in a sequencer or piano roll and the overall length increasing.
But, it will begin to make sense as we go through more elements of mini-notation.

## Multiplication

A sequence can be sped up by multiplying it by a number using the asterisk symbol (`*`):



The multiplication by two here means that the sequence will play twice per cycle.

Multiplications can also be decimal (`*2.75`):



## Division

Contrary to multiplication, division can slow the sequence down by enclosing it in brackets and dividing it by a number (`/2`):



The division by two means that the sequence will be played over the course of two cycles.
You can also use decimal numbers for any tempo you like (`/2.75`).



## Angle Brackets

Using angle brackets `<>`, we can define the sequence length based on the number of events:

```javascript
note("<e5 b4 d5 c5>")
```
*This example includes visual pattern representation*

The above snippet is the same as:



The advantage of the angle brackets, is that we can add more events without needing to change the number at the end.

```javascript
note("<e5 b4 d5 c5 e5>")
```
*This example includes visual pattern representation*

```javascript
note("<e5 b4 d5 c5 e5 b4>")
```
*This example includes visual pattern representation*

This is more similar to traditional music sequencers and piano rolls, where adding a note increases the perceived overall duration.
We can also play a certain number of notes per cycle by using angle brackets with multiplication:

```javascript
note("<e5 b4 d5 c5 a4 c5>*8")
```
*This example includes visual pattern representation*

Now we are playing 8 notes per cycle!

## Subdividing time with bracket nesting

To create more interesting rhythms, you can _nest_ or _enclose_ sequences (put sequences inside sequences) with brackets `[]`, like this:

Compare the difference between the following:







What's going on here? When we nest/enclose multiple events inside brackets (`[]`), their duration becomes the length of one event in the outer sequence.

This is a very simple change to make, but it has profound consequences.
Remember what we said earlier about how the cycles in tidal stay the same length, and the individual event lengths are divided up in this cycle?
Well, what this means is that in TidalCycles, not only can you divide time any way you want, and you can also subdivide time any way you want!

## Rests

The "~" represents a rest, and will create silence between other events:



## Parallel / polyphony

Using commas, we can play chords.
The following are the same:




But to play multiple chords in a sequence, we have to wrap them in brackets:

```javascript
note("<[g3,b3,e4] [a3,c3,e4] [b3,d3,f#4] [b3,e4,g4]>*2")
```
*This example includes visual pattern representation*

## Elongation

With the "@" symbol, we can specify temporal "weight" of a sequence child:

```javascript
note("<[g3,b3,e4]@2 [a3,c3,e4] [b3,d3,f#4]>*2")
```
*This example includes visual pattern representation*

Here, the first chord has a weight of 2, making it twice the length of the other chords. The default weight is 1.

## Replication

Using "!" we can repeat without speeding up:

```javascript
note("<[g3,b3,e4]!2 [a3,c3,e4] [b3,d3,f#4]>*2")
```
*This example includes visual pattern representation*

## Mini-notation review

To recap what we've learned so far, compare the following patterns:

```javascript
note("<g3 b3 e4 [a3,c3,e4] [b3,d3,f#4]>*2")
```
```javascript
note("<[g3,b3,e4] [a3,c3,e4] [b3,d3,f#4]>*2")
```
```javascript
note("<[g3,b3,e4]/2 [a3,c3,e4] [b3,d3,f#4]>*2")
```
```javascript
note("<[g3,b3,e4]*2 [a3,c3,e4] [b3,d3,f#4]>*2")
```
```javascript
note("<[g3,b3,e4] _ [a3,c3,e4] [b3,d3,f#4]>*2")
```
```javascript
note("<[g3,b3,e4]@2 [a3,c3,e4] [b3,d3,f#4]>*2")
```
```javascript
note("<[g3,b3,e4]!2 [a3,c3,e4] [b3,d3,f#4]>*2")
```

## Euclidian rhythms

Using round brackets after an event, we can create rhythmical sub-divisions based on three parameters: `beats`, `segments` and `offset`.
This algorithm can be found in many different types of music software, and is often referred to as a [Euclidean rhythm](https://en.wikipedia.org/wiki/Euclidean_rhythm) sequencer, after computer scientist Godfriend Toussaint.
Why is it interesting? Well, consider the following simple example:



Sound familiar?
This is a popular Euclidian rhythm going by various names, such as "Pop Clave".
These rhythms can be found in all musical cultures, and the Euclidian rhythm algorithm allows us to express them extremely easily.
Writing this rhythm out in full require describing:



But using the Euclidian rhythm notation, we only need to express "3 beats over 8 segments, starting on position 1".

This makes it easy to write patterns with interesting rhythmic structures and variations that still sound familiar:



Note that since the example above does not use the third `offset` parameter, it can be written simply as `"(3,8)"`.



Let's look at those three parameters in detail.

### Beats

`beats`: the first parameter controls how may beats will be played.
Compare these:





### Segments

`segments`: the second parameter controls the total amount of segments the beats will be distributed over:





### Offsets

`offset`: the third (optional) parameter controls the starting position for distributing the beats.
We need a secondary rhythm to hear the difference:





## Mini-notation exercise

The most fun thing about the mini-notation, is that everything you have just learned can be combined in various ways!

Starting with this one `n`, can you make a _pattern string_ that uses every single mini-notation element above?



<br />

Next: How do [Samples](/learn/samples) play into this?

---

## Notes

# Notes

Pitches are an important building block in many musical traditions.
In Strudel, pitches can be expressed as note names, note numbers or frequencies.
Here's the same pattern written in three different ways:

- `note`: letter notation, good for those who are familiar with western music theory:

  

- `note`: number notation, good for those who want to use recognisable pitches, but don't care about music theory:

  

- `freq`: frequency notation, good for those who want to go beyond standardised tuning systems:

  

Let's look at those in more detail...

## `note` names

Notes names can be notated with the note letter, followed by the octave number. You can notate flats with `b` and sharps with `#`.



By the way, you can edit the contents of the player, and press "update" to hear your change!
You can also press "play" on the next player without needing to stop the last one.

## `note` numbers

If you prefer, you can also use numbers with `note` instead:



These numbers are interpreted as so called [MIDI numbers](https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies), where adjacent whole numbers are one 'semitone' apart.

You could also write decimal numbers to get 'microtonal' pitches (in between the black and white piano notes):



## `freq`

To get maximum freedom, you can also use `freq` to directly control the frequency:



## Hearing and frequency

In the above example, we play A3 (220Hz), C#4 natural (275Hz), E4 (330Hz) and A4 (440Hz), mirroring our previous examples.

But can you hear the difference between these individual frequencies?



How about these?



The higher we go up...



The less distance we can hear between the frequencies!



Why is this? [Human hearing operates logarithmically](https://www.audiocheck.net/soundtests_nonlinear.php).

## From notes to sounds

In this page, when we played a pattern of notes like this:



We heard a simple synthesised sound, in fact we heard a [triangle wave oscillator](https://en.wikipedia.org/wiki/Triangle_wave).

This is the default synthesiser used by Strudel, but how do we then make different sounds in Strudel?

Let's find out in the next page on [Sounds](/learn/sounds).

<br />

---

## Pwa

# Using Strudel Offline

You can use Strudel even without a network! When you first visit the [Strudel REPL](https://strudel.cc/),
your browser will download the whole web app including documentation.
When the download is finished (&lt;1MB), you can visit the website even when offline,
getting the downloaded website instead of the online one.

When the site gets updated, your browser will download that update on the next online visit.
When an update is available, the site will refresh after the download is finished.

This works because Strudel is implemented as progessive web app (using [Vite PWA](https://vite-pwa-org.netlify.app/)).

## Samples

While the browser will download the app itself, samples are only downloaded when you're actively using them.
So to make sure a specific set of samples is available when offline, just use them.
Also, only samples from these domains will be cached for offline use:

- `https://raw.githubusercontent.com/*` for samples uploaded to github
- `https://freesound.org/*` / `https://cdn.freesound.org/*` for freesound
- `https://shabda.ndre.gr/.*` for shabda

## Inspecting / Clearing Cache

You can view all cached files in your browser.

### Firefox

- Open the Developer Tools (`Tools > Web Developer > Web Developer Tools`)
- go to `Storage` tab and expand `Cache Storage > https://strudel.cc`.
- or go to the `Application` tab and view the latest updates in `Service Workers`

### Chromium based Browsers

- Open Developer Tools (`Right Click > Inspect`)
- go to the `Application` tab
- view downloaded files under `Cache > Cache Storage`
- view the latest updates in `Service Workers`

## Strudel Standalone App

You can also install Strudel as a standalone app on most devices.
A standalone app has its own desktop / homescreen icon and launches in a separate window,
without the browser ui.

<figure>
  ![Strudel on MacOS](/pwa/strudel-macos.png)
  <figcaption>Strudel on MacOS</figcaption>
</figure>

### Desktop

With a chromium based browser:

1. go to the [Strudel REPL](https://strudel.cc).
2. on the right of the adress bar, click `install Strudel REPL`
3. the REPL should now run as a standalone chromium app

Without a chromium based browser, you can use [nativefier](https://github.com/nativefier/nativefier) to generate a desktop app:

1. make sure you have NodeJS installed
2. run `npx nativefier strudel.cc`

<figure>
  ![Strudel on Linux](/pwa/strudel-linux.png)
  <figcaption>Strudel on Linux</figcaption>
</figure>

### iOS

1. open to the [Strudel REPL](https://strudel.cc/) in safari
2. press the share icon and tab `Add to homescreen`
3. You should now have a strudel app icon that opens the repl in full screen

### Android

1. open to the [Strudel REPL](https://strudel.cc/)
2. Tab the install button at the bottom

Ok, what are [Patterns](/technical-manual/patterns) all about?

---

## Random Modifiers

# Random Modifiers

These methods add random behavior to your Patterns.

## choose

##choose##

*Function documentation for `choose`*

## wchoose

##wchoose##

*Function documentation for `wchoose`*

## chooseCycles

##chooseCycles##

*Function documentation for `chooseCycles`*

## wchooseCycles

##wchooseCycles##

*Function documentation for `wchooseCycles`*

## degradeBy

##Pattern.degradeBy##

*Function documentation for `Pattern.degradeBy`*

## degrade

##Pattern.degrade##

*Function documentation for `Pattern.degrade`*

## undegradeBy

##Pattern.undegradeBy##

*Function documentation for `Pattern.undegradeBy`*

## undegrade

##Pattern.undegrade##

*Function documentation for `Pattern.undegrade`*

## sometimesBy

##Pattern.sometimesBy##

*Function documentation for `Pattern.sometimesBy`*

## sometimes

##Pattern.sometimes##

*Function documentation for `Pattern.sometimes`*

## someCyclesBy

##Pattern.someCyclesBy##

*Function documentation for `Pattern.someCyclesBy`*

## someCycles

##Pattern.someCycles##

*Function documentation for `Pattern.someCycles`*

## often

##Pattern.often##

*Function documentation for `Pattern.often`*

## rarely

##Pattern.rarely##

*Function documentation for `Pattern.rarely`*

## almostNever

##Pattern.almostNever##

*Function documentation for `Pattern.almostNever`*

## almostAlways

##Pattern.almostAlways##

*Function documentation for `Pattern.almostAlways`*

## never

##Pattern.never##

*Function documentation for `Pattern.never`*

## always

##Pattern.always##

*Function documentation for `Pattern.always`*

Next up: [Conditional Modifiers](/learn/conditional-modifiers)

---

## Samples

# Samples

Samples are the most common way to make sound with tidal and strudel.
A sample is a (commonly short) piece of audio that is used as a basis for sound generation, undergoing various transformations.
Music that is based on samples can be thought of as a collage of sound. [Read more about Sampling](<https://en.wikipedia.org/wiki/Sampling_(music)>)

Strudel allows loading samples in the form of audio files of various formats (wav, mp3, ogg) from any publicly available URL.

# Default Samples

By default, strudel comes with a built-in "sample map", providing a solid base to play with.



Here, we are using the `s` function to play back different default samples (`bd`, `sd`, `hh` and `misc`) to get a drum beat.

For drum sounds, strudel uses the comprehensive [tidal-drum-machines](https://github.com/ritchse/tidal-drum-machines) library, with the following naming convention:

| Drum                 | Abbreviation |
| -------------------- | ------------ |
| Bass drum, Kick drum | bd           |
| Snare drum           | sd           |
| Rimshot              | rim          |
| Clap                 | cp           |
| Closed hi-hat        | hh           |
| Open hi-hat          | oh           |
| Crash                | cr           |
| Ride                 | rd           |
| High tom             | ht           |
| Medium tom           | mt           |
| Low tom              | lt           |

<img src="/img/drumset.png" />

<a class="text-right text-xs" href="https://de.wikipedia.org/wiki/Schlagzeug#/media/Datei:Drum_set.svg" target="_blank">
  original von Pbroks13
</a>

More percussive sounds:

| Source                              | Abbreviation |
| ----------------------------------- | ------------ |
| Shakers (and maracas, cabasas, etc) | sh           |
| Cowbell                             | cb           |
| Tambourine                          | tb           |
| Other percussions                   | perc         |
| Miscellaneous samples               | misc         |
| Effects                             | fx           |

Furthermore, strudel also loads instrument samples from [VCSL](https://github.com/sgossner/VCSL) by default.

To see which sample names are available, open the `sounds` tab in the [REPL](https://strudel.cc/).

Note that only the sample maps (mapping names to URLs) are loaded initially, while the audio samples themselves are not loaded until they are actually played.
This behaviour of loading things only when they are needed is also called `lazy loading`.
While it saves resources, it can also lead to sounds not being audible the first time they are triggered, because the sound is still loading.
[This might be fixed in the future](https://codeberg.org/uzu/strudel/issues/187)

# Sound Banks

If we open the `sounds` tab and then `drum-machines`, we can see that the drum samples are all prefixed with drum machine names: `RolandTR808_bd`, `RolandTR808_sd`, `RolandTR808_hh` etc..

We _could_ use them like this:



... but thats obviously a bit much to write. Using the `bank` function, we can shorten this to:



You could even pattern the bank to switch between different drum machines:

```javascript
s("bd sd,hh*16").bank("<RolandTR808 RolandTR909>")
```

Behind the scenes, `bank` will just prepend the drum machine name to the sample name with `_` to get the full name.
This of course only works because the name after `_` (`bd`, `sd` etc..) is standardized.
Also note that some banks won't have samples for all sounds!

# Selecting Sounds

If we open the `sounds` tab again, followed by tab `drum machines`, there is also a number behind each name, indicating how many individual samples are available.
For example `RolandTR909_hh(4)` means there are 4 samples of a TR909 hihat available.
By default, `s` will play the first sample, but we can select the other ones using `n`, starting from 0:



Numbers that are too high will just wrap around to the beginning



Here, 0-3 will play the same sounds as 4-7, because `RolandTR909_hh` only has 4 sounds.

Selecting sounds also works inside the mini notation, using "`:`" like this:



# Loading Custom Samples

You can load a non-standard sample map using the `samples` function.

## Loading samples from file URLs

In this example we assign names `bassdrum`, `hihat` and `snaredrum` to specific audio files on a server:



You can freely choose any combination of letters for each sample name. It is even possible to override the default sounds.
The names you pick will be made available in the `s` function.
Make sure that the URL and each sample path form a correct URL!

In the above example, `bassdrum` will load:

```
https://raw.githubusercontent.com/tidalcycles/Dirt-Samples/master/bd/BT0AADA.wav
|----------------------base path --------------------------------|--sample path-|
```

Note that we can either load a single file, like for `bassdrum` and `hihat`, or a list of files like for `snaredrum`!
As soon as you run the code, your chosen sample names will be listed in `sounds` -> `user`.

## Loading Samples from a strudel.json file

The above way to load samples might be tedious to write out / copy paste each time you write a new pattern.
To avoid that, you can simply pass a URL to a `strudel.json` file somewhere on the internet:



The file is expected to define a sample map using JSON, in the same format as described above.
Additionally, the base path can be defined with the `_base` key.
The last section could be written as:

```json
{
  "_base": "https://raw.githubusercontent.com/tidalcycles/Dirt-Samples/master/",
  "bassdrum": "bd/BT0AADA.wav",
  "snaredrum": "sd/rytm-01-classic.wav",
  "hihat": "hh27/000_hh27closedhh.wav"
}
```

## Github Shortcut

Because loading samples from github is common, there is a shortcut:



The format is `samples('github:<user>/<repo>/<branch>')`. If you omit `branch` (like above), the `main` branch will be used.
It assumes a `strudel.json` file to be present at the root of the repository:

```
https://raw.githubusercontent.com/<user>/<repo>/<branch>/strudel.json
```

## From Disk via "Import Sounds Folder"

If you don't want to upload your samples to the internet, you can also load them from your local disk.
Go to the `sounds` tab in the REPL and open the `import-sounds` tab below the search bar.
Press the "import sounds folder" button and select a folder that contains audio files.
The folder you select can also contain subfolders with audio files.
Example:

```
└─ samples
   ├─ swoop
   │  ├─ swoopshort.wav
   │  ├─ swooplong.wav
   │  └─ swooptight.wav
   └─ smash
      ├─ smashhigh.wav
      ├─ smashlow.wav
      └─ smashmiddle.wav
```

In the above example the folder `samples` contains 2 subfolders `swoop` and `smash`, which contain audio files.
If you select that `samples` folder, the `user` tab (next to the `import-sounds` tab) will then contain 2 new sounds: `swoop(3) smash(3)`
The individual samples can the be played normally like `s("swoop:0 swoop:1 smash:2")`.
The samples within each sound use zero-based indexing in alphabetical order.

## From Disk via @strudel/sampler

Instead of loading your samples into your browser with the "import sounds folder" button, you can also serve the samples from a local file server.
The easiest way to do this is using [@strudel/sampler](https://www.npmjs.com/package/@strudel/sampler):

```sh
cd samples
npx @strudel/sampler
```

Then you can load it via:

```javascript
samples('http://localhost:5432/');
 
n("<0 1 2>").s("swoop smash")
```

The handy thing about `@strudel/sampler` is that it auto-generates the `strudel.json` file based on your folder structure.
You can see what it generated by going to `http://localhost:5432` with your browser.

Note: You need [NodeJS](https://nodejs.org/) installed on your system for this to work.

## Specifying Pitch

To make sure your samples are in tune when playing them with `note`, you can specify a base pitch like this:

```javascript
samples({
  'gtr': 'gtr/0001_cleanC.wav',
  'moog': { 'g3': 'moog/005_Mighty%20Moog%20G3.wav' },
}, 'github:tidalcycles/dirt-samples');
note("g3 [bb3 c4] <g4 f4 eb4 f3>@2").s("gtr,moog").clip(1)
  .gain(.5)
```

We can also declare different samples for different regions of the keyboard:

```javascript
setcpm(60)
samples({
  'moog': {
    'g2': 'moog/004_Mighty%20Moog%20G2.wav',
    'g3': 'moog/005_Mighty%20Moog%20G3.wav',
    'g4': 'moog/006_Mighty%20Moog%20G4.wav',
  }}, 'github:tidalcycles/dirt-samples')

note("g2!2 <bb2 c3>!2, <c4@3 [<eb4 bb3> g4 f4]>")
.s('moog').clip(1)
.gain(.5)
```

The sampler will always pick the closest matching sample for the current note!

Note that this notation for pitched sounds also works inside a `strudel.json` file.

## Shabda

If you don't want to select samples by hand, there is also the wonderful tool called [shabda](https://shabda.ndre.gr/).
With it, you can enter any sample name(s) to query from [freesound.org](https://freesound.org/). Example:



You can also generate artificial voice samples with any text, in multiple languages.
Note that the language code and the gender parameters are optional and default to `en-GB` and `f`



# Sampler Effects

Sampler effects are functions that can be used to change the behaviour of sample playback.

### begin

##Pattern.begin##

*Function documentation for `Pattern.begin`*

### end

##Pattern.end##

*Function documentation for `Pattern.end`*

### loop

##loop##

*Function documentation for `loop`*

### loopBegin

##loopBegin##

*Function documentation for `loopBegin`*

### loopEnd

##loopEnd##

*Function documentation for `loopEnd`*

### cut

##cut##

*Function documentation for `cut`*

### clip

##clip##

*Function documentation for `clip`*

### loopAt

##Pattern.loopAt##

*Function documentation for `Pattern.loopAt`*

### fit

##fit##

*Function documentation for `fit`*

### chop

##Pattern.chop##

*Function documentation for `Pattern.chop`*

### striate

##Pattern.striate##

*Function documentation for `Pattern.striate`*

### slice

##Pattern.slice##

*Function documentation for `Pattern.slice`*

### splice

##splice##

*Function documentation for `splice`*

### speed

##speed##

*Function documentation for `speed`*

After samples, let's see what [Synths](/learn/synths) afford us.

---

## Signals

# Continuous Signals

Signals are patterns with continuous values, meaning they have theoretically infinite steps.
They can provide streams of numbers that can be sampled at discrete points in time.

## saw

##saw##

*Function documentation for `saw`*

## sine

##sine##

*Function documentation for `sine`*

## cosine

##cosine##

*Function documentation for `cosine`*

## tri

##tri##

*Function documentation for `tri`*

## square

##square##

*Function documentation for `square`*

## rand

##rand##

*Function documentation for `rand`*

## Ranges from -1 to 1

There is also `saw2`, `sine2`, `cosine2`, `tri2`, `square2` and `rand2` which have a range from -1 to 1!

## perlin

##perlin##

*Function documentation for `perlin`*

## irand

##irand##

*Function documentation for `irand`*

## brand

##brand##

*Function documentation for `brand`*

## brandBy

##brandBy##

*Function documentation for `brandBy`*

## mouseX

##mousex##

*Function documentation for `mousex`*

## mouseY

##mousey##

*Function documentation for `mousey`*

Next up: [Random Modifiers](/learn/random-modifiers)

---

## Sounds

# Sounds

We can play sounds with `s`, in two different ways:

- `s` can trigger audio samples, where a sound file is loaded in the background and played back:
  
- `s` can trigger audio synthesisers, which are synthesised in real-time using code also running in the background:
  

You can learn more about both of these approaches in the pages [Synths](/learn/synths) and [Samples](/learn/samples).

# Combining notes and sounds

In both of the above cases, we are no longer directly controlling the `note`/`freq` of the sound heard via `s`, as we were in the [Notes](/workshop/first-notes/) page.

So how can we both control the sound and the pitch? We can _combine_ `note`/`freq` with `s` to change the sound of our pitches:







The last example will actually sound the same with or without `s`, because `triangle` is the default value for `s`.

What about combining different notes with different sounds at the same time?



Hmm, something interesting is going on there, related to there being five notes and three sounds.

Let's now take a step back and think about the Strudel [Code](/learn/code/) we've been hearing so far.

---

## Stepwise

# Stepwise patterning (experimental)

This is a developing area of strudel, and behaviour might change or be renamed in future versions. Feedback and ideas are welcome!

## Introduction

Usually in strudel, the only reference point for most pattern transformations is the _cycle_. Now it is possible to also work with _steps_, via a growing range of functions.

For example usually when you `fastcat` two patterns together, the cycles will be squashed into half a cycle each:



With the new stepwise `stepcat` function, the steps of the two patterns will be evenly distributed across the cycle:



By default, steps are counted according to the 'top level' in mini-notation. For example `"a [b c] d e"` has five events in it per cycle, but is counted as four steps, where `[b c]` is counted as a single step.

However, you can mark a different metrical level to count steps relative to, using a `^` at the start of a sub-pattern. If we do this to the subpattern in our example: `"a [^b c] d e"`, then the pattern is now counted as having _eight_ steps. This is because 'b' and 'c' are each counted as single steps, and the events in the pattern are twice as long, and so counted as two steps each.

## Pacing the steps

Some stepwise functions don't appear to do very much on their own, for example these two examples of the `expand` function sound exactly the same despite being expanded by different amounts:





The number of steps per cycle is being changed behind the scenes, but on its own, that doesn't do anything. You will hear a difference however, once you use another stepwise function with it, for example `stepcat`:





You should be able to hear that `expand` increases the duration of the steps of the first subpattern, proportionally to the second one.

You can also change the speed of a pattern to match a given number of steps per cycle, with the `pace` function:





The first example has ten steps, and the second example has 18 steps, but are then both played a rate of 8 steps per cycle.

The argument to `expand` can also be patterned, and will be treated in a stepwise fashion. This means that the patterns from the changing values in the argument will be `stepcat`ted together:



This results in a dense pattern, because the different expanded versions are squashed into a single cycle. `pace` is again handy here for slowing down the pattern to a particular number of steps per cycle:



Earlier versions of many of these functions had `s_` prefixes, and the `pace` function was previously known as `steps`. These still exist as aliases, but may have changed behaviour and will soon be removed. Please update your patterns!

## Stepwise functions

### pace

##pace##

*Function documentation for `pace`*

### stepcat

##stepcat##

*Function documentation for `stepcat`*

### stepalt

##stepalt##

*Function documentation for `stepalt`*

### expand

##expand##

*Function documentation for `expand`*

### contract

##contract##

*Function documentation for `contract`*

### extend

##extend##

*Function documentation for `extend`*

### take

##take##

*Function documentation for `take`*

### drop

##drop##

*Function documentation for `drop`*

### polymeter

##polymeter##

*Function documentation for `polymeter`*

### shrink

##shrink##

*Function documentation for `shrink`*

### grow

##grow##

*Function documentation for `grow`*

### tour

##tour##

*Function documentation for `tour`*

### zip

##zip##

*Function documentation for `zip`*

---

## Strudel Vs Tidal

# Comparing Strudel and Tidal

This page is dedicated to exisiting tidal users, giving an overview of all the differences between Strudel and Tidal.

## Language

Strudel is written in JavaScript, while Tidal is written in Haskell.

### Example

This difference is most obvious when looking at the syntax:

```haskell
iter 4 $ every 3 (||+ n "10 20") $ (n "0 1 3") # s "triangle" # crush 4
```

One _could_ express that pattern to Strudel like so:

```
iter(4, every(3, add.squeeze("10 20"), n("0 1 3").s("triangle").crush(4)))
```

- The `$` operator does not exist, so the `iter` function has to wrap everything in parens.
- Custom operators like `||+` are explicit function calls, `add.squeeze` in this case
- The `#` operator is replaced with a chained function call `# crush 4` => `.crush(4)`

Unlike Haskell, JavaScript lacks the ability to define custom infix
operators, or change the meaning of existing ones.

Before you discard Strudel as an unwieldy paren monster, look at this alternative way to write the above:

```
n("0 1 3").every(3, add.squeeze("10 20")).iter(4).s("triangle").crush(4)
```

By reordering calls, the parens are much less nested.
As a general rule by thumb, you could say that everything Tidal does with `$` is reversed in Strudel:

`iter 4 $ every 3 (||+ n "10 20") $ (n "0 1 3")`

becomes

`n("0 1 3").every(3, add.squeeze("10 20")).iter(4)`

Simply put, `foo x $ bar x` becomes `bar(x).foo(x)`.

### Operators

The [custom operators of tidal](https://tidalcycles.org/docs/reference/pattern_structure/#all-the-operators) are normal functions in strudel:

| function    | tidal  | strudel |
| ----------- | ------ | ------- |
| add         | \|+ n  | .add(n) |
| subtract    | \|- n  | .sub(n) |
| multiply    | \|\* n | .mul(n) |
| divide      | \|\/ n | .div(n) |
| modulo      | \|\% n | .mod(n) |
| left values | \|\< n | .set(n) |

The above list only displays the operators taking the structure comes from the `left`.
For each of those, a `right` and `both` variant also exists.
As this directional thinking only works with code, strudel calls these `in` / `out` / `mix`:

| direction | tidal   | strudel     |
| --------- | ------- | ----------- |
| left      | \|+ n   | .add.in(n)  |
| right     | +\| n   | .add.out(n) |
| both      | \|+\| n | .add.mix(n) |

Instead of `+` / `add`, you can use any of the available operators of the first list.

## Function Compatibility

[This issue](https://codeberg.org/uzu/strudel/issues/31) tracks which Tidal functions are implemented in Strudel.
The list might not be 100% up to date and probably also misses some functions completely..
Feel encouraged to search the source code for a function you're looking for.
If you find a function that's not on the list, please tell!

## Control Params

As seen in the example, the `#` operator (shorthand for `|>`) is also just a function call in strudel.
So `note "c5" # s "gtr"` becomes `note("c5").s('gtr')`.

[This file](https://codeberg.org/uzu/strudel/src/branch/main/packages/core/controls.mjs) lists all available control params.
Note that not all of those work in the Webaudio Output of Strudel.
If you find a tidal control that's not on the list, please tell!

## Sound

Tidal is commonly paired with Superdirt / Supercollider for sound generation.
While Strudel also has a way of [communicating with Superdirt](/learn/input-output/),
it aims to provide a standalone live coding environment that runs entirely in the browser.

### Audio Effects

Many of SuperDirt's effects have been reimplemented in Strudel, using the Web Audio API.
You can find a [list of available effects here](/learn/effects/).

### Sampler

Strudel's sampler supports [a subset](/learn/samples) of Superdirt's sampler.
Also, samples are always loaded from a URL rather than from the disk, although [that might be possible in the future](https://codeberg.org/uzu/strudel/issues/118).

## Evaluation

The Strudel REPL does not support [block based evaluation](https://codeberg.org/uzu/strudel/issues/34) yet.
You can use labeled statements and `_` to mute:



## Tempo

Strudels tempo is 1 cycle per second, while tidal defaults to `0.5625`.
You can get the same tempo as tidal with:

```
note("c a f e").fast(.5625);
```

Next up: the [REPL](/technical-manual/repl)

---

## Synths

# Synths

In addition to the sampling engine, strudel comes with a synthesizer to create sounds on the fly.

## Basic Waveforms

The basic waveforms are `sine`, `sawtooth`, `square` and `triangle`, which can be selected via `sound` (or `s`):

```javascript
note("c2 <eb2 <g2 g1>>".fast(2))
.sound("<sawtooth square triangle sine>")
._scope()
```

If you don't set a `sound` but a `note` the default value for `sound` is `triangle`!

## Noise

You can also use noise as a source by setting the waveform to: `white`, `pink` or `brown`. These are different
flavours of noise, here written from hard to soft.

```javascript
sound("<white pink brown>")._scope()
```

Here's a more musical example of how to use noise for hihats:

```javascript
sound("bd*2,<white pink brown>*8")
.decay(.04).sustain(0)._scope()
```

Some amount of pink noise can also be added to any oscillator by using the `noise` paremeter:

```javascript
note("c3").noise("<0.1 0.25 0.5>")._scope()
```

You can also use the `crackle` type to play some subtle noise crackles. You can control noise amount by using the `density` parameter:

```javascript
s("crackle*4").density("<0.01 0.04 0.2 0.5>".slow(2))._scope()
```

### Additive Synthesis

To tame the harsh sound of the basic waveforms, we can set the `n` control to limit the overtones of the waveform:

```javascript
note("c2 <eb2 <g2 g1>>".fast(2))
.sound("sawtooth")
.n("<32 16 8 4>")
._scope()
```

When the `n` control is used on a basic waveform, it defines the number of harmonic partials the sound is getting.
You can also set `n` directly in mini notation with `sound`:

```javascript
note("c2 <eb2 <g2 g1>>".fast(2))
.sound("sawtooth:<32 16 8 4>")
._scope()
```

Note for tidal users: `n` in tidal is synonymous to `note` for synths only.
In strudel, this is not the case, where `n` will always change timbre, be it though different samples or different waveforms.

## Vibrato

### vib

##vib##

*Function documentation for `vib`*

### vibmod

##vibmod##

*Function documentation for `vibmod`*

## FM Synthesis

FM Synthesis is a technique that changes the frequency of a basic waveform rapidly to alter the timbre.

You can use fm with any of the above waveforms, although the below examples all use the default triangle wave.

### fm

##fm##

*Function documentation for `fm`*

### fmh

##fmh##

*Function documentation for `fmh`*

### fmattack

##fmattack##

*Function documentation for `fmattack`*

### fmdecay

##fmdecay##

*Function documentation for `fmdecay`*

### fmsustain

##fmsustain##

*Function documentation for `fmsustain`*

### fmenv

##fmenv##

*Function documentation for `fmenv`*

## Wavetable Synthesis

Strudel can also use the sampler to load custom waveforms as a replacement of the default waveforms used by WebAudio for the base synth. A default set of more than 1000 wavetables is accessible by default (coming from the [AKWF](https://www.adventurekid.se/akrt/waveforms/adventure-kid-waveforms/) set). You can also import/use your own. A wavetable is a one-cycle waveform, which is then repeated to create a sound at the desired frequency. It is a classic but very effective synthesis technique.

Any sample preceded by the `wt_` prefix will be loaded as a wavetable. This means that the `loop` argument will be set to `1` by default. You can scan over the wavetable by using `loopBegin` and `loopEnd` as well.

```javascript
samples('bubo:waveforms');
note("<[g3,b3,e4]!2 [a3,c3,e4] [b3,d3,f#4]>")
.n("<1 2 3 4 5 6 7 8 9 10>/2").room(0.5).size(0.9)
.s('wt_flute').velocity(0.25).often(n => n.ply(2))
.release(0.125).decay("<0.1 0.25 0.3 0.4>").sustain(0)
.cutoff(2000).cutoff("<1000 2000 4000>").fast(4)
._scope()

```

## ZZFX

The "Zuper Zmall Zound Zynth" [ZZFX](https://github.com/KilledByAPixel/ZzFX) is also integrated in strudel.
Developed by [Frank Force](https://frankforce.com/), it is a synth and FX engine originally intended to be used for size coding games.

It has 20 parameters in total, here is a snippet that uses all:

```javascript
note("c2 eb2 f2 g2") // also supports freq
  .s("{z_sawtooth z_tan z_noise z_sine z_square}%4")
  .zrand(0) // randomization
  // zzfx envelope
  .attack(0.001)
  .decay(0.1)
  .sustain(.8)
  .release(.1)
  // special zzfx params
  .curve(1) // waveshape 1-3
  .slide(0) // +/- pitch slide
  .deltaSlide(0) // +/- pitch slide (?)
  .noise(0) // make it dirty
  .zmod(0) // fm speed
  .zcrush(0) // bit crush 0 - 1
  .zdelay(0) // simple delay
  .pitchJump(0) // +/- pitch change after pitchJumpTime
  .pitchJumpTime(0) // >0 time after pitchJump is applied
  .lfo(0) // >0 resets slide + pitchJump + sets tremolo speed
  .tremolo(0) // 0-1 lfo volume modulation amount
  //.duration(.2) // overwrite strudel event duration
  //.gain(1) // change volume
  ._scope() // vizualise waveform (not zzfx related)

```

Note that you can also combine zzfx with all the other audio fx (next chapter).

Next up: [Audio Effects](/learn/effects)...

---

## Time Modifiers

# Time Modifiers

The following functions modify a pattern temporal structure in some way.
Some of these have equivalent operators in the Mini Notation:

| function               | mini         |
| ---------------------- | ------------ |
| `"x".slow(2)`          | `"x/2"`      |
| `"x".fast(2)`          | `"x*2"`      |
| `"x".euclid(3,8)`      | `"x(3,8)"`   |
| `"x".euclidRot(3,8,1)` | `"x(3,8,1)"` |

## slow

##Pattern.slow##

*Function documentation for `Pattern.slow`*

## fast

##Pattern.fast##

*Function documentation for `Pattern.fast`*

## early

##Pattern.early##

*Function documentation for `Pattern.early`*

## late

##Pattern.late##

*Function documentation for `Pattern.late`*

## clip / legato

##clip##

*Function documentation for `clip`*

## euclid

##Pattern.euclid##

*Function documentation for `Pattern.euclid`*

### euclidRot

##Pattern.euclidRot##

*Function documentation for `Pattern.euclidRot`*

### euclidLegato

##Pattern.euclidLegato##

*Function documentation for `Pattern.euclidLegato`*

## rev

##Pattern.rev##

*Function documentation for `Pattern.rev`*

## palindrome

##palindrome##

*Function documentation for `palindrome`*

## iter

##Pattern.iter##

*Function documentation for `Pattern.iter`*

### iterBack

##Pattern.iterBack##

*Function documentation for `Pattern.iterBack`*

## ply

##ply##

*Function documentation for `ply`*

## segment

##segment##

*Function documentation for `segment`*

## compress

##compress##

*Function documentation for `compress`*

## zoom

##zoom##

*Function documentation for `zoom`*

## linger

##linger##

*Function documentation for `linger`*

## fastGap

##fastGap##

*Function documentation for `fastGap`*

## inside

##inside##

*Function documentation for `inside`*

## outside

##outside##

*Function documentation for `outside`*

## cpm

##cpm##

*Function documentation for `cpm`*

## ribbon

##ribbon##

*Function documentation for `ribbon`*

## swingBy

##swingBy##

*Function documentation for `swingBy`*

## swing

##swing##

*Function documentation for `swing`*

Apart from modifying time, there are ways to [Control Parameters](/functions/value-modifiers/).

---

## Tonal

# Tonal Functions

These functions use [tonaljs](https://github.com/tonaljs/tonal) to provide helpers for musical operations.

### voicing()

##voicing##

*Function documentation for `voicing`*

Here's an example of how you can play chords and a bassline:

```javascript
chord("<C^7 A7b13 Dm7 G7>*2")
  .dict('ireal').layer(
  x=>x.struct("[~ x]*2").voicing()
  ,
  x=>n("0*4").set(x).mode("root:g2").voicing()
  .s('sawtooth').cutoff("800:4:2")
)
```

### scale(name)

##scale##

*Function documentation for `scale`*

### transpose(semitones)

Transposes all notes to the given number of semitones:

```javascript
"[c2 c3]*4".transpose("<0 -2 5 3>").note()
```

This method gets really exciting when we use it with a pattern as above.

Instead of numbers, scientific interval notation can be used as well:

```javascript
"[c2 c3]*4".transpose("<1P -2M 4P 3m>").note()
```

### scaleTranspose(steps)

Transposes notes inside the scale by the number of steps:

```javascript
"[-8 [2,4,6]]*2"
.scale('C4 bebop major')
.scaleTranspose("<0 -1 -2 -3 -4 -5 -6 -4>*2")
.note()
```

### rootNotes(octave = 2)

Turns chord symbols into root notes of chords in given octave.

```javascript
"<C^7 A7b13 Dm7 G7>*2".rootNotes(3).note()
```

Together with layer, struct and voicings, this can be used to create a basic backing track:

```javascript
"<C^7 A7b13 Dm7 G7>*2".layer(
  x => x.voicings('lefthand').struct("[~ x]*2").note(),
  x => x.rootNotes(2).note().s('sawtooth').cutoff(800)
)
```

---

## Visual Feedback

# Visual Feedback

There are several function that add visual feedback to your patterns.

## Mini Notation Highlighting

When you write mini notation with "double quotes" or \`backticks\`, the active parts of the mini notation will be highlighted:

```javascript
n("<0 2 1 3 2>*8")
.scale("<A1 D2>/4:minor:pentatonic")
.s("supersaw").lpf(300).lpenv("<4 3 2>\*4")
```

You can change the color as well, even pattern it:

```javascript
n("<0 2 1 3 2>*8")
.scale("<A1 D2>/4:minor:pentatonic")
.s("supersaw").lpf(300).lpenv("<4 3 2>*4")
.color("cyan magenta")
```

## Global vs Inline Visuals

The following functions all come with in 2 variants.

**Without prefix**: renders the visual to the background of the page:



**With `_` prefix**: renders the visual inside the code. Allows for multiple visuals



Here we see the 2 variants for `punchcard`. The same goes for all others below.
To improve readability the following demos will all use the inline variant.

## Punchcard / Pianoroll

These 2 functions render a pianoroll style visual.
The only difference between the 2 is that `pianoroll` will render the pattern directly,
while `punchcard` will also take the transformations into account that occur afterwards:



Here, the `color` is still visible in the visual, even if it is applied after `_punchcard`.
On the contrary, the color is not visible when using `_pianoroll`:



<br />

`punchcard` is less resource intensive because it uses the same data as used for the mini notation highlighting.

The visual can be customized by passing options. Those options are the same for both functions.

What follows is the API doc of all the options you can pass:

##pianoroll##

*Function documentation for `pianoroll`*

## Spiral

##spiral##

*Function documentation for `spiral`*

## Scope

##scope##

*Function documentation for `scope`*

## Pitchwheel

##pitchwheel##

*Function documentation for `pitchwheel`*

## Spectrum

##spectrum##

*Function documentation for `spectrum`*

## markcss

##markcss##

*Function documentation for `markcss`*

---

# Workshop Exercises

## First Effects

# First Effects

We have sounds, we have notes, now let's look at effects!

## Some basic effects

**low-pass filter**

```javascript
note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
.sound("sawtooth").lpf(800)
```

lpf = **l**ow **p**ass **f**ilter

- Change lpf to 200. Notice how it gets muffled. Think of it as standing in front of the club with the door closed 🚪.
- Now let's open the door... change it to 5000. Notice how it gets brighter ✨🪩

**pattern the filter**

```javascript
note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
.sound("sawtooth").lpf("200 1000 200 1000")
```

- Try adding more values
- Notice how the pattern in lpf does not change the overall rhythm

We will learn how to automate with waves later...

**vowel**

```javascript
note("<[c3,g3,e4] [bb2,f3,d4] [a2,f3,c4] [bb2,g3,eb4]>")
.sound("sawtooth").vowel("<a e i o>")
```

**gain**



Rhythm is all about dynamics!

- Remove `.gain(...)` and notice how flat it sounds.
- Bring it back by undoing (ctrl+z)

Let's combine all of the above into a little tune:

```javascript
$: sound("hh*8").gain("[.25 1]*4")

$: sound("bd*4,[~ sd:1]*2")

$: note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
.sound("sawtooth").lpf("200 1000 200 1000")

$: note("<[c3,g3,e4] [bb2,f3,d4] [a2,f3,c4] [bb2,g3,eb4]>")
.sound("sawtooth").vowel("<a e i o>")
```

**shape the sound with an adsr envelope**



Try to find out what the numbers do.. Compare the following

- attack: `.5` vs `0`
- decay: `.5` vs `0`
- sustain: `1` vs `.25` vs `0`
- release: `0` vs `.5` vs `1`

Can you guess what they do?

<QA q="Click to see solution" client:visible>

- attack: time it takes to fade in
- decay: time it takes to fade to sustain
- sustain: level after decay
- release: time it takes to fade out after note is finished

![ADSR](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/ADSR_parameter.svg/1920px-ADSR_parameter.svg.png)

</QA>

**adsr short notation**



**delay**

```javascript
$: note("[~ [<[d3,a3,f4]!2 [d3,bb3,g4]!2> ~]]*2")
  .sound("gm_electric_guitar_muted").delay(.5)

$: sound("bd rim").bank("RolandTR707").delay(".5")
```

Try some `delay` values between 0 and 1. Btw, `.5` is short for `0.5`

What happens if you use `.delay(".8:.125")` ? Can you guess what the second number does?

What happens if you use `.delay(".8:.06:.8")` ? Can you guess what the third number does?

<QA q="Click to see solution" client:visible>

`delay("a:b:c")`:

- a: delay volume
- b: delay time
- c: feedback (smaller number = quicker fade)

</QA>

**room aka reverb**

```javascript
n("<4 [3@3 4] [<2 0> ~@16] ~>")
.scale("D4:minor").sound("gm_accordion:2")
.room(2)
```

Try different values!

Add a delay too!

**little dub tune**

```javascript
$: note("[~ [<[d3,a3,f4]!2 [d3,bb3,g4]!2> ~]]*2")
.sound("gm_electric_guitar_muted").delay(.5)

$: sound("bd rim").bank("RolandTR707").delay(.5)

$: n("<4 [3@3 4] [<2 0> ~@16] ~>")
.scale("D4:minor").sound("gm_accordion:2")
.room(2).gain(.5)
```

Let's add a bass to make this complete:

```javascript
$: note("[~ [<[d3,a3,f4]!2 [d3,bb3,g4]!2> ~]]*2")
.sound("gm_electric_guitar_muted").delay(.5)

$: sound("bd rim").bank("RolandTR707").delay(.5)

$: n("<4 [3@3 4] [<2 0> ~@16] ~>")
.scale("D4:minor").sound("gm_accordion:2")
.room(2).gain(.4)

$: n("[0 [~ 0] 4 [3 2] [0 ~] [0 ~] <0 2> ~]/2")
.scale("D2:minor")
.sound("sawtooth,triangle").lpf(800)
```

Try adding `.hush()` at the end of one of the patterns in the stack...

**pan**



**speed**

```javascript
sound("bd rim [~ bd] rim").speed("<1 2 -1 -2>").room(.2)
```

**fast and slow**

We can use `fast` and `slow` to change the tempo of a pattern outside of Mini-Notation:



Change the `slow` value. Try replacing it with `fast`.

What happens if you use a pattern like `.fast("<1 [2 4]>")`?

By the way, inside Mini-Notation, `fast` is `*` and `slow` is `/`.

```javascript
sound("[bd*4,~ rim ~ cp]*<1 [2 4]>")
```

## modulation with signals

Instead of changing values stepwise, we can also control them with signals:



The basic waveforms for signals are `sine`, `saw`, `square`, `tri` 🌊

Try also random signals `rand` and `perlin`!

The gain is visualized as transparency in the pianoroll.

**setting a range**

By default, waves oscillate between 0 to 1. We can change that with `range`:



What happens if you flip the range values?

We can change the modulation speed with slow / fast:

```javascript
note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
  .sound("sawtooth")
  .lpf(sine.range(100, 2000).slow(4))
```

The whole modulation will now take 8 cycles to repeat.

## Recap

| name    | example                                                                                                          |
| ------- | ---------------------------------------------------------------------------------------------------------------- |
| lpf     | ```javascript
note("c2 c3 c2 c3").s("sawtooth").lpf("<400 2000>")
```                         |
| vowel   | ```javascript
note("c3 eb3 g3").s("sawtooth").vowel("<a e i o>")
```                          |
| gain    |                                                 |
| delay   |                                                  |
| room    |                                                   |
| pan     |                                                 |
| speed   | ```javascript
s("bd rim bd cp").speed("<1 2 -1 -2>")
```                                      |
| signals | `sine`, `saw`, `square`, `tri`, `rand`, `perlin`<br/> |
| range   |                                          |

Let us now take a look at some of Tidal's typical [pattern effects](/workshop/pattern-effects).

---

## First Notes

# First Notes

Let's look at how we can play notes

## numbers and notes

**play notes with numbers**

<MiniRepl
  client:visible
  tune={`note("48 52 55 59").sound("piano")`}
  claviature
  claviatureLabels={Object.fromEntries(
    Array(49)
      .fill()
      .map((_, i) => [midi2note(i + 36), i + 36]),
  )}
/>

Try out different numbers!

Try decimal numbers, like 55.5

**play notes with letters**

<MiniRepl
  client:visible
  tune={`note("c e g b").sound("piano")`}
  claviature
  claviatureLabels={Object.fromEntries(['c3', 'd3', 'e3', 'f3', 'g3', 'a3', 'b3'].map((n) => [n, n.split('')[0]]))}
/>

Try out different letters (a - g).

Can you find melodies that are actual words? Hint: ☕ 😉 ⚪

**add flats or sharps to play the black keys**

<MiniRepl
  client:visible
  tune={`note("db eb gb ab bb").sound("piano")`}
  claviature
  claviatureLabels={Object.fromEntries(
    ['db3', 'eb3', 'gb3', 'ab3', 'bb3'].map((n) => [n, n.split('').slice(0, 2).join('')]),
  )}
/>

<MiniRepl
  client:visible
  tune={`note("c# d# f# g# a#").sound("piano")`}
  claviature
  claviatureLabels={Object.fromEntries(
    ['c#3', 'd#3', 'f#3', 'g#3', 'a#3'].map((n) => [n, n.split('').slice(0, 2).join('')]),
  )}
/>

**play notes with letters in different octaves**

<MiniRepl
  client:visible
  tune={`note("c2 e3 g4 b5").sound("piano")`}
  claviature
  claviatureLabels={Object.fromEntries(
    Array(49)
      .fill()
      .map((_, i) => [midi2note(i + 36), midi2note(i + 36)]),
  )}
/>

Try out different octaves (1-8)

If you are not comfortable with the note letter system, it should be easier to use numbers instead.
Most of the examples below will use numbers for that reason.
We will also look at ways to make it easier to play the right notes later.

## changing the sound

Just like with unpitched sounds, we can change the sound of our notes with `sound`:



{/* c2 g2, e3 b3 d4 e4 */}

Try out different sounds:

- gm_electric_guitar_muted
- gm_acoustic_bass
- gm_voice_oohs
- gm_blown_bottle
- sawtooth
- square
- triangle
- how about bd, sd or hh?
- remove `.sound('...')` completely

**switch between sounds**



**stack multiple sounds**



The `note` and `sound` patterns are combined!

We will see more ways to combine patterns later..

## Longer Sequences

**Divide sequences with `/` to slow them down**



The `/4` plays the sequence in brackets over 4 cycles (=8s).

So each of the 4 notes is 2s long.

Try adding more notes inside the brackets and notice how it gets faster.

**Play one per cycle with `< ... >`**

In the last section, we learned that `< ... >` (angle brackets) can be used to play only one thing per cycle,
which is useful for longer melodies too:

```javascript
note("<36 34 41 39>").sound("gm_acoustic_bass")
```
*This example includes visual pattern representation*

Try adding more notes inside the brackets and notice how the tempo stays the same.

The angle brackets are actually just a shortcut:

`<a b c>` = `[a b c]/3`

`<a b c d>` = `[a b c d]/4`

...

**Play one sequence per cycle**

We can combine the 2 types of brackets in all sorts of different ways.
Here is an example of a repetitive bassline:

```javascript
note("<[36 48]*4 [34 46]*4 [41 53]*4 [39 51]*4>")
.sound("gm_acoustic_bass")
```
*This example includes visual pattern representation*

**Alternate between multiple things**

```javascript
note("60 <63 62 65 63>")
.sound("gm_xylophone")
```
*This example includes visual pattern representation*

This is also useful for unpitched sounds:

```javascript
sound("bd*4, [~ <sd cp>]*2, [~ hh]*4")
.bank("RolandTR909")
```
*This example includes visual pattern representation*

## Scales

Finding the right notes can be difficult.. Scales are here to help:

```javascript
setcpm(60)
n("0 2 4 <[6,8] [7,9]>")
.scale("C:minor").sound("piano")
```
*This example includes visual pattern representation*

Try out different numbers. Any number should sound good!

Try out different scales:

- C:major
- A2:minor
- D:dorian
- G:mixolydian
- A2:minor:pentatonic
- F:major:pentatonic

**automate scales**

Just like anything, we can automate the scale with a pattern:

```javascript
setcpm(60)
n("<0 -3>, 2 4 <[6,8] [7,9]>")
.scale("<C:major D:mixolydian>/4")
.sound("piano")
```
*This example includes visual pattern representation*

If you have no idea what these scale mean, don't worry.
These are just labels for different sets of notes that go well together.

Take your time and you'll find scales you like!

## Repeat & Elongate

**Elongate with @**



Not using `@` is like using `@1`. In the above example, c is 3 units long and eb is 1 unit long.

Try changing that number!

**Elongate within sub-sequences**

```javascript
setcpm(60)
n("<[4@2 4] [5@2 5] [6@2 6] [5@2 5]>*2")
.scale("<C2:mixolydian F2:mixolydian>/4")
.sound("gm_acoustic_bass")
```
*This example includes visual pattern representation*

This groove is called a `shuffle`.
Each beat has two notes, where the first is twice as long as the second.
This is also sometimes called triplet swing. You'll often find it in blues and jazz.

**Replicate**

```javascript
setcpm(60)
note("c!2 [eb,<g a bb a>]").sound("piano")
```
*This example includes visual pattern representation*

Try switching between `!`, `*` and `@`

What's the difference?

## Recap

Let's recap what we've learned in this chapter:

| Concept   | Syntax | Example                                                  |
| --------- | ------ | -------------------------------------------------------- |
| Slow down | \/     |  |
| Alternate | \<\>   | ```javascript
note("c a f <e g>")
``` |
| Elongate  | @      |        |
| Replicate | !      |        |

New functions:

| Name  | Description                   | Example                                                                           |
| ----- | ----------------------------- | --------------------------------------------------------------------------------- |
| note  | set pitch as number or letter |                |
| scale | interpret `n` as scale degree |  |
| $:    | play patterns in parallel     |              |

## Examples

**Classy Bassline**

```javascript
note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
.sound("gm_synth_bass_1")
.lpf(800) // <-- we'll learn about this soon
```

**Classy Melody**

<MiniRepl
  client:visible
  tune={`n(\`<
[~ 0] 2 [0 2] [~ 2]
[~ 0] 1 [0 1] [~ 1]
[~ 0] 3 [0 3] [~ 3]
[~ 0] 2 [0 2] [~ 2]
>*4\`).scale("C4:minor")
.sound("gm_synth_strings_1")`}
/>

**Classy Drums**

```javascript
sound("bd*4, [~ <sd cp>]*2, [~ hh]*4")
.bank("RolandTR909")
```

**If there just was a way to play all the above at the same time.......**

You can use `$:` 😙

## Playing multiple patterns

If you want to play multiple patterns at the same time, make sure to write `$:` before each:

<MiniRepl
  client:visible
  tune={`$: note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
  .sound("gm_synth_bass_1").lpf(800)
  
$: n(\`<
  [~ 0] 2 [0 2] [~ 2]
  [~ 0] 1 [0 1] [~ 1]
  [~ 0] 3 [0 3] [~ 3]
  [~ 0] 2 [0 2] [~ 2]
  >*4\`).scale("C4:minor")
  .sound("gm_synth_strings_1")
  
$: sound("bd*4, [~ <sd cp>]*2, [~ hh]*4")
.bank("RolandTR909")`}
/>

Try changing `$` to `_$` to mute a part!

This is starting to sound like actual music! We have sounds, we have notes, now the last piece of the puzzle is missing: [effects](/workshop/first-effects)

---

## First Sounds

# First Sounds

This is the first chapter of the Strudel Workshop, nice to have you on board!

## Code Fields

The workshop is full of interactive code fields. Let's learn how to use those. Here is one:



1. ⬆️ click into the text field above ⬆️
2. press `ctrl`+`enter` to play
3. change `casio` to `metal`
4. press `ctrl`+`enter` to update
5. press `ctrl`+`.` to stop

Congratulations, you are now live coding!

## Sounds

We have just played a sound with `sound` like this:



`casio` is one of many standard sounds.

Try out a few other sounds:

```
insect wind jazz metal east crow casio space numbers
```

You might hear a little pause while the sound is loading

**Change Sample Number with :**

One Sound can contain multiple samples (audio files).

You can select the sample by appending `:` followed by a number to the name:



Try different sound / sample number combinations.

Not adding a number is like doing `:0`

Now you know how to use different sounds.
For now we'll stick to this little selection of sounds, but we'll find out how to load your own sounds later.

## Drum Sounds

By default, Strudel comes with a wide selection of drum sounds:



These letter combinations stand for different parts of a drum set:

<img src="/img/drumset.png" />

<a class="text-right text-xs" href="https://de.wikipedia.org/wiki/Schlagzeug#/media/Datei:Drum_set.svg" target="_blank">
  original image by Pbroks13
</a>

- `bd` = **b**ass **d**rum
- `sd` = **s**nare **d**rum
- `rim` = **rim**shot
- `hh` = **h**i**h**at
- `oh` = **o**pen **h**ihat
- `lt` = **l**ow tom
- `mt` = **m**iddle tom
- `ht` = **h**igh tom
- `rd` = **r**i**d**e cymbal
- `cr` = **cr**ash cymbal

Try out different drum sounds!

To change the sound character of our drums, we can use `bank` to change the drum machine:



In this example `RolandTR909` is the name of the drum machine that we're using.
It is a famous drum machine for house and techno beats.

Try changing `RolandTR909` to one of

- `AkaiLinn`
- `RhythmAce`
- `RolandTR808`
- `RolandTR707`
- `ViscoSpaceDrum`

There are a lot more, but let's keep it simple for now

🦥 Pro-Tip: Mark a name via double click. Then just copy and paste!

## Sequences

In the last example, we already saw that you can play multiple sounds in a sequence by separating them with a space:



Notice how the currently playing sound is highlighted in the code and also visualized below.

Try adding more sounds to the sequence!

**The longer the sequence, the faster it runs**



The content of a sequence will be squished into what's called a cycle. A cycle is 2s long by default.

**One per cycle with `< .. >`**

Here is the same sequence, but this time sourrounded with `< .. >` (angle brackets):

```javascript
sound("<bd bd hh bd rim bd hh bd>")
```
*This example includes visual pattern representation*

This will play only one sound per cycle. With these brackets, the tempo doesn't change when we add or remove elements!

Because this is now very slow, we can speed it up again like this:

```javascript
sound("<bd bd hh bd rim bd hh bd>*8")
```
*This example includes visual pattern representation*

Here, the `*8` means we make the whole thing 8 times faster.

Wait a minute, isn't this the same as without `< ... >*8`? Why do we need it then?

That's true, the special thing about this notation is that the tempo won't change when you add or remove elements, try it!

Try also changing the number at the end to change the tempo!

**changing the tempo with setcpm**

```javascript
setcpm(90/4)
sound("<bd hh rim hh>*8")
```
*This example includes visual pattern representation*

cpm = cycles per minute

By default, the tempo is 30 cycles per minute = 120/4 = 1 cycle every 2 seconds

In western music terms, you could say the above are 8ths notes at 90bpm in 4/4 time.
But don't worry if you don't know these terms, as they are not required to make music with Strudel.

**Add a rests in a sequence with '-' or '~'**



**Sub-Sequences with [brackets]**



Try adding more sounds inside a bracket!

Similar to the whole sequence, the content of a sub-sequence will be squished to its own length.

**Multiplication: Speed things up**



**Multiplication: Speed up subsequences**



**Multiplication: Speeeeeeeeed things up**



Pitch = really fast rhythm

**Sub-Sub-Sequences with [[brackets]]**



You can go as deep as you want!

**Play sequences in parallel with comma**



You can use as many commas as you want:



Commas can also be used inside sub-sequences:



Notice how the 2 above are the same?

It is quite common that there are many ways to express the same idea.

**Multiple Lines with backticks**



**selecting sample numbers separately**

Instead of using ":", we can also use the `n` function to select sample numbers:



This is shorter and more readable than:



## Recap

Now we've learned the basics of the so called Mini-Notation, the rhythm language of Tidal.
This is what we've learned so far:

| Concept           | Syntax   | Example                                                                 |
| ----------------- | -------- | ----------------------------------------------------------------------- |
| Sequence          | space    |                |
| Sample Number     | :x       |        |
| Rests             | - or ~   |        |
| Alternate         | \<\>     | ```javascript
sound("<bd hh rim oh bd rim>")
```     |
| Sub-Sequences     | \[\]     |    |
| Sub-Sub-Sequences | \[\[\]\] |  |
| Speed up          | \*       |               |
| Parallel          | ,        |         |

The Mini-Notation is usually used inside some function. These are the functions we've seen so far:

| Name   | Description                         | Example                                                                           |
| ------ | ----------------------------------- | --------------------------------------------------------------------------------- |
| sound  | plays the sound of the given name   |                      |
| bank   | selects the sound bank              |  |
| setcpm | sets the tempo in cycles per minute |          |
| n      | select sample number                |            |

## Examples

**Basic rock beat**



**Classic house**



Notice that the two patterns are extremely similar.
Certain drum patterns are reused across genres.

We Will Rock you



**Yellow Magic Orchestra - Firecracker**



**Imitation of a 16 step sequencer**



**Another one**



**Not your average drums**



Now that we know the basics of how to make beats, let's look at how we can play [notes](/workshop/first-notes)

---

## Getting Started

# Welcome

<div className="w-32 animate-pulse md:float-right ml-8">![Strudel Icon](/icons/strudel_icon.png)</div>

Welcome to the Strudel documentation pages!
You've come to the right place if you want to learn how to make music with code.

## What is Strudel?

With Strudel, you can expressively write dynamic music pieces.<br/>
It is an official port of the [Tidal Cycles](https://tidalcycles.org/) pattern language to JavaScript.<br/>
You don't need to know JavaScript or Tidal Cycles to make music with Strudel.
This interactive tutorial will guide you through the basics of Strudel.<br/>
The best place to actually make music with Strudel is the [Strudel REPL](https://strudel.cc/)

<div className="clear-both" />

## What can you do with Strudel?

- live code music: make music with code in real time
- algorithmic composition: compose music using tidal's unique approach to pattern manipulation
- teaching: focussing on a low barrier of entry, Strudel is a good fit for teaching music and code at the same time.
- integrate into your existing music setup: either via MIDI or OSC, you can use Strudel as a really flexible sequencer

## Examples

Here are some examples of how strudel can sound:



These examples cannot fully encompass the variety of things you can do, so [check out the showcase](/intro/showcase/) for some videos of how people use Strudel.

## Getting Started

The best way to start learning Strudel is the workshop.
If you're ready to dive in, let's start with your [first sounds](/workshop/first-sounds)

---

## Pattern Effects

# Pattern Effects

Up until now, most of the functions we've seen are what other music programs are typically capable of: sequencing sounds, playing notes, controlling effects.

In this chapter, we are going to look at functions that are more unique to tidal.

**reverse patterns with rev**



**play pattern left and modify it right with jux**



This is the same as:



Let's visualize what happens here:



Try commenting out one of the two by adding `//` before a line

**multiple tempos**



This is like doing



Try commenting out one or more by adding `//` before a line

**add**

```javascript
setcpm(60)
note("c2 [eb3,g3] ".add("<0 <1 -1>>"))
.color("<cyan <magenta yellow>>").adsr("[.1 0]:.2:[1 0]")
.sound("gm_acoustic_bass").room(.5)
```
*This example includes visual pattern representation*

If you add a number to a note, the note will be treated as if it was a number

We can add as often as we like:

```javascript
setcpm(60)
note("c2 [eb3,g3]".add("<0 <1 -1>>").add("0,7"))
.color("<cyan <magenta yellow>>").adsr("[.1 0]:.2:[1 0]")
.sound("gm_acoustic_bass").room(.5)
```
*This example includes visual pattern representation*

**add with scale**

```javascript
n("0 [2 4] <3 5> [~ <4 1>]".add("<0 [0,2,4]>"))
.scale("C5:minor").release(.5)
.sound("gm_xylophone").room(.5)
```
*This example includes visual pattern representation*

**time to stack**

```javascript
$: n("0 [2 4] <3 5> [~ <4 1>]".add("<0 [0,2,4]>"))
  .scale("C5:minor")
  .sound("gm_xylophone")
  .room(.4).delay(.125)
$: note("c2 [eb3,g3]".add("<0 <1 -1>>"))
  .adsr("[.1 0]:.2:[1 0]")
  .sound("gm_acoustic_bass")
  .room(.5)
$: n("0 1 [2 3] 2").sound("jazz").jux(rev)
```

**ply**



this is like writing:



Try patterning the `ply` function, for example using `"<1 2 1 3>"`

**off**

```javascript
n("0 [4 <3 2>] <2 3> [~ 1]"
  .off(1/16, x=>x.add(4))
  //.off(1/8, x=>x.add(7))
).scale("<C5:minor Db5:mixolydian>/2")
.s("triangle").room(.5).dec(.1)
```
*This example includes visual pattern representation*

In the notation `.off(1/16, x=>x.add(4))`, says:

- take the original pattern named as `x`
- modify `x` with `.add(4)`, and
- play it offset to the original pattern by `1/16` of a cycle.

off is also useful for modifying other sounds, and can even be nested:

```javascript
s("bd sd [rim bd] sd,[~ hh]*4").bank("CasioRZ1")
  .off(2/16, x=>x.speed(1.5).gain(.25)
  .off(3/16, y=>y.vowel("<a e i o>*8")))
```

| name | description                    | example                                                                                     |
| ---- | ------------------------------ | ------------------------------------------------------------------------------------------- |
| rev  | reverse                        |             |
| jux  | split left/right, modify right |          |
| add  | add numbers / notes            | ```javascript
n("0 2 4 6 ~ 7 9 5".add("<0 1 2 1>")).scale("C:minor")
``` |
| ply  | speed up each event n times    | ```javascript
s("bd sd [~ bd] sd").ply("<1 2 3>")
```                    |
| off  | copy, shift time & modify      | ```javascript
s("bd sd [~ bd] sd, hh*8").off(1/16, x=>x.speed(2))
```    |

---

## Recap

# Workshop Recap

This page is just a listing of all functions covered in the workshop!

## Mini Notation

| Concept           | Syntax   | Example                                                               |
| ----------------- | -------- | --------------------------------------------------------------------- |
| Sequence          | space    |  |
| Sample Number     | :x       |      |
| Rests             | ~        |      |
| Sub-Sequences     | \[\]     |  |
| Sub-Sub-Sequences | \[\[\]\] |     |
| Speed up          | \*       |             |
| Parallel          | ,        |       |
| Slow down         | \/       |               |
| Alternate         | \<\>     | ```javascript
note("c <e g>")
```                  |
| Elongate          | @        |                     |
| Replicate         | !        |                     |

## Sounds

| Name  | Description                       | Example                                                                 |
| ----- | --------------------------------- | ----------------------------------------------------------------------- |
| sound | plays the sound of the given name |                      |
| bank  | selects the sound bank            |  |
| n     | select sample number              |          |

## Notes

| Name      | Description                   | Example                                                                           |
| --------- | ----------------------------- | --------------------------------------------------------------------------------- |
| note      | set pitch as number or letter |                |
| n + scale | set note in scale             |  |
| $:        | play patterns in parallel     |              |

## Audio Effects

| name  | example                                                                                 |
| ----- | --------------------------------------------------------------------------------------- |
| lpf   |   |
| vowel | ```javascript
note("c3 eb3 g3").s("sawtooth").vowel("<a e i o>")
``` |
| gain  |                        |
| delay |                         |
| room  |                          |
| pan   |                        |
| speed | ```javascript
s("bd rim bd cp").speed("<1 2 -1 -2>")
```             |
| range |                 |

## Pattern Effects

| name   | description                         | example                                                                             |
| ------ | ----------------------------------- | ----------------------------------------------------------------------------------- |
| setcpm | sets the tempo in cycles per minute |            |
| fast   | speed up                            |                |
| slow   | slow down                           |                |
| rev    | reverse                             |             |
| jux    | split left/right, modify right      |          |
| add    | add numbers / notes                 | ```javascript
n("0 2 4 6".add("<0 1 2 1>")).scale("C:minor")
``` |
| ply    | speed up each event n times         | ```javascript
s("bd sd").ply("<1 2 3>")
```                      |
| off    | copy, shift time & modify           | ```javascript
s("bd sd, hh*4").off(1/8, x=>x.speed(2))
```       |

---

# Pattern Recipes

## Arpeggios

# Build Arpeggios

Note: This has been (partly) translated from https://tidalcycles.org/docs/patternlib/howtos/buildarpeggios

# Build Arpeggios

This page will teach you how to get started writing arpeggios using different techniques. It is a good way to learn Strudel in a more intuitive way.

## Arpeggios from notes

Start with a simple sequence of notes:

```javascript
note("c a f e").piano().slow(2)
```

Now, let's play one per cycle:

```javascript
note("<c a f e>").piano().slow(2)
```

On top of that, put a copy of the sequence, offset in time and pitch:

```javascript
"<c a f e>".off(1/8, add(7))
  .note().piano().slow(2)
```

Add some structure to the original sequence:

```javascript
"<c*2 a(3,8) f(3,8,2) e*2>"
  .off(1/8, add(7))
  .note().piano().slow(2)
```

Reverse in one speaker:

```javascript
"<c*2 a(3,8) f(3,8,2) e*2>"
  .off(1/8, add(7))
  .note().piano()
  .jux(rev).slow(2)
```

Let's add another layer:

```javascript
"<c*2 a(3,8) f(3,8,2) e*2>"
  .off(1/8, add(7))
  .off(1/8, add(12))
  .note().piano()
  .jux(rev).slow(2)
```

- added slow(2) to approximate tidals cps
- n was replaced with note, because using n does not work as note for samples
- legato 2 was removed because it does not work in combination with rev (bug)

## Arpeggios from chords

TODO

---

## Microrhythms

# Microrhythms

see https://strudel.cc/?zMEo5kowGrFc

# Microrhythms

Inspired by this [Mini-Lecture on Microrhythm Notation](https://www.youtube.com/watch?v=or7B6vI3jOo), let's look at how we can express microrhythms with Strudel.

The timestamps of the first rhythm are `0 1/5 1/2 2/3 1`. We could naively express this with a stack:



While this works, it has two problems:

- it is not very compact
- the durations are wrong, e.g. the first note takes up the whole cycle

In the video, the duration of a timestamp is calculated by subtracting it from the next timestamp:

- 1/5 - 0 = 1/5 = 6/30
- 1/2 - 1/5 = 3/10 = 9/30
- 2/3 - 1/2 = 1/6 = 5/30
- 1 - 2/3 = 1/3 = 10/30

Using those, we can now express the rhythm much shorter:



The problems of the first notation are now fixed: it is much shorter and the durations are correct.
Still, this notation involved calculating the durations by hand, which could be automated:

```javascript
Pattern.prototype.micro = function (...timestamps) {
  const durations = timestamps.map((x, i, a) => {
    const next = i < a.length-1 ? a[i+1] : 1;
    return next - a[i]
  })
  return this.struct(timeCat(...durations.map(d => [d, 1]))).late(timestamps[0])
}
s('hh').micro(0, 1/5, 1/2, 2/3)
```

This notation is even shorter and it allows directly filling in the timestamps!

This is the second example of the video:

```javascript
Pattern.prototype.micro = function (...timestamps) {
  const durations = timestamps.map((x, i, a) => {
    const next = i < a.length-1 ? a[i+1] : 1;
    return next - a[i]
  })
  return this.struct(timeCat(...durations.map(d => [d, 1]))).late(timestamps[0])
}
s('hh').micro(0, 1/6, 2/5, 2/3, 3/4)
```

with bass: https://strudel.cc/?sTglgJJCPIeY

---

## Recipes

# Recipes

This page shows possible ways to achieve common (or not so common) musical goals.
There are often many ways to do a thing and there is no right or wrong.
The fun part is that each representation will give you different impulses when improvising.

## Arpeggios

An arpeggio is when the notes of a chord are played in sequence.
We can either write the notes by hand:



...or use scales:



...or chord symbols:



...using off:



## Chopping Breaks

A sample can be looped and chopped like this:



This fits the break into 8 cycles + chops it in 16 pieces.
The chops are not audible yet, because we're not doing any manipulation.
Let's add randmized doubling + reversing:



If we want to specify the order of samples, we can replace `chop` with `slice`:

```javascript
samples('github:yaxu/clean-breaks')
s("amen/4").fit()
  .slice(8, "<0 1 2 3 4*2 5 6 [6 7]>*2")
  .cut(1).rarely(ply("2"))
```
*This example includes visual pattern representation*

If we use `splice` instead of `slice`, the speed adjusts to the duration of the event:

```javascript
samples('github:yaxu/clean-breaks')
s("amen")
  .splice(8, "<0 1 2 3 4*2 5 6 [6 7]>*2")
  .cut(1).rarely(ply("2"))
```
*This example includes visual pattern representation*

Note that we don't need `fit`, because `splice` will do that by itself.

## Filter Envelopes

Using `lpenv`, we can make the filter move:

```javascript
note("g1 bb1 <c2 eb2> d2")
  .s("sawtooth")
  .lpf(400).lpenv(4)
  .scope()
```

The type of envelope depends on the methods you're setting. Let's set `lpa`:

```javascript
note("g1 bb1 <c2 eb2> d2")
  .s("sawtooth").lpq(8)
  .lpf(400).lpa(.2).lpenv(4)
  .scope()
```

Now the filter is attacking, rather than decaying as before (decay is the default). We can also do both

```javascript
note("g1 bb1 <c2 eb2> d2")
  .s("sawtooth").lpq(8)
  .lpf(400).lpa(.1).lpd(.1).lpenv(4)
  .scope()
```

You can play around with `lpa` | `lpd` | `lps` | `lpd` to see what the filter envelope will do.

## Layering Sounds

We can layer sounds by separating them with ",":

```javascript
note("<g1 bb1 d2 f1>")
.s("sawtooth, square") // <------
.scope()
```

We can control the gain of individual sounds like this:

```javascript
note("<g1 bb1 d2 f1>")
.s("sawtooth, square:0:.5") // <--- "name:number:gain"
.scope()
```

For more control over each voice, we can use `layer`:

```javascript
note("<g1 bb1 d2 f1>").layer(
  x=>x.s("sawtooth").vib(4),
  x=>x.s("square").add(note(12))
).scope()
```

Here, we give the sawtooth a vibrato and the square is moved an octave up.
With `layer`, you can use any pattern method available on each voice, so sky is the limit..

## Oscillator Detune

We can fatten a sound by adding a detuned version to itself:

```javascript
note("<g1 bb1 d2 f1>")
.add(note("0,.1")) // <------ chorus
.s("sawtooth").scope()
```
*This example includes visual pattern representation*

Try out different values, or add another voice!

## Polyrhythms

Here is a simple example of a polyrhythm:



A polyrhythm is when 2 different tempos happen at the same time.

## Polymeter

This is a polymeter:

```javascript
s("<bd rim, hh hh oh>*4")
```
*This example includes visual pattern representation*

A polymeter is when 2 different bar lengths play at the same tempo.

## Phasing

This is a phasing:

```javascript
note("<C D G A Bb D C A G D Bb A>*[6,6.1]").piano()
```
*This example includes visual pattern representation*

Phasing happens when the same sequence plays at slightly different tempos.

## Running through samples

Using `run` with `n`, we can rush through a sample bank:



This works great with sample banks that contain similar sounds, like in this case different recordings of a tabla.
Often times, you'll hear the beginning of the phrase not where the pattern begins.
In this case, I hear the beginning at the third sample, which can be accounted for with `early`.



Let's add some randomness:



## Tape Warble

We can emulate a pitch warbling effect like this:

```javascript
note("<c4 bb f eb>*8")
.add(note(perlin.range(0,.5))) // <------ warble
.clip(2).s("gm_electric_guitar_clean")
```

## Sound Duration

There are a number of ways to change the sound duration. Using clip:

```javascript
note("f ab bb c")
.clip("<2 1 .5 .25>")
```

The value of clip is relative to the duration of each event.
We can also create overlaps using release:

```javascript
note("f ab bb c")
.release("<2 1 .5 .25>")
```

This will smoothly fade out each sound for the given number of seconds.
We could also make the notes shorter by using a decay envelope:

```javascript
note("f ab bb c")
.decay("<2 1 .5 .25>")
```

When using samples, we also have `.end` to cut relative to the sample length:

```javascript
s("oh*4").end("<1 .5 .25 .1>")
```

Compare that to clip:

```javascript
s("oh*4").clip("<1 .5 .25 .1>")
```

or decay:

```javascript
s("oh*4").decay("<1 .5 .25 .1>")
```

## Wavetable Synthesis

You can loop a sample with `loop` / `loopEnd`:

```javascript
note("<c eb g f>").s("bd").loop(1).loopEnd(.05).gain(.2)
```

This allows us to play the first 5% of the bass drum as a synth!
To simplify loading wavetables, any sample that starts with `wt_` will be looped automatically:



Running through different wavetables can also give interesting variations:



...adding a filter envelope + reverb:

---

## Rhythms

# Build Rhythms

Note:

- this has been (partly) translated from https://tidalcycles.org/docs/patternlib/howtos/buildrhythms
- this only sounds good with `samples('github:tidalcycles/dirt-samples')` in prebake

# Build Rhythms

This page will teach you how to get started writing rhythms using different techniques. It is a good way to learn Strudel in a more intuitive way.

## From a simple to a complex rhythm

Simple bass drum - snare:



Let's pick a different snare sample:



Now, we are going to change the rhythm:



And add some toms:



Start to transform, shift a quarter cycle every other cycle:



Pattern the shift amount:

```javascript
s("bd*2 [[~ lt] sd:3] lt:1 [ht mt*2]")
.every(2, early("<.25 .125 .5>")).slow(2)
```

Add some patterned effects:

```javascript
s("bd*2 [[~ lt] sd:3] lt:1 [ht mt*2]")
.every(2, early("<.25 .125 .5>"))
.shape("<0 .5 .3>")
.room(saw.range(0,.2).slow(4))
.slow(2)
```

More transformation:

```javascript
s("bd*2 [[~ lt] sd:3] lt:1 [ht mt*2]")
.every(2, early("<.25 .125 .5>"))
.shape("<0 .5 .3>")
.room(saw.range(0,.2).slow(4))
.jux(id, rev, x=>x.speed(2))
.slow(2)
```

## Another rhythmic construction

Let's start with a sequence:



We add a bit of flavour:

```javascript
n("0 <0 4> [2 0] [2 3]").s("feel").speed(1.5).slow(2)
```

Swap the samples round every other cycle:

TODO: implement `rot`

---

# Function Reference

## Intro

# Pattern Functions

Let's learn all about functions to create and modify patterns.
At the core of Strudel, everything is made of functions.

For example, everything you can do with the Mini-Notation can also be done with a function.
This Pattern in Mini Notation:



is equivalent to this Pattern without Mini Notation:



Similarly, there is an equivalent function for every aspect of the mini notation.

Which representation to use is a matter of context. As a rule of thumb, functions
are better suited in a larger context, while mini notation is more practical for individual rhythms.

## Limits of Mini Notation

While the Mini Notation is a powerful way to write rhythms concisely, it also has its limits. Take this example:



Here, we are using mini notation for the individual rhythms, while using the function `stack` to mix them.
While stack is also available as `,` in mini notation, we cannot use it here, because we have different types of sounds.

## Combining Patterns

You can freely mix JS patterns, mini patterns and values! For example, this pattern:



...is equivalent to:



... as well as:

```javascript
note("<[g3,b3,e4] [a3,c3,e4] [b3,d3,f#4] [b3,e4,g4]>")
```

While mini notation is almost always shorter, it only has a handful of modifiers: \* / ! @.
When using JS patterns, there is a lot more you can do.

Next, let's look at how you can [create patterns](/learn/factories)

---

## Value Modifiers

# Control Parameters

Besides functions that control time, we saw earlier that functions like `note` and `cutoff` control different parameters (short params) of an event.
Let's now look more closely at how these `param(eter) functions` work.

# Parameter Functions

A very powerful feature of tidal patterns is that each parameter can be controlled independently:

```javascript
note("c a f e")
.cutoff("<500 1000 2000 [4000 8000]>")
.gain(.8)
.s('sawtooth')
.log()
```

In this example, the parameters `note`, `cutoff`, `gain` and `s` are controlled independently by either patterns or plain values (numbers / text).
After pressing play, we can observe the time and parameter values of each event (hap) in the output created by `.log()`.

## Plain vs Parameterized Values

Patterns that are not wrapped inside a param function will contain unlabeled `plain values`:

```javascript
"<c e g>".log()
```

This will not generate any sound output, because Strudel could only guess which param is meant by these letters.

Now compare that to the version wrapped in `note`:

```javascript
note("<c e g>").log()
```

Now it is clear that these letters are meant to be played as notes.
Under the hood, the `note` function (as well as all other param functions)
will wrap each plain value in an object. If the note function did not exist, we would need to write:



This will have the same output, though it is rather unwieldy to read and write.

## Wrapping Parameter Functions

To avoid too much nesting, param functions can also be chained like this:



This is equivalent to `note(cat('c','e','g')).log()`.

You can use this with any function that declares a type (like `n`, `s`, `note`, `freq` etc), just make sure to leave the parens empty!

## Plain Value Modification

Patterns of plain values can be modified with any of the following operators:

```javascript
"50 60 70".add("<0 1 2>").log()
```

Here, the add function modifies the numbers on the left.
Again, there is no output because these numbers have no meaning without a param.

## Param Value Modification

To modify a parameter value, you can either:

- Use the operator on the plain value pattern, inside the param function:

  ```javascript
note("50 60 70".add("<0 1 2>")).room(.1).log()
```

- Similarly, use the operator on the plain value pattern and wrap it later:

  ```javascript
"50 60 70".add("<0 1 2>").note().room(.1).log()
```

- Specify which param should be modified inside the operator function:

  ```javascript
note("50 60 70").room(.1).add(note("<0 1 2>")).log()
```

Remember the execution of the chained functions goes from left to right.

# Operators

This group of functions allows to modify the value of events.

## add

##Pattern.add##

*Function documentation for `Pattern.add`*

## sub

##Pattern.sub##

*Function documentation for `Pattern.sub`*

## mul

##Pattern.mul##

*Function documentation for `Pattern.mul`*

## div

##Pattern.div##

*Function documentation for `Pattern.div`*

## round

##Pattern.round##

*Function documentation for `Pattern.round`*

## floor

##Pattern.floor##

*Function documentation for `Pattern.floor`*

## ceil

##Pattern.ceil##

*Function documentation for `Pattern.ceil`*

## range

##Pattern.range##

*Function documentation for `Pattern.range`*

## rangex

##Pattern.rangex##

*Function documentation for `Pattern.rangex`*

## range2

##Pattern.range2##

*Function documentation for `Pattern.range2`*

## ratio

##Pattern.ratio##

*Function documentation for `Pattern.ratio`*

## as

##as##

*Function documentation for `as`*

# Custom Parameters

You can also create your own parameters:



Multiple params can also be created in a more consice way, using `createParams`:



Note that these params will not do anything until you give them meaning in your custom output!

From modifying parameters we transition to the concept of [Signals](/learn/signals).

---

# Technical Details

## About

# Untitled

This section introduces you to Strudel in a technical sense. If you just want to _use_ Strudel, have a look at the [Tutorial](/workshop/getting-started).

TODO

---

## Alignment

# Pattern Aligment & Combination

One core aspect of Strudel, inherited from Tidal, is the flexible way that patterns can be combined, irrespective of their structure. Its declarative approach means a live coder does not have to think about the details of _how_ this is done, only _what_ is to be done.

As a simple example, consider two number patterns `"0 [1 2] 3"`, and `"10 20"`. The first has three contiguous steps of equal lengths, with the second step broken down into two substeps, giving four events in total. There are a very large number of ways in which the structure of these two patterns could be combined, but the default method in both Strudel and Tidal is to line up the cycles of the two patterns, and then take events from the first pattern and match them with those in the second pattern. Therefore, the following two lines are equivalent:

```js
'0 [1 2] 3'.add('10 20');
('10 [11 22] 23');
```

Where the events only partially overlap, they are treated as fragments
of the event in the first pattern. This is a little difficult to
conceptualise, but lets start by comparing the two patterns in the
following example:

```js
'0 1 2'.add('10 20');
('10 [11 21] 22');
```

They are similar to the previous example in that the number `1` is split in two, with its two halves added to `10` and `20` respectively. However, the `11` 'remembers' that it is a fragment of that original `1` event, and so is treated as having a duration of a third of a cycle, despite only being active for a sixth of a cycle. Likewise, the `21` is also a fragment of that original `1` event, but a fragment of its second half. Because the start of its event is missing, it wouldn't actually trigger a sound (unless it underwent further pattern transformations/combinations).

In practice, the effect of this default, implicit method for combining two patterns is that the second pattern is added _in_ to the first one, and indeed this can be made explicit:

```js
'0 1 2'.add.in('10 20');
```

This makes way for other ways to align the pattern, and several are already defined, in particular:

- `in` - as explained above, aligns cycles, and applies values from the pattern on the right _in_ to the pattern on the left.
- `out` - as with `in`, but values are applied _out_ of the pattern on the left (i.e. _in_ to the one on the right).
- `mix` - structures from both patterns are combined, so that the new events are not fragments but are created at intersections of events from both sides.
- `squeeze` - cycles from the pattern on the right are squeezed into events on the left. So that e.g. `"0 1 2".add.squeeze("10 20")` is equivalent to `"[10 20] [11 21] [12 22]"`.
- `squeezeout` - as with `squeeze`, but cycles from the left are squeezed into events on the right. So, `"0 1 2".add.squeezeout("10 20")` is equivalent to `[10 11 12] [20 21 22]`.
- `reset` is similar to `squeezeout` in that cycles from the right are aligned with events on the left. However those cycles are not 'squeezed', rather they are truncated to fit the event. So `"0 1 2 3 4 5 6 7".add.reset("10 [20 30]")` would be equivalent to `10 11 12 13 20 21 30 31`. In effect, events on the right 'reset' cycles on the left.
- `restart` is similar to `reset`, but the pattern is 'restarted' from its very first cycle, rather than from the current cycle. `reset` and `restart` therefore only give different results where the leftmost pattern differs from one cycle to the next.

We will save going deeper into the background, design and practicalities of these alignment functions for future publications. However in the next section, we take them as a case study for looking at the different design affordances offered by Haskell to Tidal, and JavaScript to Strudel.

Ok, so how do Strudel and Tidal [compare](/learn/strudel-vs-tidal)?

---

## Docs

# Docs

The docs page is built ontop of astro's [docs site](https://github.com/withastro/astro/tree/main/examples/docs).

## Adding a new Docs Page

1. add a `.mdx` file in a path under `website/src/pages/`, e.g. [website/src/pages/learn/code.mdx](https://codeberg.org/uzu/strudel/src/branch/main/website/src/pages/learn/code.mdx) will be available under https://strudel.cc/learn/code/ (or locally under `http://localhost:4321/learn/code/`)
2. make sure to copy the top part of another existing docs page. Adjust the title accordingly
3. To add a link to the sidebar, add a new entry to `SIDEBAR` to [`config.ts`](https://codeberg.org/uzu/strudel/src/branch/main/website/src/config.ts)

## Using the Mini REPL

To add a Mini REPL, make sure to import:

```js

```

add a mini repl with

```jsx

```

- `client:idle` is required to tell astro that the repl should be interactive, see [Client Directive](https://docs.astro.build/en/reference/directives-reference/#client-directives)
- `tune`: be any valid pattern code
- `punchcard`: if added, a punchcard / pianoroll visualization is renderd
- `drawTime`: time window for drawing, defaults to `[0, 4]`
- `canvasHeight`: height of the canvas, defaults to 100px

See `mini-notation.mdx` for usage examples

## In-Source Documentation

You can add the in-source documentation for a function by using the `JsDoc` component. Import:

```js

```

Usage:

```jsx
##bandf##

*Function documentation for `bandf`*
```

- `name`: function name, as named with `@name` in jsdoc
- `h`: level of heading. `0` will hide the heading. Hiding it allows using a manual heading which results in a nav link being generated in the right sidebar.
- `hideDescription`: if set, the description will be hidden

### Writing jsdoc

Documentation is written with [jsdoc](https://jsdoc.app/) comments. Example:

```js
/**
 * Select a sound / sample by name.
 *
 * @name s
 * @param {string | Pattern} sound The sound / pattern of sounds to pick
 * @example
 * s("bd hh")
 *
 */
// implementation of s function
```

- Before each build, these comments will be rendered into `doc.json` using [jsdoc-json](https://www.npmjs.com/package/jsdoc-json) as a template
- To regenerate the `doc.json` file manually, run `npm run jsdoc-json`
- The file is used by the `JsDoc` component to find the documentation by name
- Also, it is used for the `examples.test.mjs` snapshot test

How does Strudel do its [Testing](/technical-manual/testing)?

---

## Internals

# Internal Functions

These functions are more low level, probably not needed by the live coder.

# Haskell-style functor, applicative and monadic operations

## withValue

##Pattern#withValue##

*Function documentation for `Pattern#withValue`*

## appWhole

##Pattern#appWhole##

*Function documentation for `Pattern#appWhole`*

## appBoth

##Pattern#appBoth##

*Function documentation for `Pattern#appBoth`*

## appLeft

##Pattern#appLeft##

*Function documentation for `Pattern#appLeft`*

## appRight

##Pattern#appRight##

*Function documentation for `Pattern#appRight`*

## bindWhole

##Pattern#bindWhole##

*Function documentation for `Pattern#bindWhole`*

## bind

##Pattern#bind##

*Function documentation for `Pattern#bind`*

## join

##Pattern#join##

*Function documentation for `Pattern#join`*

## outerBind

##Pattern#outerBind##

*Function documentation for `Pattern#outerBind`*

## outerJoin

##Pattern#outerJoin##

*Function documentation for `Pattern#outerJoin`*

## innerBind

##Pattern#innerBind##

*Function documentation for `Pattern#innerBind`*

## innerJoin

##Pattern#innerJoin##

*Function documentation for `Pattern#innerJoin`*

## resetJoin

##Pattern#resetJoin##

*Function documentation for `Pattern#resetJoin`*

## restartJoin

##Pattern#restartJoin##

*Function documentation for `Pattern#restartJoin`*

## squeezeJoin

##Pattern#squeezeJoin##

*Function documentation for `Pattern#squeezeJoin`*

## squeezeBind

##Pattern#squeezeBind##

*Function documentation for `Pattern#squeezeBind`*

# Utility methods mainly for internal use

## queryArc

##Pattern#queryArc##

*Function documentation for `Pattern#queryArc`*

## splitQueries

##Pattern#splitQueries##

*Function documentation for `Pattern#splitQueries`*

## withQuerySpan

##Pattern#withQuerySpan##

*Function documentation for `Pattern#withQuerySpan`*

## withQuerySpanMaybe

##Pattern#withQuerySpanMaybe##

*Function documentation for `Pattern#withQuerySpanMaybe`*

## withQueryTime

##Pattern#withQueryTime##

*Function documentation for `Pattern#withQueryTime`*

## withHapSpan

##Pattern#withHapSpan##

*Function documentation for `Pattern#withHapSpan`*

## withHapTime

##Pattern#withHapTime##

*Function documentation for `Pattern#withHapTime`*

## withHaps

##Pattern#withHaps##

*Function documentation for `Pattern#withHaps`*

## withHap

##Pattern#withHap##

*Function documentation for `Pattern#withHap`*

## setContext

##Pattern#setContext##

*Function documentation for `Pattern#setContext`*

## withContext

##Pattern#setContext##

*Function documentation for `Pattern#setContext`*

## stripContext

##Pattern#stripContext##

*Function documentation for `Pattern#stripContext`*

## withLoc

##Pattern#withLoc##

*Function documentation for `Pattern#withLoc`*

## filterHaps

##Pattern#filterHaps##

*Function documentation for `Pattern#filterHaps`*

## filterValues

##Pattern#filterValues##

*Function documentation for `Pattern#filterValues`*

## removeUndefineds

##Pattern#filterValues##

*Function documentation for `Pattern#filterValues`*

## onsetsOnly

##Pattern#onsetsOnly##

*Function documentation for `Pattern#onsetsOnly`*

## discreteOnly

##Pattern#discreteOnly##

*Function documentation for `Pattern#discreteOnly`*

## defragmentHaps

##Pattern#defragmentHaps##

*Function documentation for `Pattern#defragmentHaps`*

## firstCycle

##Pattern#firstCycle##

*Function documentation for `Pattern#firstCycle`*

## firstCycleValues

##Pattern#firstCycleValues##

*Function documentation for `Pattern#firstCycleValues`*

## showFirstCycle

##Pattern#showFirstCycle##

*Function documentation for `Pattern#showFirstCycle`*

## sortHapsByPart

##Pattern#sortHapsByPart##

*Function documentation for `Pattern#sortHapsByPart`*

## asNumber

##Pattern#sortHapsByPart##

*Function documentation for `Pattern#sortHapsByPart`*

# Operators

- \_opIn
- \_opOut
- \_opMix
- \_opSqueeze
- \_opSqueezeOut
- \_opTrig
- \_opTrigzero

# Other

## onTrigger

##Pattern#onTrigger##

*Function documentation for `Pattern#onTrigger`*

## log

##Pattern#log##

*Function documentation for `Pattern#log`*

## logValues

##Pattern#logValues##

*Function documentation for `Pattern#logValues`*

## drawLine

##Pattern#drawLine##

*Function documentation for `Pattern#drawLine`*

## collect

# Functions

## groupHapsBy

##groupHapsBy##

*Function documentation for `groupHapsBy`*

## pure

##pure##

*Function documentation for `pure`*

## reify

##reify##

*Function documentation for `reify`*

## slowcatPrime

##slowcatPrime##

*Function documentation for `slowcatPrime`*

## isPattern

##isPattern##

*Function documentation for `isPattern`*

## register

##register##

*Function documentation for `register`*

## toBipolar

##toBipolar##

*Function documentation for `toBipolar`*

## fromBipolar

##fromBipolar##

*Function documentation for `fromBipolar`*

## compressSpan

##compressSpan##

*Function documentation for `compressSpan`*

## focus

##focus##

*Function documentation for `focus`*

## focusSpan

## \_composeOp

# Composers

```
set keep keepif add sub mul div mod pow band bor bxor blshift brshift lt gt lte gte eq eqt ne net and or func
```

```
In Out Mix Squeeze SqueezeOut Trig Trigzero
```

---

## Packages

# Strudel Packages

The [strudel repo](https://codeberg.org/uzu/strudel) is organized as a monorepo, containing multiple npm packages.
The purpose of the multiple packages is to

- organize the codebase into more modular, encapsulated pieces
- be able to opt out of certain functionalities
- keep the dependencies of the core packages small

## Overview

[See the latest published packages on npm](https://www.npmjs.com/search?q=%40strudel).
Here is an overview of all the packages:

### Umbrella Packages

These packages give you a batteries-included point of getting started, and most likely the thing you'd want to use in your project:

- [repl](https://codeberg.org/uzu/strudel/src/branch/main/packages/repl): The Strudel REPL as a web component.
- [web](https://codeberg.org/uzu/strudel/src/branch/main/packages/web): Strudel library for the browser, without UI.

To find out more about these two, read [Using Strudel in Your Project](/technical-manual/project-start)

### Essential Packages

These package are the most essential. You might want to use all of those if you're using strudel in your project:

- [core](https://codeberg.org/uzu/strudel/src/branch/main/packages/core#strudelcore): tidal pattern engine with core primitives
- [mini](https://codeberg.org/uzu/strudel/src/branch/main/packages/mini#strudelmini): mini notation parser + core bindings
- [transpiler](https://codeberg.org/uzu/strudel/src/branch/main/packages/transpiler#strudeltranspiler): user code transpiler. syntax sugar + highlighting

### Language Extensions

These packages extend the pattern language by specific functions

- [tonal](https://codeberg.org/uzu/strudel/src/branch/main/packages/tonal): tonal functions for scales and chords
- [xen](https://codeberg.org/uzu/strudel/src/branch/main/packages/xen): microtonal / xenharmonic functions

### Outputs

These packages provide bindings for different ways to output strudel patterns:

- [webaudio](https://codeberg.org/uzu/strudel/src/branch/main/packages/webaudio#strudelwebaudio): the default webaudio output
- [osc](https://codeberg.org/uzu/strudel/src/branch/main/packages/osc#strudelosc): bindings to communicate via OSC
- [midi](https://codeberg.org/uzu/strudel/src/branch/main/packages/midi#strudelmidi): webmidi bindings
- [csound](https://codeberg.org/uzu/strudel/src/branch/main/packages/csound#strudelcsound): csound bindings
- [soundfonts](https://codeberg.org/uzu/strudel/src/branch/main/packages/serial#strudelsoundfonts): Soundfont support
- [serial](https://codeberg.org/uzu/strudel/src/branch/main/packages/serial#strudelserial): webserial bindings

### Others

- [embed](https://codeberg.org/uzu/strudel/src/branch/main/packages/embed#strudelembed): embeddable REPL web component

### No Longer Maintained

- [react](https://www.npmjs.com/package/@strudel.cycles/react): react hooks and components for strudel
- [eval](https://www.npmjs.com/package/@strudel.cycles/eval): old code transpiler
- [tone](https://www.npmjs.com/package/@strudel.cycles/tone): bindings for Tone.js instruments and effects
- [webdirt](https://www.npmjs.com/package/@strudel.cycles/webdirt): webdirt bindings, replaced by webaudio package
- any `@strudel.cycles/*` packages have been renamed to `@strudel/*` since version 0.10.0.

## Tools

- [pnpm](https://pnpm.io/) for package management, workspaces and publishing
- [lerna](https://lerna.js.org/) for bumping versions
- see CONTRIBUTING.md for more info

---

## Patterns

# Patterns

Patterns are the essence of Tidal. Its patterns are abstract entities that represent flows of time as functions, adapting a technique called pure functional reactive programming. Taking a time span as its input, a Pattern can output a set of events that happen within that time span. It depends on the structure of the Pattern how the events are located in time.
From now on, this process of generating events from a time span will be called **querying**.
Example:

```javascript
const pattern = sequence("c3", ["e3", "g3"])
const events = pattern.queryArc(0, 1)
console.log(events.map((e) => e.show()))
silence
```

In this example, we create a pattern using the `sequence` function and **query** it for the time span from `0` to `1`.
Those numbers represent units of time called **cycles**. The length of one cycle depends on the tempo, which defaults to one cycle per second.
The resulting events are:

```js
[
  '[ 0/1 -> 1/2 | c3 ]', //
  '[ 1/2 -> 3/4 | e3 ]',
  '[ 3/4 -> 1/1 | g3 ]',
];
```

Each event has a value, a begin time and an end time, where time is represented as a fraction. In the above case, the events are placed in sequential order, where c3 takes the first half, and e3 and g3 together take the second half. This temporal placement is the result of the `sequence` function, which divides its arguments equally over one cycle. If an argument is an array, the same rule applies to that part of the cycle. In the example, e3 and g3 are divided equally over the second half of the whole cycle.

Note that the query function is not just a way to access a pattern, but true to the principles of functional programming, is the pattern itself. This means that in theory there is no way to change a pattern, it is opaque as a pure function. In practice though, Strudel and Tidal are all about transforming patterns, so how is this done? The answer is, by replacing the pattern with a new one, that calls the old one. This new one is only able to manipulate the query before passing it to the old pattern, and manipulate the results from it before returning them to caller. But, this is enough to support all the temporal and structural manipulations provided by Strudel (and Tidal's) extensive library of functions.

The above examples do not represent how Strudel is used in practice. In the live coding editor, the user only has to type in the pattern itself, the querying will be handled by the scheduler. The scheduler will repeatedly query the pattern for events, which are then scheduled as sound synthesis or other event triggers.

Can we [align](/technical-manual/alignment) patterns?

---

## Project Start

# Using Strudel in your Project

This Guide shows you the different ways to get started with using Strudel in your own project.

## Embedding the Strudel REPL

There are 3 quick ways to embed strudel in your website:

1. Embed the strudel website as an iframe directly
2. Embed the strudel website as an iframe using `@strudel/embed`
3. Embed the REPL directly using `@strudel/repl`

### Inside an iframe

Using an iframe is the most easy way to embed a studel tune.
You can embed any pattern of your choice via an iframe and the URL of the pattern of your choice:

```html
<iframe src="https://strudel.cc/?xwWRfuCE8TAR" width="600" height="300"></iframe>
```

The URL can be obtained by pressing `share` in the REPL.
Note that these share links depend on a database, which is not guaranteed to live forever.
To make sure your code is not lost, you can also use the long url:

```html
<iframe
  src="https://strudel.cc/#c2V0Y3BzKDEpCm4oIjwwIDEgMiAzIDQ%2BKjgiKS5zY2FsZSgnRzQgbWlub3InKQoucygiZ21fbGVhZF82X3ZvaWNlIikKLmNsaXAoc2luZS5yYW5nZSguMiwuOCkuc2xvdyg4KSkKLmp1eChyZXYpCi5yb29tKDIpCi5zb21ldGltZXMoYWRkKG5vdGUoIjEyIikpKQoubHBmKHBlcmxpbi5yYW5nZSgyMDAsMjAwMDApLnNsb3coNCkp"
  width="600"
  height="300"
></iframe>
```

That long URL can just be copy pasted from the URL bar when you're on the strudel website. It always reflects the latest evaluation of your code.

### @strudel/embed

To simplify the process of emebdding via an iframe, you can use the package `@strudel/embed`:

```html
<script src="https://unpkg.com/@strudel/embed@latest"></script>
<strudel-repl>
  
</strudel-repl>
```

This will load the strudel website in an iframe, using the code provided within the HTML comments ``.
The HTML comments are needed to make sure the browser won't interpret it as HTML.

For alternative ways to load this package, see the [@strudel/embed README](https://codeberg.org/uzu/strudel/src/branch/main/packages/embed#strudel-embed).

### @strudel/repl

Loading strudel directly in your site, without an iframe, looks similar to the iframe variant:

```html
<script src="https://unpkg.com/@strudel/repl@latest"></script>
<strudel-editor>
  
</strudel-editor>
```

Here, we're loading `@strudel/repl` instead of `@strudel/embed`, and the component is called `strudel-editor` instead of `strudel-repl`.
Yes the naming is a bit confusing..

The upside of using the repl without an iframe is that you can pin the strudel version you're using:

```html
<script src="https://unpkg.com/@strudel/repl@1.0.2"></script>
<strudel-editor>
  
</strudel-editor>
```

This will guarantee your pattern wont break due to changes to the strudel project in the future.

For more info on this package, see the [@strudel/repl README](https://codeberg.org/uzu/strudel/src/branch/main/packages/repl#strudel-repl).

## With your own UI

The above approach assumes you want to use the builtin [codemirror](https://codemirror.net/) editor.
If you'd rather use your own UI, you can use the `@strudel/web` package:

```html
<!doctype html>
<script src="https://unpkg.com/@strudel/web@1.0.3"></script>
<button id="play">play</button>
<button id="stop">stop</button>
<script>
  initStrudel();
  document.getElementById('play').addEventListener('click', () => note('<c a f e>(3,8)').jux(rev).play());
  document.getElementById('stop').addEventListener('click', () => hush());
</script>
```

For more info on this package, see the [@strudel/web README]https://codeberg.org/uzu/strudel/src/branch/main/packages/web#strudel-web).

## Via npm

[All the packages and many more are available on npm under the @strudel namespace](https://www.npmjs.com/search?q=%40strudel).
There are actually many more packages you can use to have fine grained control over what you use and what not.
To use these packages, you have to use a bundler that supports es modules, like [vite](https://vitejs.dev/).

To find out more about the purpose of each package, see [Packages](/technical-manual/packages)

---

## Repl

# REPL

{/* The [REPL](https://strudel.cc/) is the place where all packages come together to form a live coding system. It can also be seen as a reference implementation for users of the library. */}

While Strudel can be used as a library in any JavaScript codebase, its main, reference user interface is the Strudel REPL^[REPL stands for read, evaluate, print/play, loop. It is friendly jargon for an interactive programming interface from computing heritage, usually for a commandline interface but also applied to live coding editors.], which is a browser-based live coding environment. This live code editor is dedicated to manipulating Strudel patterns while they play. The REPL features built-in visual feedback, highlighting which elements in the patterned (mini-notation) sequences are influencing the event that is currently being played. This feedback is designed to support both learning and live use of Strudel.

Besides a UI for playback control and meta information, the main part of the REPL interface is the code editor powered by CodeMirror. In it, the user can edit and evaluate pattern code live, using one of the available synthesis outputs to create music and/or sound art. The control flow of the REPL follows 3 basic steps:

1. The user writes and updates code. Each update transpiles and evaluates it to create a `Pattern` instance
2. While the REPL is running, the `Scheduler` queries the active `Pattern` by a regular interval, generating `Events` (also known as `Haps` in Strudel) for the next time span.
3. For each scheduling tick, all generated `Events` are triggered by calling their `onTrigger` method, which is set by the output.

<img src="https://codeberg.org/uzu/strudel/raw/branch/talk/talk/public/strudelflow.png" width="600" />

## User Code

To create a `Pattern` from the user code, two steps are needed:

1. Transpile the JS input code to make it functional
2. Evaluate the transpiled code

### Transpilation & Evaluation

In the JavaScript world, using transpilation is a common practise to be able to use language features that are not supported by the base language. Tools like `babel` will transpile code that contains unsupported language features into a version of the code without those features.

In the same tradition, Strudel can add a transpilation step to simplify the user code in the context of live coding. For example, the Strudel REPL lets the user create mini-notation patterns using just double quoted strings, while single quoted strings remain what they are:

```strudel
note("c3 [e3 g3]*2")
```

is transpiled to:

```strudel
note(m('c3 [e3 g3]', 5))
```

Here, the string is wrapped in `m`, which will create a pattern from a mini-notation string. As the second parameter, it gets passed source code location of the string, which enables highlighting active events later.

After the transpilation, the code is ready to be evaluated into a `Pattern`.

Behind the scenes, the user code string is parsed with `acorn`, turning it into an Abstract Syntax Tree (AST). The AST allows changing the structure of the code before generating the transpiled version using `escodegen`.

### Mini-notation

While the transpilation allows JavaScript to express Patterns in a less verbose way, it is still preferable to use the mini-notation as a more compact way to express rhythm. Strudel aims to provide the same mini-notation features and syntax as used in Tidal.

The mini-notation parser is implemented using `peggy`, which allows generating performant parsers for Domain Specific Languages (DSLs) using a concise grammar notation. The generated parser turns the mini-notation string into an AST which is used to call the respective Strudel functions with the given structure. For example, `"c3 [e3 g3]*2"` will result in the following calls:

```strudel
seq(
  reify('c3').withLoc(6, 9),
  seq(reify('e3').withLoc(10, 12), reify('g3',).withLoc(13, 15))
)
```

### Highlighting Locations

As seen in the examples above, both the mini-notation parser adds the source code locations using `withLoc`.
This location is calculated inside the `m` function, as the sum of 2 locations:

1. the location where the mini notation string begins, as obtained from the JS parser
2. the location of the substring inside the mini notation, as obtained from the mini notation parser

The sum of both is passed to `withLoc` to tell each element its location, which can be later used for highlighting when it's active.

### Mini Notation

Another important part of the user code is the mini notation, which allows to express rhythms in a short manner.

- the mini notation is [implemented as a PEG grammar](https://codeberg.org/uzu/strudel/src/branch/talk/packages/mini/krill.pegjs), living in the [mini package](https://codeberg.org/uzu/strudel/src/branch/main/packages/mini)
- it is based on [krill](https://github.com/Mdashdotdashn/krill) by Mdashdotdashn
- the peg grammar is used to generate a parser with [peggyjs](https://peggyjs.org/)
- the generated parser takes a mini notation string and outputs an AST
- the AST can then be used to construct a pattern using the regular Strudel API

Here's an example AST for `c3 [e3 g3]`

```json
{
  "type_": "pattern",
  "arguments_": { "alignment": "h" },
  "source_": [
    {
      "type_": "element", "source_": "c3",
      "location_": { "start": { "offset": 1, "line": 1, "column": 2 }, "end": { "offset": 4, "line": 1, "column": 5 } }
    },
    {
      "type_": "element",
      "location_": { "start": { "offset": 4, "line": 1, "column": 5 }, "end": { "offset": 11, "line": 1, "column": 12 } }
      "source_": {
        "type_": "pattern", "arguments_": { "alignment": "h" },
        "source_": [
          {
            "type_": "element", "source_": "e3",
            "location_": { "start": { "offset": 5, "line": 1, "column": 6 }, "end": { "offset": 8, "line": 1, "column": 9 } }
          },
          {
            "type_": "element", "source_": "g3",
            "location_": { "start": { "offset": 8, "line": 1, "column": 9 }, "end": { "offset": 10, "line": 1, "column": 11 } }
          }
        ]
      },
    }
  ]
}
```

which translates to `seq(c3, seq(e3, g3))`

## Scheduling Events

After an instance of `Pattern` is obtained from the user code,
it is used by the scheduler to get queried for events. Once started, the scheduler runs at a fixed interval to query the active pattern for events within the current interval's time span. A simplified implementation looks like this:

```js
let pattern = seq('c3', ['e3', 'g3']); // pattern from user
let interval = 0.5; // query interval in seconds
let time = 0; // beginning of current time span
let minLatency = 0.1; // min time before a hap should trigger
setInterval(() => {
  const haps = pattern.queryArc(time, time + interval);
  time += interval; // increment time
  haps.forEach((hap) => {
    const deadline = hap.whole.begin - time + minLatency;
    onTrigger(hap, deadline, duration);
  });
}, interval * 1000); // query each "interval" seconds
```

Note that the above code is simplified for illustrative purposes. The actual implementation has to work around imprecise callbacks of `setInterval`. More about the implementation details can be read in [this blog post](https://loophole-letters.vercel.app/web-audio-scheduling).

The fact that `Pattern.queryArc` is a pure function that maps a time span to a set of events allows us to choose any interval we like without changing the resulting output. It also means that when the pattern is changed from outside, the next scheduling callback will work with the new pattern, keeping its clock running.

The latency between the time the pattern is evaluated and the change is heard is between `minLatency` and `interval + minLatency`, in our example between 100ms and 600ms. In Strudel, the current query interval is 50ms with a minLatency of 100ms, meaning the latency is between 50ms and 150ms.

## Output

The last step is to trigger each event in the chosen output.
This is where the given time and value of each event is used to generate audio or any other form of time based output. The default output of the Strudel REPL is the WebAudio output. To understand what an output does, we first have to understand what control parameters are.

### Control Parameters

To be able to manipulate multiple aspects of sound in parallel, so called control parameters are used to shape the value of each event. Example:

```js
note('c3 e3')
  .cutoff(1000)
  .s('sawtooth')
  .queryArc(0, 1)
  .map((hap) => hap.value);
/* [
  { note: 'c3', cutoff: 1000, s: 'sawtooth' }
  { note: 'e3', cutoff: 1000, s: 'sawtooth' }
] */
```

Here, the control parameter functions `note`, `cutoff` and `s` are used, where each controls a different property in the value object. Each control parameter function accepts a primitive value, a list of values to be sequenced into a `Pattern`, or a `Pattern`. In the example, `note` gets a `Pattern` from a mini-notation expression (double quoted), while `cutoff` and `s` are given a `Number` and a (single quoted) `String` respectively.

Strudel comes with a large default set of control parameter functions that are based on the ones used by Tidal and SuperDirt, focusing on music and audio terminology. It is however possible to create custom control parameters for any purpose:

```js
const { x, y } = createParams('x', 'y');
x(sine.range(0, 200)).y(cosine.range(0, 200));
```

This example creates the custom control parameters `x` and `y` which are then used to form a pattern that descibes the coordinates of a circle.

### Outputs

Now that we know how the value of an event is manipulated using control parameters, we can look at how outputs can use that value to generate anything. The scheduler above was calling the `onTrigger` function which is used to implement the output. A very simple version of the web audio output could look like this:

```js
function onTrigger(hap, deadline, duration) {
  const { note } = hap.value;
  const time = getAudioContext().currentTime + deadline;
  const o = getAudioContext().createOscillator();
  o.frequency.value = getFreq(note);
  o.start(time);
  o.stop(time + event.duration);
  o.connect(getAudioContext().destination);
}
```

The above example will create an `OscillatorNode` for each event, where the frequency is controlled by the `note` param. In essence, this is how the WebAudio API output of Strudel works, only with many more parameters to control synths, samples and effects.

I want to help, how do I contribute to the [Docs](/technical-manual/docs)?

---

## Sounds

# Sounds

Let's take a closer look about how sounds are implemented in the webaudio output.

## Registering a sound

All sounds are registered in the sound map, using the the `registerSound` function:

```ts
function registerSound(
  name: string, // The name of the sound that should be given to `s`, e.g. `mysaw`
  // The function called by the scheduler to trigger the sound:
  (
    time: number, // The audio context time the sound should start
    value: object, // The value of the `Hap`
    onended: () => void // A callback that should be fired when the sound has ended
  ) => {
    node: AudioNode, // node to connect to rest of the effects chain
    stop: (time:number) => void // a function that will stop the sound
  },
  data: object // meta data, only for ui logic in sounds tab
);
```

When `registerSound` is called, it registers `{ onTrigger, data }` under the given `name` in a [nanostore map](https://github.com/nanostores/nanostores#maps).

### Example

This might be a bit abstract, so here is a minimal example:

```js
registerSound(
  'mysaw',
  (time, value, onended) => {
    let { freq } = value; // destructure control params
    const ctx = getAudioContext();
    // create oscillator
    const o = new OscillatorNode(ctx, { type: 'sawtooth', frequency: Number(freq) });
    o.start(time);
    // add gain node to level down osc
    const g = new GainNode(ctx, { gain: 0.3 });
    // connect osc to gain
    const node = o.connect(g);
    // this function can be called from outside to stop the sound
    const stop = (time) => o.stop(time);
    // ended will be fired when stop has been fired
    o.addEventListener('ended', () => {
      o.disconnect();
      g.disconnect();
      onended();
    });
    return { node, stop };
  },
  { type: 'synth' },
);
// use the sound
freq(220, 440, 330).s('mysaw');
```

You can actually use this code in the [REPL](https://strudel.cc/) and it'll work.
After evaluating the code, you should see `mysaw` in listed in the sounds tab.

## Playing sounds

Now here is what happens when a sound is played:
When the webaudio output plays a `Hap`, it will lookup and call the `onTrigger` function for the given `s`.
The returned `node` can then be connected to the rest of the standard effects chain
Having the stop function separate allows playing sounds via midi too, where you don't know how long the noteon will last

---

## Testing

# Testing

Strudel uses [vitest](https://vitest.dev/) for testing, with 2 types of testing strategies:

- unit tests for fine grained testing
- automated snapshot tests for broader testing

## Unit Tests

Each package has a `test` folder where tests are written on a file by file basis, e.g. `util.test.mjs` implements all tests for `util.mjs`.

## Snapshot Tests

Snapshot tests allow testing larger chunks of data. Strudel uses snapshot tests for:

- Example Snippets: `examples.test.mjs`, using snippets under `@example` inside jsdoc comments
- Example Tunes: `tunes.test.mjs`, using all patterns in `tunes.mjs`

The snapshot (`.snap`) files contain all haps within a certain number of cycles for each tested pattern.
They allow testing for breaking changes on a larger scale.
If breaking changes are intentional, the snapshots can be updated with `npm run snapshot`.
Just make sure to verify that all affected patterns behave as expected.

---

# Advanced Concepts

## Cycles

# Understanding Cycles

The concept of cycles is very central to be able to understand how Strudel works.
Strudel's mother language, TidalCycles, even has it in its name.

## Cycles and BPM

In most music software, the unit BPM (beats per minute) is used to set the tempo.
Strudel expresses tempo as CPS (cycles per second), with a default of 0.5 CPS:



Here we can hear the 0.5CPS in action: The kick repeats once every two seconds.
Let's make it 4 kicks:



Now we have 4 kicks per cycle, but the whole pattern still plays at 0.5CPS.
In terms of BPM, most musicians would tell you this is playing at 120bpm.
What about this one:



Because the second sound is now a hihat, the tempo feels slower again.
This brings us to an important realization:

Tempo is based on perception.
The choice of sounds also has an impact on the tempo feel.
This is why the same CPS can produce different perceived tempos.

## Setting CPM

If you're familiar with BPM, you can use the `setcpm` method to set the global tempo in cycles per minute:



If you want to add more beats per cycle, you might want to divide the cpm:



Or using 2 beats per cycle:



To set a specific bpm, use `setcpm(bpm/bpc)`

- bpm: the target beats per minute
- bpc: the number of perceived beats per cycle

## Cycles and Bars

Also in most music software, multiple beats form a bar (or measure).
The so called time signature specifies how many beats are in each bar.
In many types of music, it is common to use 4 beats per bar, also known as 4/4 time.
Many music programs use it as a default.

Strudel does not a have concept of bars or measures, there are only cycles.
How you use them is up to you. Above, we've had this example:



This could be interpreted as 4/4 time with a tempo of 110bpm.
We could write out multiple bars like this:

<MiniRepl
  client:visible
  tune={`setcpm(110/4)
s(\`<
[bd sd bd rim, hh*8] 
[bd sd bd rim*2, hh*8]
>\`)`}
/>

Instead of writing out each bar separately, we could express this much shorter:

```javascript
setcpm(110/2)
s("bd <sd rim*<1 2>>,hh*4")
```

Here we can see that thinking in cycles rather than bars simplifies things a lot!
These types of simplifications work because of the repetitive nature of rhythm.
In computational terms, you could say the former notation has a lot of redundancy.

## Time Signatures

To get a time signature, just change the number of elements per bar. Here is a rhythm with 7 beats:



or with 5:



We could also write multiple bars with different time signatures:

<MiniRepl
  client:visible
  tune={`setcpm(110*2)
s(\`<
[bd hh rim]@3
[bd hh rim sd]@4
>\`)`}
/>

Here we switch between 3/4 and 4/4, keeping the same tempo.

If we don't specify the length, we get what's called a metric modulation:

<MiniRepl
  client:visible
  tune={`setcpm(110/2)
s(\`<
[bd hh rim]
[bd hh rim sd]
>\`)`}
/>

Now the 3 elements get the same time as the 4 elements, which is why the tempo changes.

---

## Pitch

# Understanding Pitch

Let's learn how pitch works! The slider below controls the <span style="color:#3b82f6;">frequency</span> of an oscillator, producing a pitch:

{/*  */}

- Drag the slider to hear a pitch
- Move the slider to change the pitch
- Observe how the Hz number changes
- <span className="text-red-300">Caution</span>: The higher frequencies could be disturbing for children or animals!

The Hz number is the frequency of the pitch you're hearing.
The higher the frequency, the higher the pitch and vice versa.
A pitch occurs whenever something is vibrating / oscillating at a frequency, in this case it's your speaker.
The unit **Hz** describes how many times that oscillation happens per second.
Our eyes are too slow to actually see the oscillation on the speaker, but we can <a href="https://www.youtube.com/watch?v=CDMBWw7OuJQ" target="_blank">see it in slow motion</a>.

The hearing range of a newborn is said to be between 20Hz and 20000Hz.
The upper limit decreases with age. What's your upper limit?

In Strudel, we can play frequencies directly with the `freq` control:

```javascript
freq("<200 [300,500] 400 [500,<600 670 712 670>]>*8")
```

## Frequency vs Pitch Perception

Maybe you have already noticed that the <span style="color:#3b82f6;">frequency slider</span> is "lopsided",
meaning the pitch changes more in the left region and less in the right region.<br/>
To make that more obvious, let's add a <span style="color:#eab308">pitch slider</span>
that controls the frequency on a different scale:

Try out the buttons above to sweep through the frequency range in 2 different ways:

- Frequency Sweep: <span style="color:#3b82f6;">frequency rises linear</span> , <span style="color:#eab308">pitch rises logarithmic</span>
- Pitch Sweep: <span style="color:#3b82f6;">frequency rises exponential</span> , <span style="color:#eab308">pitch rises linear</span>

Don't be scared of these mathematical terms:

- "logarithmic" is just a fancy way of saying "it starts fast and slows down"
- "exponential" is just a fancy way of saying "it starts slow and gets faster"

Most of the time, we might want to control pitch in a way that matches our perception,
which is what the <span style="color:#eab308">pitch slider</span> does.

## From Hz to Semitones

Because Hz does not match our perception, let's try to find a unit for pitch that matches.
To approach that unit of pitch, let's look at how frequency behaves when it is doubled:

- Use the now stepped pitch slider above
- Can you hear how these pitches seem related to each other?

In musical terms, a pitch with double the frequency of another is an `octave` higher.

Because octaves are pretty far apart, octaves are typically divided into 12 smaller parts:

This step is also called a semitone, which is the most common division of pitched music.
For example, the keys on a piano keyboard are also divided into semitones.

In Strudel, we could do that with `freq` like this:

```javascript
freq(
  "0 4 7 12"
  .fmap(n => 440 * 2**(n/12))
)
```

Of course, this can be written shorter with note, as we will see below.

## From Semitones to MIDI numbers

Now we know what the distance of a semitone is.
Above, we used an arbitrary base frequency of 440Hz, which means the exponent 0 is equal to 440Hz.
Typically, 440Hz is standardized to the number 69, which leads to this calculation:

The yellow number is now a MIDI number, covering more than the whole human hearing range with numbers from 0 to 127.
In Strudel, we can use MIDI numbers inside `note`:



## From MIDI numbers to notes

In western music theory, notes are used instead of numbers.
For each midi number, there is at least one note label:

A full note label consists of a letter (A-G), 0 or more accidentals (b | #) and an octave number.
This system is also known as [Scientific Pitch Notation](https://en.wikipedia.org/wiki/Scientific_pitch_notation).
In Strudel, these note labels can also be used inside `note` as an alternative to midi numbers:



## Open Questions

Now that we have learned about different representations of pitch, there are still open questions:

- Why 12 notes? What about different divisions of the octave?
- Why are notes labeled as they are? Why only 7 letters?
- Are there other labeling systems?
- What about Just Intonation Systems?
- What about Timbre?

All those questions are important to ask and will be answered in another article.

## Definition

At first, I wanted to start this article with a definition, but then thought it might be a good idea to focus on intuitive exploration.
Maybe you now understand this definition much better:

From [wikipedia](<https://en.wikipedia.org/wiki/Pitch_(music)>): "Pitch is a perceptual property of sounds that allows their ordering on a frequency-related scale, or more commonly, pitch is the quality that makes it possible to judge sounds as "higher" and "lower" in the sense associated with musical melodies."

---

## Voicings

# Understanding Chords and Voicings

Let's dig deeper into how chords and voicings work in strudel.
I'll try to keep theory jargon to a minimum, so hopefully this is approachable for anyone interested.

## What is a chord

Playing more than one note at a time is generally called a `chord`. Here's an example:

```javascript
note("<[c3,eb3,g3] [f3,a3,c4]>").room(.5)
```

Here's the same with midi numbers:

```javascript
note("<[48,51,55] [53,57,60]>").room(.5)
```

Here, we have two 3-note chords played in a loop.
You could already stop here and write chords in this style, which is totally fine and gives you control over individual notes.
One downside is that it can be difficult to find good sounding chords and maybe you're yearning for a way to organize chords in some other way.

## Labeling Chords

Chords are typically given different labels depending on the relationship of the notes within.
In the number example above, we have `48,51,55` and `53,57,60`.

To analyze the relationship of those notes, they are typically compared to some `root`, which is often the lowest note.
In our case, the `roots` would be `48` (= `c3`) and `53` (= `f3`).
We can express the same chords relative to those `roots` like this:

```javascript
note("<[0,3,7] [0,4,7]>".add("<48 53>")).room(.5)
```

Now within each chord, each number represents the distance from the root.
A distance between pitches is typically called `interval`, but let's stick to distance for now.

Now we can see that our 2 chords are actually quite similar, as the only difference is the middle note (and the root of course).
They are part of a group of chords called `triads` which are chords with 3 notes.

### Triads

These 4 shapes are the most common types of `triads` you will encounter:

| shape | label      |
| ----- | ---------- |
| 0,4,7 | major      |
| 0,3,7 | minor      |
| 0,3,6 | diminished |
| 0,4,8 | augmented  |

Here they are in succession:

```javascript
note("<[0,4,7] [0,3,7] [0,3,6] [0,4,8]>".add("60"))
.room(.5)._pitchwheel()
```

Many types of music often only use minor and major chords, so we already have the knowledge to accompany songs. Here's one:

<MiniRepl
  client:visible
  tune={`
note(\`<
[0,3,7] [0,4,7] [0,4,7] [0,4,7]
[0,3,7] [0,4,7] [0,3,7] [0,4,7]
>\`.add(\`<
a c d f
a e a e
>\`)).room(.5)`}
/>

These are the chords for "The House of the Rising Sun" by The Animals.
So far, it doesn't sound too exciting, but at least it's recognizable.

## Voicings

A `voicing` is one of many ways a certain chord shape can be arranged.
The term comes from choral music, where chords can be sung in different ways by assigning different notes to each voice.
For example we could add 12 semitones to one or more notes in the chord:

```javascript
note("<[0,3,7] [12,3,7] [12,15,7] [12,15,19]>".add("48"))
.room(.5)
```

Notes that are 12 semitone steps apart (= 1 `octave`) are considered to be equal in a harmonic sense, which is why they get the same note letter.
Here's the same example with note letters:

```javascript
note("<[c3,eb3,g3] [c4,eb3,g3] [c4,eb4,g3] [c4,eb4,g4]>")
.room(.5)
```

These types of voicings are also called `inversions`. There are many other ways we could `voice` this minor chord:

```javascript
note("<[0,3,7,12] [0,15,24] [0,3,12]>".add("48"))
.room(.5)
```

Here we are changing the flavour of the chord slightly by

1. doubling notes 12 steps higher,
2. using very wide distances
3. omitting notes

## Voice Leading

When we want to meaningfully connect chords in a sequence, the chosen voicings affect the way each chord transitions to the next.
Let's revisit "The House of the Rising Sun", this time using our newly acquired voicing techniques:

<MiniRepl
  client:visible
  tune={`note(\`<
[0,3,7] [7,12,16] [0,7,16] [4,7,12]
[0,3,7] [4,7,12] [0,3,7] [4,7,12]
>\`.add(\`<
a c d f
a e a e
>\`)).room(.5)`}
  punchcard
/>

These voicings make the chords sound more connected and less jumpy, compared to the earlier version, which didn't focus on voicing.
The way chords interact is also called `voice leading`, reminiscent of how an
individual choir voice would move through a sequence of chords.

For example, try singing the top voice in the above example. Then try the same
on the example not focusing on voice leading. Which one's easier?

Naturally, there are many ways a progression of chords could be voiced and there is no definitive right or wrong.

## Chord Symbols

Musicians playing chord-based music often use a `lead sheet`, which is a simplified notation for a piece of music.
These sheets condense the essential elements, such as chords, into symbols that make the music easy to read and follow.
For example, a lead sheet for "The House of the Rising Sun" might include chords written like this:

```
Am | C | D  | F
Am | E | Am | E
```

Here, each symbol consists of the `root` of the chord and optionally an `m` to signal it's a minor chord (just the root note means it's major).
We could mirror that notation in strudel using the `pick` function:

```javascript
"<Am C D F Am E Am E>"
  .pick({
    Am: "57,60,64",
    C: "55,60,64",
    D: "50,57,66",
    F: "57,60,65",
    E: "56,59,64",
  })
  .note().room(.5)
```
*This example includes visual pattern representation*

## The voicing function

Coming up with good sounding voicings that connect well can be a difficult and time consuming process.
The `chord` and `voicing` functions can be used to automate that:

```javascript
chord("<Am C D F Am E Am E>").voicing().room(.5)
```
*This example includes visual pattern representation*

Here we're also using chord symbols but the voicings will be automatically generated with smooth `voice leading`, minimizing jumps.
It is inspired by the way a piano or guitar player would pick chords to accompany a song.

## Voicing Dictionaries

The voicing function internally uses so called `voicing dictionaries`, which can also be customized:

```javascript
addVoicings('house', {
  '': ['7 12 16', '0 7 16', '4 7 12'],
  'm': ['0 3 7']
})
chord("<Am C D F Am E Am E>")
  .dict('house').anchor(66)
  .voicing().room(.5)
```
*This example includes visual pattern representation*

In a `voicing dictionary`, each chord symbol is assigned one or more voicings.
The `voicing` function then picks the voicing that is closest to the `anchor` (defaults to `c5`).

The handy thing about this approach is that a `voicing dictionary` can be used to play any chord progression with automated voice leading!

## The default dictionary

When using the default dictionary, you can use these chord symbols:

```
2 5 6 7 9 11 13 69 add9
o h sus ^ - ^7 -7 7sus
h7 o7 ^9 ^13 ^7#11 ^9#11
^7#5 -6 -69 -^7 -^9 -9
-add9 -11 -7b5 h9 -b6 -#5
7b9 7#9 7#11 7b5 7#5 9#11
9b5 9#5 7b13 7#9#5 7#9b5
7#9#11 7b9#11 7b9b5 7b9#5
7b9#9 7b9b13 7alt 13#11
13b9 13#9 7b9sus 7susadd3
9sus 13sus 7b13sus
aug M m M7 m7 M9 M13
M7#11 M9#11 M7#5 m6 m69
m^7 -M7 m^9 -M9 m9 madd9
m11 m7b5 mb6 m#5 mM7 mM9
```

The available chords and the format is very much inspired by [ireal pro chords](https://technimo.helpshift.com/hc/en/3-ireal-pro/faq/88-chord-symbols-used-in-ireal-pro/).
Some symbols are synonymous:

- "-" is the same as "m", for example C-7 = Cm7
- "^" is the same as "M", for example C^7 = CM7
- "+" is the same as "aug"

You can decide which ones you prefer. There is no international standard for these symbols.
To get a full chord, the symbols have to be prefixed with a root pitch, e.g. D7#11 is the 7#11 chord relative to the pitch D.

Here are all possible chords with root C:

<MiniRepl
  client:visible
  tune={`chord(\`<
C2 C5 C6 C7 C9 C11 C13 C69
Cadd9 Co Ch Csus C^ C- C^7 
C-7 C7sus Ch7 Co7 C^9 C^13 
C^7#11 C^9#11 C^7#5 C-6 C-69 
C-^7 C-^9 C-9 C-add9 C-11 
C-7b5 Ch9 C-b6 C-#5 C7b9 
C7#9 C7#11 C7b5 C7#5 C9#11 
C9b5 C9#5 C7b13 C7#9#5 C7#9b5 
C7#9#11 C7b9#11 C7b9b5 C7b9#5 
C7b9#9 C7b9b13 C7alt C13#11 
C13b9 C13#9 C7b9sus C7susadd3 
C9sus C13sus C7b13sus C Caug 
CM Cm CM7 Cm7 CM9 CM13 CM7#11 
CM9#11 CM7#5 Cm6 Cm69 Cm^7 
C-M7 Cm^9 C-M9 Cm9 Cmadd9 
Cm11 Cm7b5 Cmb6 Cm#5
>\`).voicing().room(.5)`}
  punchcard
/>

Note that the default dictionary contains multiple ways (= `voicings`) to play each chord symbol.
By default, the `voicing` function tries to minimize jumps.
You can alter the picked voicings in various ways, which are now explained in further detail:

## anchor

The `anchor` is a note that is used to align the voicings to:

```javascript
anchor("<c4 g4 c5 g5>").chord("C").voicing().room(.5)
```
*This example includes visual pattern representation*

By default, the anchor is the highest possible note the voicing can contain.
When deciding which voicing of the dictionary to pick for a certain chord, the voicing with a top note closest to the anchor wins.

Note that the anchors in the above example match up with the top notes in the pianoroll.
Like `note`, anchor accepts either midi numbers or note names.

## mode

With `mode`, you can change the way the voicing relates to the `anchor`:

```javascript
mode("<below above duck root>").chord("C").anchor("c5").voicing().room(.5)
```
*This example includes visual pattern representation*

The modes are:

- `below`: the top note of the voicing is lower than or equal to the anchor (default)
- `above`: the bottom note of the voicing is higher than or equal to the anchor
- `duck`: the top note of the voicing is lower than the anchor
- `root`: the bottom note of the voicing is always the root note closest to the anchor

The `anchor` can also be set from within the `mode` function:

```javascript
mode("<below above duck root>:c5").chord("C").voicing().room(.5)
```
*This example includes visual pattern representation*

## n

The `n` control can be used with `voicing` to select individual notes:

```javascript
n("0 3 1 2").chord("<C <Fm Db>>").voicing()
.clip("4 3 2 1").room(.5)
```
*This example includes visual pattern representation*

## Example

Here's an example of a Jazz Blues in F:

<MiniRepl
  client:visible
  tune={`let chords = chord(\`<
F7 Bb7 F7 [Cm7 F7]
Bb7 Bo F7 [Am7 D7]
Gm7 C7 [F7 D7] [Gm7 C7]
>\`)
$: n("7 8 [10 9] 8").set(chords).voicing().dec(.2)
$: chords.struct("- x - x").voicing().room(.5)
$: n("0 - 1 -").set(chords).mode("root:g2").voicing()
`}
  punchcard
/>

The chords are reused for melody, chords and bassline of the tune.

---

