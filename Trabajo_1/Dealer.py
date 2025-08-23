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

Generar_mazo_noOrden= generar_mazo()
print(Generar_mazo_noOrden)
print(f"Numero de cartas en el mazo: {len(Generar_mazo_noOrden)}")