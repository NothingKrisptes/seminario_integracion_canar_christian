for paseo in range(1, 6):
    print("Firulais da la vuelta número", paseo, "al parque")

for numero in range(1, 11):
    print("Croquetas ", 5, '*', numero, "=", 5*numero)

for numero in range(1, 11, 2):
    print("Croquetas ", 5, '*', numero, "=", 5*numero)

mascotas = [
    {"id": 1, "nombre": "Firulais", "especie": "Perro", "estado": "Disponible"},
    {"id": 2, "nombre": "Mishi", "especie": "Gato", "estado": "Disponible"},
    {"id": 3, "nombre": "Copito", "especie": "Conejo", "estado": "Adoptado"},
]

print("Lista de mascotas")
for mascota in mascotas:
    print(f"{mascota['id']} - nombre : {mascota['nombre']}")

nombres = ["Pedro", "Pablo", "Juan"]
for nombre in nombres:
    print("Adoptante actual: ", nombre)

socializacion = {
    "Firulais": 95,
    "Rocky": 60,
    "Toby": 60,
    "Luna": 45
}

for nombre, puntaje in socializacion.items():
    if puntaje >= 90:
        print(nombre, "está listo para ser adoptado")
    else:
        print(nombre, "necesita más socialización")

print("Ciclo for anidados")
mascotas_visitadas = ["Firulais", "Rocky", "Toby", "Mishi", "Luna", "Copito"]
for mascota in mascotas_visitadas:
    print("Turno de: ", mascota)
    for visita in range(1, 4):
        print("Visita: ", visita)

print("Break y Continue")
for mascota in mascotas_visitadas:
    if (mascota == "Luna"):
        break
    if (mascota == "Rocky"):
        continue
    print("Mascota", mascota)
