from cx_Freeze import setup, Executable
import os

def list_files(directory, dest):
    files = []
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            src_file = os.path.join(dirpath, filename)
            dest_file = os.path.join(dest, os.path.relpath(src_file, directory))
            files.append((src_file, dest_file))
    return files

additional_files = []
additional_files.extend(list_files('GUI', 'GUI'))
additional_files.extend(list_files('source', 'source'))
additional_files.extend(list_files('salidas', 'salidas'))


build_options = {
    'packages': ["pandas", "PySide6", "seaborn", "matplotlib", "numpy", "csv", "os", "sys", "modulos", "GUI", "faker", "random", "openpyxl"],
    'excludes': [],
    'include_files': additional_files
}

base = 'gui'

executables = [
    Executable('main_UI.py', base=base, target_name='HR')
]

setup(
    name='HRHelper',
    version='0.3.0',
    description='Programa de ayuda para empleados de recursos humanos',
    options={'build_exe': build_options},
    executables=executables
)
