print("Funciones ")
print("Autor: Christian Cañar")

def kamehameha():
    print("Goku concentra su energía")
    print("!Kamehameha¡")

kamehameha()
kamehameha()
kamehameha()
kamehameha()

def atacar(guerrero):
    print(guerrero, "realiza un ataque")

atacar("Goku")
atacar("Vegeta")
atacar("Piccolo")
atacar("Christian")
atacar("Josue")
atacar("Cañar")
atacar("Muñoz")

def calcular_poder(poder, ataques):
    danio = poder * ataques
    return danio

resultado = calcular_poder(25, 2500)
print("El poder de Christian Cañar es: ", resultado)

resultado = calcular_poder(4, 5000)
print("El poder de Goku es: ", resultado)

def transformar_saiyayin(nombre, poder):
    if poder >= 9000:
        print(f"Transformación de {nombre} a SuperSayayin exitosa")
    else:
        print(f"{nombre} necesitas aumentar tu poder")
transformar_saiyayin("Christian Cañar", 8668)
transformar_saiyayin("Goku", 15000)

nombre_personaje: str = "Goku"
edad: int = 33
altura: float = 1.74
es_activo: bool = True

def multiplicador_poder(entrenamiento: float, edad: int) -> float:
    return entrenamiento * edad

poder: float = multiplicador_poder(15.5,2)
print("Poder calculado", poder)