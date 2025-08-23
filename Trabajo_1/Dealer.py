import random

def generar_mazo():

    Tipo_carta = ["C","T","D","P"]
    Valores = list(range(1,14))

    Mazo = []
    for Tipo_carta in Tipo_carta:
        for Valor in Valores:
            Mazo.append(f"{Valor}{Tipo_carta}")

    random.shuffle(Mazo)
    return Mazo


#--- metodo de insertion sort --------

def insertion_sort(lista):
    n = len(lista)
    # Recorre la lista desde el segundo elemento
    for i in range(1, n):
        key = lista[i]
        key_num = int(key[:-1])  #Se creo esta key con un int para evitar problemas de cadena de texto el [:-1] es para separar el ultimo caracter 
        j = i - 1

        print(f"Baraja actaul:{key}, indice: {i}") #Contador para saber cuantas veces se ha realizado la inserccion

        while j >= 0 and key_num < int(lista[j][:-1]):
            lista[j + 1] = lista[j]
            print(lista)
            j -= 1
        lista[j + 1] = key
        print(lista)
        print(f"Lista actual: {lista}")
    return lista

Generar_mazo_noOrden= generar_mazo()
print(Generar_mazo_noOrden)
print(f"Numero de cartas en el mazo: {len(Generar_mazo_noOrden)}")

Mazo_Ordenado = insertion_sort(Generar_mazo_noOrden)
print(f"\nMazo ordenado por numero:{Mazo_Ordenado}")