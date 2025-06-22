# Strudel Code Samples

This is a collection of all code samples found in the documentation.

## Sample 1 - from [recap](workshop/recap.md)

```javascript
note("c <e g>")
```

## Sample 2 - from [recap](workshop/recap.md)

```javascript
note("c2 c3").s("sawtooth").lpf("<400 2000>")
```

## Sample 3 - from [recap](workshop/recap.md)

```javascript
note("c3 eb3 g3").s("sawtooth").vowel("<a e i o>")
```

## Sample 4 - from [recap](workshop/recap.md)

```javascript
s("bd rim").speed("<1 2 -1 -2>")
```

## Sample 5 - from [recap](workshop/recap.md)

```javascript
n("0 2 4 6".add("<0 1 2 1>")).scale("C:minor")
```

## Sample 6 - from [recap](workshop/recap.md)

```javascript
s("bd sd").ply("<1 2 3>")
```

## Sample 7 - from [recap](workshop/recap.md)

```javascript
s("bd sd, hh*4").off(1/8, x=>x.speed(2))
```

## Sample 8 - from [getting-started](workshop/getting-started.md)

```javascript
stack(
  // drums
  s("bd,[~ <sd!3 sd(3,4,2)>],hh*8")
  .speed(perlin.range(.8,.9)), // random sample speed variation
  // bassline
  "<a1 b1\*2 a1(3,8) e2>" 
  .off(1/8,x=>x.add(12).degradeBy(.5)) // random octave jumps
  .add(perlin.range(0,.5)) // random pitch variation
  .superimpose(add(.05)) // add second, slightly detuned voice
  .note() // wrap in "note"
  .decay(.15).sustain(0) // make each note of equal length
  .s('sawtooth') // waveform
  .gain(.4) // turn down
  .cutoff(sine.slow(7).range(300,5000)), // automate cutoff
  // chords
  "<Am7!3 <Em7 E7b13 Em7 Ebm7b5>>".voicings('lefthand') 
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

## Sample 9 - from [first-notes](workshop/first-notes.md)

```javascript
note("<36 34 41 39>").sound("gm_acoustic_bass")
```

*Includes visual pattern representation*

## Sample 10 - from [first-notes](workshop/first-notes.md)

```javascript
note("<[36 48] [34 46] [41 53] [39 51]>")
.sound("gm_acoustic_bass")
```

*Includes visual pattern representation*

## Sample 11 - from [first-notes](workshop/first-notes.md)

```javascript
note("<[36 48]*4 [34 46]*4 [41 53]*4 [39 51]*4>/2")
.sound("gm_acoustic_bass")
```

*Includes visual pattern representation*

## Sample 12 - from [first-notes](workshop/first-notes.md)

```javascript
note("60 <63 62 65 63>")
.sound("gm_xylophone")
```

*Includes visual pattern representation*

## Sample 13 - from [first-notes](workshop/first-notes.md)

```javascript
sound("bd*2, ~ <sd cp>, [~ hh]*2")
.bank("RolandTR909")
```

*Includes visual pattern representation*

## Sample 14 - from [first-notes](workshop/first-notes.md)

```javascript
n("0 2 4 <[6,8] [7,9]>")
.scale("C:minor").sound("piano")
```

*Includes visual pattern representation*

## Sample 15 - from [first-notes](workshop/first-notes.md)

```javascript
n("<0 -3>, 2 4 <[6,8] [7,9]>")
.scale("<C:major D:mixolydian>/4")
.sound("piano")
```

*Includes visual pattern representation*

## Sample 16 - from [first-notes](workshop/first-notes.md)

```javascript
n("<[4@2 4] [5@2 5] [6@2 6] [5@2 5]>*2")
.scale("<C2:mixolydian F2:mixolydian>/4")
.sound("gm_acoustic_bass")
```

*Includes visual pattern representation*

## Sample 17 - from [first-notes](workshop/first-notes.md)

```javascript
note("c!2 [eb,<g a bb a>]").sound("piano")
```

*Includes visual pattern representation*

## Sample 18 - from [first-notes](workshop/first-notes.md)

```javascript
note("c <e g>")
```

## Sample 19 - from [first-notes](workshop/first-notes.md)

```javascript
note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>/2")
.sound("gm_synth_bass_1")
.lpf(800) // <-- we'll learn about this soon
```

## Sample 20 - from [first-notes](workshop/first-notes.md)

```javascript
sound("bd*2, ~ <sd cp>, [~ hh]*2")
.bank("RolandTR909")
```

## Sample 21 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
note("c2 [eb3,g3]".add("<0 <1 -1>>"))
.color("<cyan <magenta yellow>>").adsr("[.1 0]:.2:[1 0]")
.sound("gm_acoustic_bass").room(.5)
```

*Includes visual pattern representation*

## Sample 22 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
note("c2 [eb3,g3]".add("<0 <1 -1>>").add("0,7"))
.color("<cyan <magenta yellow>>").adsr("[.1 0]:.2:[1 0]")
.sound("gm_acoustic_bass").room(.5)
```

*Includes visual pattern representation*

## Sample 23 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
n("<0 [2 4] <3 5> [~ <4 1>]>*2".add("<0 [0,2,4]>/4"))
.scale("C5:minor").release(.5)
.sound("gm_xylophone").room(.5)
```

