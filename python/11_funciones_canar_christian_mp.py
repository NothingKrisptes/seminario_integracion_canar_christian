print("Funciones ")
print("Autor: Christian Cañar")

def alimentar_mascota():
    print("Se prepara la comida")
    print("¡Firulais está comiendo!")

alimentar_mascota()
alimentar_mascota()
alimentar_mascota()
alimentar_mascota()

def saludar(mascota):
    print(mascota, "recibe a los visitantes")

saludar("Firulais")
saludar("Mishi")
saludar("Copito")
saludar("Rocky")
saludar("Toby")
saludar("Luna")
saludar("Piolín")

def calcular_costo(costo_base, mascotas):
    total = costo_base * mascotas
    return total

resultado = calcular_costo(25, 2)
print("El costo de adoptar 2 mascotas es: ", resultado)

resultado = calcular_costo(4, 5)
print("El costo de adoptar 5 mascotas es: ", resultado)

def evaluar_adopcion(nombre, puntaje):
    if puntaje >= 70:
        print(f"La adopción de {nombre} fue aprobada")
    else:
        print(f"{nombre} necesita más referencias para adoptar")
evaluar_adopcion("Christian Cañar", 65)
evaluar_adopcion("Ana", 90)

nombre_mascota: str = "Firulais"
edad: int = 2
peso: float = 24.5
es_activo: bool = True

def calcular_racion(gramos_por_kilo: float, peso: float) -> float:
    return gramos_por_kilo * peso

racion: float = calcular_racion(15.5, 2)
print("Ración calculada", racion)
