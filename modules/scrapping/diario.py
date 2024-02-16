import requests
from bs4 import BeautifulSoup

def obtener_diario():
    url = 'https://www.dxtcampeon.com/'
    paxina = requests.get(url)

    soup = BeautifulSoup(paxina.content, 'html.parser')
    
    elementos_front_title = soup.find_all(class_='front_title')

    titulares_enlaces = []

    for elemento in elementos_front_title:
        texto_titular = elemento.get_text(strip=True)
        enlace = elemento.find('a')
        
        if enlace:
            enlace_titular = enlace['href']
            titulares_enlaces.append(f'<a href="{enlace_titular}">{texto_titular}</a>')
        else:
            titulares_enlaces.append(texto_titular)

    return (titulares_enlaces)