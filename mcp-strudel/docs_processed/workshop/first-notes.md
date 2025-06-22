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