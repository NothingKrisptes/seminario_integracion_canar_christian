"""
Manejo de Cadena de Caracteres
"""
nombre1 = "Firulais Rex"
print(f"Mascota 1: {nombre1}")
print(f"Tipo de datos: {type(nombre1)}")
nombre2 = "Mishi Luna"
print(f"Mascota 2: {nombre2}")
print(f"Tipo de datos: {type(nombre2)}")

##### Funciones comunes de las variables String
print("Funciones comunes de texto")
mascota_1 = "Firulais"
mascota_2 = "Mishi"
longitud_mascota_1 = len(mascota_1)
longitud_mascota_2 = len(mascota_2)
print("nombre mascota 1: ", mascota_1)
print("longitud mascota 1: ", longitud_mascota_1)
print("nombre mascota 2: ", mascota_2)
print("longitud mascota 2: ", longitud_mascota_2)

print("Convertir Mayusculas y minúsculas")
mensaje = "El refugio abre su jornada de Adopción"
mensaje_mayuscula = mensaje.upper()
mensaje_minuscula = mensaje.lower()
print("Mensaje Original: ", mensaje)
print("Mensaje en Mayusculas: ", mensaje_mayuscula)
print("Mensaje en Minusculas: ", mensaje_minuscula)

print("Reemplazo de substring")
mensaje = "La mascota viajará al refugio Norte"
nuevo_mensaje = mensaje.replace("Norte", "Sur")
print("Mensaje Original: ", mensaje)
print("Mensaje Reemplazado: ", nuevo_mensaje)

print("Separacion de cadenas en un arreglo")
mascotas = "Firulais,Mishi,Copito"
print("mascotas: ", mascotas)
lista_mascotas = mascotas.split(",")
print(lista_mascotas)
print("Primera mascota : ", lista_mascotas[0])

print("Extraer subcadenas")
mensaje = "Adopta un amigo fiel para siempre"
verbo = mensaje[0:6]
adjetivo = mensaje[16:20]
print("verbo es : ", verbo)
print("adjetivo es : ", adjetivo)

print("Comprobaciones útiles")
codigo = "FIR01"
numero = "2026"
nombre = "RefugioUTE"
identificador = "MASCOTA1"
print(codigo.isalnum())
print(numero.isdigit())
print(numero.isalpha())
print(identificador.isalnum())
print(identificador.isdigit())
