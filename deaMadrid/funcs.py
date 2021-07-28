import json
import utm

def get_data(dataset):
	with open(dataset, encoding="utf8") as file:
		return json.load(file)
	
def qty_M30(dataset, zc_list):
    return len([dea for dea in dataset if dea["direccion_codigo_postal"] in zc_list])

def get_private(dataset):
    return len([dea for dea in dataset if dea["tipo_titularidad"] == "Privada"])

def menu():
    print("1. Users")
    print("2. DEA finder")
    print("Q. Quit")

def menu_dea():
    print("1. DEA by code")
    print("2. DEA by position")
    print("3. DEA update")

def menu_by_position():
    x = int(input("Lat:"))
    y = int(input("Long:"))
    return (x,y)


class DEA:
    def __init__(self, x, y):
        if type(x) != int:
            raise ValueError("X it only can be an integer")
        if type(y) != int:
            raise ValueError("Y it only can be an integer")
        self.x = x
        self.y = y
    
    def distance(self, user_x, user_y):
        c_1 = (user_x - self.x) ** 2
        c_2 = (user_y - self.y) ** 2
        return ((c_1 + c_2)**0.5)

def get_nearest(dataset, user_x, user_y):
    result = {}
    dea_x = "direccion_coordenada_x"
    dea_y = "direccion_coordenada_y"

    for dea in dataset:
        dea_object = DEA(int(dea[dea_x]), int(dea[dea_y]))
        distance = dea_object.distance(user_x, user_y)
        result[distance] = dea
    # a comment
    return sorted(result.items(), key=lambda dea: dea[0])[0]