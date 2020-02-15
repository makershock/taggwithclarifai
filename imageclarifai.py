# Este es el codigo que hace el llamado a la api directamente y el que genera el json con las tags asociadas a cada una de la imagen mediante su uuid
# en este caso descargue primero las imagenes con el archivo downloadimage.py y luego de tener todo organizado de forma adecuada procedi a referienciar las imagenes

from clarifai.rest import ClarifaiApp
import requests
import json
import os
import glob
import urllib.request



app = ClarifaiApp(api_key='b6b8f6b826774549b2919eab7f315a8f')

model = app.public_models.general_model


# imgspath apunta al contenedor donde se encuentran las imagenes solamente... tratar de que hayan solo imagenes al momento 
# de inicial el render de las imagenes con respecto a la api de clarifai porque no hice un filtro aun

# entonces el siguiente es el directorio de las imagenes descargadas 
imgsdirgen = 'toTagImages'

imgspath = "./{0}/".format(imgsdirgen)
arrpath = os.listdir(imgspath)
uuids = []
paths = []
elementTotals = []
for arrname in arrpath:
    element = []
    uuid = arrname.replace(".png", "")
    uuids.append(uuid)
    paths.append(arrname)
    response = model.predict_by_filename("./{0}/{1}".format(imgsdirgen, arrname))
    tags = response["outputs"][0]["data"]["concepts"]
    elementTags = []
    for tag in tags:
        nametag = tag["name"]
        valuetag = tag["value"]
        tagparam = {'name':nametag, 'value':valuetag}
        elementTags.append(tagparam)
    elementDef = {'uuid': uuid, 'tags': elementTags}
    elementTotals.append(elementDef)

# por ultimo crea el json con las referencias de cada imagen, toca cambiar la ruta para cada categoria/caso 
with open('tagset_isolated.json', 'w', encoding='utf-8') as f:
    json.dump(elementTotals, f, ensure_ascii=False, indent=4)

