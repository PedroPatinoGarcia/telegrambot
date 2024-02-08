import requests

def obtener_datos_pokemon(numero):
    url = f'https://pokeapi.co/api/v2/pokemon/{numero}/'
    
    try:
        response = requests.get(url)
        datos = response.json()

        nombre = datos['name']
        imagen_url = datos['sprites']['front_default']
        descripcion = obtener_descripcion_pokemon(numero)

        return nombre, imagen_url, descripcion

    except Exception as e:
        print(f'Error al obtener datos del Pokémon: {e}')
        return None, None, None
    
def obtener_descripcion_pokemon(numero):
    url_especies = f'https://pokeapi.co/api/v2/pokemon-species/{numero}/'
    
    try:
        response = requests.get(url_especies)
        datos_especies = response.json()

        descripcion = datos_especies['flavor_text_entries'][0]['flavor_text']

        return descripcion

    except Exception as e:
        print(f'Error al obtener descripción del Pokémon: {e}')
        return None