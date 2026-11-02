from lista import Lista

lista1 = Lista(5)
print(f"Capacidade: {lista1.capacidade}")
print(f"Tamanho: {lista1.tamanho}")
print(lista1.array)


print("\n~~~ADICIONAR~~~")
lista1.adicionar(2)
lista1.adicionar(4)
lista1.adicionar(9)

if (lista1.adicionar(14)):
    print(f"Número adicionado!")
else:
    print(f"Erro, número não adicionado")

print("Lista: ")
print(lista1.array)


print("\n~~~PESQUISAR~~~")
print(f"Tem número 4 na lista? -> {lista1.pesquisar(4)}")


print("\n~~~OBTER~~~")
print(f"Número da posição 2 da lista: {lista1.obter(2)}")


print("\n~~~INSERIR~~~")
print(lista1.array)
lista1.inserir(1,66)
print(lista1.array)


print("\n~~~REMOVER~~~")
lista1.remover(2)
print(lista1.array)