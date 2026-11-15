class Mascota:
    nombre: str
    especie: str

    def __init__(self, nombre: str, especie: str):
        self.nombre = nombre
        self.especie = especie

    def mostrar_info(self):
        print("Nombre: ", self.nombre)
        print("Especie: ", self.especie)

class Perro(Mascota):
    def __init__(self, nombre: str, especie: str):
        super().__init__(nombre, especie)

    def muestra_nombre(self):
        print("Nombre: ", self.nombre)

firulais = Perro("Firulais", "Perro")
rocky = Perro("Rocky", "Perro")

firulais.mostrar_info()
rocky.mostrar_info()
firulais.muestra_nombre()
rocky.muestra_nombre()
