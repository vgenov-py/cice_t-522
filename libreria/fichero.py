import os
real_path = os.path.dirname(__file__)
print(real_path)
# real_path = os.path.dirname()
# # . == D:\t-522
with open(f"{real_path}/img/img.txt", "w") as file:
    file.write("HOLA")
