# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['mc_chunk_get_V2_py_edition_final.py'],
             pathex=['/home/flux/.python/MC_Chunk_Get/src'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['PyQt5.QtNetwork','PyQt5.QtOpenGL','PyQt5.QtPrintSupport','PyQt5.QtQml','PyQt5.QtQuick','PyQt5.QtSensors','PyQt5.QtSerialPort','PyQt5.QtSql','PyQt5.QtSql','PyQt5.QtSvg','PyQt5.QtTest','PyQt5.QtHelp','PyQt5.QtMultimedia','PyQt5.QtQuickWidgets','PyQt5.QtXml','xml.etree.cElementTree.','xml','sysconfig','_tkinter','distutils','lib2to3','pydoc','PyQt5.QtWebEngineWidgets'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='mc_chunk_get_v2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='mc_chunk_get.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='mc_chunk_get_v2')
