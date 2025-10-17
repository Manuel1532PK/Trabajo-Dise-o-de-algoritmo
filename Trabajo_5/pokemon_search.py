class BuscadorPokemon:  #Clase que implementa el algoritmo de búsqueda binaria
    
    def busqueda_binaria(self, lista, objetivo):
        izquierda, derecha = 0, len(lista) - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            valor_medio = lista[medio]

            if valor_medio == objetivo:
                return True
            elif valor_medio < objetivo:
                izquierda = medio + 1
            else:
                derecha = medio - 1

        return False