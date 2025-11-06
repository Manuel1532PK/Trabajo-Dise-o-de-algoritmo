from nodo import Nodo

class Grafo:
    def __init__(self):
        self.nodos = {}
    
    def agregar_nodo(self, nombre, latitud=None, longitud=None):
        if nombre not in self.nodos:
            self.nodos[nombre] = Nodo(nombre, latitud, longitud)
        return self.nodos[nombre]
    
    def agregar_arista(self, origen, destino, peso):
        if origen in self.nodos and destino in self.nodos:
            self.nodos[origen].agregar_vecino(destino, peso)
    
    def obtener_nodo(self, nombre):
        return self.nodos.get(nombre)
    
    def dijkstra(self, inicio, fin):
        #Algoritmo de Dijkstra para encontrar el camino más corto
        distancias = {nodo: float('inf') for nodo in self.nodos}
        distancias[inicio] = 0
        visitados = set()
        previos = {}
        
        while len(visitados) < len(self.nodos):
            # Encontrar nodo no visitado con menor distancia
            nodo_actual = None
            min_distancia = float('inf')
            
            for nodo in self.nodos:
                if nodo not in visitados and distancias[nodo] < min_distancia:
                    min_distancia = distancias[nodo]
                    nodo_actual = nodo
            
            if nodo_actual is None:
                break
            
            visitados.add(nodo_actual)
            
            # Actualizar distancias de vecinos
            for vecino, peso in self.nodos[nodo_actual].vecinos.items():
                nueva_distancia = distancias[nodo_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    previos[vecino] = nodo_actual
        
        # Reconstruir camino
        camino = []
        nodo_actual = fin
        
        while nodo_actual in previos:
            camino.insert(0, nodo_actual)
            nodo_actual = previos[nodo_actual]
        
        if camino or inicio == fin:
            camino.insert(0, inicio)
        
        return camino, distancias[fin] if fin in distancias else float('inf')