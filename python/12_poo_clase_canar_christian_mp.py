class Mascota:
    nombre: str
    especie: str
    def __init__(self, nombre: str, especie: str):
        self.nombre = nombre
        self.especie = especie

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Especie ", self.especie)

firulais = Mascota("Firulais", "Perro")
mishi = Mascota("Mishi", "Gato")
copito = Mascota("Copito", "Conejo")
piolin = Mascota("Piolín", "Ave")

firulais.mostrar_info()
mishi.mostrar_info()
copito.mostrar_info()
piolin.mostrar_info()