*Includes visual pattern representation*

## Sample 24 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
stack(
  n("<0 [2 4] <3 5> [~ <4 1>]>*2".add("<0 [0,2,4]>/4"))
  .scale("C5:minor")
  .sound("gm_xylophone")
  .room(.4).delay(.125),
  note("c2 [eb3,g3]".add("<0 <1 -1>>"))
  .adsr("[.1 0]:.2:[1 0]")
  .sound("gm_acoustic_bass")
  .room(.5),
  n("0 1 [2 3] 2").sound("jazz").jux(rev).slow(2)
)
```

## Sample 25 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
n("<0 [4 <3 2>] <2 3> [~ 1]>"
  .off(1/8, x=>x.add(4))
  //.off(1/4, x=>x.add(7))
).scale("<C5:minor Db5:mixolydian>/4")
.s("triangle").room(.5).dec(.1).delay(.5)
```

*Includes visual pattern representation*

## Sample 26 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
s("bd sd,[~ hh]*2").bank("CasioRZ1")
  .off(1/8, x=>x.speed(1.5).gain(.25))
```

## Sample 27 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
n("0 2 4 6".add("<0 1 2 1>")).scale("C:minor")
```

## Sample 28 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
s("bd sd").ply("<1 2 3>")
```

## Sample 29 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
s("bd sd, hh*4").off(1/8, x=>x.speed(2))
```

## Sample 30 - from [first-sounds](workshop/first-sounds.md)

```javascript
sound("<bd bd hh bd rim bd hh bd>")
```

*Includes visual pattern representation*

## Sample 31 - from [first-sounds](workshop/first-sounds.md)

```javascript
sound("<bd bd hh bd rim bd hh bd>*8")
```

*Includes visual pattern representation*

## Sample 32 - from [first-sounds](workshop/first-sounds.md)

```javascript
setcpm(90/4)
sound("<bd hh rim hh>*8")
```

*Includes visual pattern representation*

## Sample 33 - from [first-effects](workshop/first-effects.md)

```javascript
note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>/2")
.sound("sawtooth").lpf(800)
```

## Sample 34 - from [first-effects](workshop/first-effects.md)

```javascript
note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>/2")
.sound("sawtooth").lpf("200 1000")
```

## Sample 35 - from [first-effects](workshop/first-effects.md)

```javascript
note("<[c3,g3,e4] [bb2,f3,d4] [a2,f3,c4] [bb2,g3,eb4]>/2")
.sound("sawtooth").vowel("<a e i o>/2")
```

## Sample 36 - from [first-effects](workshop/first-effects.md)

```javascript
stack(
  stack(
    sound("hh*8").gain("[.25 1]*2"),
    sound("bd*2,~ sd:1")
  ),
  note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>/2")
  .sound("sawtooth").lpf("200 1000"),
  note("<[c3,g3,e4] [bb2,f3,d4] [a2,f3,c4] [bb2,g3,eb4]>/2")
  .sound("sawtooth").vowel("<a e i o>/2")
) 
```

## Sample 37 - from [first-effects](workshop/first-effects.md)

```javascript
note("<c3 bb2 f3 eb3>")
.sound("sawtooth").lpf(600)
.attack(.1)
.decay(.1)
.sustain(.25)
.release(.2)
```

## Sample 38 - from [first-effects](workshop/first-effects.md)

```javascript
note("<c3 bb2 f3 eb3>")
.sound("sawtooth").lpf(600)
.adsr(".1:.1:.5:.2")

```

## Sample 39 - from [first-effects](workshop/first-effects.md)

```javascript
stack(
  note("~ [<[d3,a3,f4]!2 [d3,bb3,g4]!2> ~]")
  .sound("gm_electric_guitar_muted"),
  sound("<bd rim>").bank("RolandTR707")
).delay(".5")
```

## Sample 40 - from [first-effects](workshop/first-effects.md)

```javascript
n("<4 [3@3 4] [<2 0> ~@16] ~>/2")
.scale("D4:minor").sound("gm_accordion:2")
.room(2)
```

## Sample 41 - from [first-effects](workshop/first-effects.md)

```javascript
stack(
  note("~ [<[d3,a3,f4]!2 [d3,bb3,g4]!2> ~]")
  .sound("gm_electric_guitar_muted").delay(.5),
  sound("<bd rim>").bank("RolandTR707").delay(.5),
  n("<4 [3@3 4] [<2 0> ~@16] ~>/2")
  .scale("D4:minor").sound("gm_accordion:2")
  .room(2).gain(.5)
)
```

## Sample 42 - from [first-effects](workshop/first-effects.md)

