import requests

def obtener_pais():
    url = 'https://restcountries.com/v3.1/region/europe'
    response = requests.get(url)
    if response.status_code == 200 :
        return response.json
    elif response.status_code == 404 :
        print("Recurso no encontrado error (404). Revisar la URL")
        return []
    elif response.status_code == 500 :
        print("Error al conectar con el servidor (500). Intente mas terde")
        return []
    else:
        print("Error al consumir la API")
        return []