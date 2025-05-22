#!/bin/bash

LOG_DIR="../data/commands"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/commands_$(date +%Y-%m-%d).log"

# Get history entries since 12am today
today=$(date '+%Y-%m-%d')
history_file="$HOME/.bash_history"
[[ -f "$HOME/.zsh_history" ]] && history_file="$HOME/.zsh_history"

echo "🔍 Scanning commands for: $today"

awk -v d="$today" '
  $0 ~ d {
    print $0
  }
' "$history_file" >> "$LOG_FILE"

echo "📁 Saved terminal commands to $LOG_FILE"
