@echo off
echo ================================================
echo    APP Video Server - Starting...
echo ================================================
echo.

echo [1/2] Starting local file server on port 8080...
start "FileServer-8080" cmd /k "cd /d %~dp0 && python cors_server.py"

echo Waiting for file server to start...
timeout /t 3 /nobreak > nul

echo [2/2] Starting ngrok tunnel...
start "ngrok-tunnel" cmd /k "ngrok http --domain=game-semisoft-routine.ngrok-free.dev 8080"

echo.
echo ================================================
echo  Done! Two windows should now be open.
echo  Video URL: https://game-semisoft-routine.ngrok-free.dev/videos/1.mp4
echo ================================================
echo.
pause
