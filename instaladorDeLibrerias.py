#!/usr/bin/python 

#ESTE PROGRAMA DEBE SER EJECUTADO ANTES QUE ESCOBAUNEMI.PY PARA SU CORRECTO FUNCIONAMIENTO


#Importa instalador de librerias de python
import pip

#funcion que prepara el comando para la instalacion de librerias
def packetInstaller(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

#array de librerias por instalar
libs = ["beautifulsoup4", "requests", "openpyxl", "lxml", "pyqt5", "pyqt5-tools"]

#por cada libreria en el array, instala esa libreria 
for lib in libs:
    packetInstaller(str(lib))
