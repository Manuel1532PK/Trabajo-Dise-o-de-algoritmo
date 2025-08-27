import Dealer

Generar_mazo_noOrden= Dealer.generar_mazo()
print(f"Mazo generado{Generar_mazo_noOrden}")
print(f"Numero de cartas en el mazo: {len(Generar_mazo_noOrden)}")

Corazon,Trevol,Diamante,Picas = Dealer.Clasificar_Carta(Generar_mazo_noOrden)
print(f"\nCorazon: {Corazon}")
print(f"\nTrevol: {Trevol}")
print(f"\nDiamante: {Diamante}")
print(f"\nPica :{Picas}")
