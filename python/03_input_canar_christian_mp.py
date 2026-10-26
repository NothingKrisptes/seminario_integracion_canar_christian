print("Incluir Datos con Input")
nombre = input("¿Cual es tu nombre?: ")
print("¡Hola", nombre, "!")
print("Bienvenido al refugio de mascotas")
print("Hasta luego " + nombre)

cantidad = int(input("¿Cuántas mascotas hay disponibles?: "))
total = cantidad + 2
print("Mascotas totales: ", total)

print(" CONVERSIONES ")
print("=== TIENDA DEL REFUGIO ===")
nombre_cliente = input("Nombre del adoptante: ")
precio = float(input("Precio de la vacuna: "))
cantidad = int(input("Cantidad de vacunas: "))
total = cantidad * precio
print("Total a pagar: ", total)
print("Total a pagar (round): ", round(total, 2))
print(f"Total a pagar (f): ${total:.2f}")
