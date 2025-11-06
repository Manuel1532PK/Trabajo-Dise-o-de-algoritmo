class Furgon:
    def __init__(self, id):
        self.id = id
        self.capacidad_max = 40
        self.paquetes_actuales = 0
        self.ruta = []
        self.tiempo_total = 0  # segundos

    def puede_agregar(self, cantidad, tiempo_est):
        return (self.paquetes_actuales + cantidad <= self.capacidad_max) and (self.tiempo_total + tiempo_est <= 7200)

    def agregar_entrega(self, nodo, cantidad, tiempo_est):
        self.paquetes_actuales += cantidad
        self.ruta.append(nodo)
        self.tiempo_total += tiempo_est