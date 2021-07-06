book = {
    "id": "cf_1",
    "title": "El hombre bicentenario",
    "author": "Isaac Asimov",
    "genre": "Ciencia ficción"
}

book_items = list(book.items())

# count = 0
# while count < len(book_values):
#     print(book_values[count])
#     count += 1

for tupla in book_items:
    print(tupla[1])

# nums = [1,2,3,4]
# loquequieras = 0
# while  loquequieras < len(nums):
#     print(nums[loquequieras])
#     loquequieras += 1