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