#!/bin/bash

echo "Bienvenido al programa que descarga Python por ti"
echo "1.Descargar Python3 para Windows (32 bits)\n2.Descargar Python3 para Windows (64 bits)\n3.Descargar Python3 para macOS\n4.Descargar Python3 para Linux (Debian)\n5.Salir"
echo "\nSelecciona la opcion que deseas escoger"
read OPCION
reg='^[1-5]{1}$'
while [[ ! $OPCION =~ $reg ]]
do
 echo "Porfavor seleccione una de las opciones con su número correspondiente\n"
 echo "Selecciona la opcion que deseas escoger"
 read OPCION
done
if [ $OPCION == 1 ]
then
  echo "Descargando Python3 para Windows (32 bits)\n\n"
  curl "https://www.python.org/ftp/python/3.9.1/python-3.9.1.exe" -O
elif [ $OPCION == 2 ]
then
  echo "Descargando Python3 para Windows (64 bits)\n\n"
  curl "https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe" -O
elif [ $OPCION == 3 ]
then
  echo "Descargando Python3 para macOS\n\n"
  curl "https://www.python.org/ftp/python/3.9.1/python-3.9.1-macos11.0.pkg" -O
elif [ $OPCION == 4 ]
then
  echo "Descargando Python3 para Linux (Debiam)"
  curl "https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz" -O
elif [ $OPCION == 5 ]
then
  exit
fi
