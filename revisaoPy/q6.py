from q5 import fatorial

while True:
    num = int(input("Número inteiro positivo: "))

    if num < 0:
        #print("Erro, número negativo!")
        break
    else:
        print(f"Fatorial de {num} é {fatorial(num)}")

print("Fim.")
