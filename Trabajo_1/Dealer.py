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

#-------- Organizar por Tipo de cartas ---------------

def Clasificar_Carta(mazo):
    Corazon=[]
    Trevol=[]
    Diamante=[]
    Picas=[]

    for carta in mazo:

        Tipo = carta[-1]
        if Tipo == "C":
            Corazon.append(carta)
        elif Tipo == "T":
            Trevol.append(carta)
        elif Tipo == "D":
            Diamante.append(carta)
        elif Tipo == "P":
            Picas.append(carta)

    Corazon=insertion_sort(Corazon)
    Trevol=insertion_sort(Trevol)
    Diamante=insertion_sort(Diamante)
    Picas=insertion_sort(Picas)

    return Corazon,Trevol,Diamante,Picas