```javascript
stack(
  note("~ [<[d3,a3,f4]!2 [d3,bb3,g4]!2> ~]")
  .sound("gm_electric_guitar_muted").delay(.5),
  sound("<bd rim>").bank("RolandTR707").delay(.5),
  n("<4 [3@3 4] [<2 0> ~@16] ~>/2")
  .scale("D4:minor").sound("gm_accordion:2")
  .room(2).gain(.4),
  n("<0 [~ 0] 4 [3 2] [0 ~] [0 ~] <0 2> ~>*2")
  .scale("D2:minor")
  .sound("sawtooth,triangle").lpf(800)
)
```

## Sample 43 - from [first-effects](workshop/first-effects.md)

```javascript
sound("bd rim").speed("<1 2 -1 -2>").room(.2)
```

## Sample 44 - from [first-effects](workshop/first-effects.md)

```javascript
sound("[bd*2,~ rim]*<1 [2 4]>")
```

## Sample 45 - from [first-effects](workshop/first-effects.md)

```javascript
note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>/2")
.sound("sawtooth")
.lpf(sine.range(100, 2000).slow(8))
```

## Sample 46 - from [first-effects](workshop/first-effects.md)

```javascript
note("c2 c3").s("sawtooth").lpf("<400 2000>")
```

## Sample 47 - from [first-effects](workshop/first-effects.md)

```javascript
note("c3 eb3 g3").s("sawtooth").vowel("<a e i o>")
```

## Sample 48 - from [first-effects](workshop/first-effects.md)

```javascript
s("bd rim").speed("<1 2 -1 -2>")
```

## Sample 49 - from [pitch](understand/pitch.md)

```javascript
freq("<200 [300,500] 400 [500,<600 670 712 670>]>*8")
```

## Sample 50 - from [pitch](understand/pitch.md)

```javascript
freq(
  "0 4 7 12"
  .fmap(n => 440 * 2**(n/12))
)
```

## Sample 51 - from [voicings](understand/voicings.md)

```javascript
note("<[c3,eb3,g3] [f3,a3,c4]>").room(.5)
```

## Sample 52 - from [voicings](understand/voicings.md)

```javascript
note("<[48,51,55] [53,57,60]>").room(.5)
```

## Sample 53 - from [voicings](understand/voicings.md)

```javascript
note("<[0,3,7] [0,4,7]>".add("<48 53>")).room(.5)
```

## Sample 54 - from [voicings](understand/voicings.md)

```javascript
note("<[0,4,7] [0,3,7] [0,3,6] [0,4,8]>".add("60"))
.room(.5)._pitchwheel()
```

## Sample 55 - from [voicings](understand/voicings.md)

```javascript
note("<[0,3,7] [12,3,7] [12,15,7] [12,15,19]>".add("48"))
.room(.5)
```

## Sample 56 - from [voicings](understand/voicings.md)

```javascript
note("<[c3,eb3,g3] [c4,eb3,g3] [c4,eb4,g3] [c4,eb4,g4]>")
.room(.5)
```

## Sample 57 - from [voicings](understand/voicings.md)

```javascript
note("<[0,3,7,12] [0,15,24] [0,3,12]>".add("48"))
.room(.5)
```

## Sample 58 - from [voicings](understand/voicings.md)

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

*Includes visual pattern representation*

## Sample 59 - from [voicings](understand/voicings.md)

```javascript
chord("<Am C D F Am E Am E>").voicing().room(.5)
```

*Includes visual pattern representation*

## Sample 60 - from [voicings](understand/voicings.md)

```javascript
addVoicings('house', {
  '': ['7 12 16', '0 7 16', '4 7 12'],
  'm': ['0 3 7']
})
chord("<Am C D F Am E Am E>")
  .dict('house').anchor(66)
  .voicing().room(.5)
```

*Includes visual pattern representation*

## Sample 61 - from [voicings](understand/voicings.md)

```javascript
anchor("<c4 g4 c5 g5>").chord("C").voicing().room(.5)
```

*Includes visual pattern representation*

## Sample 62 - from [voicings](understand/voicings.md)

```javascript
mode("<below above duck root>").chord("C").anchor("c5").voicing().room(.5)
```

*Includes visual pattern representation*

## Sample 63 - from [voicings](understand/voicings.md)

```javascript
mode("<below above duck root>:c5").chord("C").voicing().room(.5)
```

*Includes visual pattern representation*

## Sample 64 - from [voicings](understand/voicings.md)

```javascript
n("0 3 1 2").chord("<C <Fm Db>>").voicing()
.clip("4 3 2 1").room(.5)
```

*Includes visual pattern representation*

## Sample 65 - from [cycles](understand/cycles.md)

```javascript
setcpm(110/2)
s("bd <sd rim*<1 2>>,hh*4")
```

## Sample 66 - from [recap](workshop/recap.md)

```javascript
note("c <e g>")
```

## Sample 67 - from [recap](workshop/recap.md)

```javascript
note("c3 eb3 g3").s("sawtooth").vowel("<a e i o>")
```

## Sample 68 - from [recap](workshop/recap.md)

```javascript
s("bd rim bd cp").speed("<1 2 -1 -2>")
```

## Sample 69 - from [recap](workshop/recap.md)

```javascript
n("0 2 4 6".add("<0 1 2 1>")).scale("C:minor")
```

