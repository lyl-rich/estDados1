'''
tamanho = int(input("Tamanho da lista: "))
lista = [None] * tamanho

def add():
    for i in lista:
        lista[i] = input("Novo item: ")
    print("Lista cheia!")

def pesquisar():
    procurar = input("Procurando: ")
    for i in lista:
        if procurar == i:
            print(f"{procurar} está na lista!")
        else:
            print("Nao encontrado.")

fazer = input("Deseja:\n1 - Criar lista\n2 - Pesquisar")
match fazer:
    case 1:
        add()
    case 2:
        pesquisar()
'''

capacidade = 10
lista = [None] * capacidade
tamanho = 0

def adiciona(numero, tamanho):
    if tamanho < capacidade:
        lista[tamanho] = numero
        tamanho += 1
        print("salvo")
    else:
        return False

def pesquisa(numero):
    pass

for i in range(11):
    num = int(input("Número: "))
    if adiciona(num):
        print("Salvo na lista")
    else:
        print("Lista cheia")