from bs4 import BeautifulSoup as bs
from requests import Session
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import PatternFill
import sys 

#Input de las credenciales de pregradovirtual.unemi.edu.ec
user = input("Ingresa tu usuario del pregrado virtual, el cual es el mismo que el sga: ")
password = input("Ingresa tu contraseña del pregrado virtual, esta contraseña no se guarda en ninguna base de datos: ")

#Activacion y creación del excel 
workbook = Workbook()
sheet = workbook.active

# Settings del excel generado
sheet.column_dimensions["A"].width = 45
sheet.column_dimensions["B"].width = 20
sheet.column_dimensions["C"].width = 35

#Url del login de pregradovirtual.unemi.edu.ec
url = "https://pregradovirtual.unemi.edu.ec/login/index.php"

#Crea la sesión 
with Session() as s:

    #Automatización del login
    s.verify = False    #se conecta de manera HTTP en vez de HTTPS, esto es lo que crea todos los warnings
    site = s.get(url)
    bs_content = bs(site.content, "html.parser")
    token = bs_content.find("input", {"name":"logintoken"})["value"]
    login_data = {"username":str(user),"password":str(password), "logintoken":token}
    s.post(url, login_data)

    #Array de links de los sitios de calificaciones de cada materia 
    links = ['https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4870', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4871', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4872', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4874', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4876', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4877']

    #Definición de variables y herramintas para el proceso de recolección de datos
    arrayTareasLinks = []
    arrayTitulos = []
    arrayTipo = []
    arrayMateria = []
    days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    i = 1
    entregado = PatternFill(start_color= '7cc464', end_color= '7cc464', fill_type = "solid")

    #Proceso de recolleción de datos
    for site in links:
        html = s.get(site)
        soup = bs( html.content, "lxml" )
        materia = soup.find("h1")
        a = soup.find_all("a", class_="gradeitemheader")
        for minia in a:
            alts = minia.find_all("img", class_="itemicon")
            for alt in alts:
                arrayTipo.append(alt["alt"])
                arrayTareasLinks.append(minia.attrs["href"])
                html2 = s.get(minia["href"])
                readable = bs(html2.content, "lxml")
                h2 = readable.find("h2")
                if alt["alt"] == "Foro":
                    fechas = readable.find("div", class_="alert-info")
                    date = fechas.text
                    
                    if any(day in date for day in days):
                        dateSplitted = date.split("es", 2)
                        datePrint = dateSplitted[2]
                    elif "límite" in date:
                        datePrint = "Cerrado"
                    nombreMateria = materia.text
                    sheet["A"+str(i)] = nombreMateria.split("-", 1)[0]
                    sheet["B"+str(i)] = alt["alt"]
                    sheet["C"+str(i)] = datePrint.strip()
                    i += 1
                if alt["alt"] == "Cuestionario":
                    pSearcher = readable.find("div", class_="quizinfo")                    
                    fechas = pSearcher.find_all("p")
                    spans = readable.find("span", class_="statedetails")
                    if spans is not None:
                        span = spans.text
                        status = span.split(":", 1)
                        if status[0] == "Enviado":
                            fecha = "Enviado, dont worry"
                    else:
                        for p in fechas:
                            d = p.text
                            if any(day in d for day in days):
                                date = d
                                fecha = date.split("el", 1)[1]
                    
                        
                    nombreMateria = materia.text
                    sheet["A"+str(i)] = nombreMateria.split("-", 1)[0]
                    sheet["B"+str(i)] = alt["alt"]
                    sheet["C"+str(i)] = fecha
                    sheet["C"+str(i)].fill = entregado
                    i += 1
                    
                if alt["alt"] == "Tarea":
                    table = readable.find_all("td", attrs={"class": "c1"})
                    if table[1].text == "Enviado para calificar" or table[0].text == "Enviado para calificar":
                        nombreMateria = materia.text
                        sheet["A"+str(i)] = nombreMateria.split("-", 1)[0]
                        sheet["B"+str(i)] = alt["alt"]
                        sheet["C"+str(i)] = "Entregado, dont worry"
                        sheet["C"+str(i)].fill = entregado
                        i += 1
                    else:
                        if materia.text == "ALGEBRA LINEAL - [TI01-01] - C1 - TICS-ENLINEA: Vista: Usuario":
                            nombreMateria = materia.text
                            sheet["A"+str(i)] = nombreMateria.split("-", 1)[0]
                            sheet["B"+str(i)] = alt["alt"]
                            sheet["C"+str(i)] = table[3].text
                            i += 1
                        else:
                            nombreMateria = materia.text
                            sheet["A"+str(i)] = nombreMateria.split("-", 1)[0]
                            sheet["B"+str(i)] = alt["alt"]
                            sheet["C"+str(i)] = table[2].text
                            i += 1

    
workbook.save(filename="horario.xlsx")



