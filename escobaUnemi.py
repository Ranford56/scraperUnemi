from bs4 import BeautifulSoup as bs
from requests import Session
import requests, json
from datetime import datetime
import locale
from todoist.api import TodoistAPI, json_default
locale.setlocale(locale.LC_TIME, '')

api = TodoistAPI('918c229832c4a9aa038294ac0e406f903f744b4f')
api.sync()

def jsonTodoist():
    data = api.projects.get_data(2271037183)
    data2 = data['items']
    jsonString = json.dumps(data2)
    jsonFile = open('todoist.json', 'w')
    jsonFile.write(jsonString)
    jsonFile.close()
jsonTodoist()


global s
s = Session()

def meh(username, password):

    #Url del login de pregradovirtual.unemi.edu.ec
    url = "https://pregradovirtual.unemi.edu.ec/login/index.php"

    #Automatización del login
    s.verify = False    #se conecta de manera HTTP en vez de HTTPS, esto es lo que crea todos los warnings
    site = s.get(url)
    bs_content = bs(site.content, "html.parser")
    token = bs_content.find("input", {"name":"logintoken"})["value"]
    login_data = {"username":str(username),"password":str(password), "logintoken":token}
    print(s.post(url, login_data))
    s.post(url, login_data)

    #Proceso de recolleción de datos
    i = 1
        #Array de links de los sitios de calificaciones de cada materia
    links = ['https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=319', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=314', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=315', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=317', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=318', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=316', 'https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=313','https://pregradovirtual.unemi.edu.ec/grade/report/user/index.php?id=2126']

    #Definición de variables y herramintas para el proceso de recolección de datos
    arrayTareasLinks = []
    arrayTipo = []
    days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    for site in links:
        html = s.get(site)
        soup = bs( html.content, "lxml" )
        materia = soup.find("h3", class_="page-title")
        print('materia')
        print(materia)
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
                        print(datePrint)
                        nombreMateria = materia.text
                        addTask(h2.text, nombreMateria.split("-", 1)[0], dateFormatChanger(datePrint.strip()), minia["href"])
                        #createPage(dbID, headers, selector(alt["alt"], tipoActividades), dateFormatChanger(datePrint.strip()), selector(nombreMateria.split("-", 1)[0], materias), h2.text, minia["href"])
                        i += 1
                if alt["alt"] == "Cuestionario":
                    pSearcher = readable.find("div", class_="quizinfo")
                    fechas = pSearcher.find_all("p")
                    spans = readable.find("span", class_="statedetails")

                    for p in fechas:
                        d = p.text
                        if any(day in d for day in days):
                            date = d
                            fecha = date.split("el", 1)[1]

                    nombreMateria = materia.text
                    addTask(h2.text, nombreMateria.split("-", 1)[0], dateFormatChanger(fecha.strip()), minia["href"])
                    #createPage(dbID, headers, selector(alt['alt'], tipoActividades), dateFormatChanger(fecha.strip()), selector(nombreMateria.split("-", 1)[0], materias), h2.text, minia["href"])

                    i += 1

                if alt["alt"] == "Tarea":
                    table = readable.find_all("td", attrs={"class": "c1"})
                    print(minia["href"])
                    if 'GRUPO' in table[0].text.upper():
                        nombreMateria = materia.text
                        if dateFormatChanger(table[3].text.strip()) is False:
                            continue
                        else:
                            fechaArreglada = dateFormatChanger(table[3].text.strip())
                        print(type(fechaArreglada))
                        addTask(h2.text, nombreMateria.split("-", 1)[0], fechaArreglada, minia["href"])
                        #createPage(dbID, headers, selector(alt['alt'], tipoActividades), fechaArreglada, selector(nombreMateria.split("-", 1)[0], materias), h2.text, minia["href"])
                    else:
                        nombreMateria = materia.text
                        addTask(h2.text, nombreMateria.split("-", 1)[0], dateFormatChanger(table[2].text.strip()), minia["href"])
                        #createPage(dbID, headers, selector(alt['alt'], tipoActividades), dateFormatChanger(table[2].text.strip()), selector(nombreMateria.split("-", 1)[0], materias), h2.text, minia["href"])

                        i += 1


tipoActividades = [
    {"id": "0f43a7d8-0112-4449-9574-f9f05fea6fec",
	"name": "Tarea",
	"color": "pink"},
    {"id": "e8f6cd22-73ed-4b0f-ab62-e360da3d58b2",
	"name": "Foro",
	"color": "orange"},
    {"id": "055b3d92-a382-4b49-b0c9-be7fde6be98a",
	"name": "Cuestionario",
	"color": "blue"}
]

materias = [
	{"id": "62e144d8-17a8-4b96-9421-076dac92012a",
	"name": "Probabilidad y Estadística ",
	"color": "pink"},
	{"id": "2473e5b2-d5e7-4ca4-a722-0abb4363ef81",
	"name": "Ingles I (General English)",
	"color": "purple"},
	{"id": "42fffb71-e419-4b68-8cbb-3c3b58f09aa6",
	"name": "Matemáticas Discretas ",
	"color": "gray"},
	{"id": "440ccbff-6419-4ccc-a5b6-fd594282d51f",
	"name": "Epistemología de la investigación ",
	"color": "blue"},
	{"id": "5bc6f8e7-1ea9-4eff-8142-1a42766fdbb0",
	"name": "Electricidad y Magnetismo",
	"color": "green"},
	{"id": "403a1184-bb76-4fb7-8bd9-ebc6b4e80646",
	"name": "Cálculo Integral y Vectorial ",
	"color": "red"},
	{"id": "70e411eb-03fb-48ea-9177-d31ed9e4fb6d",
	"name": "Programación Orientada a Objetos ",
	"color": "brown"},
	{"id": "d4485fd0-f932-4c07-b7cf-148775cdb9fc",
	"name": "Apreciación del Arte y Cultura ",
	"color": "orange"}
]
def createPage(dbID, headers, tipoActividad, fecha, materia, nombre, link):
    createUrl = 'https://api.notion.com/v1/pages'
    newPageData={
        'parent': {'database_id': dbID},
        "properties": {
				"Realizado por": {
					"id": "BTaX",
					"type": "multi_select",
					"multi_select": []
				},
				"Tipo": {
					"id": "WImE",
					"type": "select",
					"select": tipoActividad
				},
				"Fecha de estudio": {
					"id": "ZfKl",
					"type": "date",
					"date": {
						"start": fecha,
						"end": None
					}
				},
				"Materia": {
					"id": "odsw",
					"type": "select",
					"select": materia
				},
				"Nombre": {
					"id": "title",
					"type": "title",
					"title": [
						{
							"type": "text",
							"text": {
								"content": nombre,
								"link": None
							},
							"annotations": {
								"bold": False,
								"italic": False,
								"strikethrough": False,
								"underline": False,
								"code": False,
								"color": "default"
							},
							"plain_text": nombre,
							"href": None
						}
					]
				}
			},
    }
    data = json.dumps(newPageData)
    res = requests.request('POST', createUrl, headers=headers, data=data)
    print(res.status_code)
    addTask(materia, nombre, fecha, link)
def updatePage(pageId, headers):
    updateUrl = f'https://api.notion.com/v1/pages/{pageId}'
    updateData = {
        "properties": {
            "Materia": {
                "id": "gJaW",
                "type": "relation",
                "relation": [
                    {
                        "id": '0da60ff5-acb5-44c8-92c3-4d3f409dc5c6'
                    }
                ]
            }
        }
    }
    data = json.dumps(updateData)
    res = requests.request('PATCH', updateUrl, headers=headers, data=data)
    print(res.status_code)
#createPage(dbID, headers)

def deletePages(pageId, headers):
    updateUrl = f'https://api.notion.com/v1/pages/{pageId}'
    updateData={
		"archived": True
	}
    data = json.dumps(updateData)
    res = requests.request('PATCH', updateUrl, headers=headers, data=data)
    print(res.status_code)

def selector(name, lista):
    materia = name.lower().strip().replace(" ", "")
    print(materia)
    materias = lista
    for dic in materias:
    	if materia in dic['name'].lower().strip().replace(" ", ""):
         print(dic['name'].lower().strip().replace(" ", ""))
         return dic['name']

def dateFormatChanger(dateStr):
    try:
        if '.' in dateStr:
            y = datetime.strptime(dateStr, '%A, %d de %B de %Y, %H:%M.')
        else:
            y = datetime.strptime(dateStr, '%A, %d de %B de %Y, %H:%M')
        newFormat = y.strftime('%Y-%m-%d')
        return newFormat
    except Exception:
        return False

def search(name):
    with open('./todoist.json') as jsonFile:
        items = json.load(jsonFile)
        for keyval in items:
            if name == keyval['description']:
                return keyval['id']

def addTask(nombre, materia, fecha, link):
    if search(link):
        updateTask(fecha, search(link))
    else:
        data = api.projects.get_data(2271037183)
        meh = data['items']
        if meh ==[]:
            task = api.items.add(content=str(materia)+'-'+str(nombre), description=link, project_id=2256798468, section_id=57173105, due={'date': fecha, 'is_recurring': False})
        else:
            task = api.items.add(content=str(materia)+'-'+str(nombre), description=link, project_id=2256798468, section_id=57173105, due={'date': fecha, 'is_recurring': False})

def updateTask(fecha, Id):
    item = api.items.get_by_id(Id)
    item.update(due={'date': fecha, 'is_recurring': False})


meh('user', 'pass')
api.commit()