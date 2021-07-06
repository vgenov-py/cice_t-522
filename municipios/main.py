import json
import os.path
print(os.path)
# url = "https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/301aed82-339b-4005-ab20-06db41ee7017/download/municipio_comunidad_madrid.json"
# response = req.get(url).json()
# -------------------------------------------- UN DICCIONARIO COMÚN Y CORRIENTE : ----------------------------------------

def get_data():
    with open("./municipalities.json", "r", encoding="utf8") as file:
        data = json.load(file)["data"]
        return data

data = get_data()
# print(data["data"][0]["municipio_nombre"])

def get_by_ine(codigo, dataset):
    result = list(filter(lambda mun: mun["municipio_codigo_ine"] == codigo, dataset))
    if len(result) == 1:
        return result[0]
    else:
        return None
    
result = get_by_ine("2803", data)
# print(result)

def get_area(data):
    return sum([mun["superficie_km2"] for mun in data])

area_total = get_area(data)
# print(area_total)

def biggest_area(data):
    the_biggest = data[0]
    for mun in data:
        if mun["superficie_km2"] > the_biggest["superficie_km2"]:
            the_biggest = mun
    return the_biggest

the_biggest = biggest_area(data)
# print(the_biggest)

def population(data):
    densidades = list(map(lambda mun: mun["densidad_por_km2"],data))
    superficies = list(map(lambda mun: mun["superficie_km2"],data))
    resultado = list(map(lambda den, sup: den* sup,densidades,superficies))
    return sum(resultado)

total = population(data)
print(total)

def top_x(until, data):
    return sorted(data, key = lambda mun: mun["superficie_km2"], reverse=True)[0:until]

print(top_x(179,data))

def benford(data):
    starts_1 = []
    starts_2 = []
    starts_3 = []
    for mun in data:
        if str(mun["densidad_por_km2"]).startswith("1"):
            starts_1.append(mun["densidad_por_km2"])
        elif str(mun["densidad_por_km2"]).startswith("2"):
            starts_2.append(mun["densidad_por_km2"])
        elif str(mun["densidad_por_km2"]).startswith("3"):
            starts_3.append(mun["densidad_por_km2"])
    
    return [starts_1, starts_2, starts_3]

benford_results = benford(data)
# print(len(benford_results[2])/len(data))

def benford_2(data):
    proportion = 1/len(data)
    result = {}
    for num in range(1,10):
        result[str(num)] = 0
    for mun in data:
        result[str(mun["densidad_por_km2"])[0]] += proportion
    return result

ben_2 = benford_2(data)
# print(ben_2)
