from abc import ABC, abstractmethod

class Mascota(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Mascota):
    def hacer_sonido(self):
        return "Guau guau!"

firulais = Perro()
print(firulais.hacer_sonido())
