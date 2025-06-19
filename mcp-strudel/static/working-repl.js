// Import Strudel modules from CDN
const { repl, evalScope } = await import('https://unpkg.com/@strudel/core@latest');
const { getAudioContext, webaudioOutput, initAudioOnFirstClick, registerSynthSounds } = await import('https://unpkg.com/@strudel/webaudio@latest');
const { transpiler } = await import('https://unpkg.com/@strudel/transpiler@latest');

// Pattern library
const patterns = {
  basic: `samples('github:tidalcycles/dirt-samples')
s("bd sn hh sn").slow(2)`,
  
  drums: `samples('github:tidalcycles/dirt-samples')
stack(
  s("bd bd ~ bd"),
  s("~ sn ~ sn"),
  s("hh*8").gain(0.3)
)`,
  
  melody: `samples('github:tidalcycles/dirt-samples')
note("c4 d4 e4 f4 g4 a4 b4 c5")
.slow(2)
.s("bleep")
.room(0.3)`,
  
  complex: `samples('github:tidalcycles/dirt-samples')
stack(
  note("c2 [eb2 g2] bb1 f2").slow(4).s("sawtooth").lpf(400),
  note("<c4 eb4 g4 bb4>*4").s("bleep").gain(0.6),
  s("bd ~ bd ~").fast(2),
  s("~ sn ~ sn")
)`,
  
  custom: `samples('github:tidalcycles/dirt-samples')
s("cp bd ~ sn").fast(2).room(0.5)`
};

// Initialize audio context and components
const ctx = getAudioContext();
const input = document.getElementById('text');

// Set initial pattern
input.value = patterns.basic;

// Initialize audio and sounds
initAudioOnFirstClick();
registerSynthSounds();

// Setup evaluation scope
evalScope(
  import('https://unpkg.com/@strudel/core@latest'), 
  import('https://unpkg.com/@strudel/mini@latest'), 
  import('https://unpkg.com/@strudel/webaudio@latest'), 
  import('https://unpkg.com/@strudel/tonal@latest')
);

// Create REPL instance
const { evaluate, hush, getScheduler } = repl({
  defaultOutput: webaudioOutput,
  getTime: () => ctx.currentTime,
  transpiler,
});

// Play button functionality
document.getElementById('start').addEventListener('click', async () => {
  try {
    await ctx.resume();
    console.log('🎵 Evaluating:', input.value);
    evaluate(input.value);
    console.log('✅ Pattern started');
  } catch (error) {
    console.error('❌ Evaluation error:', error);
  }
});

// Stop button functionality
document.getElementById('stop').addEventListener('click', () => {
  try {
    hush();
    console.log('🛑 All patterns stopped');
  } catch (error) {
    console.error('❌ Stop error:', error);
  }
});

// Pattern selection functions
window.setPattern = function(patternName) {
  const code = patterns[patternName];
  if (code) {
    input.value = code;
    console.log(`📝 Loaded pattern: ${patternName}`);
    
    // Auto-play the new pattern
    setTimeout(async () => {
      try {
        await ctx.resume();
        evaluate(code);
        console.log(`🎵 Auto-playing: ${patternName}`);
      } catch (error) {
        console.error('❌ Auto-play error:', error);
      }
    }, 100);
  }
};

console.log('🌀 Strudel REPL ready! Click pattern buttons or type code.');