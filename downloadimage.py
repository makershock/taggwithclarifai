import requests
import json
import os
import urllib.request

# para descargar las imagenes es vital tener las imagenes con uuids arriba en la base de datos 
# con eso los ids de las imagenes coinciden de forma adecuada

# primero seleccione la categoria y de acuerdo a ella se genera una carpeta con su nombre donde
# seran almacenadas la imagenes descargadas

# para revisar las diferentes categorias toca ver el json de https://www.bypeople.com/labo/api/v1/sources/category/mockups/
# tambien con el anterior se revisan cuantos elementos tiene la categoria


# el numero de elementos que tenga la categoria se reemplaza en el apartado de ?count=numero

dirPath = 'reales'

URL = "https://www.bypeople.com/labo/api/v1/sources/category/mockups/{0}?count=368".format(dirPath)
# r = requests.get(url = URL, params = PARAMS) 
r = requests.get(url = URL) 
data = r.json() 


ele_list = []
    
    
if dirPath not in os.listdir(os.getcwd()):
    os.makedirs("./{0}".format(dirPath))

for i in range(len(data['data'])):
    element = data['data'][i]
    ele_uuid = element['uuid_key']
    ele_urlsvg = element['url_svg']
    uuid = "./{0}/{1}.png".format(dirPath, ele_uuid)
    urllib.request.urlretrieve( ele_urlsvg, uuid)

# esto lo hice para poder organizar las imagenes en grupos facilmente referenciables e igualarlos con los
# modelos predefinidos de clarifai que se pueden encontrar en : https://www.clarifai.com/models

# tambien porque hay muchas imagenes de un mismo elemento en diferentes posiciones entonces para ahorrar 
# tanto queries como tener algo mas consistente en la data

# por ejemplo el folder isolated-set contiene las imagenes ya organizadas de la categoria isolated de mockups, y el folder isolated-page-1 contiene 
# de igualforma las imagenes pero las que se parecen o son de un mismo elemento las organize en carpetas con el uuid del elemento al que se le hizo 
# referencia que es una imagen dentro del set pero con caracteristicas mas marcadas para que sea identificada de forma eficaz por la herramienta.

