from pokeapi_request import PokeAPI
from poke_grafo import GrafoPokemon
from pokemon_search import BuscadorPokemon

def menu():
    evolution_id = input("Digite un numero del 1 al 151:")      
    url = f"https://pokeapi.co/api/v2/evolution-chain/{evolution_id}/"

    # Consumir la API
    api = PokeAPI(url)
    dates = api.get_data()
    if not dates:
        print("No se pudieron obtener los datos de la PokéAPI.")
        return

    # Construir el grafo
    grafo = GrafoPokemon()
    grafo.build_grafo(dates["chain"])

    # Mostrar la cadena de evolución
    print("Cadena de evolución:")
    grafo.show_grafo()

    # Obtener el Pokémon inicial (primer nodo en la cadena)
    pokemon_inicial = dates["chain"]["species"]["name"]
    print(f"Pokémon inicial en la cadena: {pokemon_inicial}")

    # First_names de los Pokémon en la cadena (ordenados)
    Names = sorted(grafo.grafo.keys())

    # Crear buscador (versión con self)
    Search = BuscadorPokemon()
    First_name = pokemon_inicial
    if Search.busqueda_binaria(Names, First_name):
        evoluciones = grafo.grafo.get(First_name, [])

        if evoluciones:
            print(f"{First_name} evoluciona a: {evoluciones}")
        else:
            print(f"{First_name} no tiene evoluciones.")
    else:
        print(f"{First_name} no se encuentra en esta cadena de evolución.")

# Ejecutar automáticamente
menu()