"""
Crie um sistema completo de gerenciamento de biblioteca que:

Tenha classes para Livro, Usuario e Biblioteca
Permita cadastrar livros e usuários
Implemente empréstimo e devolução
Salve todos os dados em arquivos JSON
Tenha funcionalidade para:
Gerar relatório de livros mais emprestados (CSV)
Buscar informações de livros em uma API pública (ex: Open Library)
Importar lista de livros de um CSV
Use tratamento de exceções adequado
Implemente log de operações em arquivo de texto
"""
class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Nome: {self.nome}"




class Livro:
    def __init__(self, nome, autor, ano_lancado, disponibilidade):
        self.nome = nome
        self.autor = autor
        self.ano_lancado = ano_lancado

    def __str__(self):
        return f"Nome:{self.nome}"



class Biblioteca:
    def __init__(self, nome, filial, localidade):
        self.nome = nome
        self.filial = filial
        self.localidade = localidade

    def __str__(self):
        return f"Nome: {self.nome}, filial: {self.filial}, localidade: {self.localidade}"
    


usuarios = []
livros = []
bibliotecas = []




usuario1 = Usuario("Nahomi")

usuario2 = Usuario("Romario")
usuario3 = Usuario("Gabriel")

livro1 = Livro("Hábitos bons", "Freud", 2000)
livro2 = Livro("Artes Lendárias", "Da vinci", 1500)
livro3 = Livro("Matemática Fácil", "Albert Einstein", 1900)

bbt1 = Biblioteca("Biblioteca Lapa", "filial 1", "Rio de janeiro")
bbt2 = Biblioteca("Biblioteca Ilha", "filial 6", "Rio de janeiro")
bbt3 = Biblioteca("Biblioteca Flamengo", "filial 3", "Rio de janeiro")

