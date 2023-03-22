import json
from datetime import date


json_file = open("my_portfolio/Loto_Euro/loto_eu.json", "r+")
contenido = json_file.read()
decoded_content = json.loads(contenido)
 # Rellenar el diccionario con los datos a dumpear
dump_bolet = []


json.dump(dump_bolet,json_file, indent=6)	
print("Archivo actualizado" + dump_bolet)