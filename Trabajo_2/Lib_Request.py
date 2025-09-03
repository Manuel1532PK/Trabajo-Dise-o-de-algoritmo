import requests

def obtener_pais():
    url = 'https://restcountries.com/v3.1/region/europe'
    response = requests.get(url)
    if response.status_code == 200 :
        return response.json()
    elif response.status_code == 404 :
        print("Recurso no encontrado error (404). Revisar la URL")
        return []
    elif response.status_code == 500 :
        print("Error al conectar con el servidor (500). Intente mas terde")
        return []
    else:
        print("Error al consumir la API")
        return []
    
def busqueda_lineal(paises, nombre):
    for pais in paises:
        if pais["name"]["common"].lower() == nombre.lower():
            return pais
    return None

def busqueda_binaria(paises, nombre):
    izquierda = 0
    derecha = len(paises) - 1
    nombre = nombre.lower()

    while izquierda <=derecha:
        medio = (izquierda+derecha) //2
        pais_medio = paises[medio]["name"]["common"].lower()

        if pais_medio == nombre.lower():
            return paises[medio]
        elif pais_medio < nombre.lower():
            izquierda = medio + 1 
        else:
            derecha = medio - 1
    return None