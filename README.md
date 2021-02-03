# scraperUnemi
Un webscraper el cual generará un excel con todos los deberes y sus fechas de entrega a los estudiantes de la carrera de TICS en linea en la Universidad Estatal de Milagro.

### Pre-requisitos 

Este webscraper utiliza las librerías BeautifulSoup4, Requests, lxml y OpenPyxl las cuales se deben instalar en su computador utilizando pip.
Python 3 es preferible, para verificar su versión de python ejecute este comando en su terminal.
```
> python --version
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
> python get-pip.py
```

### Instalación de librerías
Las librerías deben ser instaladas para el correcto funcionamiento del webscraper utilizando pip con los siguientes comandos:
```
> pip install beautifulsoup4
> pip install requests
> pip install openpyxl
> pip install lxml
```

### Instalación 🔧

La instalación es sencilla, se va a descargar un .zip el cual contiene el programa, la licencia y este README.txt.
Al extraer el .zip, si se ha seguido los pasos anteriores, un simple comando para ejecutar el webscraper funcionará 

```
> python escobaUnemi.py
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

#### Ingreso automático 

En la línea número 32, el programa define la variable en la que se almacenan las variables user y password. Si se quiere saltar el paso de inicio de credenciales en vez de tener:
```
    login_data = {"username":str(user),"password":str(password), "logintoken":token}
```

Se puede remplazar las variables con las credenciales escritas de esta manera:
```
    login_data = {"username":"nombre de usuario entre comillas","password":"contraseña entre comillas", "logintoken":token}
```
y se comenta (con el simbolo # en el inicio de la linea) o se borra la linea 9 y 10 donde se ejecuta el input de esta manera:
```
    #user = input("Ingresa tu usuario del pregrado virtual, el cual es el mismo que el sga: ")
    #password = input("Ingresa tu contraseña del pregrado virtual, esta contraseña no se guarda en ninguna base de datos: ")
```

#### Selección de la carrera para el webscraper 

Es posible que el la linea 36, donde se tienen en un array los url de la sección de calificaciones de cada materia, pueda ser intercambiada por los links de materias de otra carrera y si estas siguen el mismo layout de las materias en la carrera de TICS en linea, es posible que funcione sin problemas.
```
links = ['https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4870', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4871', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4872', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4874', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4876', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4877']
```

Solo se agrega el link entre comillas y se separa con comas.

Si eres alguien de otra carrera y esto no funciona y quieres tener un programa similar a este porfavor contactate conmigo y yo lo desarrollaré o si alguien ha modificado esta paerte del codigo y funcionó para otra carrera de la UNEMI o para otra universidad concactense conmigo y dejenmelo saber.


### Bugs conocidos

Existen veces que los profesores modifican las tareas de maneras diferentes a las que el programa busca, asi que de vez en cuando en vez de imprimir la fecha de entrega, se imprime otro tipo de información, no hay una solución para esto además de esperar a que los profesores sigan mandando tareas de la misma manera que lo hacen siempre 

## Construido con 

* Python
* BeautifulSoup4
* Requests
* OpenPyxl

## Autores 

Este proyecto fue desarrollado por:

* **Raúl Alberto García** 

## Licencia

Este proyecto está bajo la Licencia GNU Lesser General Public License v3.0 - mira el archivo LICENSE.md para detalles

## Expresiones de Gratitud 

* Este proeycto comenzó por necesidad propia ya que soy experto en olvidarme en deberes, pero al desarrollarlo quise compartirlo con todos los que lo necesitan.
* Si este programa les sirvio de alguna manera, la manera que pueden agradacerme es no compartiendo este archivo directamente con otros compañeros, a mi me ayuda muchisimo que lo descarguen desde mi github. 
