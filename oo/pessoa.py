class Pessoa:
    def __init__(self, nome=None, age=None):
        self.age = age
        self.nome = nome

    def cumprimentar(self):
        return f'Hola {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Prueba Prueba',44) #Aqui estoy creando/construyendo un objeto p con la plantilla de la clase Pessoa, por ende se ejecuta el método init
    print(p.cumprimentar())

    print(p.nome) #Aqui acceso a un atributo del objeto P
    p.nome = 'Alfonso' #Aqui modifico el atributo del objeto P
    print(p.nome)  # Imprimo la modificación anterior

    print(p.age) # Imprimo el atributo age del objeto p