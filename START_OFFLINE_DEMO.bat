@echo off
cd /d "%~dp0"
title CommerceBuddy AI (Offline Demo)
where python >nul 2>nul || (echo Python is not installed. See README.md & pause & exit /b 1)
set OFFLINE_ONLY=1
start "" cmd /c "timeout /t 2 >nul & start http://127.0.0.1:8000"
python backend\app.py
pause
