import requests as req
import csv
import os
import json
from languages import languages
real_path = os.path.dirname(__file__)

def menu():
    print("COUNTRIES".center(50, "-"))
    print("1. COUNTRY")
    print("2. REGION")
    print("3. COUNTRYS BY LANGUAGE")
    print("4. DOWNLOAD FLAG")
    print("5. HISTORY")
    print("Q. QUIT")

def ls_regions():
    regions = ["Asia", "Africa", "Americas", "Europe", "Oceania"]
    for region in regions:
        print(region)


def get_by_name(country_name):
    res = req.get(f"https://restcountries.eu/rest/v2/name/{country_name}").json()

    if type(res) == list:
        country = res[0]
        result = [country["name"], country["capital"], country["region"] , country["population"], country["area"], country["languages"][0]["name"], country["flag"]]
        return result

    elif type(res) == dict:
        return res["message"]

def write_csv(country):
    if type(country) == list:
        with open(f"{real_path}/record.csv", "a", encoding="utf8", newline="") as file:
            csv_writer = csv.writer(file, delimiter=",")
            csv_writer.writerow(country)

def get_by_region(region_name):
    res = req.get(f"https://restcountries.eu/rest/v2/region/{region_name}").json()
    return res

def write_json(data, json_name):
    if type(data) == list:
        with open(f"{real_path}/{json_name}.json", "w", encoding="utf8") as file: # ESTO ES, PARA ESCRIBIR JSON
            json.dump({"data": data},file, ensure_ascii=False, indent=4) # <--- {"data": data}

def read_json(json_name):
    with open(f"{real_path}/{json_name}.json", "r", encoding="utf8") as file:
        return json.load(file)["data"]

def get_total_region(region):
    result = 0
    for country in region:
        result += country["population"]
    return result

def get_iso(user_language):
    for tupla in languages:
        if tupla[1].lower().find(user_language) == 0:
            return tupla[0]

def get_by_language(iso_language):
    if iso_language:
        res = req.get(f"https://restcountries.eu/rest/v2/lang/{iso_language}").json()
        return f"{len(res)} countries speaks {iso_language}"
    else:
        return f"No matches for your search"

def download_flag(country):
    if type(country) == list:
        res = req.get(country[-1]).content
        name_flag = country[-1][-7:]
        with open(f"{real_path}/img/{name_flag}", "wb") as file:
            file.write(res)
            return "Download succesfully"
    else:
        return "Some problem"

def read_csv(data):
    with open(f"{real_path}/{data}", encoding="utf8") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        result = [row for row in csv_reader]
        return result

def show_record(data):
    rows = read_csv(data)
    for row in rows:
        print(f"name: {row[0]} - population: {row[3]}")

def get_biggest(data):
    return sorted(data,key= lambda country: country["area"]  if country["area"] else 0, reverse=True)[0:11]

def get_by_density(data):
    return sorted(data,key= lambda country: country["population"]/country["area"]  if country["area"] and country["population"] else 0, reverse=True)[0:11]

def top_language(data):
    # result = {}
    # languages = [country["languages"][0]["iso639_1"] for country in data]
    # u_languages = set([country["languages"][0]["iso639_1"] for country in data])
    # for u_language in u_languages:
    #     result[u_language] = languages.count(u_language)
    # return dict(sorted(result.items(), key=lambda tupla: tupla[1], reverse=True))
    result = {}
    for country in data:
        language = country["languages"][0]["name"]
        try:
            result[language] += 1
        except KeyError:
            result[language] = 1
    return dict(sorted(result.items(), key=lambda tupla: tupla[1], reverse=True))
