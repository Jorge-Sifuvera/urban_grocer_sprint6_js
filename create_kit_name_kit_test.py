


import data
import sender_stand_request as req

def positive_assert(kit_body):

    kit_response = req.crear_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def negative_assert(kit_body):

    kit_response = req.crear_kit(kit_body)

    assert kit_response.status_code == 400

def test_valido_num_caracteres_1_name_respuesta_201():
    # hacer peticion a api para kit nuevo
    positive_assert(data.kit['prueba_1'])

def test_valido_num_caracteres_511_name_respuesta_201():
    # hacer peticion a api para kit nuevo
    positive_assert(data.kit['prueba_2'])

def test_valido_num_caracteres_vacio_name_respuesta_400():
    # hacer peticion a api para kit nuevo
   negative_assert(data.kit['prueba_3'])

def test_valido_num_caracteres_512name_respuesta_400():
    # hacer peticion a api para kit nuevo
    negative_assert(data.kit['prueba_4'])


def test_valido_num_caracteres_especiales_name_respuesta_201():
    # hacer peticion a api para kit nuevo
    positive_assert(data.kit['prueba_5'])


def test_valido_num_caracteres_per_espacios_name_respuesta_201():
    # hacer peticion a api para kit nuevo
    positive_assert(data.kit['prueba_6'])



def test_valido_num_caracteres_permiten_nmeros_name_respuesta_201():
    # hacer peticion a api para kit nuevo
    positive_assert(data.kit['prueba_7'])


def test_valido_num_caracteres_sin_parametro_name_respuesta_400():
    # hacer peticion a api para kit nuevo
    negative_assert(data.kit['prueba_8'])


def test_valido_num_caracteres_numero_name_respuesta_400():
    # hacer peticion a api para kit nuevo
    negative_assert(data.kit['prueba_9'])









