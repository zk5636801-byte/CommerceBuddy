# CommerceBuddy AI - Your Personal AI Commerce Professor

## Run it (Windows, no installs except Python)
1. Install Python from https://www.python.org/downloads/ (tick "Add python.exe to PATH"). Needs internet once.
2. Unzip this folder. Double-click **START_OFFLINE_DEMO.bat** (no AI key needed) or **START_COMMERCEBUDDY.bat** (uses AI if a key is set).
3. Your browser opens at http://127.0.0.1:8000. Use **Google Chrome or Microsoft Edge**. Keep the black window open; close it to stop.
No packages to install: the backend uses only Python's built-in libraries.

## Turn on real AI
1. Get an API key from https://console.anthropic.com
2. Run START_COMMERCEBUDDY.bat once (it creates a file named `.env`), close it.
3. Open `.env` in Notepad, paste the key after `ANTHROPIC_API_KEY=`, save, start again. Header shows "Online AI". The key stays on the laptop's backend and is never sent to the browser. Never share `.env`.

## Voice
- Speech output: the browser's built-in voices (works offline if the voice is installed).
- Speech input: Chrome/Edge Web Speech API. It sends audio to the browser vendor's cloud, so it **needs internet** and microphone permission. It is push-to-talk: the mic is only on after you tap Speak. Nothing is recorded or stored by this app. If voice fails, type instead.

## Answer sources are labelled
"AI answer", "Calculator" (exact built-in maths: simple/compound interest, current ratio, gross profit, break-even, elasticity, straight-line depreciation) and "Offline knowledge base" (about 17 topics).

## Move to another laptop
Copy the whole folder (USB), install Python there, double-click a START file. Copy `.env` too only if you want AI (keep it private).

## Troubleshooting
- "Python is not installed": reinstall Python and tick Add to PATH.
- Page says Backend not running: the black window was closed; start again.
- Port busy: close other CommerceBuddy windows.
- Mic blocked: click the lock icon next to the address, allow Microphone, refresh.
- No voice/Speak disabled: use Chrome or Edge, and check internet.
- "API key rejected": re-paste the key in `.env`.

## Tests
Double-click nothing; in the folder's address bar type `cmd`, then `python tests\test_calc.py`.

## Known limitations
Voice input needs internet and Chrome/Edge. Offline mode knows only a small set of topics. The AI can make mistakes; verify important facts. Law answers are general education, not legal advice. Visuals and voice were not tested on real Windows hardware (see TEST_REPORT.md).

## Exhibition questions
What is inflation? | Explain demand and supply | Difference between void and voidable contract | What is the accounting equation? | Simple interest on 5000 at 8% for 3 years | Break even fixed cost 5000 price 100 variable cost 50 | Explain GDP in simple words | What is the marketing mix?

## Presentation script
"CommerceBuddy AI is my commerce tutor. Ask by voice or typing. A Python backend keeps the AI key safe; each answer is labelled as AI, calculator or offline notes, so nothing is faked. Numbers come from exact formulas, not guesses. Without internet it still works in offline demo mode."
