import requests as req
import json
from .models import DEA


def get_data():
    return json
def create_one_dea(parametros):
    DEA.objects.create(parametros)
def bulk_insertion(deas):
    for dea in deas:
        # extrae datos
        create_one_dea("datosextraidos")