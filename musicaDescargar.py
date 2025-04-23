import yt_dlp
import os

# Metodo
def descargar_musica(url,carpeta="Rolas"): # pasamos parametros
    # Crear carpeta si esta no existe
    try: 
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Descargar contenido (solo audio)
        opciones = {
            'format' : 'bestaudio/best',# audio en la mejor calida disponible
            'outtmpl' : f'{carpeta}/%(title)s.%(ext)s', # guardar musica con titulo del video
            'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',  # Usa FFmpeg para extraer el audio
                'preferredcodec': 'mp3',  # Convierte a formato MP3
                'preferredquality': '192',  # Calidad del audio (192 kbps)
            },
            {  # Añade metadatos
                'key': 'FFmpegMetadata',  # Inserta metadatos básicos
            },
            {  # Añade la portada del video
                'key': 'EmbedThumbnail',  # Requiere ffmpeg
                'already_have_thumbnail': False,
            },
        ],
        'writethumbnail': True,  # Descargar thumbnail
        }
        print("Descargando audio de youtube...\n")
        
        # iniciar descarga de la url 
        with yt_dlp.YoutubeDL(opciones) as ydl: 
            ydl.download([url])
            print("Descarga completa!!!\n")
        
    # Manejo de errores
    except Exception as e:
        print(f"ocurrio un error : {e}")
if __name__ == "__main__":
    url = input("\nPege su enlace del video: ") # entrada de datos 
    descargar_musica(url) # llamar metodo