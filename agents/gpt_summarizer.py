import os
import openai
from datetime import datetime

# Load API key
openai.api_key = os.getenv("OPENAI_API_KEY")
today = datetime.now().strftime("%Y-%m-%d")

# Base directory for all logs and summaries
BASE_DIR = "/Users/paramathmuni.s/Desktop/rnd/automations/sre-assistant"

focus_log_path = os.path.join(BASE_DIR, f"data/focus/focus_{today}.log")
command_log_path = os.path.join(BASE_DIR, f"data/commands/command_{today}.log")
summary_output_path = os.path.join(BASE_DIR, f"data/summary/summary_{today}.md")

def read_log(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return f.read()
    return "No data logged."

# Read inputs
focus_data = read_log(focus_log_path)
command_data = read_log(command_log_path)

# GPT prompt
prompt = f"""
You're a productivity assistant helping an SRE engineer summarize their work for a daily standup. Here's their data:

=== Focus Check-Ins ===
{focus_data}

=== Terminal Commands ===
{command_data}

Generate a structured Markdown report with:
- Summary of tasks done
- Any patterns in focus (e.g., distracted, deep work)
- What might be improved or followed up
- Include a positive sign-off line

Be clear, concise, and professional.
"""

print("🔄 Generating summary using GPT...")

try:
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use "gpt-3.5-turbo" if you're on a free-tier
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    summary_text = response['choices'][0]['message']['content']

    os.makedirs(os.path.dirname(summary_output_path), exist_ok=True)
    with open(summary_output_path, 'w') as f:
        f.write(summary_text)

    print(f"✅ Summary saved to {summary_output_path}")

except Exception as e:
    print(f"❌ GPT summarization failed: {e}")