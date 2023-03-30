import pyttsx3
import speech_recognition as sr
import decouple  
from datetime import datetime
from dotenv import load_dotenv
from random import choice
from util_texts import opening_text, hi_there, asertive, wake_up, reading,jokes
import online_functions
from pprint import pprint
import openai
import requests
import os
import time
import cv2
import typer
from rich import print
from rich.table import Table

load_dotenv()
openai.api_key =os.getenv("Open_AI")
USERNAME = os.getenv('USER')
USERNAME_A = os.getenv('USER_A')
BOTNAME = os.getenv('BOTNAME')
VINOS = os.getenv('VINOS')
CERVEZAS = os.getenv('CERVEZAS')
COMIDAS = os.getenv('COMIDAS')
THINK = os.getenv('THINK')
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

def reconocer_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language="es-ES")
        return texto.lower()
    except:
        return ""

# Palabra clave para activar el asistente
palabra_clave = "despierta"

# Bucle que espera a que se diga la palabra clave
while True:
    
    texto_escuchado = reconocer_voz()
    if palabra_clave in texto_escuchado:
        print("[bold green]¡Hola! ¿En qué puedo ayudarte?[/bold green]")
        break


# Greet the user
def greet_user():
    speak(THINK)
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Buenos dias {USERNAME}. Bienvenidos a LA BARRICA ")
        speak("Que desearian tomar?")
      

       
       
    elif (hour >= 12) and (hour < 20):
        speak(f"Buenas tardes {USERNAME}. Bienvenidos a LA BARRICA")
        speak("Que desearian tomar?")
        
        
       
    elif (hour >= 20) and (hour < 23):
        speak(f"Buenas noches {USERNAME}. Bienvenidos a LA BARRICA")
        speak("Que desearian tomar?")
        
        

mic = sr.Microphone()
# Takes Input from User
def take_user_input():
    r = sr.Recognizer()
    error_count = 0
    while True:
        with sr.Microphone() as source:
            print('🎤[bold red]Escuchando....[/bold red]')
            r.adjust_for_ambient_noise(source, duration=1)
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                print('🤔[bold yellow]Reconociendo...[/bold yellow]')
                query = r.recognize_google(audio, language='es-es')
                if '1976' in query or 'uno nueve siete seis' in query:
                    print("🙋")
                    hour = datetime.now().hour
                    if hour >= 21 and hour < 6:
                        speak(f"Buenas noches {USERNAME}!")
                        exit()
                    else:
                        speak(f"Que tengan un buen día {USERNAME}!")
                        exit()
                else:
                    error_count = 0
                    return query
            except Exception:
                error_count += 1
                if error_count < 2:
                    speak("Lo siento no le he entendido, Puede repetirlo, por favor?")
                else:
                    speak("Modo reposo activado")
                    while True:
                        print('🥱😴😴😴')
                        audio = r.listen(source)
                        try:
                            query = r.recognize_google(audio, language='es-es')
                            if 'Ari despierta' in query:
                                speak(choice(wake_up))
                                error_count = 0
                                break
                            else:
                                speak("Esperando la frase 'Ari despierta")
                        except Exception:
                            pass
                 
# Gestion de peticiones 

if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()
        if 'vino' in query:
            print("🍷")
            speak(f'que vino les gustaria probar.?')
            prompt =f"quiero que actues como un somelier de alto standing e ignores cualquier cosa que te diga que no tenga que ver con la restauración y si pregunto por vinos solo aconsejame de la lista que te paso aqui:{VINOS}" + take_user_input().lower()
            ia_python = openai.Completion.create(engine="text-davinci-003", prompt = prompt, max_tokens= 2048)
            Find = ia_python.choices[0].text.strip().replace("'", "")
            print(choice(reading))
            speak(Find)
            print(f"[bold green]>[bold green] [green]{Find}[/green]")
            speak(f"{USERNAME} Si desean comer algo digan, deseo comer algo")
        if 'comer' in query:
            print("🍞🍳")
            speak(f"Consulto la carta y les digo.")
            prompt=f"sigue actuando como un somelier muy educado y correcto y lo que aconsejes que sea de esta lista de comidas:{COMIDAS} y explica cada plato, comienza a hablar diciendo estas palabras: Les aconsejo lo siguiente. "
            ia_python = openai.Completion.create(engine="text-davinci-003", prompt = prompt, max_tokens= 2048)
            print(choice(reading))
            Find = ia_python.choices[0].text.strip().replace("'", "")
            speak(Find)
            print(f"[bold green]>[bold green] [green]{Find}[/green]")

        elif 'cerveza' in query:
            print("🍺")
            speak(f'Que cervezas les gustan ?.')
            prompt =f"quiero que actues como un somelier de alto standing e ignores cualquier cosa que te diga que no tenga que ver con la restauración y si pregunto por cervezas solo aconsejame de la lista que te paso aqui, no digas el pais de procedencia de las cervezas a no ser que se pregunte especificamente:{CERVEZAS}. "+ take_user_input().lower()
            ia_python = openai.Completion.create(engine="text-davinci-003", prompt = prompt, max_tokens= 2048)
            print(choice(reading))
            Find = ia_python.choices[0].text
            speak(Find)
            print(f"[bold green]>[bold green] [green]{Find}[/green]")
            speak(f"{USERNAME} Si desean comer algo digan, deseo comer algo")
        elif 'gracias' in query:
            print("😍")
            speak(f"De nada, estoy aquí para servirle")
        elif 'llamas' in query:
            speak(f"[bold green]Me llamo {BOTNAME} y estoy para servirles.[/bold green]😉")
        elif 'comandos' in query or 'comando' in query:
            speak("Aquí os muestro los comandos que, de momento, acepto")
            table = Table("Comando", "Descripción")
            table.add_row("ARI despierta", "Activa  ARI.")
            table.add_row("🍷ARI dime que vinos tienes🍷", "Te preguntará cuales te gustan.")
            table.add_row("🍺ARI dime que cervezas tienes.🍺", "Te preguntara que cervezas te gustan.")
            table.add_row("🍳🍞ARI dime que tienes de comer.🍳🍞", "Consultara la carta y explicara le explicara")
            print(table)
        elif 'chiste' in query:
            speak(choice(jokes))
            print("😂😂😂😂😂😂")
            speak("Desean alguna otra cosa?")

    
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
                   cv2.imwrite('Virtual_Assistant\snapshoots', frame)
                   nombre_base = "foto"

             # Obtener la hora actual como una cadena de caracteres
                   hora_actual = time.strftime("%Y%m%d-%H%M%S")
             
             # Nombre completo del archivo
                   photo = nombre_base + "-" + hora_actual + ".jpg"
             
             # Tomar la foto y guardarla con el nombre completo del archivo
             # (sustituye esta línea con tu código para tomar la foto)
                   foto = None
             # guardar la foto con el nombre completo del archivo
                   with open(photo, "wb") as f:
                     f.write(foto)
             
             # Mover la foto a la carpeta "snapshoots"
                     ruta_vieja = photo
                     ruta_nueva = os.path.join("snapshoots", photo)
                     os.rename(ruta_vieja, ruta_nueva)
                     break
            # Esperar a que el usuario presione 'q' para salir
               if cv2.waitKey(1) & 0xFF == ord('q'):
                break
               # Liberar la cámara y cerrar la ventana de visualización
            cap.release()
            cv2.destroyAllWindows()




# .\env\Scripts\activate

# python main.py
