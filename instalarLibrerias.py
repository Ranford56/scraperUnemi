import subprocess
import sys


def install(package):
    	subprocess.check_call([sys.executable, "-m", "pip", "install", package])

librerias = ['PySimpleGUI', 'beautifulsoup4', 'requests', 'openpyxl']

for lib in librerias:
        install(lib)