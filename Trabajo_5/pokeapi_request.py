import requests

class PokeAPI:          #Clase para obtener datos desde la PokéAPI con control de error
    def __init__(self, url):
        self.url = url

    def get_data(self):        #Realiza la petición HTTP y valida la estructura de la respuesta

        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error al solicitar la API: {e}")
            return None

        try:
            return response.json()
        except ValueError:
            print("Error: la respuesta no tiene formato JSON válido.")
            return None