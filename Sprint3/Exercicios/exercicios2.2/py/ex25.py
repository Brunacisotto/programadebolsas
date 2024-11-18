# exercicio 25 parte 1

import re
class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = 'azul'

    def imprimir_especificacao(self):
        print(f'O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima}, capacidade para {self.capacidade} passageiros e é de cor {self.cor}.')

def getModelo(text):
    return text.split('modelo ')[1]

def getVelocidadeMaxima(text):
    return text.split(' valocidade máxima ')[1]

def getPassageiros(text):
    return re.sub('[^0-9]','', text)

entrada1 = "modelo BOIENG458: valocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul"
entrada2 = "modelo Embraer Praetor 600: valocidade máxima 863 km/h: capacidade para 14 passageiros: Cor Azul"
entrada3 = "modelo Antonov An-2: valocidade máxima 258 km/h: capacidade para 12 passageiros: Cor Azul"

lista_entrada1 = entrada1.split(':')
lista_entrada2 = entrada2.split(':')
lista_entrada3 = entrada3.split(':')

aviao1 = Aviao(getModelo(lista_entrada1[0]), getVelocidadeMaxima(lista_entrada1[1]), getPassageiros(lista_entrada1[2]))
aviao2 = Aviao(getModelo(lista_entrada2[0]), getVelocidadeMaxima(lista_entrada2[1]), getPassageiros(lista_entrada2[2]))
aviao3 = Aviao(getModelo(lista_entrada3[0]), getVelocidadeMaxima(lista_entrada3[1]), getPassageiros(lista_entrada3[2]))

lista = [aviao1, aviao2, aviao3]

for aviao in lista:
    aviao.imprimir_especificacao()