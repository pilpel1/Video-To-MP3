# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Define additional files to include in the EXE
added_files = [
    ('ffmpeg/ffmpeg.exe', 'ffmpeg')  # Copy ffmpeg.exe to the ffmpeg directory inside the EXE
]

a = Analysis(
    ['mp4_to_mp3.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=['numpy', 'numpy.core._dtype_ctypes'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'matplotlib', 'PyQt5', 'PIL', 'sqlite3', 'pandas', 'scipy.spatial'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Remove many files from sys library and other unused modules
a.datas = [d for d in a.datas if not 
    (d[0].startswith('tk') or 
     d[0].startswith('tcl') or
     'matplotlib' in d[0] or
     'Qt5' in d[0] or
     'PyQt5' in d[0] or
     'PIL' in d[0] or
     'pandas' in d[0] or
     'test' in d[0] or
     'tests' in d[0] or
     'idle' in d[0])
]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Video To MP3',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Compress file using UPX
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='app_icon.ico',  # Path to your icon file
) 