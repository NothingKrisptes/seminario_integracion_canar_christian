class Mascota:
    nombre: str
    __chip: int

    def __init__(self, nombre: str, chip: int):
        self.nombre = nombre
        self.__chip = chip

    def mostrar_info(self):
        print("Nombre ", self.nombre)

    def get_chip(self):
        return self.__chip

firulais = Mascota("Firulais", 9000)
mishi = Mascota("Mishi", 6000)
copito = Mascota("Copito", 10000)
piolin = Mascota("Piolín", 8600)

firulais.mostrar_info()
mishi.mostrar_info()
copito.mostrar_info()
piolin.mostrar_info()
print(firulais.nombre)
print(mishi.nombre)
print(mishi.get_chip())
