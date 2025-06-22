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