# se llama al archivo con todas las funciones
import Dealer
import time

# se llama a la funcion para generar el mazo de 52 cartas ordenadas
Generar_mazo_noOrden= Dealer.generar_mazo()

print(f"Mazo generado{Generar_mazo_noOrden}") # se muestra maso generado aleatoriamente
print(f"Numero de cartas en el mazo: {len(Generar_mazo_noOrden)}") # numero total de cartas (52)

# se llama a la funcion que separa las cartas  y las ordena
# tambien devuelve 4 listas ordenadas

Corazon,Trevol,Diamante,Picas = Dealer.Clasificar_Carta(Generar_mazo_noOrden)

# se imprime cada grupo de cartas
print(f"\nCorazones: {Corazon}")
time.sleep(2)
print(f"\nTrevoles: {Trevol}")
time.sleep(2)
print(f"\nDiamantes: {Diamante}")
time.sleep(2)
print(f"\nPicas: {Picas}")
