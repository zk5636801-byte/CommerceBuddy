@echo off
cd /d "%~dp0"
set "PATH=%LOCALAPPDATA%\Programs\MinGit\cmd;%PATH%"
echo =======================================================
echo Pushing CommerceBuddy to GitHub
echo Repository: https://github.com/zk5636801-byte/CommerceBuddy.git
echo =======================================================
echo.
git push -u origin main
echo.
if %ERRORLEVEL% equ 0 (
    echo =======================================================
    echo SUCCESS! Code is now on GitHub!
    echo Next step: Deploy on Render: https://dashboard.render.com
    echo =======================================================
) else (
    echo.
    echo If GitHub asks for a password, note that GitHub requires a Personal Access Token:
    echo 1. Go to: https://github.com/settings/tokens
    echo 2. Generate a token (classic) with 'repo' checked.
    echo 3. Paste the token as the password.
)
pause
