#!/bin/bash

echo "=== LYRA Intelligence Bootstrap ==="
echo "Initializing system context..."

# === Paths & Flags ===
ACTIVATION_KEY_PATH="./activation.key"
SECURE_MODE_FLAG="LYRA_SECURE_MODE"
LAUNCH_LOG="launch_lyra.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# === Logging Helper ===
log_event() {
    echo "[$TIMESTAMP] $1" | tee -a "$LAUNCH_LOG"
}

# === Activation Key Check ===
if [[ -f "$ACTIVATION_KEY_PATH" ]]; then
    log_event "🔐 Activation key detected. Secure mode enabled."
    export $SECURE_MODE_FLAG=1
else
    log_event "⚠️ No activation key found. Running in plugin fallback mode."
    export $SECURE_MODE_FLAG=0
fi

# === Secure Mode Logic ===
if [[ "$LYRA_SECURE_MODE" -eq 1 ]]; then
    log_event "Launching LYRA Core Engine..."
    
    # Placeholder for full stack start (e.g., containers, LLMs, secure tools)
    # Example: docker-compose -f secure-stack.yml up --build

    # Simulated core launch (stub)
    python3 ./lyra/core.py --secure --key "$ACTIVATION_KEY_PATH"
else
    log_event "Fallback: Running public demo plugin interface..."
    
    # Use the demo CLI interface (legacy-compatible)
    python3 ./scripts/cli_lyra_demo.py
fi

log_event "🧠 LYRA interface exit complete."
echo "---"

