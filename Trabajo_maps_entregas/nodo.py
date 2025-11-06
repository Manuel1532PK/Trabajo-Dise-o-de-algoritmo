class Nodo:
    def __init__(self, nombre, latitud=None, longitud=None, Longitud=None, paquetes=0, ventana_tiempo=None, tiempo_servicio=5):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.paquetes = paquetes  # Número de paquetes a entregar en este nodo
        self.ventana_tiempo = ventana_tiempo  # (inicio, fin)
        self.tiempo_servicio = tiempo_servicio  # Tiempo en minutos para entregar paquetes
        self.vecinos = {}  # {nodo_destino: peso (distancia)}
    
    def agregar_vecino(self, vecino, peso):
        self.vecinos[vecino] = peso

    def __str__(self):
        return f"Nodo({self.nombre})"
    
    def __repr__(self):
        return self.__str__()