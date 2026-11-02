@echo off
cd /d "%~dp0"
title CommerceBuddy AI
where python >nul 2>nul
if errorlevel 1 (
  echo Python is not installed. Install it from https://www.python.org/downloads/
  echo IMPORTANT: tick "Add python.exe to PATH" during installation.
  pause & exit /b 1
)
if not exist ".env" copy ".env.example" ".env" >nul
start "" cmd /c "timeout /t 2 >nul & start http://127.0.0.1:8000"
python backend\app.py
if errorlevel 1 echo Something went wrong. See README.md - Troubleshooting.
pause
