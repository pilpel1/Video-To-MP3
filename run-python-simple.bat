@echo off
cd /d %~dp0
echo Running MP4 to MP3 Converter...
python mp4_to_mp3.py
echo.
echo Conversion completed! Press any key to exit.
pause
