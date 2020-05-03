from smtpd import MailmanProxy
from unittest import TestCase
from oo.motor import Motor


class CarroTestCase(TestCase):
    def test_velocidade_incial(self):
        motor = Motor()
        self.assertEqual(0,motor.velocidade) #Testing que o valor inicial é 0, comparando entre 0 e motor.velocidade.

    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()    #executo um método que acrescenta a velocidade
        self.assertEqual(1, motor.velocidade) #testing que após acrescentado o valor, a velocidade seja igual a um.

    def test_frear(self):
        motor = Motor()
        motor.acelerar()
        motor.acelerar()
        self.assertEqual(2, motor.velocidade)  # testing que após acrescentado o valor, a velocidade seja igual a 2.
        motor.frear()
        self.assertEqual(0, motor.velocidade)  # testing que após frear a velocidade seja igual a 0.