#função para questão 6
def fatorial(n):
    fat = 1
    for i in range(1,n+1):
        fat *= i

    return fat

'''
num = int(input("Número: "))
if num < 0:
    print("Erro, número inválido!")
else:
    print(f"Fatorial de {num} é {fatorial(num)}")
'''
