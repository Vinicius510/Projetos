class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero
        self.disponibilidade = True  # Inicialmente todos os livros estão disponíveis

class Usuario:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print("Livro adicionado com sucesso!")

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

    def emprestar_livro(self, livro, usuario):
        if livro in self.livros and livro.disponibilidade:
            livro.disponibilidade = False
            print(f"O livro '{livro.titulo}' foi emprestado para o usuário {usuario.nome}.")
        else:
            print("Livro não disponível ou não cadastrado na biblioteca.")

    def listar_livros_disponiveis(self):
        print("Livros disponíveis na biblioteca:")
        for livro in self.livros:
            if livro.disponibilidade:
                print(f"- {livro.titulo} ({livro.autor})")

    def listar_livros_emprestados(self):
        print("Livros atualmente emprestados:")
        for livro in self.livros:
            if not livro.disponibilidade:
                print(f"- {livro.titulo} ({livro.autor})")

    def listar_usuarios(self):
        print("Usuários cadastrados na biblioteca:")
        for usuario in self.usuarios:
            print(f"- {usuario.nome} (ID: {usuario.id})")