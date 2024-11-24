from cx_Freeze import setup, Executable
import os

# Función para recorrer recursivamente un directorio
def list_files(directory, dest):
    files = []
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            src_file = os.path.join(dirpath, filename)
            dest_file = os.path.join(dest, os.path.relpath(src_file, directory))
            files.append((src_file, dest_file))
    return files

# Obtener la lista de archivos en las carpetas adicionales
additional_files = []
additional_files.extend(list_files(os.path.join('GUI', '.ui'), os.path.join('GUI', '.ui')))
additional_files.extend(list_files('source', 'source'))

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {
    'packages': ["pandas", "PySide6", "seaborn", "matplotlib", "numpy", "csv", "os", "sys", "modulos", "GUI"],
    'excludes': [],
    'include_files': additional_files
}

base = 'gui'

executables = [
    Executable('main_UI.py', base=base, target_name='HR')
]

setup(
    name='HRHelper',
    version='0.0.1',
    description='Programa de ayuda para empleados de recursos humanos',
    options={'build_exe': build_options},
    executables=executables
)
