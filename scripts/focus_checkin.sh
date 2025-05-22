#!/bin/bash

LOG_DIR="../data/focus"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/focus_$(date +%Y-%m-%d).log"

echo "🔁 [$(date '+%H:%M:%S')] Focus check-in triggered."

read -t 300 -p "🧠 What are you working on right now? (5 min timeout) > " response

if [[ -z "$response" ]]; then
  response="⚠️ No response. Possibly distracted or away."
fi

echo "[$(date '+%H:%M:%S')] $response" >> "$LOG_FILE"
