def display_tower(tower):
    print("A:", tower['A'])
    print("B:", tower['B'])
    print("C:", tower['C'])
    print("-" * 20)


def move_disk(origin, destiny, tower):
    # Verifica qué torre tiene el disco más pequeño disponible
    if not tower[origin]:
        tower[origin].append(tower[destiny].pop())
        print(f"Mover disco de {destiny} -> {origin}")

    elif not tower[destiny]:
        tower[destiny].append(tower[origin].pop())
        print(f"Mover disco de {origin} -> {destiny}")

    elif tower[origin][-1] < tower[destiny][-1]:
        tower[destiny].append(tower[origin].pop())
        print(f"Mover disco de {origin} -> {destiny}")

    else:
        tower[origin].append(tower[destiny].pop())
        print(f"Mover disco de {destiny} -> {origin}")

    display_tower(tower)


def tower_hanoi_iterativa(n):
    tower = {
        'A': list(reversed(range(1, n + 1))),  # Torre origen
        'B': [],  # Torre auxiliar
        'C': []   # Torre destino
    }

    display_tower(tower)

    # Si el número de discos es par, intercambiamos destino y auxiliar
    if n % 2 == 0:
        origin, auxiliary, destiny = 'A', 'C', 'B'
    else:
        origin, auxiliary, destiny = 'A', 'B', 'C'

    num_movimientos = 2 ** n - 1
    print(f"\nNúmero total de movimientos: {num_movimientos}\n")

    for i in range(1, num_movimientos + 1):
        if i % 3 == 1:
            move_disk(origin, destiny, tower)
        elif i % 3 == 2:
            move_disk(origin, auxiliary, tower)
        elif i % 3 == 0:
            move_disk(auxiliary, destiny, tower)


# Ejecutar con los discos que desees
discos = int(input("Cuántos discos quieres usar en la Torre de Hanoi? "))
tower_hanoi_iterativa(discos)