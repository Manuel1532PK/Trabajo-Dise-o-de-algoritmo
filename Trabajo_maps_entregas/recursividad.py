def encontrar_todas_rutas(grafo, inicio, fin, visitados=None, camino_actual=None):
    #Función recursiva para encontrar todas las rutas posibles entre dos nodos
    
    if visitados is None:
        visitados = set()
    if camino_actual is None:
        camino_actual = []
    
    visitados.add(inicio)
    camino_actual.append(inicio)
    
    if inicio == fin:
        # Calcular peso total del camino
        peso_total = 0
        for i in range(len(camino_actual) - 1):
            peso_total += grafo.nodos[camino_actual[i]].vecinos.get(camino_actual[i + 1], 0)
        
        yield camino_actual.copy(), peso_total
    else:
        for vecino in grafo.nodos[inicio].vecinos:
            if vecino not in visitados:
                yield from encontrar_todas_rutas(grafo, vecino, fin, visitados.copy(), camino_actual.copy())
    
    camino_actual.pop()
    visitados.remove(inicio)

def encontrar_ruta_optima(grafo, inicio, fin):
    #Encuentra la ruta óptima usando fuerza bruta recursiva
    mejor_ruta = None
    mejor_peso = float('inf')
    
    for ruta, peso in encontrar_todas_rutas(grafo, inicio, fin):
        if peso < mejor_peso:
            mejor_peso = peso
            mejor_ruta = ruta
    
    return mejor_ruta, mejor_peso

def permutaciones_rutas(grafo, nodos):
    #Genera todas las permutaciones posibles de rutas (para el problema del viajante)
    from itertools import permutations
    
    mejor_ruta = None
    mejor_distancia = float('inf')
    
    # Generar todas las permutaciones de los nodos intermedios
    for perm in permutations(nodos[1:]):
        ruta_actual = [nodos[0]] + list(perm)
        distancia_total = 0
        
        # Calcular distancia total de esta permutación
        for i in range(len(ruta_actual) - 1):
            distancia = grafo.nodos[ruta_actual[i]].vecinos.get(ruta_actual[i + 1], float('inf'))
            if distancia == float('inf'):
                break
            distancia_total += distancia
        else:
            if distancia_total < mejor_distancia:
                mejor_distancia = distancia_total
                mejor_ruta = ruta_actual
    
    return mejor_ruta, mejor_distancia