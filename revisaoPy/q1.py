n1 = float(input("Nota1: "))
n2 = float(input("Nota2: "))
n3 = float(input("Nota3: "))

m = (n1+n2+n3)/3
print(f"\nMédia: {m:.2f}")

if (m >= 7):
    print("Aprovado!")
elif (m >= 4):
    print("Prova final.")
else:
    print("Reprovado!")
    