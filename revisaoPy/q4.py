import random
nomes = []

print("LISTE 10 NOMES")
for i in range(1,11):
    nomes.append(input(f"{i}º nome: "))

print("\nNome sorteado: {}".format(random.choice(nomes)))
