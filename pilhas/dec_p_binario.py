from pilhas.pilha import Pilha


def decimal_para_binario(num):
    pilha = Pilha()

    while num > 0:
        resto = num % 2
        pilha.empilhar(resto)
        num = num // 2

    binario = ""

    while not pilha.vazia():
        binario += str(pilha.desempilhar())

    return binario


print(decimal_para_binario(13)) #1101