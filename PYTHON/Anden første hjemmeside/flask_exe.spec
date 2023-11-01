# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['flask_exe.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['email','email.message',
                   'email.mime.message','email.mime.image',
                   'email.mime.text','email.mime.multipart',
                   'email.mime.audio','email.mime.multipart',
                   ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

def extra_datas(mydir):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if is.path.isfile(d):
                files.append(d)
            rec_glob("%s/'" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    extra_datas = []
    for f in files:
        extra_datas.append((f, f, 'DATA'))
    return extra_datas

#include our "data" directiories
a.datas += extra_datas("static")
a.datas += extra_datas("templates")

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='flask_exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