## Sample 70 - from [recap](workshop/recap.md)

```javascript
s("bd sd").ply("<1 2 3>")
```

## Sample 71 - from [recap](workshop/recap.md)

```javascript
s("bd sd, hh*4").off(1/8, x=>x.speed(2))
```

## Sample 72 - from [first-notes](workshop/first-notes.md)

```javascript
note("<36 34 41 39>").sound("gm_acoustic_bass")
```

*Includes visual pattern representation*

## Sample 73 - from [first-notes](workshop/first-notes.md)

```javascript
note("<[36 48]*4 [34 46]*4 [41 53]*4 [39 51]*4>")
.sound("gm_acoustic_bass")
```

*Includes visual pattern representation*

## Sample 74 - from [first-notes](workshop/first-notes.md)

```javascript
note("60 <63 62 65 63>")
.sound("gm_xylophone")
```

*Includes visual pattern representation*

## Sample 75 - from [first-notes](workshop/first-notes.md)

```javascript
sound("bd*4, [~ <sd cp>]*2, [~ hh]*4")
.bank("RolandTR909")
```

*Includes visual pattern representation*

## Sample 76 - from [first-notes](workshop/first-notes.md)

```javascript
setcpm(60)
n("0 2 4 <[6,8] [7,9]>")
.scale("C:minor").sound("piano")
```

*Includes visual pattern representation*

## Sample 77 - from [first-notes](workshop/first-notes.md)

```javascript
setcpm(60)
n("<0 -3>, 2 4 <[6,8] [7,9]>")
.scale("<C:major D:mixolydian>/4")
.sound("piano")
```

*Includes visual pattern representation*

## Sample 78 - from [first-notes](workshop/first-notes.md)

```javascript
setcpm(60)
n("<[4@2 4] [5@2 5] [6@2 6] [5@2 5]>*2")
.scale("<C2:mixolydian F2:mixolydian>/4")
.sound("gm_acoustic_bass")
```

*Includes visual pattern representation*

## Sample 79 - from [first-notes](workshop/first-notes.md)

```javascript
setcpm(60)
note("c!2 [eb,<g a bb a>]").sound("piano")
```

*Includes visual pattern representation*

## Sample 80 - from [first-notes](workshop/first-notes.md)

```javascript
note("c a f <e g>")
```

## Sample 81 - from [first-notes](workshop/first-notes.md)

```javascript
note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
.sound("gm_synth_bass_1")
.lpf(800) // <-- we'll learn about this soon
```

## Sample 82 - from [first-notes](workshop/first-notes.md)

```javascript
sound("bd*4, [~ <sd cp>]*2, [~ hh]*4")
.bank("RolandTR909")
```

## Sample 83 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
setcpm(60)
note("c2 [eb3,g3] ".add("<0 <1 -1>>"))
.color("<cyan <magenta yellow>>").adsr("[.1 0]:.2:[1 0]")
.sound("gm_acoustic_bass").room(.5)
```

*Includes visual pattern representation*

## Sample 84 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
setcpm(60)
note("c2 [eb3,g3]".add("<0 <1 -1>>").add("0,7"))
.color("<cyan <magenta yellow>>").adsr("[.1 0]:.2:[1 0]")
.sound("gm_acoustic_bass").room(.5)
```

*Includes visual pattern representation*

## Sample 85 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
n("0 [2 4] <3 5> [~ <4 1>]".add("<0 [0,2,4]>"))
.scale("C5:minor").release(.5)
.sound("gm_xylophone").room(.5)
```

*Includes visual pattern representation*

## Sample 86 - from [pattern-effects](workshop/pattern-effects.md)

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

## Sample 87 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
n("0 [4 <3 2>] <2 3> [~ 1]"
  .off(1/16, x=>x.add(4))
  //.off(1/8, x=>x.add(7))
).scale("<C5:minor Db5:mixolydian>/2")
.s("triangle").room(.5).dec(.1)
```

*Includes visual pattern representation*

## Sample 88 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
s("bd sd [rim bd] sd,[~ hh]*4").bank("CasioRZ1")
  .off(2/16, x=>x.speed(1.5).gain(.25)
  .off(3/16, y=>y.vowel("<a e i o>*8")))
```

## Sample 89 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
n("0 2 4 6 ~ 7 9 5".add("<0 1 2 1>")).scale("C:minor")
```

