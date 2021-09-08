
# def chao():
#         print("chao")

# def hola():
#     print("hola")
#     chao()

# # hola()

# def container():
#     print("I'm outside")
#     # meter el return de la función que contiene en la lista de atributos del objeto creado...
#     def n():
#         print("n")

#     return n

# a = container()
# print(a())


# def outer(a_func):
#     def inside(*args):
#         b_list = [int(digit) for digit in str(args[1])]
#         b_com = ""
#         for digit in b_list:
#             count = 0
#             for value in range(digit, 9):
#                 count += 1
#             b_com += str(count)
#         result = a_func(args[0], int(b_com))
#         result = str(result)[1:]
#         result = int(result) + 1
#         return result
#     return inside

# @outer
# def add(a,b):
#     return a + b

# print(add(121, 120))


def write_in_log(external_func):
    def inner(*args):    
        with open("func_recorder.log", "a") as file:
            file.write(f"{external_func.__name__} func have been used with at least this arguments: {args}\n")
        return external_func(*args)
    return inner

@write_in_log
def add(a, b):
    return a + b
add(1,2)
# a = write_in_log(add)
# print(a(2,3))
# a(2,3)
# a(2,3)
# a(2,3)

# print(a(2,3))















# def log_a(a_func):
#     def log_writer(*args):
#         a_func(args[0], args[1])
#         with open("func_recorder.log", "a") as file:
#             file.write(f"{a_func.__name__} func have been used with the followings parameters: {args[0]} & {args[1]}\n")
#     return log_writer

# @log_a
# def add(a,b):
#     return a + b

# add(1,2)
    
