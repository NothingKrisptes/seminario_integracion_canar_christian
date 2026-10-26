print("CRUD DE LISTAS EN PYTHON")
mascotas = [
    {"id": 1, "nombre": "Firulais", "especie": "Perro", "estado": "Disponible"},
    {"id": 2, "nombre": "Mishi", "especie": "Gato", "estado": "Disponible"},
    {"id": 3, "nombre": "Copito", "especie": "Conejo", "estado": "Disponible"},
]
id_publico = 4


def create():
    global id_publico
    print("Registrar mascota")
    nombre = input("Nombre de la mascota: ")
    especie = input("Especie: ")
    estado = input("Estado (Disponible, Adoptado, En tratamiento): ")
    nueva_mascota = {
        "id": id_publico,
        "nombre": nombre,
        "especie": especie,
        "estado": estado
    }
    mascotas.append(nueva_mascota)
    id_publico += 1
    print("Creado")


def read():
    print("Lista de mascotas")
    for mascota in mascotas:
        print(f"{mascota['id']} - nombre : {mascota['nombre']} - especie : {mascota['especie']} - estado : {mascota['estado']}")


def update():
    print("Actualizar mascota")
    id_update = int(input("id a modificar: "))
    for mascota in mascotas:
        if mascota["id"] == id_update:
            mascota["nombre"] = input("Nuevo nombre: ")
            mascota["especie"] = input("Nueva especie: ")
            mascota["estado"] = input("Nuevo estado: ")
            print("Actualizado")
            return
    print("No existe una mascota con ese id")


def delete():
    print("Eliminar mascota")
    id_delete = int(input("id a borrar: "))
    for mascota in mascotas:
        if mascota["id"] == id_delete:
            mascotas.remove(mascota)
            print("Mascota eliminada")
            return
    print("No existe una mascota con ese id")


def menu():
    while True:
        print("Refugio de mascotas")
        print("1. Crear")
        print("2. Leer")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Salir")
        option = input("Seleccione 1 al 5: ")
        if option == "1":
            create()
        elif option == "2":
            read()
        elif option == "3":
            update()
        elif option == "4":
            delete()
        elif option == "5":
            print("Cerrando sistema")
            break
        else:
            print("Intente nueva opcion")


if __name__ == "__main__":
    menu()
