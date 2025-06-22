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