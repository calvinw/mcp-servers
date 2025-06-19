let ws = null;
const statusDot = document.getElementById('statusDot');
const statusText = document.getElementById('statusText');
const messageLog = document.getElementById('messageLog');
let strudelIframe = null;

function addLogEntry(message, type = 'info') {
    const timestamp = new Date().toLocaleTimeString();
    const logLine = `[${timestamp}] ${message}\n`;
    messageLog.textContent += logLine;
    messageLog.scrollTop = messageLog.scrollHeight;
    
    // Keep only last 50 lines
    const lines = messageLog.textContent.split('\n');
    if (lines.length > 50) {
        messageLog.textContent = lines.slice(-50).join('\n');
    }
}

function updateConnectionStatus(connected) {
    if (connected) {
        statusDot.classList.add('connected');
        statusText.textContent = 'Connected to MCP server - Ready for live coding!';
    } else {
        statusDot.classList.remove('connected');
        statusText.textContent = 'Disconnected from MCP server';
    }
}

function connectWebSocket() {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const wsUrl = `${protocol}//${window.location.host}/ws`;
    
    ws = new WebSocket(wsUrl);
    
    ws.onopen = function() {
        updateConnectionStatus(true);
        addLogEntry('WebSocket connected to MCP server', 'success');
    };
    
    ws.onmessage = async function(event) {
        try {
            const data = JSON.parse(event.data);
            
            if (data.type === 'strudel-code') {
                const description = data.metadata?.description || '';
                const logMessage = description ? 
                    `Received: ${description}` : 
                    `Received: ${data.code.substring(0, 50)}...`;
                
                addLogEntry(logMessage);
                
                // Update the Strudel editor with new code
                try {
                    // Wait for editor to be ready
                    await initializeAudio();
                    
                    // Update the iframe with new code
                    if (window.strudel && window.strudel.evaluate) {
                        await window.strudel.evaluate(data.code);
                    } else {
                        addLogEntry('Strudel iframe not ready for code update');
                    }
                    
                    if (data.autoplay) {
                        addLogEntry('Auto-playing pattern...');
                        
                        // The iframe will auto-update and auto-play
                        addLogEntry('Pattern loaded and auto-playing in Strudel iframe!');
                    }
                } catch (error) {
                    addLogEntry(`Error: ${error.message}`);
                    // Send error back to server
                    if (ws && ws.readyState === WebSocket.OPEN) {
                        ws.send(JSON.stringify({
                            type: 'evaluation-error',
                            error: error.message,
                            code: data.code.substring(0, 100) + '...'
                        }));
                    }
                }
            } else if (data.type === 'strudel-stop') {
                addLogEntry('Stop signal received');
                
                try {
                    addLogEntry('Stop signal received - use the stop button in the Strudel interface');
                } catch (error) {
                    addLogEntry(`Stop error: ${error.message}`);
                }
            } else if (data.type === 'pong') {
                // Handle ping response
            }
        } catch (error) {
            addLogEntry(`Error parsing message: ${error.message}`, 'error');
        }
    };
    
    ws.onclose = function() {
        updateConnectionStatus(false);
        addLogEntry('WebSocket connection closed', 'error');
        
        // Try to reconnect after 3 seconds
        setTimeout(connectWebSocket, 3000);
    };
    
    ws.onerror = function() {
        addLogEntry('WebSocket error occurred', 'error');
    };
}

// Send periodic ping to keep connection alive
setInterval(() => {
    if (ws && ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify({ type: 'ping' }));
    }
}, 30000);

// Initialize Strudel audio context on first user interaction
let audioInitialized = false;

async function initializeAudio() {
    if (audioInitialized) return;
    
    try {
        // Wait for Strudel to be ready
        if (window.strudel && typeof window.strudel.initAudio === 'function') {
            await window.strudel.initAudio();
            audioInitialized = true;
            addLogEntry('🔊 Strudel audio initialized', 'success');
        } else {
            // Fallback: try to start audio context manually
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            await audioContext.resume();
            audioInitialized = true;
            addLogEntry('🔊 Audio context started', 'success');
        }
    } catch (error) {
        addLogEntry(`Audio init failed: ${error.message}`, 'error');
    }
}

// Add click handler to initialize audio
document.addEventListener('click', initializeAudio, { once: true });

// Wait for Strudel to load and initialize
async function waitForStrudel() {
    let attempts = 0;
    while (attempts < 100) {
        // Check for any Strudel-related functions
        const hasEmbed = window.embed || window.strudelEmbed;
        const hasREPL = window.StrudelREPL || window.strudelREPL;
        const hasCore = window.strudel || window.Strudel;
        
        console.log(`Attempt ${attempts}: checking for Strudel...`, {
            embed: !!window.embed,
            strudelEmbed: !!window.strudelEmbed,
            StrudelREPL: !!window.StrudelREPL,
            strudelREPL: !!window.strudelREPL,
            strudel: !!window.strudel,
            Strudel: !!window.Strudel,
            allKeys: Object.keys(window).filter(k => k.toLowerCase().includes('strudel')).length
        });
        
        if (window.strudelLoaded) {
            addLogEntry('Strudel library loaded', 'success');
            return true;
        }
        await new Promise(resolve => setTimeout(resolve, 200));
        attempts++;
    }
    addLogEntry('Strudel library failed to load', 'error');
    return false;
}

// Initialize Strudel web component
function initializeStrudelEditor() {
    try {
        const strudelRepl = document.getElementById('strudelRepl');
        
        if (strudelRepl) {
            // Store reference for global access
            window.strudelRepl = strudelRepl;
            
            addLogEntry('Strudel REPL component loaded - ready for MCP patterns!');
            return true;
        } else {
            addLogEntry('Strudel REPL not ready yet...');
        }
    } catch (e) {
        console.error('Strudel REPL initialization error:', e);
        addLogEntry(`Strudel REPL initialization error: ${e.message}`);
    }
    return false;
}

// Connect when page loads
document.addEventListener('DOMContentLoaded', async function() {
    connectWebSocket();
    addLogEntry('Strudel MCP Player initialized');
    
    // Wait for Strudel to be ready
    await waitForStrudel();
    
    // Initialize the editor with retries
    let retries = 0;
    const maxRetries = 10;
    
    const tryInitialize = () => {
        if (initializeStrudelEditor()) {
            addLogEntry('Strudel editor initialized');
        } else if (retries < maxRetries) {
            retries++;
            addLogEntry(`Retrying editor initialization... (${retries}/${maxRetries})`);
            setTimeout(tryInitialize, 500);
        } else {
            addLogEntry('Failed to initialize Strudel editor after max retries');
        }
    };
    
    setTimeout(tryInitialize, 1000);
});