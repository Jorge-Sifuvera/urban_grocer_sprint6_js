
import requests
import configuration
import data

def obtener_token():
    #1 hacer petición: método, endpoint y body
    respuesta = requests.post(configuration.URL_SERVICE + configuration.USER_ENDPOINT,
                              json=data.user)
    #2 Obtener el json dado que viene token de autentificación
    resp_json = respuesta.json()
    #3 impresion  token para vereficar la petición
    return resp_json['authToken']

auth_token = obtener_token()
data.authorization["Authorization"] = f'Bearer {auth_token}'


def crear_kit(name):
    # 1 hacer petición: método, endpoint y headers
    respuesta = requests.post(configuration.URL_SERVICE + configuration.KIT_ENDPOINT,
                              json=name,
                              headers=data.authorization)
    # 2 impresion petición
    return respuesta






