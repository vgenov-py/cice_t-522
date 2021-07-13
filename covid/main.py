import requests as req
import json
import os
import time
start = time.perf_counter()
finish = time.perf_counter()
print(finish - start)
cwd = os.path.dirname(__file__)

# res = req.get("https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json").json()

# with open("covid.json", "w", encoding="utf8") as file:
#     json.dump(res, file, ensure_ascii=False, indent=4)

def get_data():
    with open(f"{cwd}/covid.json", encoding="utf8") as file:
        return json.load(file)["data"]


data = get_data()

def get_total(dataset, date):
    result = 0
    mun_by_date = filter(lambda mun: mun["fecha_informe"].split(" ")[0] == date, dataset)
    # sum(map(lambda mun: mun["casos_confirmados_totales"] if mun["fecha_informe"].split(" ")[0] == date and mun["casos_confirmados_totales"] else 0, dataset))
    for mun in mun_by_date:
        try:
            result += mun["casos_confirmados_totales"]
        except KeyError:
            continue
    return result

# print(get_total(data, "2020/02/26"))






















