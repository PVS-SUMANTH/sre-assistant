import os
import json
import requests
from datetime import datetime

TEAMS_WEBHOOK_URL = os.getenv("TEAMS_WEBHOOK_URL")
FOCUS_LOG_PATH = os.path.expanduser("~/sre-agent/data/focus/focus_" + datetime.now().strftime("%Y-%m-%d") + ".log")
SUMMARY_PATH = os.path.expanduser("~/sre-agent/data/summary/summary_" + datetime.now().strftime("%Y-%m-%d") + ".md")

# Load summary content
if os.path.exists(SUMMARY_PATH):
    with open(SUMMARY_PATH, 'r') as f:
        summary_content = f.read()
else:
    summary_content = "⚠️ No summary generated. GPT may not have run."

# Check for missed check-ins (assuming 30-min interval from 9 AM to 2 PM => 10 entries expected)
expected_entries = 10
focus_checkins = []
if os.path.exists(FOCUS_LOG_PATH):
    with open(FOCUS_LOG_PATH, 'r') as f:
        focus_checkins = [line for line in f.readlines() if line.strip()]

missed_count = max(0, expected_entries - len(focus_checkins))
reminder_text = ""
if missed_count > 2:
    reminder_text = f"\n🚨 *Missed {missed_count} focus check-ins!* Stay locked in, warrior."

# Format for Teams
teams_message = {
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "summary": "Daily Standup Summary",
    "themeColor": "0078D7",
    "title": "🤖 SRE Daily Standup Summary",
    "text": f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n{summary_content}{reminder_text}"
}

# Send to Teams
if TEAMS_WEBHOOK_URL:
    response = requests.post(TEAMS_WEBHOOK_URL, headers={"Content-Type": "application/json"}, data=json.dumps(teams_message))
    if response.status_code == 200:
        print("✅ Standup summary sent to Teams.")
    else:
        print(f"❌ Failed to send to Teams. Status code: {response.status_code}")
else:
    print("⚠️ TEAMS_WEBHOOK_URL not set. Please export it in .env or shell environment.")
