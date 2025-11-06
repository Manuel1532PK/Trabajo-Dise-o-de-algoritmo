import time
from recursividad import permutaciones_rutas
from furgon import Furgon

class CalculadorRutas:
    def __init__(self, grafo, mapa_api):
        self.grafo = grafo
        self.mapa_api = mapa_api
    
    def calcular_rutas_individuales(self, origen, destinos):
        #Calcula la ruta óptima entre el origen y cada destino individualmente
        print("RUTAS ÓPTIMAS INDIVIDUALES")
        
        for destino in destinos:
            print(f"\n---Ruta: {origen} → {destino}  ---")
            
            # Usar Dijkstra para encontrar la ruta más corta
            ruta, distancia = self.grafo.dijkstra(origen, destino)
            
            if distancia == float('inf'):
                print("No se encontró una ruta válida")
                continue
            
            # Obtener detalles de la ruta desde Google Maps
            ruta_detallada = self.mapa_api.obtener_ruta_detallada(origen, destino)
            
            if ruta_detallada:
                leg = ruta_detallada['legs'][0]
                distancia_real = leg['distance']['text']
                duracion_real = leg['duration']['text']
                
                print(f"Ruta: {' → '.join(ruta)}")
                print(f"Distancia: {distancia_real} ({distancia:.1f} km en grafo)")
                print(f"Duración: {duracion_real}")
                print(f"Pasos:")
                
            else:
                print(f"Ruta en grafo: {' → '.join(ruta)}")
                print(f"Distancia: {distancia:.1f} km")
                print(f"Duración estimada: {distancia / 60 * 60:.1f} minutos")
    
    def calcular_ruta_viajante(self, origen, destinos):
        #Resuelve el problema del viajante para visitar todos los destinos
        print("     PROBLEMA DEL VIAJANTE - RUTA ÓPTIMA")
        
        
        if len(destinos) > 6:
            print("Advertencia: Con más de 6 destinos, el cálculo puede ser lento")
            print("(Complejidad O(n!))")
        
        print(f"\nBuscando la mejor ruta para visitar {len(destinos)} destinos...")
        
        ruta_optima, distancia_total = permutaciones_rutas(self.grafo, [origen] + destinos)
        
        if ruta_optima:
            print(f"\RUTA ÓPTIMA ENCONTRADA:")
            print(f"Recorrido: {' → '.join(ruta_optima)}")
            print(f"Distancia total: {distancia_total:.1f} km")
            print(f"Tiempo estimado: {distancia_total / 60 * 60:.1f} minutos")
            
            # Mostrar detalles de cada tramo
            print(f"DETALLES POR TRAMO:")
            for i in range(len(ruta_optima) - 1):
                tramo_origen = ruta_optima[i]
                tramo_destino = ruta_optima[i + 1]
                distancia_tramo = self.grafo.nodos[tramo_origen].vecinos[tramo_destino]
                
                ruta_detallada = self.mapa_api.obtener_ruta_detallada(tramo_origen, tramo_destino)
                if ruta_detallada:
                    leg = ruta_detallada['legs'][0]
                    duracion = leg['duration']['text']
                    print(f"  {i+1}. {tramo_origen} → {tramo_destino}: {distancia_tramo:.1f} km, {duracion}")
                else:
                    print(f"  {i+1}. {tramo_origen} → {tramo_destino}: {distancia_tramo:.1f} km")
        else:
            print("No se pudo encontrar una ruta que visite todos los destinos")
    
    def planificar_entregas(self, origen, destinos):
        furgones = [Furgon(i+1) for i in range(5)]
        destinos_pendientes = destinos.copy()

        for destino in destinos_pendientes:
            nodo = self.grafo.obtener_nodo(destino)
            if not nodo:
                print(f"Destino {destino} no existe en el grafo")
                continue

            # Calcular ruta y tiempo real desde el origen
            _, duracion_seg = self.mapa_api.calcular_distancia(origen, destino)

            # Asignar al primer furgón que tenga capacidad y tiempo disponible
            asignado = False
            for f in furgones:
                if f.puede_agregar(nodo.paquetes, duracion_seg):
                    f.agregar_entrega(destino, nodo.paquetes, duracion_seg)
                    asignado = True
                    break

            if not asignado:
                print(f"No se pudo asignar el destino {destino} (excede tiempo o capacidad)")

        # Mostrar resumen
        for f in furgones:
            print(f"\nFurgón {f.id}:")
            print(f"Paquetes: {f.paquetes_actuales}/40")
            print(f"Tiempo total: {f.tiempo_total/3600:.2f} h")
            print(f"Ruta: {' → '.join(f.ruta) if f.ruta else 'Sin entregas'}")