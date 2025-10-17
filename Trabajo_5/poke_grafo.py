#Clase que construye el grafo de evolución Pokémon.
class GrafoPokemon:
    def __init__(self):
        self.grafo = {}

    def build_grafo(self, chains):  #Construye el grafo de manera recursiva.
        if not chains:
            return

        current_name = chains["species"]["name"]
        evolutions = [evo["species"]["name"] for evo in chains["evolves_to"]]

        self.grafo[current_name] = evolutions

        for evolution in chains["evolves_to"]:
            self.build_grafo(evolution)

    def show_grafo(self, nodo=None, visitados=None):
        if visitados is None:
            visitados = set()

        if nodo is None and self.grafo:
            nodo = list(self.grafo.keys())[0]

        if nodo in visitados:
            return
        visitados.add(nodo)

        evolutiones = self.grafo.get(nodo, [])
        for evolution in evolutiones:
            print(f"[{nodo}] -> [{evolution}]")
            self.show_grafo(evolution, visitados)

        if not evolutiones:
            print(f"[{nodo}] -> []")