# exercicio 21 parte 1

class Passaro():
    def __init__(self, nome, som):
        self.nome = nome
        self.voo = "Voando..."
        self.som = som

    def voar(self) -> None:
        print(self.nome)
        print(self.voo)

    def emitir_som(self) -> None:
        print(f"{self.nome} emitindo som...")
        print(self.som)


class Pato(Passaro):
    def __init__(self, nome, som):
        super().__init__(nome, som)


class Pardal(Passaro):
    def __init__(self, nome, som):
        super().__init__(nome, som)


pato: Pato = Pato("Pato", "Quack Quack")
pardal: Pardal = Pardal("Pardal", "Piu Piu")

pato.voar()
pato.emitir_som()
pardal.voar()
pardal.emitir_som()