import random

# nombre = "Vito"
# apellido = "Genovese" # Designo apellido
# space = " "

# edad = 12
# is_adult = edad >= 18

# IF STATEMENTS:

# if edad >= 18:
#     print("Es adulto")
# else:
#     print("No es adulto")

# apellido_en_mayus = apellido.upper()
# print(apellido_en_mayus)
# edad.
# nombre_completo = "Vito Genoves"

# result = nombre_completo.replace("Genoves", "Fernández")
# print(result)

lorem = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of 'de Finibus Bonorum et Malorum' (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, 'Lorem ipsum dolor sit amet..'"

a = "hola"
b = "Hola"
# print(f"{a} hola")
# EJERCICIO 1:
# print(a.title()== b)
# print(a.capitalize() == b)
# print(a == b.lower())
# print(a.endswith("a") == b.endswith("a"))

# EJERCICIO 3:
# print(lorem.count("it") + lorem.count("It"))

# EJERCICIO 4:
# print(lorem.find("Ipsum"))
# print(lorem[34:39])

# EJERCICIO 5:
palabra = lorem.split(" ")
con_count = lorem.count(" ") + 1
# print("Con la función len: ", len(palabra))
# print("Con el método count: ", len(palabra))

# EJERCICIO 6:
limite_inferior = lorem.find("Richard")
resultado = lorem[limite_inferior: 171]
resultado = resultado.lower()
# print(resultado)

lista_palabras = lorem.split(" ")  # Ejercicio 7
resultado = lista_palabras[30].lower()

# Explicación:
# ejemplo = "hola cómo estás?"
# print(ejemplo.find("h"))
# ejemplo = "Hola chau adi"
# print(ejemplo[5:9])
# ejemplo = "1"
# print(len(ejemplo))

# EJERCICIO 8
lista_palabras = lorem.split(" ")
# print(type(lista_palabras))
# print(lista_palabras[0])
# lista_ejemplo = [1, "una palabra", 3, 4, 5]
# print(lista_ejemplo[1])
# print(lista_palabras)
password = "contraseña"
# edad = 15
# edad = str(edad) --> convertir de int a str
longitud_password = len(password)
# print(lista_palabras)
password = password + str(longitud_password)
# print(f"Actualmente la variable password guarda la siguiente string: {password}")
password = password.capitalize()
# print(f"Actualmente la variable password guarda la siguiente string: {password}")
password = password.replace("o", "u")
# print("3: ", password)
password = password.replace("a", "e")
# print("4: ", password)

# EJERCICIOS CONDICIONALES: IF, ELIF, ELSE (Ej. 4)
lista_palabras = lorem.split(" ")
cantidad_palabras = len(lista_palabras)
# print(lista_palabras)
# if cantidad_palabras  >= 100:
# print("Se ha ejecutado el IF")

# if cantidad_palabras  >= 80:
# print("Se ha ejecutado el ELIF")

# elif cantidad_palabras < 80 and cantidad_palabras > 0:
#     print("Se he ejecutado el ELSE")

# if cantidad_palabras <= 100 or cantidad_palabr  as >= 150:
#     print("El texto se encuentra en un rango de 120 a 130 palabras")

# EJERCICIO 5:
# user = input("Search in Lorem: ")
# indice = lorem.find(user)
# print(indice)
# if lorem.find(user) > -1:
#     print("Palabra encontrada!")
# else:
#     print("La palabra no se encuentra en el texto")

# cadena = "Natura non facit saltum"
# indice_encontrado = 7
# print(cadena[indice_encontrado:indice_encontrado + 6])


# EJERCICIO 6 (RPS):

# user = input("Elige: ")
# alternatives = ["rock", "paper", "scissors"] # ["rock", "scissors"]
# # print(type(alternatives))
# pc = random.choice(alternatives)
# print(pc)
# tie = "Tie!"
# win = "Win!"
# lose = "Lose!"


# if user == pc:
#     print(tie)
# else:
#     alternatives.pop(alternatives.index(user))
#     if pc == alternatives[0] and user != "paper":
#         print(lose)
#     else:
#         print(win)

# sorted y sort 
test = [2,1.4,4,3] # lista de char
test_ordenado = sorted(test)
# print(test_ordenado)

test_2 = [2,1.4,4,3]
test_2.sort(reverse=True)
print(test_2)



# roca = "rock"
# print(roca[0:3])
# alternatives = ["rock", "paper", "scissors"]
# print(alternatives[0:3])
# user_index = alternatives.index(user)
# print(alternatives.pop(user_index))
# print(alternatives)

# print("---------------------------------")
# print("#################################")
# print("---------------------------------")

# hola = "hola"
# print(hola)
# hola_mayus = hola.upper()
# print(hola_mayus)

# test_lista = [1,2,3,4]
# print(test_lista)
# test_lista_con_s = test_lista.append("s")
# print(test_lista_con_s)
