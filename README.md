# 🛠️ SRE Copilot CLI Assistant

A personal AI-powered standup and focus tracker for DevOps/SRE engineers.
Logs your workday, prompts for focus, and summarizes it all into Teams.

## Structure
- scripts/: Bash automation tools
- agents/: Python GPT + Teams integrations
- configs/: API keys, crontabs
- data/: Raw shell history logs
- logs/: Final standup summaries

## Setup
1. Run `crontab configs/crontab.txt`
2. Copy `.env.template` to `.env` and add your secrets
3. Start coding your agents!

Built to help you stay focused, accountable.