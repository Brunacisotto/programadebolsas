# exercicio 22 parte1

class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = ''

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

#pessoa = Pessoa(0)
#pessoa.nome = 'Fulano De Tal'
#print(pessoa.nome)