#!/bin/bash

echo "=== LYRA Intelligence Bootstrap ==="
echo "Initializing system context..."

# === Paths & Flags ===
ACTIVATION_KEY_PATH="./activation.key"
SECURE_MODE_FLAG="LYRA_SECURE_MODE"
FORCE_LEGACY_FLAG="${LYRA_FORCE_LEGACY:-0}"
LAUNCH_LOG="launch_lyra.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# === Logging Helper ===
log_event() {
    echo "[$TIMESTAMP] $1" | tee -a "$LAUNCH_LOG"
}

# === Mode Determination ===
if [[ "$FORCE_LEGACY_FLAG" -eq 1 ]]; then
    log_event "Legacy mode forced via environment override."
    export $SECURE_MODE_FLAG=0

elif [[ -f "$ACTIVATION_KEY_PATH" ]]; then
    log_event "Activation key detected. Secure mode enabled."
    export $SECURE_MODE_FLAG=1
else
    log_event "No activation key found. Defaulting to plugin fallback mode."
    export $SECURE_MODE_FLAG=0
fi

# === Secure Mode Execution ===
if [[ "${!SECURE_MODE_FLAG}" -eq 1 ]]; then
    log_event "Launching LYRA Core Engine in secure context..."
    
    # Stub for full secure stack — customize below
    if [[ -f "./lyra/core.py" ]]; then
        python3 ./lyra/core.py --secure --key "$ACTIVATION_KEY_PATH"
    else
        log_event "Core engine not found. Abort secure launch."
        exit 1
    fi

else
    log_event "Entering demo interface (plugin-only fallback)..."

    if [[ -f "./scripts/cli_lyra_demo.py" ]]; then
        python3 ./scripts/cli_lyra_demo.py
    else
        log_event "Demo interface not found. Aborting."
        exit 1
    fi
fi

log_event "LYRA execution complete."
echo "---"
