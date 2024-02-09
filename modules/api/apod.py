import requests

def obtener_apod_nasa(api_key_nasa):
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key_nasa}'

    try:
        response = requests.get(url)
        datos = response.json()

        titulo = datos['title']
        descripcion = datos['explanation']
        url_imagen = datos['url']

        return titulo, descripcion, url_imagen

    except Exception as e:
        print(f'Error al obtener la APOD: {e}')
        return None
