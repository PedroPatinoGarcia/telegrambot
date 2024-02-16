import requests
from bs4 import BeautifulSoup


def obtener_cartelera():
    url = 'https://www.cantonescines.com/peliculas/cartelera'
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        elementos_front_title = soup.find_all(class_='qb-movie-name')

        peliculas_enlaces = []

        for elemento in elementos_front_title:
            texto_pelicula = elemento.get_text(strip=True)
            enlace = elemento.find('a')
            
            if enlace:
                enlace_pelicula = enlace['href']
                peliculas_enlaces.append(f'› <a href="{enlace_pelicula}">{texto_pelicula}</a>\n\n')
            else:
                peliculas_enlaces.append(f'› {texto_pelicula}\n\n')

        return ''.join(peliculas_enlaces)

    except requests.exceptions.RequestException as e:
        raise Exception('Error al realizar la solicitud HTTP: ', e)

    except Exception as e:
        raise Exception('No hay listados de películas para ti :( ', e)


# def getCinemaListings():

#     url = 'https://yelmocines.es/cartelera/a-coruna'
#     try:
#         response = requests.get(URL)
#         response.raise_for_status()
#         soup, html = BeautifulSoup(response.content, 'html.parser'), ''

#         for noticia in soup.find_all(class_="list-films__content"):
#             film = noticia.find(class_="film-title data-link").text
#             url = noticia.h3.get('data-link')
#             html += f'› <a href="{url}">{film}</a>\n\n'
#         return html

#     except requests.exceptions.RequestException as e:
#         raise Exception('Error when making HTTP request: ', e)

#     except Exception as e:
#         raise Exception('There is no movie listings for you :( ', e)