

import data
import sender_stand_request as req



def test_valido_num_caracteres_1_name_respuesta_201():
    # hacer peticion a api para kit nuevo
    respuesta = req.crear_kit(data.kit['prueba_1'])
    #assert para evaluar respuesta esperada
    assert respuesta.status_code == 201


def test_valido_num_caracteres_511_name_respuesta_201():
    # hacer peticion a api para kit nuevo
    respuesta = req.crear_kit(data.kit['prueba_2'])
    #assert para evaluar respuesta esperada
    assert respuesta.status_code == 201


def test_valido_num_caracteres_vacio_name_respuesta_400():
    # hacer peticion a api para kit nuevo
    respuesta = req.crear_kit(data.kit['prueba_3'])
    #assert para evaluar respuesta esperada
    assert respuesta.status_code == 400


def test_valido_num_caracteres_512name_respuesta_400():
    # hacer peticion a api para kit nuevo
    respuesta = req.crear_kit(data.kit['prueba_4'])
    #assert para evaluar respuesta esperada
    assert respuesta.status_code == 400

def test_valido_num_caracteres_especiales_name_respuesta_201():
    # hacer peticion a api para kit nuevo
    respuesta = req.crear_kit(data.kit['prueba_5'])
    #assert para evaluar respuesta esperada
    assert respuesta.status_code == 201

def test_valido_num_caracteres_per_espacios_name_respuesta_201():
    # hacer peticion a api para kit nuevo
    respuesta = req.crear_kit(data.kit['prueba_6'])
    #assert para evaluar respuesta esperada
    assert respuesta.status_code == 201


def test_valido_num_caracteres_permiten_nmeros_name_respuesta_201():
    # hacer peticion a api para kit nuevo
    respuesta = req.crear_kit(data.kit['prueba_7'])
    #assert para evaluar respuesta esperada
    assert respuesta.status_code == 201

def test_valido_num_caracteres_sin_parametro_name_respuesta_400():
    # hacer peticion a api para kit nuevo
    respuesta = req.crear_kit(data.kit['prueba_8'])
    #assert para evaluar respuesta esperada
    assert respuesta.status_code == 400

def test_valido_num_caracteres_numero_name_respuesta_400():
    # hacer peticion a api para kit nuevo
    respuesta = req.crear_kit(data.kit['prueba_9'])
    #assert para evaluar respuesta esperada
    assert respuesta.status_code == 400








