poder = 2000
while poder < 10000:
    print("Vegeta esta entrenando")
    poder+=2000

print("!Vegeta alcanzó su objetivo¡")

while poder>0:
    print("Majin Buu tiene", poder, "de poder")
    poder-=500
print("Majin buu quedó sin energía")

print("Continue y Break")
dia = 0
while dia < 10:
    dia+=1
    if dia == 4:
        print("Día 4: Gohan estudia")
        continue
    print("Dia", dia, "Gohan entrena")
    if dia == 8:
        print("Fin del sistema")
        break

sectores = ["1","2","3","4","5","6","7","8","9","10"]
for sector in sectores:
    if sector == "3":
        print("Zona destruida")
        continue
    if sector == "7":
        print("Encuentra a los androides")
        break
    else:
        print("Exploracion normal")
