try:
    read_json = "Africa" # FileNotFoundError
    print(read_jsons) # NameError
    
except FileNotFoundError:
    print("FileNotFoundError")

except NameError:
    print("NameError")
