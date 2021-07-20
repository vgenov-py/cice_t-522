import json
import os
import time

start = time.perf_counter()
print(start)
finish = time.perf_counter()
print(finish)

cwd = os.path.dirname(__file__)

with open(f"{cwd}/data.json", "r", encoding="utf8") as file:
    data = json.load(file)
    # print(data)

a = [1,2,3,4]
b = [num ** 2 if num % 2 == 0 else num ** 3 for num in a ]

for num in a:
    b.append(num ** 2)
# print(b)
# print(finish-start)

