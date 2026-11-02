confianza = 20
while confianza < 100:
    print("Firulais está ganando confianza")
    confianza += 20

print("¡Firulais ya confía en su nuevo hogar!")

comida = 1000
while comida > 0:
    print("En el plato de Firulais quedan", comida, "gramos de croquetas")
    comida -= 250
print("Firulais terminó sus croquetas")

print("Continue y Break")
dia = 0
while dia < 10:
    dia += 1
    if dia == 4:
        print("Día 4: Firulais va al veterinario")
        continue
    print("Dia", dia, "Firulais se prepara para la adopción")
    if dia == 8:
        print("Fin de la jornada de adopción")
        break

jaulas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
for jaula in jaulas:
    if jaula == "3":
        print("Jaula en mantenimiento")
        continue
    if jaula == "7":
        print("Se encuentra la mascota extraviada")
        break
    else:
        print("Revisión normal")
