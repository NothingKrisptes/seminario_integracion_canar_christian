print("CRUD DE LISTAS EN PYTHON")
avengers = [
    {"id": 1, "nombre": "Tony Stark", "heroe": "Iron Man", "estado": "Activo"},
    {"id": 2, "nombre": "Steve Rogers", "heroe": "Capitan América", "estado": "Activo"},
    {"id": 3, "nombre": "Thor Odinson", "heroe": "Thor", "estado": "Activo"},
]
id_publico = 4
def create():
    id = 4
    print("Reclutar avenger")
    nombre = input("Nombre heroe: ")
    heroe = input("Heroe: ")
    estado = input("Estado (Activo, Retirado, Desaparecido)")
    nuevo_avenger = {
        "id": id_publico,
        "nombre": nombre,
        "heroe": heroe,
        "estado": estado
    }
    avengers.append(nuevo_avenger)
    print("Creado")

def read():
    print("Lista de avengers")
    for avenger in avengers:
        print(f"{avenger["id"]} - nombre : {avenger["nombre"]}")

def update():
    print("Actualizar avenger")
    id_update = int(input("id a modificar: "))
    for avenger in avengers:
        if (avenger[id]==id_update):
            avenger["nombre"] = input("Nuevo nombre")
            avenger["heroe"] = input("Nuevo heroe")
            avenger["estado"] = input("Nuevo estado")
            print("Actualizado")

def delete():
    print("Eliminar avenger")
    id_delete = int(input("id a borrar"))
    for avenger in avengers:
        if (avenger[id]==id_delete):
            avengers.remove(avenger)
            print("Avenger eliminado")
def menu():
    while True:
        print("Avengers")
        print("1. Crear")
        print("2. Leer")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Salir")
        option = input("Seleccione 1 al 5")
        if option=="1":
            create()
        elif option=="2":
            read()
        elif option=="3":
            update()
        elif option=="4":
            delete()
        elif option=="5":
            print("Cerrando sistema")
            break
        else:
            print("Intente nueva opcion")

if __name__ == "__main__":
    menu()