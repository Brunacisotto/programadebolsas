#exercicio 11 parte2

import json
person = open("person.json", "r")
leitura = json.load(person)
person.close()
print(leitura)