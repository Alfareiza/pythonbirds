"""
    A direção terá a responsibilidade de controlar a direção. Ela oferecerá os seguintes atributos
    1) Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
    2) Método girar a direita
    3) Método girar a esquerda
        N
    O       L
        S
"""
NORTE = 'Norte'
LESTE = 'Leste'
OESTE = 'Oeste'
SUL = 'Sul'
class Direcao:
    rotacao_a_direita_dict = {NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE}
    rotacao_a_esquerda_dict = {NORTE:OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}
    def __init__(self):
        self.valor = 'Norte'

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dict[self.valor] #aqui el valor que llega, lo busca en el dict (key) y retorna el value

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dict[self.valor]

    # Las dos funciones debajo las hice yo en modo amateur
    # def girar_a_direita(self):
    #     if self.valor == 'Norte':
    #         self.valor = 'Leste'
    #     elif self.valor == 'Leste':
    #         self.valor = 'Sul'
    #     elif self.valor == 'Sul':
    #         self.valor ='Oeste'
    #     elif self.valor =='Oeste':
    #         self.valor = 'Norte'
    #
    # def girar_a_esquerda(self):
    #     if self.valor == 'Norte':
    #         self.valor = 'Oeste'
    #     elif self.valor == 'Oeste':
    #         self.valor = 'Sul'
    #     elif self.valor == 'Sul':
    #         self.valor = 'Leste'
    #     elif self.valor == 'Leste':
    #         self.valor = 'Norte'

#
# if __name__ == '__main__':
#     direcao = Direcao()
#     print('Direcao Inical é',direcao.valor)
#     direcao.girar_a_direita()
#     print('Luego de Girar a Derecha',direcao.valor)
#     direcao.girar_a_direita()
#     print('Luego de Girar a Derecha',direcao.valor)
#     direcao.girar_a_direita()
#     print('Luego de Girar a Derecha',direcao.valor)
#     direcao.girar_a_direita()
#     print('Luego de Girar a Derecha',direcao.valor)
#     direcao.girar_a_esquerda()
#     print('Luego de Girar a Derecha',direcao.valor)
#     direcao.girar_a_esquerda()
#     print('Luego de Girar a Derecha',direcao.valor)
#     direcao.girar_a_esquerda()
#     print('Luego de Girar a Derecha',direcao.valor)
#     direcao.girar_a_esquerda()
#     print('Luego de Girar a Derecha',direcao.valor)