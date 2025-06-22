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