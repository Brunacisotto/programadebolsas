# exercicio 23 parte 1

class Calculo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def soma(self) -> int:
        return self.x + self.y

    def subtracao(self) -> int:
        return self.x - self.y

calculo = Calculo(4, 5)

print(f"Somando: {calculo.x}+{calculo.y} = {calculo.soma()}")
print(f"Subtraindo: {calculo.x}-{calculo.y} = {calculo.subtracao()}")