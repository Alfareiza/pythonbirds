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
if __name__ == '__main__':
    Gilma = Pessoa(nome='Gilma',age=61) #Aqui estoy creando/construyendo un objeto Gilma con la plantilla de la clase Pessoa, por ende se ejecuta el método init
    Arturo = Pessoa(nome ='Arturo')
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



