from statistics import mode
import json, random
    
json_file = open("loto_eu.json", "r+")
contenido = json_file.read()
decoded_content = json.loads(contenido)
busqueda = input("Introduce una Fecha?: ")
if not busqueda:
    print("Debes introducir una fecha para realizar la búsqueda.")
    exit()
NotFound = "Ese dia no hubo sorteo de Euromillones"
search = bool(False)
# Aqui dato es cada bloque de datos del json, y al encontrar  Fecha imprime todo el bloque
for dato in decoded_content["Euromillones"]:
    fecha = dato["FECHA"]
    uno = dato["PRIMER"]
    dos = dato["SEGUN"]
    tres = dato["TERCER"]
    cuatro = dato["CUAR"]
    cinco = dato["QUINT"]
    star_1 = dato["ES1"]
    star_2 = dato["ES2"]
    if dato["FECHA"] == busqueda:
        search = bool(True)
        print("En la fecha {} el resultado de Euromillones fue {}, {}, {}, {}, {} y las estrellas fueron Estrella 1: {} y estrella 2: {}".format(
            fecha, uno, dos, tres, cuatro, cinco, star_1, star_2))

if not search:
    print("Fecha no encontrada")

 # Buscaremos los numeros que mas salen y con ellos crearemos un boleto


count = 1602
plus_1 = 0
plus_2 = 0
plus_3 = 0
plus_4 = 0
plus_5 = 0
plus_6 = 0
plus_7 = 0
for resultado in decoded_content["Euromillones"]:
    if "FECHA" in resultado:
        plus_1 += int(resultado["PRIMER"])/count
        plus_2 += int(resultado["SEGUN"])/count
        plus_3 += int(resultado["TERCER"])/count
        plus_4 += int(resultado["CUAR"])/count
        plus_5 += int(resultado["QUINT"])/count
        plus_6 += int(resultado["ES1"])/count
        plus_7 += int(resultado["ES2"])/count


primeros = [dato["PRIMER"] for dato in decoded_content["Euromillones"]]
segundos = [dato["SEGUN"] for dato in decoded_content["Euromillones"]]
terceros = [dato["TERCER"] for dato in decoded_content["Euromillones"]]
cuartos = [dato["CUAR"] for dato in decoded_content["Euromillones"]]
quintos = [dato["QUINT"] for dato in decoded_content["Euromillones"]]
estrella_1 = [dato["ES1"] for dato in decoded_content["Euromillones"]]
estrella_2 = [dato["ES2"] for dato in decoded_content["Euromillones"]]
premo_1 = mode(primeros)
premo_2 = mode(segundos)
premo_3 = mode(terceros)
premo_4 = mode(cuartos)
premo_5 = mode(quintos)
premo_6 = mode(estrella_1)
premo_7 = mode(estrella_2)
print("El número que pronostico según la moda para el siguiente sorteo es {}, {}, {}, {}, {} y las estrellas son el número {} y el número {}".format(premo_1, premo_2, premo_3, premo_4, premo_5, premo_6, premo_7))

numeros = []
estrellas = []

for resultado in decoded_content["Euromillones"]:
    numeros += [int(resultado["PRIMER"]), int(resultado["SEGUN"]), int(resultado["TERCER"]), int(resultado["CUAR"]), int(resultado["QUINT"])]
    estrellas += [int(resultado["ES1"]), int(resultado["ES2"])]

# Calcular probabilidades de cada número y estrella
numeros_probabilidades = [numeros.count(i) / len(numeros) for i in range(1, 51)]
estrellas_probabilidades = [estrellas.count(i) / len(estrellas) for i in range(1, 13)]

# Generar combinación aleatoria de números y estrellas con base en los números que mas salen
numeros_elegidos = random.choices(range(1, 51), numeros_probabilidades, k=5)
estrellas_elegidas = random.choices(range(1, 13), estrellas_probabilidades, k=2)
OrderedNumbers = sorted(numeros_elegidos)
OrderedStars = sorted(estrellas_elegidas)
# Imprimir combinación generada
print("La combinación generada por probabilidades es: {}, {}, {}, {}, {}, Estrella 1: {}, Estrella 2: {}".format(*OrderedNumbers, *OrderedStars))
