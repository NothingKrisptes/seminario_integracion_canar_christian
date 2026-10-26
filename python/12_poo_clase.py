class Guerrero:
    nombre: str
    raza: str
    def __init__(self, nombre:str, raza:str):
        self.nombre = nombre
        self.raza = raza

    def mostrat_info(self):
        print("Nombre ",self.nombre)
        print("Raza ",self.raza)

goku = Guerrero("Goku", "Sayayin")
vegeta = Guerrero("Vegeta", "Sayayin")
piccolo = Guerrero("Piccolo", "Namek")
christian = Guerrero("Christian", "Humano")

goku.mostrat_info()
vegeta.mostrat_info()
piccolo.mostrat_info()
christian.mostrat_info()