## Sample 90 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
s("bd sd [~ bd] sd").ply("<1 2 3>")
```

## Sample 91 - from [pattern-effects](workshop/pattern-effects.md)

```javascript
s("bd sd [~ bd] sd, hh*8").off(1/16, x=>x.speed(2))
```

## Sample 92 - from [first-sounds](workshop/first-sounds.md)

```javascript
sound("<bd bd hh bd rim bd hh bd>")
```

*Includes visual pattern representation*

## Sample 93 - from [first-sounds](workshop/first-sounds.md)

```javascript
sound("<bd bd hh bd rim bd hh bd>*8")
```

*Includes visual pattern representation*

## Sample 94 - from [first-sounds](workshop/first-sounds.md)

```javascript
setcpm(90/4)
sound("<bd hh rim hh>*8")
```

*Includes visual pattern representation*

## Sample 95 - from [first-sounds](workshop/first-sounds.md)

```javascript
sound("<bd hh rim oh bd rim>")
```

## Sample 96 - from [first-effects](workshop/first-effects.md)

```javascript
note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
.sound("sawtooth").lpf(800)
```

## Sample 97 - from [first-effects](workshop/first-effects.md)

```javascript
note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
.sound("sawtooth").lpf("200 1000 200 1000")
```

## Sample 98 - from [first-effects](workshop/first-effects.md)

```javascript
note("<[c3,g3,e4] [bb2,f3,d4] [a2,f3,c4] [bb2,g3,eb4]>")
.sound("sawtooth").vowel("<a e i o>")
```

## Sample 99 - from [first-effects](workshop/first-effects.md)

```javascript
$: sound("hh*8").gain("[.25 1]*4")

$: sound("bd*4,[~ sd:1]*2")

$: note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
.sound("sawtooth").lpf("200 1000 200 1000")

$: note("<[c3,g3,e4] [bb2,f3,d4] [a2,f3,c4] [bb2,g3,eb4]>")
.sound("sawtooth").vowel("<a e i o>")
```

## Sample 100 - from [first-effects](workshop/first-effects.md)

```javascript
$: note("[~ [<[d3,a3,f4]!2 [d3,bb3,g4]!2> ~]]*2")
  .sound("gm_electric_guitar_muted").delay(.5)

$: sound("bd rim").bank("RolandTR707").delay(".5")
```

## Sample 101 - from [first-effects](workshop/first-effects.md)

```javascript
n("<4 [3@3 4] [<2 0> ~@16] ~>")
.scale("D4:minor").sound("gm_accordion:2")
.room(2)
```

## Sample 102 - from [first-effects](workshop/first-effects.md)

```javascript
$: note("[~ [<[d3,a3,f4]!2 [d3,bb3,g4]!2> ~]]*2")
.sound("gm_electric_guitar_muted").delay(.5)

$: sound("bd rim").bank("RolandTR707").delay(.5)

$: n("<4 [3@3 4] [<2 0> ~@16] ~>")
.scale("D4:minor").sound("gm_accordion:2")
.room(2).gain(.5)
```

## Sample 103 - from [first-effects](workshop/first-effects.md)

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

## Sample 104 - from [first-effects](workshop/first-effects.md)

```javascript
sound("bd rim [~ bd] rim").speed("<1 2 -1 -2>").room(.2)
```

## Sample 105 - from [first-effects](workshop/first-effects.md)

```javascript
sound("[bd*4,~ rim ~ cp]*<1 [2 4]>")
```

## Sample 106 - from [first-effects](workshop/first-effects.md)

```javascript
note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
  .sound("sawtooth")
  .lpf(sine.range(100, 2000).slow(4))
```

## Sample 107 - from [first-effects](workshop/first-effects.md)

```javascript
note("c2 c3 c2 c3").s("sawtooth").lpf("<400 2000>")
```

## Sample 108 - from [first-effects](workshop/first-effects.md)

```javascript
note("c3 eb3 g3").s("sawtooth").vowel("<a e i o>")
```

## Sample 109 - from [first-effects](workshop/first-effects.md)

```javascript
s("bd rim bd cp").speed("<1 2 -1 -2>")
```

## Sample 110 - from [arpeggios](recipes/arpeggios.md)

```javascript
note("c a f e").piano().slow(2)
```

## Sample 111 - from [arpeggios](recipes/arpeggios.md)

```javascript
note("<c a f e>").piano().slow(2)
```

## Sample 112 - from [arpeggios](recipes/arpeggios.md)

```javascript
"<c a f e>".off(1/8, add(7))
  .note().piano().slow(2)
```

## Sample 113 - from [arpeggios](recipes/arpeggios.md)

```javascript
"<c*2 a(3,8) f(3,8,2) e*2>"
  .off(1/8, add(7))
  .note().piano().slow(2)
```

## Sample 114 - from [arpeggios](recipes/arpeggios.md)

```javascript
"<c*2 a(3,8) f(3,8,2) e*2>"
  .off(1/8, add(7))
  .note().piano()
  .jux(rev).slow(2)
```

## Sample 115 - from [arpeggios](recipes/arpeggios.md)

```javascript
"<c*2 a(3,8) f(3,8,2) e*2>"
  .off(1/8, add(7))
  .off(1/8, add(12))
  .note().piano()
  .jux(rev).slow(2)
