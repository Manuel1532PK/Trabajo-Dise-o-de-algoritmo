import os
import time
from grafo import Grafo
from API_google_maps import GoogleMapsAPI
from calcular_rutas import CalculadorRutas

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_ubicaciones(grafo, mapa_api):
    #Obtiene y valida las ubicaciones del usuario
    # Obtener origen
    origen = input("Ingrese la ciudad de ORIGEN: ").strip()
    
    # Geocodificar origen
    print(f"Buscando coordenadas para: {origen}...")
    lat_origen, lng_origen = mapa_api.geocodificar(origen)
    
    if lat_origen is None:
        print(f"No se pudo encontrar: {origen}")
        return None, []
    
    grafo.agregar_nodo(origen, lat_origen, lng_origen)
    print(f"Origen establecido: {origen} ({lat_origen:.4f}, {lng_origen:.4f})")
    
    # Obtener destinos/paradas
    destinos = []
    print("Ingrese ciudades de DESTINO/PARADAS (deje vacío para terminar):")
    
    while True:
        destino = input(f"Parada {len(destinos) + 1}: ").strip()
        
        if not destino:
            if len(destinos) == 0:
                print("Debe ingresar al menos un destino")
                continue
            break
        
        print(f"Buscando coordenadas para: {destino}...")
        lat_dest, lng_dest = mapa_api.geocodificar(destino)
        
        if lat_dest is None:
            print(f"No se pudo encontrar: {destino}")
            continue
        
        grafo.agregar_nodo(destino, lat_dest, lng_dest)
        destinos.append(destino)
        print(f"Destino agregado: {destino} ({lat_dest:.4f}, {lng_dest:.4f})")
    
    return origen, destinos

def construir_grafo_completo(grafo, mapa_api, ubicaciones):
    #Construye el grafo completo con todas las distancias
    print("Calculando distancias entre ubicaciones...")
    
    for i, ubicacion1 in enumerate(ubicaciones):
        for j, ubicacion2 in enumerate(ubicaciones):
            if i != j:
                print(f"Calculando {ubicacion1} → {ubicacion2}...")
                distancia, duracion = mapa_api.calcular_distancia(ubicacion1, ubicacion2)
                
                if distancia != float('inf'):
                    # Convertir a kilómetros para el grafo
                    distancia_km = distancia / 1000
                    grafo.agregar_arista(ubicacion1, ubicacion2, distancia_km)
                    print(f"{distancia_km:.1f} km, {duracion/60:.1f} min")
                else:
                    print(f"No se pudo calcular la distancia")
                
                # Pequeña pausa para no saturar la API
                time.sleep(0.1)

def main():
    # Configurar API Key
    api_key = input("Ingrese su API Key de Google Maps: ").strip()
    
    if not api_key:
        print("Error: Se requiere una API Key válida")
        return
    
    # Inicializar componentes
    try:
        mapa_api = GoogleMapsAPI(api_key)
        grafo = Grafo()
    except Exception as e:
        print(f"Error inicializando API: {e}")
        return
    
    limpiar_pantalla()
    
    # Obtener ubicaciones
    origen, destinos = obtener_ubicaciones(grafo, mapa_api)
    if origen is None:
        return
    
    # Construir grafo completo
    todas_ubicaciones = [origen] + destinos
    construir_grafo_completo(grafo, mapa_api, todas_ubicaciones)
    
    # Inicializar calculador de rutas
    calculador = CalculadorRutas(grafo, mapa_api)
    
    # Menú de opciones de cálculo
    limpiar_pantalla()
    print("OPCIONES DE CÁLCULO")
    print("\n1. Ruta óptima entre origen y cada destino")
    print("2. Ruta que visite todos los destinos (problema del viajante)")
    
    opcion = input("\nSeleccione una opción (1-2): ").strip()
    
    if opcion == "1":
        calculador.calcular_rutas_individuales(origen, destinos)
    elif opcion == "2":
        calculador.calcular_ruta_viajante(origen, destinos)
    else:
        print("Opción no válida")
    
    print("¡Gracias por usar el sistema de optimización de rutas!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Programa interrumpido por el usuario")
    except Exception as e:
        print(f"Error inesperado: {e}")