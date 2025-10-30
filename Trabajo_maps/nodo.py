class Nodo:
    def __init__(self, nombre, latitud=None, longitud=None):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.vecinos = {}  # {nodo_destino: peso (distancia)}
    
    def agregar_vecino(self, vecino, peso):
        self.vecinos[vecino] = peso
    
    def __str__(self):
        return f"Nodo({self.nombre})"
    
    def __repr__(self):
        return self.__str__()