```

## Sample 116 - from [rhythms](recipes/rhythms.md)

```javascript
s("bd*2 [[~ lt] sd:3] lt:1 [ht mt*2]")
.every(2, early("<.25 .125 .5>")).slow(2)
```

## Sample 117 - from [rhythms](recipes/rhythms.md)

```javascript
s("bd*2 [[~ lt] sd:3] lt:1 [ht mt*2]")
.every(2, early("<.25 .125 .5>"))
.shape("<0 .5 .3>")
.room(saw.range(0,.2).slow(4))
.slow(2)
```

## Sample 118 - from [rhythms](recipes/rhythms.md)

```javascript
s("bd*2 [[~ lt] sd:3] lt:1 [ht mt*2]")
.every(2, early("<.25 .125 .5>"))
.shape("<0 .5 .3>")
.room(saw.range(0,.2).slow(4))
.jux(id, rev, x=>x.speed(2))
.slow(2)
```

## Sample 119 - from [rhythms](recipes/rhythms.md)

```javascript
n("0 <0 4> [2 0] [2 3]").s("feel").speed(1.5).slow(2)
```

## Sample 120 - from [microrhythms](recipes/microrhythms.md)

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

## Sample 121 - from [microrhythms](recipes/microrhythms.md)

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

## Sample 122 - from [recipes](recipes/recipes.md)

```javascript
samples('github:yaxu/clean-breaks')
s("amen/4").fit()
  .slice(8, "<0 1 2 3 4*2 5 6 [6 7]>*2")
  .cut(1).rarely(ply("2"))
```

*Includes visual pattern representation*

## Sample 123 - from [recipes](recipes/recipes.md)

```javascript
samples('github:yaxu/clean-breaks')
s("amen")
  .splice(8, "<0 1 2 3 4*2 5 6 [6 7]>*2")
  .cut(1).rarely(ply("2"))
```

*Includes visual pattern representation*

## Sample 124 - from [recipes](recipes/recipes.md)

```javascript
note("g1 bb1 <c2 eb2> d2")
  .s("sawtooth")
  .lpf(400).lpenv(4)
  .scope()
```

## Sample 125 - from [recipes](recipes/recipes.md)

```javascript
note("g1 bb1 <c2 eb2> d2")
  .s("sawtooth").lpq(8)
  .lpf(400).lpa(.2).lpenv(4)
  .scope()
```

## Sample 126 - from [recipes](recipes/recipes.md)

```javascript
note("g1 bb1 <c2 eb2> d2")
  .s("sawtooth").lpq(8)
  .lpf(400).lpa(.1).lpd(.1).lpenv(4)
  .scope()
```

## Sample 127 - from [recipes](recipes/recipes.md)

```javascript
note("<g1 bb1 d2 f1>")
.s("sawtooth, square") // <------
.scope()
```

## Sample 128 - from [recipes](recipes/recipes.md)

```javascript
note("<g1 bb1 d2 f1>")
.s("sawtooth, square:0:.5") // <--- "name:number:gain"
.scope()
```

## Sample 129 - from [recipes](recipes/recipes.md)

```javascript
note("<g1 bb1 d2 f1>").layer(
  x=>x.s("sawtooth").vib(4),
  x=>x.s("square").add(note(12))
).scope()
```

## Sample 130 - from [recipes](recipes/recipes.md)

```javascript
note("<g1 bb1 d2 f1>")
.add(note("0,.1")) // <------ chorus
.s("sawtooth").scope()
```

*Includes visual pattern representation*

## Sample 131 - from [recipes](recipes/recipes.md)

```javascript
s("<bd rim, hh hh oh>*4")
```

*Includes visual pattern representation*

## Sample 132 - from [recipes](recipes/recipes.md)

```javascript
note("<C D G A Bb D C A G D Bb A>*[6,6.1]").piano()
```

*Includes visual pattern representation*

## Sample 133 - from [recipes](recipes/recipes.md)

```javascript
note("<c4 bb f eb>*8")
.add(note(perlin.range(0,.5))) // <------ warble
.clip(2).s("gm_electric_guitar_clean")
```

## Sample 134 - from [recipes](recipes/recipes.md)

```javascript
note("f ab bb c")
.clip("<2 1 .5 .25>")
```

## Sample 135 - from [recipes](recipes/recipes.md)

```javascript
note("f ab bb c")
.release("<2 1 .5 .25>")
```

## Sample 136 - from [recipes](recipes/recipes.md)

```javascript
note("f ab bb c")
.decay("<2 1 .5 .25>")
```

## Sample 137 - from [recipes](recipes/recipes.md)

```javascript
s("oh*4").end("<1 .5 .25 .1>")
```

## Sample 138 - from [recipes](recipes/recipes.md)

```javascript
s("oh*4").clip("<1 .5 .25 .1>")
```

## Sample 139 - from [recipes](recipes/recipes.md)

```javascript
s("oh*4").decay("<1 .5 .25 .1>")
```

## Sample 140 - from [recipes](recipes/recipes.md)

```javascript
note("<c eb g f>").s("bd").loop(1).loopEnd(.05).gain(.2)
```

## Sample 141 - from [patterns](technical-manual/patterns.md)

```javascript
const pattern = sequence("c3", ["e3", "g3"])
const events = pattern.queryArc(0, 1)
console.log(events.map((e) => e.show()))
silence
```

## Sample 142 - from [visual-feedback](learn/visual-feedback.md)

```javascript
n("<0 2 1 3 2>*8")
.scale("<A1 D2>/4:minor:pentatonic")
.s("supersaw").lpf(300).lpenv("<4 3 2>\*4")
```

## Sample 143 - from [visual-feedback](learn/visual-feedback.md)

```javascript
n("<0 2 1 3 2>*8")
.scale("<A1 D2>/4:minor:pentatonic")
.s("supersaw").lpf(300).lpenv("<4 3 2>*4")
.color("cyan magenta")
```

## Sample 144 - from [synths](learn/synths.md)

```javascript
note("c2 <eb2 <g2 g1>>".fast(2))
.sound("<sawtooth square triangle sine>")
._scope()
```

## Sample 145 - from [synths](learn/synths.md)

```javascript
sound("<white pink brown>")._scope()
```

## Sample 146 - from [synths](learn/synths.md)

```javascript
sound("bd*2,<white pink brown>*8")
.decay(.04).sustain(0)._scope()
```

## Sample 147 - from [synths](learn/synths.md)

```javascript
note("c3").noise("<0.1 0.25 0.5>")._scope()
```

## Sample 148 - from [synths](learn/synths.md)

```javascript
s("crackle*4").density("<0.01 0.04 0.2 0.5>".slow(2))._scope()
```

## Sample 149 - from [synths](learn/synths.md)

```javascript
note("c2 <eb2 <g2 g1>>".fast(2))
.sound("sawtooth")
.n("<32 16 8 4>")
._scope()
```

## Sample 150 - from [synths](learn/synths.md)

```javascript
note("c2 <eb2 <g2 g1>>".fast(2))
.sound("sawtooth:<32 16 8 4>")
._scope()
```

## Sample 151 - from [synths](learn/synths.md)

```javascript
samples('bubo:waveforms');
note("<[g3,b3,e4]!2 [a3,c3,e4] [b3,d3,f#4]>")
.n("<1 2 3 4 5 6 7 8 9 10>/2").room(0.5).size(0.9)
.s('wt_flute').velocity(0.25).often(n => n.ply(2))
.release(0.125).decay("<0.1 0.25 0.3 0.4>").sustain(0)
.cutoff(2000).cutoff("<1000 2000 4000>").fast(4)
._scope()

