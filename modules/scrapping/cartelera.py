import requests
from bs4 import BeautifulSoup

def obtener_cartelera():
    url = 'https://www.cantonescines.com/peliculas/cartelera'
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        elementos_qb_movie_link = soup.find_all(class_='qb-movie-link')

        peliculas_enlaces = []

        for elemento in elementos_qb_movie_link:
            titulo_elemento = elemento.find(class_='qb-movie-name')
            enlace = elemento['href'] if elemento.has_attr('href') else None

            if titulo_elemento:
                titulo_pelicula = titulo_elemento.get_text(strip=True)
                peliculas_enlaces.append((titulo_pelicula, enlace))
                
        peliculas_enlaces.sort(key=lambda x: x[0].lower())
        
        return peliculas_enlaces
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la cartelera: {e}")
        return []
