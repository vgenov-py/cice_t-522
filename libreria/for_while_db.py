bookshop = [{
    "id": "cf_1",
    "title": "El hombre bicentenario",
    "author": "Isaac Asimov",
    "genre": "Ciencia ficción"
},
{
    "id": "ne_1",
    "title": "Lobo de mar",
    "author": "Jack London",
    "genre": "Narrativa extranjera"
},
{
    "id": "np_1",
    "title": "El legado de los huesos",
    "author": "Dolores Redondo",
    "genre": "Narrativa policíaca"
},
{
    "id": "dc_1",
    "title": "El error de Descartes",
    "author": "Antonio Damasio",
    "genre": "Divulgación científica"
},
{
    "id": "dc_2",
    "title": "El ingenio de los pájaros",
    "author": "Jennifer Ackerman",
    "genre": "Divulgación científica"
},
{
    "id": "ne_1",
    "title": "El corazón de las tinieblas",
    "author": "Joseph Conrad",
    "genre": "Narrativa extranjera"
},
{
    "id": "dc_5",
    "title": "Metro 2033",
    "author": "Dmitri Glujovski",
    "genre": "Divulgación científica"
},
{
    "id": "dc_5",
    "title": "Sidharta",
    "author": "Hermann Hesse",
    "genre": "Narrativa extranjera"
},
{
    "id": "el_1",
    "title": "Andres Trapiello",
    "author": "Las armas y las letras",
    "genre": "Narrativa extranjera"
},
{
    "id": "aa_1",
    "title": "El poder del ahora",
    "author": "Ekhart Tolle",
    "genre": "Narrativa extranjera"
},
]




# id_book = "dc_1"

# for book in bookshop: 
#     if book["id"] == id_book:
#         print(book)


user = "0"
while user != "q":
    genres = ["Narrativa extranjera", "Divulgación científica", "Narrativa policíaca", "Ciencia ficción", "Autoayuda"]
    
    print("Bookshop".center(50, "-"))
    print("1. ID")
    print("2. Author")
    print("3. Title")
    print("4. Genre")
    print("5. New book")
    print("6. Modify book")
    print("7. Delete book")    
    print("Q. Exit")
    user = input("Choose: ")

    if user == "1":
        book_id = input("ID: ") # dc_1

        for book in bookshop: 
            if book["id"] == book_id:
        #         print("".center(50,"-"))
        #         print(f"ID: {book['id']}")
        #         print(f"Author: {book['author']}")
        #         print(f"Title: {book['title']}")
        #         print(f'Genre: {book["genre"]}')
        #         print("".center(50,"-"))

                for k,v in book.items():
                    print(f"{k}: {v}")
                
    elif user == "2":
        user_author = input("Author: ").lower()
        count = 0
        for book in bookshop:
            author = book["author"].lower()
            if author.find(user_author) > -1:
                print(book)
                count += 1
        if count == 0:
            print(f"Ninguno de nuestros libros cumplen el siguiente : {user_author} criterio de búsqueda...\n La próxima vez, busque bien :)")

    elif user == "3": # GET BY TITLE
        user_title = input("Title: ").lower()
        count = 0
        for book in bookshop:
            title = book["title"].lower()
            if title.find(user_title) > -1:
                print("".center(50,"-"))
                for k, v in book.items():
                    print(f"{k}: {v}")
                count += 1
        if count == 0:
            print(f"Ninguno de nuestros libros cumplen el siguiente : {user_title} criterio de búsqueda...\n La próxima vez, busque bien :)")

    elif user == "4": # GET BY GENRE
        
        for i, genre in enumerate(genres): 
            print(f"{i + 1 }. {genre}")
        user_index = int(input("Choose: "))
        user_genre = genres[user_index - 1]
        result = []
        for book in bookshop:
            if book["genre"] == user_genre:
                result.append(book)

        count = 0

        print(f"{user_genre}".center(50,"-"))
        for book in result:
            print(f"book {count + 1}".center(50,"-"))
            print(f"{book['title']}"  + f"{book['id']}".center(50))
            print(f"{book['author']}")
            count += 1
        if count == 0:
            print(f"No se han encontrado libros")

        elif count == 1:
            print(f"Se ha encontrado {count} libro")
        else:
            print(f"Se han encontrado {count} libros")
        print("".center(50, "-"))
        user = input("Continuar... ")

    elif user == "5":  # CREATE BOOK
        new_book = {}
        keys = list(bookshop[0].keys()) # LAS CLAVES DEL DICCIONARIO == LIST(BOOKSHOP[0])
        book_id = "nb_" + str(len(bookshop))
        new_book["id"] = book_id
        for key in keys[1:3]:
            new_book[key] = input(f"{key}: ")
        for i, genre in enumerate(genres):
            print(f"{i + 1}. {genre}")
        user_genre = int(input("Choose genre: "))
        user_genre = genres[user_genre - 1]
        new_book[keys[-1]] = user_genre 
        bookshop.append(new_book)

    elif user == "6": # UPDATE BOOK
        count = 0
        book_id = input("ID: ") # dc_1
        for book in bookshop: 
            if book["id"] == book_id:
                count += 1
                if count > 1:
                    print(f"ALERT! You have {count} books designed with the same id!")
                    user = input("Do you want to change it? (Y/N): ")
                    if user.lower() == "y":
                        print(book)
                        book_id = input("New id: ")
                        book["id"] = book_id
                else:
                    for i, tupla in enumerate(book.items()):
                        print(f"{i + 1}. {tupla[0]}: {tupla[1]}")
                    user = int(input("Choose: ")) - 1
                    keys = list(book.keys())
                    key_to_update = keys[user] # type(keys) == list, user es una posición --> key_to_update = alguna de las claves
                    book[key_to_update] = input(f"{key_to_update}: ")
                    #una pequeña modificación


    

    elif user == "7": # DELETE BOOK
        book_id = input("ID: ")
        for book in bookshop:
            if book["id"] == book_id:
                for k, v in book.items(): # IMPRIMIR LAS SPECS DEL LIBRO
                    print(f"{k}: {v}")
                user = input(f"The book {book['title']} will be erase from the db. Are you sure (Y/N)?: ")
                if user.lower() == "y":
                    bookshop.remove(book)
                    print("The book was erased")
                                

    elif user.lower() == "q":
        user = user.lower()
        print("Bye!")
    else:
        user = "1"
        

