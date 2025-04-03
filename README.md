# Video To MP3 Converter

A simple tool to convert video files to MP3 audio format.

[Hebrew version below | גרסה בעברית בהמשך](#hebrew)

## Overview
This project is a simple tool for converting video files to MP3 audio files. The software is designed to be accessible to non-technical users and can be distributed as a standalone executable without installation requirements.

## Technologies
- Python 3.x
- MoviePy - for video and audio processing
- FFmpeg - for encoding and conversion (included in the project)
- PyInstaller - for creating a standalone executable

## Project Structure
```
Audio_from_video/
├── mp4_to_mp3.py           # Main source code
├── build_exe.bat           # Script to generate executable
├── mp4_to_mp3.spec         # PyInstaller configuration
├── run-python-simple.bat   # Run through Python
├── app_icon.ico            # Executable icon
├── README.txt              # End-user instructions
├── README.md               # Development documentation (this file)
├── ffmpeg/                 # FFmpeg for executable
├── ffmpeg-minimal/         # Minimal version of FFmpeg
├── input-videos/           # Input directory for video files
└── output-audios/          # Output directory for audio files
```

## Installation (for Development)

### Prerequisites
- Python 3.8 or newer
- [FFmpeg](https://ffmpeg.org/download.html) - although the project comes with its own version, you might want to install a full version for development

### Installing Required Python Libraries
```bash
pip install moviepy
pip install pyinstaller
```

## Running the Software in Development
You can run the software directly from the source code:
```bash
python mp4_to_mp3.py
```
Or using the included batch file:
```bash
run-python-simple.bat
```

## Building an Executable
To build a standalone executable (EXE):
```bash
build_exe.bat
```
The output will be in the `dist/` directory.

## Development Notes
1. The software comes with built-in FFmpeg located in the project directory, which simplifies the user experience and removes the need to install additional software.

2. The spec file is configured to clean out unused libraries to reduce the final EXE file size.

3. The code is built to work both as a script and as a compiled executable through PyInstaller.

## Licensing
FFmpeg licensing information should be included according to its terms of use.

---

<a name="hebrew"></a>
# ממיר וידאו ל-MP3

המרת קבצי וידאו (MP4, AVI, MOV, MKV) לפורמט אודיו MP3 בקלות.

## סקירה
פרויקט זה הוא כלי פשוט להמרת קבצי וידאו לקבצי אודיו בפורמט MP3. התוכנה נבנתה כך שתהיה נגישה למשתמשים שאינם טכניים, וניתנת להפצה כקובץ הרצה עצמאי ללא צורך בהתקנה.

## טכנולוגיות
- Python 3.x
- MoviePy - לעיבוד הווידאו והאודיו
- FFmpeg - לקידוד והמרה (כלול בתוך הפרויקט)
- PyInstaller - ליצירת קובץ הרצה סטנדלוני

## מבנה הפרויקט
```
Audio_from_video/
├── mp4_to_mp3.py           # קוד המקור הראשי
├── build_exe.bat           # סקריפט להפקת קובץ הרצה
├── mp4_to_mp3.spec         # הגדרות PyInstaller
├── run-python-simple.bat   # הרצת התוכנה דרך Python
├── app_icon.ico            # אייקון לקובץ ההרצה
├── README.txt              # הוראות למשתמש הקצה
├── README.md               # תיעוד לפיתוח (קובץ זה)
├── ffmpeg/                 # FFmpeg להפקת הקובץ
├── ffmpeg-minimal/         # גרסה מינימלית של FFmpeg
├── input-videos/           # תיקיית קלט לקבצי וידאו
└── output-audios/          # תיקיית פלט לקבצי אודיו
```

## התקנה (לפיתוח)

### דרישות מקדימות
- Python 3.8 או גרסה חדשה יותר
- [FFmpeg](https://ffmpeg.org/download.html) - למרות שהפרויקט מגיע עם גרסה משלו, ייתכן שתרצה להתקין גרסה מלאה לפיתוח

### התקנת ספריות Python הנדרשות
```bash
pip install moviepy
pip install pyinstaller
```

## הפעלת התוכנה בפיתוח
ניתן להריץ את התוכנה ישירות מקוד המקור:
```bash
python mp4_to_mp3.py
```
או באמצעות קובץ האצווה המצורף:
```bash
run-python-simple.bat
```

## בניית קובץ הרצה
כדי לבנות קובץ הרצה עצמאי (EXE):
```bash
build_exe.bat
```
התוצאה תהיה בתיקיית `dist/`.

## הערות פיתוח
1. התוכנה מגיעה עם FFmpeg מובנה וממוקם בתיקיית הפרויקט, מה שמקל על חוויית המשתמש ומסיר את הצורך בהתקנת תוכנות נוספות.

2. קובץ ה-spec מוגדר לנקות ספריות שאינן בשימוש כדי לצמצם את גודל קובץ ה-EXE הסופי.

3. הקוד בנוי כך שיעבוד הן כסקריפט והן כקובץ הרצה מקומפל דרך PyInstaller.

## מתן רישיון
יש לכלול מידע על הרישיון של FFmpeg בהתאם לתנאי השימוש שלו. 