from lista import Lista

print("~~~~~CRIAÇÃO~~~~~")
n = int(input("Capacidade da sua lista: "))
lista1 = Lista(n)

print(f"\nCapacidade: {lista1.capacidade}")
print(f"Tamanho: {lista1.tamanho}")
print(lista1.array)


print("\n~~~ADICIONAR~~~")
for i in range(n):
    if (lista1.adicionar(int(input(f'Adicionar {i+1}º elemento: ')))):
        print("Número adicionado!\n")
    else:
        print("Erro, número não adicionado.")

print(lista1.array)


print("\n~~~PESQUISAR~~~")
pesq = int(input('número: '))
print(f"Tem {pesq} na lista?\n-> {lista1.pesquisar(pesq)}")


print("\n~~~OBTER~~~")
obt = int(input('número da posição: '))
print(f"{obt}º elemento da lista: {lista1.obter(obt-1)}")


print("\n~~~INSERIR~~~")
print(lista1.array)
pos = int(input('posição de inserção: '))
num = int(input('número: '))

if (lista1.inserir(pos,num)):
    print("Número inserido!\n")
else:
    print("Erro, número não adicionado.")

print(lista1.array)


print("\n~~~REMOVER~~~")
rem = int(input('posição: '))
lista1.remover(rem)
print(lista1.array)