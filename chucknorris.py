import requests

def obtener_chiste():
    url = 'https://api.chucknorris.io/jokes/random'

    try:
        response = requests.get(url)
        datos = response.json()

        chiste = datos['value']

        return chiste

    except Exception as e:
        print(f'Error al obtener el chiste de Chuck Norris: {e}')
        return None