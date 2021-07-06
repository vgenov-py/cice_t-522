import requests as req
import funcs
import os
# res = req.get("https://restcountries.eu/rest/v2/all").json()
# print(res)

user = 0
while user != "Q":
    funcs.menu()
    user = input("Select: ")

    if user == "1": # BY COUNTRY:
        country = input("Country: ")
        country = funcs.get_by_name(country)
        print(country)
        funcs.write_csv(country)
    
    elif user == "2":
        funcs.ls_regions()
        region = input("Region: ")

        try:
            population = funcs.get_total_region(funcs.read_json(region))
            print(population)

        except FileNotFoundError:
            result = funcs.get_by_region(region)
            funcs.write_json(result,region)
            population = funcs.get_total_region(funcs.read_json(region))
            print(population)

    elif user == "3":
        language = input("Search by language: ")
        print(funcs.get_iso(language))
        iso_language = funcs.get_iso(language)
        print(funcs.get_by_language(iso_language))

    elif user == "4":
        country = input("Country: ")
        country = funcs.get_by_name(country)
        msg = funcs.download_flag(country)
        print(msg)
    
    elif user == "5":
        funcs.show_record("record.csv")
        user = input("Continue...")

    elif user == "6":
        result = funcs.get_by_density(req.get(f"https://restcountries.eu/rest/v2/all").json())
        print(result)
        
    elif user == "7":
        result = funcs.top_language(req.get(f"https://restcountries.eu/rest/v2/all").json())
        print(result)

    elif user == "q" or user == "Q":
        user = "Q"

