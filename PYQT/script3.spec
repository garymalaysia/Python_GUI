# -*- mode: python -*-

block_cipher = None


a = Analysis(['script3.py'],
             pathex=['C:\\Users\\FreddyAnthony\\Documents\\Python\\Python_GUI\\PYQT'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='script3',
          debug=False,
          strip=False,
          upx=True,
          console=True )
