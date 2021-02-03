from typing import Text
from bs4 import BeautifulSoup as bs
from requests import Session
from openpyxl import Workbook
from openpyxl.styles import Color
import sys 

workbook = Workbook()
sheet = workbook.active

url = "https://pregradovirtual.unemi.edu.ec/login/index.php"

with Session() as s:
    s.verify = False
    site = s.get(url)
    bs_content = bs(site.content, "html.parser")
    token = bs_content.find("input", {"name":"logintoken"})["value"]
    login_data = {"username":"lorem","password":"ipsum", "logintoken":token}
    s.post(url, login_data)

    nombreCompleto = "Raúl Alberto García Campodónico"

    links = ['https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4870', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4871', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4872', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4874', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4876', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=4877']
    arrayTareasLinks = []
    arrayTitulos = []
    arrayTipo = []
    arrayMateria = []
    days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    i = 1
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
                    for p in fechas:
                        d = p.text
                        if any(day in d for day in days):
                            date = d
                        
                    nombreMateria = materia.text
                    sheet["A"+str(i)] = nombreMateria.split("-", 1)[0]
                    sheet["B"+str(i)] = alt["alt"]
                    sheet["C"+str(i)] = date.split("el", 1)[1]
                    i += 1
                    
                if alt["alt"] == "Tarea":
                    table = readable.find_all("td", attrs={"class": "c1"})
                    if table[1].text == "Enviado para calificar" or table[0].text == "Enviado para calificar":
                        nombreMateria = materia.text
                        sheet["A"+str(i)] = nombreMateria.split("-", 1)[0]
                        sheet["B"+str(i)] = alt["alt"]
                        sheet["C"+str(i)] = "Entregado, dont worry"
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
    #         for link in arrayTareasLinks:
    #             html2 = s.get(link)
    #             readable = bs(html2.content, "lxml")
    #             h2 = readable.find("h2")
    #             objetivo = readable.find("p", id="text")
    #             arrayTitulos.append(h2)
    
    # print(arrayTipo)



