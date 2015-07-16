from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('char.py', base=base),
    Executable('meta_char.py', base=base),
    Executable('bg_generate.py', base=base)
]

setup(name='Cyberpunk Char Creator',
      version = '1.0',
      description = 'Char Creator and Metachar creator for cyberpunk v3',
      options = dict(build_exe = buildOptions),
      executables = executables)
