while True:
    print("_"*25)
    login = input("\nLogin: ").lower()
    senha = input("Senha: ")

    if (login == 'aluno' and senha == '123'):
        print("\nSEJA BEM VINDO!")
        break
    else:
        print("\nLOGIN/SENHA INVÁLIDOS.")
