import requests

def obtener_imagen_perro():
    url = "https://dog.ceo/api/breeds/image/random"

    try:
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json()

        if datos and datos["status"] == "success":
            imagen_url = datos["message"]
            return imagen_url

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud a la API: {e}")
        print(f"Detalles del error: {str(e)}")

    return None
