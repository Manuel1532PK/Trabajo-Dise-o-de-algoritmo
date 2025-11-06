import os
import time
from grafo import Grafo
from API_google_maps import GoogleMapsAPI
from calcular_rutas import CalculadorRutas

#Funciones utilitarias

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Módulo: Búsqueda de ubicaciones

def menu_buscar_ubicacion(mapa_api):
    limpiar_pantalla()
    print("=== BÚSQUEDA DE UBICACIONES ===\n")
    direccion = input("Ingrese una dirección o ciudad: ").strip()
    
    if not direccion:
        print("Debe ingresar una dirección válida.")
        return
    
    print(f"Buscando coordenadas para: {direccion}...")
    lat, lng = mapa_api.geocodificar(direccion)
    
    if lat and lng:
        print(f"Resultado:")
        print(f"Dirección: {direccion}")
        print(f"Latitud: {lat:.6f}")
        print(f"Longitud: {lng:.6f}")
    else:
        print("No se pudo encontrar la ubicación en Google Maps.")
    
    input("\nPresione ENTER para volver al menú principal...")

# Módulo: Planificación de entregas

def obtener_ubicaciones(grafo, mapa_api):
    print("=== PLANIFICAR ENTREGAS ===\n")

    origen = input("Ingrese la ciudad de ORIGEN: ").strip()
    if not origen:
        print("Debe ingresar un origen válido.")
        return None, []

    lat_origen, lng_origen = mapa_api.geocodificar(origen)
    if lat_origen is None:
        print("No se pudo geocodificar el origen.")
        return None, []

    grafo.agregar_nodo(origen, lat_origen, lng_origen)

    destinos = []
    while True:
        destino = input(f"Destino #{len(destinos) + 1} (ENTER para terminar): ").strip()
        if not destino:
            break
        lat, lng = mapa_api.geocodificar(destino)
        if lat is None:
            print(f"No se encontró: {destino}")
            continue
        grafo.agregar_nodo(destino, lat, lng)
        destinos.append(destino)
        print(f"Agregado: {destino} ({lat:.4f}, {lng:.4f})")
    
    return origen, destinos

def construir_grafo_completo(grafo, mapa_api, ubicaciones):
    print("\nCalculando distancias entre ubicaciones...\n")
    for i, u1 in enumerate(ubicaciones):
        for j, u2 in enumerate(ubicaciones):
            if i != j:
                distancia, duracion = mapa_api.calcular_distancia(u1, u2)
                if distancia != float('inf'):
                    grafo.agregar_arista(u1, u2, distancia / 1000)  # a km
                    print(f"{u1} → {u2}: {distancia/1000:.2f} km ({duracion/60:.1f} min)")
                else:
                    print(f"{u1} → {u2}: no se pudo calcular")
                time.sleep(0.1)

def menu_planificar_entregas(grafo, mapa_api):
    limpiar_pantalla()
    origen, destinos = obtener_ubicaciones(grafo, mapa_api)
    if not origen or not destinos:
        input("\nPresione ENTER para volver al menú principal...")
        return
    
    todas = [origen] + destinos
    construir_grafo_completo(grafo, mapa_api, todas)
    calculador = CalculadorRutas(grafo, mapa_api)

    limpiar_pantalla()
    print("=== OPCIONES DE RUTAS ===\n")
    print("1. Ruta óptima individual (origen → cada destino)")
    print("2. Ruta completa (viajante entre todos los destinos)")
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        calculador.calcular_rutas_individuales(origen, destinos)
    elif opcion == "2":
        calculador.calcular_ruta_viajante(origen, destinos)
    else:
        print("Opción inválida.")
    
    input("\nPresione ENTER para volver al menú principal...")

# MENÚ PRINCIPAL

def main():
    api_key = "AIzaSyDiCxWwgTBVaVJxhkWp_OZt-70z8Fj5XSE" #<----------------aca va la api key
    if not api_key:
        print("Debes proporcionar una API Key de Google Maps.")
        return

    try:
        mapa_api = GoogleMapsAPI(api_key)
        grafo = Grafo()
    except Exception as e:
        print(f"Error inicializando API: {e}")
        return

    while True:
        limpiar_pantalla()
        print("=== SISTEMA DE RUTAS Y ENTREGAS ===\n")
        print("1. Buscar ubicación")
        print("2. Planificar entregas")
        print("3. Salir")

        opcion = input("\nSeleccione una opción: ").strip()
        if opcion == "1":
            menu_buscar_ubicacion(mapa_api)
        elif opcion == "2":
            menu_planificar_entregas(grafo, mapa_api)
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")
            time.sleep(1)

# ==============================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}")