```

## Sample 152 - from [synths](learn/synths.md)

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

## Sample 153 - from [input-output](learn/input-output.md)

```javascript

$: chord("<C^7 A7 Dm7 G7>").voicing().midi('IAC Driver')

```

## Sample 154 - from [input-output](learn/input-output.md)

```javascript
$:stack(
  midicmd("clock*48,<start stop>/2").midi('IAC Driver')
)
```

## Sample 155 - from [input-output](learn/input-output.md)

```javascript
// Switch between programs 0 and 1 every cycle
progNum("<0 1>").midi()

// Play notes while changing programs
note("c3 e3 g3").progNum("<0 1 2>").midi()
```

## Sample 156 - from [getting-started](learn/getting-started.md)

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

## Sample 157 - from [tonal](learn/tonal.md)

```javascript
chord("<C^7 A7b13 Dm7 G7>*2")
  .dict('ireal').layer(
  x=>x.struct("[~ x]*2").voicing()
  ,
  x=>n("0*4").set(x).mode("root:g2").voicing()
  .s('sawtooth').cutoff("800:4:2")
)
```

## Sample 158 - from [tonal](learn/tonal.md)

```javascript
"[c2 c3]*4".transpose("<0 -2 5 3>").note()
```

## Sample 159 - from [tonal](learn/tonal.md)

```javascript
"[c2 c3]*4".transpose("<1P -2M 4P 3m>").note()
```

## Sample 160 - from [tonal](learn/tonal.md)

```javascript
"[-8 [2,4,6]]*2"
.scale('C4 bebop major')
.scaleTranspose("<0 -1 -2 -3 -4 -5 -6 -4>*2")
.note()
```

## Sample 161 - from [tonal](learn/tonal.md)

```javascript
"<C^7 A7b13 Dm7 G7>*2".rootNotes(3).note()
```

## Sample 162 - from [tonal](learn/tonal.md)

```javascript
"<C^7 A7b13 Dm7 G7>*2".layer(
  x => x.voicings('lefthand').struct("[~ x]*2").note(),
  x => x.rootNotes(2).note().s('sawtooth').cutoff(800)
)
```

## Sample 163 - from [samples](learn/samples.md)

```javascript
s("bd sd,hh*16").bank("<RolandTR808 RolandTR909>")
```

## Sample 164 - from [samples](learn/samples.md)

```javascript
samples('http://localhost:5432/');
 
n("<0 1 2>").s("swoop smash")
```

## Sample 165 - from [samples](learn/samples.md)

```javascript
samples({
  'gtr': 'gtr/0001_cleanC.wav',
  'moog': { 'g3': 'moog/005_Mighty%20Moog%20G3.wav' },
}, 'github:tidalcycles/dirt-samples');
note("g3 [bb3 c4] <g4 f4 eb4 f3>@2").s("gtr,moog").clip(1)
  .gain(.5)
