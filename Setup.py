from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = 'C:\\Python36\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'C:\\Python36\\tcl\\tk8.6'

base = 'Win32GUI' #None    

executables = [Executable('ZEUM.py', base=base, icon='logo.ico')]

packages = ['idna', 'tkinter', 'random', 'tkinter.messagebox', 'tkinter.filedialog']
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = 'ZEUM',
    options = options,
    version = '1.6',
    description = 'ZEUM Chiffrement, Cryptage Décryptage Binaire Avancé',
    executables = executables
)
