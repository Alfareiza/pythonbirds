class Pessoa:
    ojos = 2
    def __init__(self,*sons, nome=None, age=None):
        self.age = age
        self.nome = nome
        self.sons = list(sons)

    def cumprimentar(self):
        return f'Hola {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_atributos_de_clase(cls):
        return f'{cls} - ojos {cls.ojos}'

class Mulher(Pessoa):
    pass

class Mutante(Pessoa):
    ojos = 3

if __name__ == '__main__':
    Gilma = Mutante(nome='Gilma',age=61) #Aqui estoy creando/construyendo un objeto Gilma con la plantilla de la clase Pessoa, por ende se ejecuta el método init
    Arturo = Mulher(nome ='Arturo')
    Ida = Pessoa(Gilma, Arturo,nome='Ida',
                   age=88)  # Aqui estoy creando/construyendo un objeto p con la plantilla de la clase Pessoa, por ende se ejecuta el método init\
    print(Gilma.cumprimentar())
    print(Gilma.nome) #Aqui acceso a un atributo del objeto P
    print(Gilma.age) # Imprimo el atributo age del objeto p
    for sons in Ida.sons:
        print(sons.nome)
    Ida.sobrenome = 'Blanco'
    del Ida.sons
    print (Ida.__dict__)
    print (Gilma.__dict__)
    print(Gilma.ojos)
    print(Ida.ojos)
    print(Pessoa.ojos)
    print(Pessoa.metodo_estatico())
    print(Ida.metodo_estatico())
    print(Pessoa.nome_atributos_de_clase())
    print(Gilma.nome_atributos_de_clase())
    pessoa = Pessoa('Anónimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Mulher))
    print(isinstance(Gilma, Pessoa))
    print(isinstance(Gilma, Mulher))
    print(Gilma.ojos)

