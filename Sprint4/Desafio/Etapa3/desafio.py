##Etapa 3 desafio Sprint 4

import hashlib

while True:
    mensagem = input("Olá digite aqui sua mensagem (ou 'SAIR' para encerrar): ")

    hash = hashlib.sha1(mensagem.encode()).hexdigest()

    if mensagem.lower() == "sair":
       break

    print(f"O hash SHA-1 da sua mensagem é: {hash}")



