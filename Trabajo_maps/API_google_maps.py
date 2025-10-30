import googlemaps
import time

class GoogleMapsAPI:
    def __init__(self, api_key):
        self.gmaps = googlemaps.Client(key=api_key)
        self.cache_distancias = {}  # Cache para evitar llamadas repetidas
    
    def geocodificar(self, direccion):
        #Convierte una dirección en coordenadas GPS
        try:
            resultado = self.gmaps.geocode(direccion)
            if resultado:
                location = resultado[0]['geometry']['location']
                return location['lat'], location['lng']
            return None, None
        except Exception as e:
            print(f"Error en geocodificación: {e}")
            return None, None
    
    def calcular_distancia(self, origen, destino, modo='driving'):
        #Calcula distancia y tiempo entre dos puntos
        cache_key = f"{origen}_{destino}_{modo}"
        
        if cache_key in self.cache_distancias:
            return self.cache_distancias[cache_key]
        
        try:
            # Obtener coordenadas si se pasan nombres de lugares
            if isinstance(origen, str):
                lat_origen, lng_origen = self.geocodificar(origen)
                origen = (lat_origen, lng_origen)
            
            if isinstance(destino, str):
                lat_destino, lng_destino = self.geocodificar(destino)
                destino = (lat_destino, lng_destino)
            
            if origen is None or destino is None:
                return float('inf'), float('inf')
            
            # Calcular distancia usando la API
            resultado = self.gmaps.distance_matrix(
                origins=[origen],
                destinations=[destino],
                mode=modo,
                units='metric'
            )
            
            if resultado['rows'][0]['elements'][0]['status'] == 'OK':
                elemento = resultado['rows'][0]['elements'][0]
                distancia = elemento['distance']['value']  # en metros
                duracion = elemento['duration']['value']   # en segundos
                
                self.cache_distancias[cache_key] = (distancia, duracion)
                return distancia, duracion
            else:
                return float('inf'), float('inf')
                
        except Exception as e:
            print(f"Error calculando distancia: {e}")
            return float('inf'), float('inf')
    
    def obtener_ruta_detallada(self, origen, destino, modo='driving'):
        #Obtiene una ruta detallada entre dos puntos
        try:
            if isinstance(origen, str):
                lat_origen, lng_origen = self.geocodificar(origen)
                origen = (lat_origen, lng_origen)
            
            if isinstance(destino, str):
                lat_destino, lng_destino = self.geocodificar(destino)
                destino = (lat_destino, lng_destino)
            
            direcciones = self.gmaps.directions(
                origin=origen,
                destination=destino,
                mode=modo
            )
            
            return direcciones[0] if direcciones else None
        except Exception as e:
            print(f"Error obteniendo ruta detallada: {e}")
            return None