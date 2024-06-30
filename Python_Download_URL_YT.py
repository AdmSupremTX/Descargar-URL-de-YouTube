import os
from pytube import YouTube
from moviepy.editor import *

def barra_de_progreso(stream, chunk, bytes_remaining):
    tamaño_total = stream.filesize
    bytes_descargados = tamaño_total - bytes_remaining
    porcentaje_de_avance = (bytes_descargados / tamaño_total) * 100
    print(f"Descargado: {porcentaje_de_avance:.1f}% del video", end='\r')

def descargar_video_youtube(url, ruta_descarga):
    try:
        youtube = YouTube(url)
        youtube.register_on_progress_callback(barra_de_progreso)
        video = youtube.streams.get_highest_resolution()
        video.download(output_path=ruta_descarga)
        print("\n¡Descarga exitosa de YouTube!")
        return os.path.join(ruta_descarga, video.default_filename)
    except Exception as e:
        print(f"Ocurrió un error al descargar el video de YouTube: {e}")

def descargar_y_convertir_a_mp3(url, ruta_descarga):
    try:
        ruta_video = descargar_video_youtube(url, ruta_descarga)
        video_clip = VideoFileClip(ruta_video)
        ruta_audio = ruta_video.replace(".mp4", ".mp3")
        video_clip.audio.write_audiofile(ruta_audio)
        os.remove(ruta_video)  # Elimina el archivo mp4 después de la conversión
        print("¡Conversión a mp3 exitosa!")
    except Exception as e:
        print(f"Ocurrió un error al convertir el video a mp3: {e}")

def menu_descarga():
    print("
██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░  ██╗░░░██╗██████╗░██╗░░░░░  ██╗░░░██╗████████╗
██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗  ██║░░░██║██╔══██╗██║░░░░░  ╚██╗░██╔╝╚══██╔══╝
██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░░░░██║░░██║███████║██║░░██║  ██║░░░██║██████╔╝██║░░░░░  ░╚████╔╝░░░░██║░░░
██║░░██║██║░░██║░░████╔═████║░██║╚████║██║░░░░░██║░░██║██╔══██║██║░░██║  ██║░░░██║██╔══██╗██║░░░░░  ░░╚██╔╝░░░░░██║░░░
██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║███████╗╚█████╔╝██║░░██║██████╔╝  ╚██████╔╝██║░░██║███████╗  ░░░██║░░░░░░██║░░░
╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚══════╝  ░░░╚═╝░░░░░░╚═╝░░░")
    print("Por favor, selecciona una opción:")
    print("1. Descargar video de YouTube como mp4")
    print("2. Descargar video de YouTube y convertirlo a mp3")
    opcion = input("Ingresa el número de tu opción: ")

    url = input("Por favor, ingresa la URL del video: ")

    if opcion == '1':
        ruta_descarga_videos = os.path.join(os.getcwd(), 'Descargas', 'Videos')
        os.makedirs(ruta_descarga_videos, exist_ok=True)
        descargar_video_youtube(url, ruta_descarga_videos)
    elif opcion == '2':
        ruta_descarga_musica = os.path.join(os.getcwd(), 'Descargas', 'Musica')
        os.makedirs(ruta_descarga_musica, exist_ok=True)
        descargar_y_convertir_a_mp3(url, ruta_descarga_musica)
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")

# Ejemplo de uso
menu_descarga()
