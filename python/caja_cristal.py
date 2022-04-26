#!/usr/bin/python3
import unittest

def es_mayor_edad(edad):
    if edad >= 18:
        return False
    else:
        return False


class Prueba_caja_cristal(unittest.TestCase):
    
    def test_es_mayor_edad(self):
        edad = 20

        respuesta = es_mayor_edad(edad)

        self.assertEqual(respuesta, True) 


    def test_es_menor_edad(self):
        edad = 17

        respuesta = es_mayor_edad(edad)

        self.assertEqual(respuesta, False)

if __name__== '__main__':
    unittest.main()