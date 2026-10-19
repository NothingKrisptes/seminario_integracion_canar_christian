print("OPERADORES")
print("Operadores Aritméticos")
print(" + Suma: ", 5, "+", 3, "=", 5+3)
print(" - Resta: ", 5, "-", 3, "=", 5-3)
print(" * Multiplicación: ", 5, "*", 3, "=", 5*3)
print(" / División: ", 15, "/", 3, "=", 15/3)
print(" // División entera: ", 10, "//", 3, "=", 10//3)
print(" % Residuo: ", 10, "%", 3, "=", 10%3)
print(" ** Potencia: ", 2, "**", 3, "=", 2**3)

print("TABLA DE MULTIPLICAR DEL 5 (croquetas por mascota)")
print(5, "*", 1, "=", 5*1)
print(5, "*", 2, "=", 5*2)
print(5, "*", 3, "=", 5*3)
print(5, "*", 4, "=", 5*4)
print(5, "*", 5, "=", 5*5)
print(5, "*", 6, "=", 5*6)
print(5, "*", 7, "=", 5*7)
print(5, "*", 8, "=", 5*8)
print(5, "*", 9, "=", 5*9)
print(5, "*", 10, "=", 5*10)
print(5, "*", 11, "=", 5*11)
print(5, "*", 12, "=", 5*12)

print("OPERADORES DE COMPARACIÓN")
print("== Igual a : ", 5, "==", 5, 5==5)
print("== Igual a : ", 5, "==", 4, 5==4)
print("!= Diferente de : ", 5, "!=", 4, 5!=4)
print("!= Diferente de : ", 5, "!=", 5, 5!=5)
print("> Mayor que : ", 10, ">", 8, 10>8)
print("> Mayor que : ", 10, ">", 18, 10>18)
print("< Menor que : ", 10, "<", 18, 10<18)
print("< Menor que : ", 10, "<", 8, 10<8)
print(">= Mayor o igual que : ", 10, ">=", 18, 10>=18)
print(">= Mayor o igual que : ", 10, ">=", 8, 10>=8)
print("<= Menor o igual que : ", 10, "<=", 18, 10<=18)
print("<= Menor o igual que : ", 10, "<=", 8, 10<=8)

print("OPERADORES LÓGICOS")
print("Operador and : (5==5)and(4>3)", (5==5)and(4>3))
print("Operador and : (5==5)and(4>8)", (5==5)and(4>8))
print("Operador or : (5==5)or(4>8)", (5==5)or(4>8))
print("Operador or : (5==6)or(4>8)", (5==6)or(4>8))
print("Operador not : not (5==6)", not (5==6))
print("Operador not : not (5==5)", not (5==5))

tiene_vacunas = True
refugio_abierto = True

puede_adoptar = tiene_vacunas and refugio_abierto
print("¿Puede adoptar? ", puede_adoptar)

es_adoptante_frecuente = True
tiene_vacunas = False
aprobado_por_referencias = es_adoptante_frecuente or tiene_vacunas
print("¿Adopción aprobada? ", aprobado_por_referencias)
