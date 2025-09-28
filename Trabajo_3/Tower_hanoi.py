def display_Tower(Tower):
    print("A:", Tower['A'])
    print("B:", Tower['B'])
    print("C:", Tower['C'])
    print("-" * 20)


def mover_disco(origin, destiny, Tower):
    # Verifica qué torre tiene el disco más pequeño disponible
    if not Tower[origin]:
        Tower[origin].append(Tower[destiny].pop())
        print(f"Mover disco de {destiny} -> {origin}")

    elif not Tower[destiny]:
        Tower[destiny].append(Tower[origin].pop())
        print(f"Mover disco de {origin} -> {destiny}")

    elif Tower[origin][-1] < Tower[destiny][-1]:
        Tower[destiny].append(Tower[origin].pop())
        print(f"Mover disco de {origin} -> {destiny}")

    else:
        Tower[origin].append(Tower[destiny].pop())
        print(f"Mover disco de {destiny} -> {origin}")

    display_Tower(Tower)


def torre_hanoi_iterativa(n):
    Tower = {
        'A': list(reversed(range(1, n + 1))),  # Torre origen
        'B': [],  # Torre auxiliar
        'C': []   # Torre destino
    }

    display_Tower(Tower)

    # Si el número de discos es par, intercambiamos destino y auxiliar
    if n % 2 == 0:
        origin, auxiliary, destiny = 'A', 'C', 'B'
    else:
        origin, auxiliary, destiny = 'A', 'B', 'C'

    num_movimientos = 2 ** n - 1
    print(f"\nNúmero total de movimientos: {num_movimientos}\n")

    for i in range(1, num_movimientos + 1):
        if i % 3 == 1:
            mover_disco(origin, destiny, Tower)
        elif i % 3 == 2:
            mover_disco(origin, auxiliary, Tower)
        elif i % 3 == 0:
            mover_disco(auxiliary, destiny, Tower)


# Ejecutar con los discos que desees
discos = int(input("Cuántos discos quieres usar en la Torre de Hanoi? "))
torre_hanoi_iterativa(discos)