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