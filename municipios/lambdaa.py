import random

# def_normal = add(3,5)
# print(def_normal)

# lambda_func = lambda a,b: a + b

# resultado_lambda = lambda_func(3,5)
# print(resultado_lambda)

# def add(a,b):
#     return a + b

# calculator = {"add": add,"substract": lambda a,b: a - b, "times": "multiplique"}

# print(calculator["substract"](3,4))


# def squares(dataset):
#     result = []
#     for num in dataset:
#         result.append(num**2)
#     return result



# a = [10,123,3,2,53,345,2,1,625,3,1,4,1,50,1,65,60]


# map_squares_result = list(map(lambda num: num ** 2, a))
# map_cubes_result = list(map(lambda num: num ** 3, a))

# impares = list(filter(lambda num: num % 2 != 0,a))

x = [10,12,20,30,41]
y = [1,3,6,7,9]

def merge_x_y():
    result = []
    for i, num in enumerate(x):
        result.append(num * y[i])
    return result

resultado = merge_x_y()
print(resultado)

merge_x_y_map = list(map(lambda num_x, num_y: num_x * num_y ,x, y))
print(merge_x_y_map)



# print(impares)


