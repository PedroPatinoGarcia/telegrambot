import requests

def obtener_informe_meteorologico(ciudad, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        datos = response.json()

        temperatura_minima = datos['main']['temp_min']
        temperatura_maxima = datos['main']['temp_max']
        informacion_clima = datos['weather'][0]['description']

        informe = f'Informe meteorológico para {ciudad}:\n'
        informe += f'Temperatura mínima: {temperatura_minima}°C\n'
        informe += f'Temperatura máxima: {temperatura_maxima}°C\n'
        informe += f'Información del clima: {informacion_clima}\n'

        return informe

    except Exception as e:
        print(f'Error al obtener el informe meteorológico: {e}')
        return None
