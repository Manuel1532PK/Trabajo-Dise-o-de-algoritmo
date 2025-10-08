def display_tower(tower):
    print("A:", tower['A'])
    print("B:", tower['B'])
    print("C:", tower['C'])
    print("-" * 20)


def move_disk(origin, destiny, tower):
    disk = tower[origin].pop()
    tower[destiny].append(disk)
    print(f"Mover disco de {origin} -> {destiny}")
    display_tower(tower)


def tower_hanoi_recursiva(n, origin, destiny, auxiliary, tower):
    # Caso base: si solo hay un disco, muévelo directamente
    if n == 1:
        move_disk(origin, destiny, tower)
    else:
        #Mover n-1 discos de origen a auxiliar
        tower_hanoi_recursiva(n - 1, origin, auxiliary, destiny, tower)

        #Mover el disco más grande de origen a destino
        move_disk(origin, destiny, tower)

        #Mover los n-1 discos de auxiliar a destino
        tower_hanoi_recursiva(n - 1, auxiliary, destiny, origin, tower)


def ejecutar_torre_hanoi_recursiva():
    n = int(input("Cuántos discos quieres usar en la Torre de Hanoi: "))

    # Inicialización de las torres
    tower = {
        'A': list(reversed(range(1, n + 1))),  # Torre origen
        'B': [],  # Torre auxiliar
        'C': []   # Torre destino
    }

    display_tower(tower)
    print(f"\nNúmero total de movimientos esperados: {2 ** n - 1}\n")

    tower_hanoi_recursiva(n, 'A', 'C', 'B', tower)


# Ejecutar
ejecutar_torre_hanoi_recursiva()