"""
    O motor terá responsabilidade de controlar a velocidade.
    Ele oferece os seguintes atributos:
    1) Atributo de dado velocidade
    2) Método acelerar, que deverá incrementar a velocidade de uma unidade
    3) Método frear que deverá decrementar a velocidade em duas unidades
"""
class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade >= 2 :
            self.velocidade -= 2
        else:
            self.velocidade = 0

# if __name__ == '__main__':
#     motor = Motor()
#     print('Velocidad inicial del Motor',motor.velocidade)
#     motor.acelerar()
#     print('Velocidad del Motor, dsps de acelerar',motor.velocidade)
#     motor.acelerar()
#     print('Velocidad del Motor, dsps de acelerar', motor.velocidade)
#     motor.acelerar()
#     print('Velocidad del Motor, dsps de acelerar',motor.velocidade)
#     motor.frear()
#     print('Velocidad del Motor después de frenar',motor.velocidade)
#     motor.frear()
#     print('Velocidad del Motor después de frenar',motor.velocidade)
#     motor.frear()
#     print('Velocidad del Motor después de frenar', motor.velocidade)