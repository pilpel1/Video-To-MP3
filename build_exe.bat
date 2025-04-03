@echo off
echo Building Video To MP3 Converter exe...
echo.

rem Clean previous build
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

rem Copy ffmpeg to directory for packaging
if not exist ffmpeg mkdir ffmpeg
copy ffmpeg-minimal\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe ffmpeg\ffmpeg.exe

rem Check if icon exists
if not exist app_icon.ico (
    echo Warning: app_icon.ico not found. The exe will use the default icon.
    echo To add a custom icon, place app_icon.ico in this directory.
    echo.
)

rem Build the exe
pyinstaller mp4_to_mp3.spec

echo.
if exist "dist\Video To MP3.exe" (
    echo Build completed successfully!
    echo The executable is located at: dist\Video To MP3.exe
    echo.
    echo Size of the executable:
    for %%A in ("dist\Video To MP3.exe") do echo %%~zA bytes
    
    rem Copy README to dist folder
    copy README.txt dist\README.txt
) else (
    echo Build failed!
)

echo.
echo Press any key to exit...
pause > nul 