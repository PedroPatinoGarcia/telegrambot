import requests
from bs4 import BeautifulSoup

def obtener_diario():
    url = 'https://praza.gal/'
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        elementos_front_title = soup.find_all(class_='article-summary-header')

        titulares_enlaces = []

        for elemento in elementos_front_title:
            texto_titular = elemento.find('h2').get_text(strip=True)
            enlace = elemento.find('a')

            if enlace:
                enlace_titular = enlace['href']
                enlace_completo = f'https://praza.gal{enlace_titular}'
                titulares_enlaces.append([texto_titular, enlace_completo])

        return titulares_enlaces
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el diario: {e}")
        return []