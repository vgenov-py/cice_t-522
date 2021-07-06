menu = "--CONVERTER PY--\n1. Longitud\n2. Volumen\n3. Masa\n4. Velocidad\n5. Salir"
menu_exit = "1. Volver al menú principal\n2. Salir"
user = "0"
is_first_time = False

while user != "5":
    if is_first_time:
        print(menu_exit)
        user = input("Elija opción: ")
        if user == "2":
            user = "5"
        is_first_time = False
    else:
        is_first_time = True
        print(menu)
        user = input("Elija opción: ")
        is_first_time = False

        if user == "1":
            print("1. km a milla")
            print("2. mt a pulgadas")
            user = input("Elija opción: ")
            if user == "1":
                km = int(input("km: "))
                miles = km * 1.6
                print(f"{km} km corresponden a {miles} millas")

            elif user == "2":
                mt = int(input("km: "))
                inches = mt * 1.6
                print(f"{km} km corresponden a {miles} millas")
                print(menu_exit)
                user = input("Elija opción: ")
    



            