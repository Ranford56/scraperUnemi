# scraperUnemi
Un webscraper el cual generará un excel con todos los deberes y sus fechas de entrega a los estudiantes de la carrera de TICS en linea en la Universidad Estatal de Milagro.

## Instalación y Ejcución
Solo se descarga todos los archivos en formato .zip y se extraen para su ejecución.

Primero se tiene que ejecutar el archivo instaladorDeLibrerias.py, el cual instala todas las librerias necesarias, y al terminar la ejecución de este, se ejecuta escobaUnemi.py, el cual es el webscraper que genera el excel
```
> python3 instaladorDeLibrerias.py
> python3 escobaUnemi.py
```

### Pre-requisitos 

Este webscraper utiliza las librerías BeautifulSoup4, Requests, lxml y OpenPyxl las cuales se deben instalar en su computador utilizando pip.
Python 3 es preferible, para verificar su versión de python ejecute este comando en su terminal.
```
> python3 --version
```
Si al ejecutarlo, la terminal devuelve una version de Python 3 o mayor, como lo hace en el ejemplo de abajo, podemos saltar el paso de actualizar Python.
```
Python 3.7.0 
```
Si la version de Python es menor a 3 se puede actualizar Python descargargando el ejecutable desde el sitio https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe y ejecutar el instalador (si se instala de esta manera, asegurarse de selecciónar la opcion pip en el proceso de instalación).

Para instalar pip se necesita descargar el archivo _get-pip.py_, ell cual se puede obtener con este comando:
```
> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

y ejecutarlo con python
```
> python3 get-pip.py
```

### Instalación de librerías
Las librerías deben ser instaladas para el correcto funcionamiento del webscraper utilizando pip con los siguientes comandos:
```
> pip3 install beautifulsoup4
> pip3 install requests
> pip3 install openpyxl
> pip3 install lxml
> pip3 install pyqt5
```

## Ejecución

Al ejecutarse, se debe introducir las credenciales del pregradocirtual.unemi.edu.ec, estas credenciales no se almacenan de ninguna manera que el desarrollador pueda acceder a ellas.

Una vez introducidas las credenciales se van a devolver varias de estas alertas
```
InsecureRequestWarning: Unverified HTTPS request is being made to host 'pregradovirtual.unemi.edu.ec'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
```
La razón de estas es por el tipo de conexión, Python a veces tiene problemas con la verificación de conexión así que para asegurar el funcionamiento del progama en todos los dispocitivos la verificación esta desactivada.
Quiero enfatizar que estas deciciones no afectan la seguridad de sus credenciales ya que estas credenciales van directamente al sitio de https://pregradovirtual.unemi.edu.ec/login/index.php

Al terminar la ejecución se va a crear un excel llamado "horario" con la información obtenida en la carpeta donde se ejecutó el programa 
### Trucos

En esta sección voy a demostrar varias modificaciones del código que, en mi opinión, son útiles. También espero que personas con mayor conocimiento que yo en Python puedan mejorarlo de cierta manera y contactarse conmigo para subir los cambios a github.

### Bugs conocidos

Existen veces que los profesores modifican las tareas de maneras diferentes a las que el programa busca, asi que de vez en cuando en vez de imprimir la fecha de entrega, se imprime otro tipo de información, no hay una solución para esto además de esperar a que los profesores sigan mandando tareas de la misma manera que lo hacen siempre 

## Construido con 

* Python
* BeautifulSoup4
* Requests
* OpenPyxl
* Qt Designer
* PyQt5

## Autores 

Este proyecto fue desarrollado por:

* **Raúl Alberto García** 

## Licencia

Este proyecto está bajo la Licencia GNU Lesser General Public License v3.0 - mira el archivo LICENSE.md para detalles

## Expresiones de Gratitud 

* Este proeycto comenzó por necesidad propia ya que soy experto en olvidarme en deberes, pero al desarrollarlo quise compartirlo con todos los que lo necesitan.
* Si este programa les sirvio de alguna manera, la manera que pueden agradacerme es no compartiendo este archivo directamente con otros compañeros, a mi me ayuda muchisimo que lo descarguen desde mi github. 
