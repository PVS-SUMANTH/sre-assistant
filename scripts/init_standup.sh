#!/bin/bash

LOG_DIR="../data/standup"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/standup_$(date +%Y-%m-%d).log"

echo "🌅 Morning check-in: $(date)"
echo "Today’s Focus Areas (comma-separated):"
read -p "📝 > " areas

echo "Top 3 Tasks for the Day:"
read -p "1. " task1
read -p "2. " task2
read -p "3. " task3

{
  echo "=== Morning Standup: $(date '+%Y-%m-%d %H:%M') ==="
  echo "Focus Areas: $areas"
  echo "Tasks:"
  echo "  1. $task1"
  echo "  2. $task2"
  echo "  3. $task3"
  echo ""
} >> "$LOG_FILE"

echo "✅ Logged your plan to $LOG_FILE"
