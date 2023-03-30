from flask import Flask, render_template, request
import main
import pyttsx3
import speech_recognition as sr
import decouple  
from datetime import datetime
from dotenv import load_dotenv, set_key
from random import choice
from util_texts import opening_text, hi_there, asertive, wake_up
import online_functions
from pprint import pprint
import openai
import requests
import os
import time
import cv2

app = Flask(__name__)

@app.route("/")
def index():
    return '¡Bienvenido a la aplicación de Flask!'





load_dotenv()
openai.api_key =os.getenv("Open_AI")
USERNAME = os.getenv('USER')
BOTNAME = os.getenv('BOTNAME')
VINOS = os.getenv('VINOS')
CERVEZAS = os.getenv('CERVEZAS')


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Text to Speech Conversion
def speak(text):
    """Usado para decir cualquier texto que le sea entregado"""

    engine.say(text)
    engine.runAndWait()



# Greet the user
def greet_user():
    """Saluda al usuario de acuerdo al horario"""
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Buenos dias {USERNAME} como quiere que le llame")
        NAME = take_user_input().lower()
        set_key('.env','USER', NAME)
       
       
    elif (hour >= 12) and (hour < 20):
        speak(f"Buenas tardes {USERNAME} como quiere que le llame")
        NAME = take_user_input().lower()
        set_key('.env','USER', NAME)
        
       
    elif (hour >= 20) and (hour < 23):
        speak(f"Buenas noches {USERNAME} como quiere que le llame")
        NAME = take_user_input().lower()
        set_key('.env','USER', NAME)
        
    speak(choice(asertive))



# Takes Input from User
def take_user_input():
    """Toma las entradas del usuario, las reconoce utilizando el módulo de reconocimiento de voz y lo transforma a texto"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Escuchando....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Reconociendo...')
        query = r.recognize_google(audio, language='es-es')
        if not 'salir' in query or 'parar' in query:
            speak(choice(asertive))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak(f"Buenas noches {USERNAME}!")
            else:
                speak(f"Que tengan un buen día {USERNAME}!")
            exit()
    except Exception:
        speak("Lo siento no le he entendido, Puede repetirlo, por favor?")
        query = 'None'
    return query



if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()
        
        
        if 'vino' in query:
            speak(f'que vino le gustaria probar {USERNAME}.?')
            prompt =f"quiero que actues como un somelier de alto standing e ignores cualquier cosa que te diga que no tenga que ver con la restauración y si pregunto por vinos solo aconsejame de la lista que te paso aqui:{VINOS}" + take_user_input().lower()
            ia_python = openai.Completion.create(engine="text-davinci-003", prompt = prompt, max_tokens= 2048)
            Find = ia_python.choices[0].text
            speak(Find)
            pprint(Find)


        elif 'cerveza' in query:
            speak(f'Que cervezas le gustan {USERNAME}?.')
            prompt =f"quiero que actues como un somelier de alto standing e ignores cualquier cosa que te diga que no tenga que ver con la restauración y si pregunto por cervezas solo aconsejame de la lista que te paso aqui:{CERVEZAS} "+ take_user_input().lower()
            ia_python = openai.Completion.create(engine="text-davinci-003", prompt = prompt, max_tokens= 2048)
            Find = ia_python.choices[0].text
            speak(Find)
            pprint(Find)
        elif 'gracias' in query:
            speak(f"De nada, estoy aqui para servirle")
    

        


        elif 'cambiar nombre' in query or 'cambiarte el nombre' in query:
            speak(f'Di que nombre quieres que tenga {USERNAME}, en la actualidad me llamo {BOTNAME}')
            name_change = take_user_input().lower()
            BOTNAME = name_change
            speak(f'Perfecto ahora me llamo {BOTNAME}, a partir de ahora me presentare así')
        elif 'cámara' in query:
            # Abrir la cámara
            cap = cv2.VideoCapture(0)
            # Comprobar que la cámara se ha abierto correctamente
            if not cap.isOpened():
             raise IOError("No se puede abrir la cámara")
            # Leer los fotogramas de la cámara
            while True:
               ret, frame = cap.read()
            # Mostrar el fotograma capturado
               cv2.imshow('Input', frame)
                 # Espera a que el usuario presione 'c' para tomar la foto
               c = cv2.waitKey(1)
               if c == ord('c'):
                   # Guarda la foto en un archivo de imagen
                   cv2.imwrite('snapshoots/foto.jpg', frame)
                   nombre_base = "foto"

             # Obtener la hora actual como una cadena de caracteres
                   hora_actual = time.strftime("%Y%m%d-%H%M%S")
             
             # Nombre completo del archivo
                   nombre_archivo = nombre_base + "-" + hora_actual + ".jpg"
             
             # Tomar la foto y guardarla con el nombre completo del archivo
             # (sustituye esta línea con tu código para tomar la foto)
                   foto = None
             # guardar la foto con el nombre completo del archivo
                   with open(nombre_archivo, "wb") as f:
                     f.write(foto)
             
             # Mover la foto a la carpeta "snapshoots"
                     ruta_vieja = nombre_archivo
                     ruta_nueva = os.path.join("snapshoots", nombre_archivo)
                     os.rename(ruta_vieja, ruta_nueva)
                     break
            # Esperar a que el usuario presione 'q' para salir
               if cv2.waitKey(1) & 0xFF == ord('q'):
                break
               # Liberar la cámara y cerrar la ventana de visualización
            cap.release()
            cv2.destroyAllWindows()

if __name__ == '__main__':
    app.run(debug=True)
    