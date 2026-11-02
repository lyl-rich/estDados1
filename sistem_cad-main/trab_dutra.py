contas = {
    "admin": "12345"
}
while True:
    print("-------ÁREA DE LOGIN---------")
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    if usuario in contas and contas[usuario] == senha:
        print("\nLogin realizado com sucesso!")
        while True:
            print("--------MENU PRINCIPAL--------")
            print("1.  Cadastrar usuário")
            print("2.  Listar usuários")
            print("3.  Remover usuário")
            print("4.  Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                novo_usuario = input("Digite o novo usuário: ")
                if novo_usuario == "":
                    print("O usuário não pode ficar vazio.")
                elif novo_usuario in contas:
                    print("Esse usuário já está cadastrado.")
                else:
                    nova_senha = input("Digite a senha: ")
                    contas[novo_usuario] = nova_senha
                    print("Usuário cadastrado com sucesso!")
            elif opcao == "2":
                print("------USUÁRIOS CADASTRADOS-------")
                for usuario in contas:
                    print(usuario)
            elif opcao == "3":
                usuario_remover = input("Digite o usuário que deseja remover: ")
                if usuario_remover == "admin":
                    print("O usuário admin não pode ser removido.")
                elif usuario_remover in contas:
                    del contas[usuario_remover]
                    print("Usuário removido com sucesso!")
                else:
                    print("Usuário não encontrado.")
            elif opcao == "4":
                print("Sistema encerrado.")
                break
            else:
                print("Opção inválida.")
        break
    else:
        print("Usuário ou senha incorretos.")