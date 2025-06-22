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