from Biblioteca import Biblioteca, Livro, Usuario

def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar livro")
    print("2. Adicionar usuário")
    print("3. Emprestar livro")
    print("4. Listar livros disponíveis")
    print("5. Listar livros emprestados")
    print("6. Listar usuários")
    print("7. Sair")

if __name__ == "__main__":
    biblioteca = Biblioteca()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            ano_publicacao = input("Digite o ano de publicação: ")
            genero = input("Digite o gênero do livro: ")
            livro = Livro(titulo, autor, ano_publicacao, genero)
            biblioteca.adicionar_livro(livro)

        elif opcao == "2":
            nome = input("Digite o nome do usuário: ")
            id = input("Digite o ID do usuário: ")
            usuario = Usuario(nome, id)
            biblioteca.adicionar_usuario(usuario)

        elif opcao == "3":
            titulo_livro = input("Digite o título do livro a ser emprestado: ")
            nome_usuario = input("Digite o nome do usuário: ")
            livro_encontrado = False
            usuario_encontrado = False

            for livro in biblioteca.livros:
                if livro.titulo == titulo_livro:
                    livro_encontrado = True
                    break

            for usuario in biblioteca.usuarios:
                if usuario.nome == nome_usuario:
                    usuario_encontrado = True
                    break

            if livro_encontrado and usuario_encontrado:
                biblioteca.emprestar_livro(livro, usuario)
            else:
                print("Livro ou usuário não encontrado.")

        elif opcao == "4":
            biblioteca.listar_livros_disponiveis()

        elif opcao == "5":
            biblioteca.listar_livros_emprestados()

        elif opcao == "6":
            biblioteca.listar_usuarios()

        elif opcao == "7":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
