# -*- mode: python -*-

block_cipher = None

a = Analysis(['SRT2KMLConverter.py'],
             pathex=['C:\\Projects\\SRT2KMLConverter\\'],
             binaries=[],
             hiddenimports=[
                    'sip',
             ],
             datas=[
                ('assets', 'assets'),
                ('assets/g2', 'assets/g2')

            ],
             hookspath=None,
             runtime_hooks=[],
             excludes=[
             'PyQt5',
             'PyQt5.QtCore',
             'PyQt5.QtGui',
             'PyQt5.QtWidgets',
             'gfortran',
             'libopenblas'
             ],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SRT/KML Converter',
          key='fWexFwr9PwelDsgn',
          debug=False,
          strip=False,
          manifest=None,
          icon='ui/assets/g2/usr.ico',
          bootloader_ignore_signals=False,
          upx=True,
          console=False,
          exclude_binaries=False)  # Changed to False
