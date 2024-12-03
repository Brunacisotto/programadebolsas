# exercicio 02

def conta_vogais(texto: str) -> int:
    return len(list(filter(lambda char: char.lower() in 'aeiou', texto)))
texto = "programacao funcional"
print(conta_vogais(texto))