```

## Sample 166 - from [samples](learn/samples.md)

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

## Sample 167 - from [hydra](learn/hydra.md)

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

## Sample 168 - from [hydra](learn/hydra.md)

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

## Sample 169 - from [hydra](learn/hydra.md)

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

## Sample 170 - from [csound](learn/csound.md)

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

## Sample 171 - from [effects](learn/effects.md)

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

## Sample 172 - from [effects](learn/effects.md)

```javascript
n("<-4,0 5 2 1>*<2!3 4>")
  .scale("<C F>/8:pentatonic")
  .s("gm_electric_guitar_jazz")
  .penv("<.5 0 7 -2>*2").vib("4:.1")
  .phaser(2).delay(.25).room(.3)
  .size(4).fast(1.5)
```

## Sample 173 - from [effects](learn/effects.md)

```javascript
n(run("<4 8>/16")).jux(rev)
.chord("<C^7 <Db^7 Fm7>>")
.dict('ireal')
.voicing().add(note("<0 1>/8"))
.dec(.1).room(.2)
.segment("<4 [2 8]>")
.penv("<0 <2 -2>>").patt(.02).fast(2)
```

## Sample 174 - from [mini-notation](learn/mini-notation.md)

```javascript
note("<e5 b4 d5 c5>")
```

*Includes visual pattern representation*

## Sample 175 - from [mini-notation](learn/mini-notation.md)

```javascript
note("<e5 b4 d5 c5 e5>")
```

*Includes visual pattern representation*

## Sample 176 - from [mini-notation](learn/mini-notation.md)

```javascript
note("<e5 b4 d5 c5 e5 b4>")
```

*Includes visual pattern representation*

## Sample 177 - from [mini-notation](learn/mini-notation.md)

```javascript
note("<e5 b4 d5 c5 a4 c5>*8")
```

*Includes visual pattern representation*

## Sample 178 - from [mini-notation](learn/mini-notation.md)

```javascript
note("<[g3,b3,e4] [a3,c3,e4] [b3,d3,f#4] [b3,e4,g4]>*2")
```

*Includes visual pattern representation*

## Sample 179 - from [mini-notation](learn/mini-notation.md)

```javascript
note("<[g3,b3,e4]@2 [a3,c3,e4] [b3,d3,f#4]>*2")
```

*Includes visual pattern representation*

## Sample 180 - from [mini-notation](learn/mini-notation.md)

```javascript
note("<[g3,b3,e4]!2 [a3,c3,e4] [b3,d3,f#4]>*2")
```

*Includes visual pattern representation*

## Sample 181 - from [mini-notation](learn/mini-notation.md)

```javascript
note("<g3 b3 e4 [a3,c3,e4] [b3,d3,f#4]>*2")
```

## Sample 182 - from [mini-notation](learn/mini-notation.md)

```javascript
note("<[g3,b3,e4] [a3,c3,e4] [b3,d3,f#4]>*2")
```

## Sample 183 - from [mini-notation](learn/mini-notation.md)

```javascript
note("<[g3,b3,e4]/2 [a3,c3,e4] [b3,d3,f#4]>*2")
```

## Sample 184 - from [mini-notation](learn/mini-notation.md)

```javascript
note("<[g3,b3,e4]*2 [a3,c3,e4] [b3,d3,f#4]>*2")
```

## Sample 185 - from [mini-notation](learn/mini-notation.md)

```javascript
note("<[g3,b3,e4] _ [a3,c3,e4] [b3,d3,f#4]>*2")
```

## Sample 186 - from [mini-notation](learn/mini-notation.md)

```javascript
note("<[g3,b3,e4]@2 [a3,c3,e4] [b3,d3,f#4]>*2")
```

## Sample 187 - from [mini-notation](learn/mini-notation.md)

```javascript
note("<[g3,b3,e4]!2 [a3,c3,e4] [b3,d3,f#4]>*2")
```

## Sample 188 - from [value-modifiers](functions/value-modifiers.md)

```javascript
note("c a f e")
.cutoff("<500 1000 2000 [4000 8000]>")
.gain(.8)
.s('sawtooth')
.log()
```

## Sample 189 - from [value-modifiers](functions/value-modifiers.md)

```javascript
"<c e g>".log()
```

## Sample 190 - from [value-modifiers](functions/value-modifiers.md)

```javascript
note("<c e g>").log()
```

## Sample 191 - from [value-modifiers](functions/value-modifiers.md)

```javascript
"50 60 70".add("<0 1 2>").log()
```

## Sample 192 - from [value-modifiers](functions/value-modifiers.md)

```javascript
note("50 60 70".add("<0 1 2>")).room(.1).log()
```

## Sample 193 - from [value-modifiers](functions/value-modifiers.md)

```javascript
"50 60 70".add("<0 1 2>").note().room(.1).log()
```

## Sample 194 - from [value-modifiers](functions/value-modifiers.md)

```javascript
note("50 60 70").room(.1).add(note("<0 1 2>")).log()
```

## Sample 195 - from [intro](functions/intro.md)

```javascript
note("<[g3,b3,e4] [a3,c3,e4] [b3,d3,f#4] [b3,e4,g4]>")
```

