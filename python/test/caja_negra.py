#!/usr/bin/python3
import unittest

def suma(num_1, num_2):
    return num_1 + num_2


class Caja_negra_test(unittest.TestCase):
    #########################################
    # test
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        respuesta = suma(num_1, num_2)

        self.assertEquals(respuesta, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        respuesta = suma(num_1, num_2)

        self.assertEquals(respuesta, -17)
    ##########################################

if __name__=='__main__':
    unittest.main()
