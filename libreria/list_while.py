students = ["Pedro", "Luís", "Milagros", "Marta", "Macarena", "Marcelo", "Epifanio"]


#Ej. 2:
students_backup = students.copy()

#Ej. 3:
# print(len(students))

#Ej. 4:
students_backup.pop(students_backup.index("Milagros"))
# print(students_backup)

# students_backup.remove("Macarena")
# print(students_backup)

#Ej. 5:
# print(students_backup.index("Macarena"))

#Ej. 6:
students_backup.insert((len(students_backup)//2),"Germán")
# print(students_backup)

#Ej. 7:
new_students = ["Felipe", "Tomás", "Facundo"]



students_backup.extend(new_students)
# print(students_backup)

#Ej. 8:
students = students_backup.copy()

#WHILE!!!

#Ej. 1

# count = 0
# while count < len(students):
#     print(students[count].upper())
#     count += 1

#Ej. 2
# lo = "lo"
# count = 0
# while count < len(students):
#     print(students[count] + lo)
#     count += 1

# perro = 3 y gato significa = 2 perro + gato * loro 

#Ej. 3
# count = 0
# resultado = 0
# while count < len(students):
#     if "M" in students[count]: # == 1. students[0], 2. students[1]
#         resultado += 1
#     count += 1
# print(resultado)

# count = 0
# resultado = 0
# while count < len(students):
#     if students[count].startswith("M"): # == 1. students[0], 2. students[1]
#         resultado += 1
#     count += 1
# print(resultado)

# count = 0
# resultado = 0
# while count < len(students):
#     if "M" == students[count][0]: # == 1. students[0], 2. students[1]
#         resultado += 1
#     count += 1
# print(resultado)

#Ej. 4:
# count = 0
# while count < len(students):
#     print(f"El estudiante {students[count]} ocupa la posición {count}")
#     count += 1

#Ej. 5:
approved_students = ["Pedro", "Felipe", "Macarena", "Epifanio"]
# count = 0
# while count < len(students):
#     if students[count] in approved_students:
#         print(f"El estudiante {students[count]} ha aprobado")
#     else:
#         print(f"El estudiante {students[count]} NO ha aprobado")
#     count += 1

#Ej. 6
# user = input("Students search: ")
# count = 0
# while count < len(students):
#     if user in students: 
#         print(f"El estudiante {user} se encuentra en la posición {count}")
#         count = len(students) 
#     count += 1

# user = input("Students search: ")
# count = 0
# while count < len(students):
#     if user == students[count]: 
#         print(f"El estudiante {user} se encuentra en la posición {count}")
#         count = len(students) 
#     count += 1

# students.index(user) # Es igual a lo que tenemos arriba


#Ej. 7:
# user = input("Students search: ")
# count = 0
# while count < len(students):
#     if user == students[count]:
#         students[count] = input("New name: ")
#         count = len(students) + 1

#     if count == len(students) -1:
#         print(f"El estudiante {user} no se encuentra en la lista")
#     count += 1
# print(students)

# numeros = [1,2,3,4]
# pares = []
# count = 0
# while count < len(numeros):
#     if numeros[count] % 2 == 0:
#         pares.append(numeros[count])
#     count += 1
# print(pares)

# count = 0
# new_course = []
# user = input("Estudiante a agregar: ")
# while count < len(students):
#     if user == students[count]:
#         new_course.append(user)
#     count += 1
# print(new_course)

print("---Bienvenido a Students App---")
print("1. Buscar estudiante") # Corresponde al ejercicio 6
print("2. Buscar y actualizar estudiante") # Corresponde al ejercicio 7
print("3. Para salir")
user = input("Elija opción: ")

while user != "3":
    if user == "1":
        user = input("Estudiante a buscar: ")
        position = students.index(user)
    user = input("Y ahora qué?: ") # == 3


youtube_res = {
    "snippets" : {
        "cover": "http://youtube.com/snippets/img.jpg"
    },
    "videos" : {
        "id" : "p5ypbEOZLUU"
    },
    "comments" : [{
        "author_id" : "84415122pd",
        "text": "I love youtube"
    },
    {
        "author_id" : "8441f5199d",
        "text": "I love facebook"
    }
    ]
}

deas = {"data": [{
            "direccion_puerta": "",
            "direccion_via_codigo": "AVDA",
            "direccion_piso": "",
            "municipio_codigo": "079",
            "municipio_nombre": "Madrid",
            "direccion_ubicacion": "MASONI MEDIA SL ",
            "direccion_via_nombre": "de la Virgen del Carmen",
            "direccion_portal_numero": "37",
            "tipo_establecimiento": "Otros",
            "direccion_codigo_postal": "28033",
            "horario_acceso": "10:00?14:00, 16:00?21:00",
            "codigo_dea": "2021-175",
            "tipo_titularidad": "Privada",
            "direccion_coordenada_y": "4480702",
            "direccion_coordenada_x": "444876"
        }]}