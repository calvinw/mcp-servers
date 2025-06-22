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