class Guerrero:
    nombre: str
    __poder: int
    
    def __init__(self, nombre:str, poder:int):
        self.nombre = nombre
        self.__poder = poder

    def mostrat_info(self):
        print("Nombre ",self.nombre)

    def get_poder(self):
        return self.__poder

goku = Guerrero("Goku", 9000)
vegeta = Guerrero("Vegeta", 6000)
piccolo = Guerrero("Piccolo", 10000)
christian = Guerrero("Christian", 8600)

goku.mostrat_info()
vegeta.mostrat_info()
piccolo.mostrat_info()
christian.mostrat_info()
print(goku.nombre)
print(vegeta.nombre)
print(vegeta.get_poder())