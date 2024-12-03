# exercicio 03

from functools import reduce
def calcula_saldo(lancamento) -> float:
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamento)
    return reduce(lambda acc, valor: acc + valor, valores, 0)
lancamento = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]
print(calcula_saldo(lancamento))