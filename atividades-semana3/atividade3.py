import json
import os
from datetime import datetime 
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

    def __repr__(self):
        return f"Nome do usuário: {self.nome}"


class Livro:
    def __init__(self, nome, autor, ano_lancado):
        self.nome = nome
        self.autor = autor
        self.ano_lancado = ano_lancado

    def __str__(self):
        return f"Nome do livro: {self.nome} | Autor: {self.autor} | Ano Lançado: {self.ano_lancado}"

    def __repr__(self):
        return self.__str__()


class Biblioteca:
    def __init__(self, nome, filial, localidade):
        self.nome = nome
        self.filial = filial
        self.localidade = localidade

    def __str__(self):
        return f"Nome da biblioteca: {self.nome} | filial: {self.filial} | localidade: {self.localidade}"
    
    def __repr__(self):
        return self.__str__()
    

usuarios = []
livros = []
bibliotecas = []
emprestimos = []
path = "atividades-semana3/log_biblioteca.txt"

#======= FUNÇÕES =======#
def inicializando_sistema_add():
    usuarios_data = ["Lorena", "Marina", "Gabriel"]

    livros_data = [
        ("Hábitos bons", "Freud", 2000),
        ("Artes Lendárias", "Da vinci", 1500),
        ("Matemática Fácil", "Albert Einstein", 1900),
    ]

    bibliotecas_data = [
        ("Biblioteca Lapa", "filial 1", "Rio de janeiro"),
        ("Biblioteca Ilha", "filial 6", "Rio de janeiro"),
        ("Biblioteca Flamengo", "filial 3", "Rio de janeiro"),
    ]

    usuarios.extend(Usuario(nome) for nome in usuarios_data)
    livros.extend(Livro(titulo, autor, ano) for titulo, autor, ano in livros_data)
    bibliotecas.extend(Biblioteca(nome, filial, cidade) for nome, filial, cidade in bibliotecas_data)



def registrar_log(mensagem):
    # Registra mensagem em log_biblioteca.txt com timestamp
    data_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # "a" significa modo append (adicionar no final do arquivo).

    with open(path, "a", encoding="utf-8") as f:
        f.write(f"[{data_hora}] {mensagem}\n")



def limpar_tela():
    # 'cls' para Windows / 'clear' para Linux e macOS
    os.system('cls' if os.name == 'nt' else 'clear')



def msg_voltar():
    msg = input(" < Clique ENTER para voltar >")
    limpar_tela()



def visualizar_lista_usuarios():
    print("============== USUÁRIOS CADASTRADOS ==================\n") 

    if not usuarios:
        print("\n\n SEM USUÁRIOS CADASTRADOS")

    else:
        for user in usuarios:
            print("-", user, "\n")
    
    msg_voltar()



def visualizar_lista_livros():
    print("=================== LIVROS CADASTRADOS ===============\n")

    if not livros:
        print("\n\nSEM LIVROS CADASTRADOS NO SISTEMA")

    else:   
        for livro in livros:
            print("-", livro,"\n")

    msg_voltar()
        


def cadastrar_usuario():
    print("==== CADASTRAR USUARIO ====\n")

    nome = input("Digite o nome do usuário: ").strip()

    novo_user = Usuario(nome)

    msg = input("\n<<Cadastrar?>>\nResponda sim ou não: ").strip().lower()

    if msg == "sim":
        usuarios.append(novo_user)
        registrar_log(f"Usuário '{nome}' cadastrado no sistema")
        print("\n <<< Usuário cadastrado com sucesso!! >>> \n")

        msg_voltar()

        
    else:
        print("\n<<< Cadastro Cancelado >>>\n")
        msg_voltar()



def cadastrar_livro():
    print("\n=========== CADASTRAR LIVRO ==========\n")

    nome = input("- Digite o nome do livro: ").strip()
    autor = input("- Digite o autor do livro: ").strip()
    ano_lancado = int(input("- Digite o ano de lancamento do livro: ").strip())
    
    novo_livro = Livro(nome, autor, ano_lancado)

    msg = input("Cadastrar?\n Responda sim ou não: ").strip().lower()

    if msg == "sim":
        livros.append(novo_livro)
        registrar_log(f"Livro cadastrado: {nome}")
        print("\n<<< Livro Cadastrado com sucesso!! >>>\n")
        msg_voltar()


    else:
        print("\n<<< Cadastro Cancelado >>>\n")
        msg_voltar()



def encontrar_usuario_por_nome(nome_procurado):
    """Retorna o objeto Usuario cujo nome bate exatamente (case-insensitive), ou None."""
    nome_proc = nome_procurado.strip()
    for u in usuarios:
        if u.nome == nome_proc:
            return u
    return None



def encontrar_livro_por_nome(nome_procurado):
    nome_proc = nome_procurado.strip()
    for l in livros:
        if l.nome == nome_proc:
            return l
    return None



def emprestimo():
    print("================ EMPRÉSTIMO DE LIVROS ===============\n")
    user_solicitou = input("Digite o nome do Usuário que solicitou o empréstimo: ").strip()

    livro_solicitado = input("\nNome do livro solicitado: ").strip()

    user = encontrar_usuario_por_nome(user_solicitou)
        
    livro = encontrar_livro_por_nome(livro_solicitado)

    if user is None:
            print(" \n<<< Usuário não encontrado >>>")
            msg_voltar()

    if livro is None:
            print(" \n<<< Livro não encontrado >>>")
            msg_voltar()

    resposta = input("Deseja concluir o empréstimo do livro?: ")
    
    if resposta == "sim":
            solicitacao = { "Empréstimo": "Ok",
                            "Livro Solicitado": (livro),
                            "Quem solicitou": (user),
                            }
                
            emprestimos.append(solicitacao)
            registrar_log(f"Empréstimo: Livro '{livro.nome}' emprestado para {user.nome}.")
            print("\n<<Empréstimo registrado com sucesso!!>>\n")
            msg_voltar()

    else: 
        print(" <<< Empréstimo cancelado >>> \n")





def apresentar_menu():
    while True:
        print("\n========  BEM-VINDO AO SISTEMA DE GERENCIAMENTO DA BIBLIOTECA  ============== \n")

        print("1. Cadastrar Livro")

        print("2. Cadastrar Usuário")

        print("3. Empréstimo")

        print("4. Devolução")

        print("5. Visualizar lista de livros")

        print("6. Visualizar lista de Usuários")

        print("7. SAIR DO SISTEMA\n")

        try:
            opcao_escolhida = int(input("O que deseja fazer? Digite o número: ").strip())

        
            if opcao_escolhida == 1:
                limpar_tela()
                cadastrar_livro()
                
            
            elif opcao_escolhida == 2:
                limpar_tela()
                cadastrar_usuario()
               

            elif opcao_escolhida == 3:
                limpar_tela()
                emprestimo()
                
            
            elif opcao_escolhida == 4:
                limpar_tela()
                
                
            elif opcao_escolhida == 5:
                limpar_tela()
                visualizar_lista_livros()
            
            elif opcao_escolhida == 6:
                limpar_tela()
                visualizar_lista_usuarios()
                

            elif opcao_escolhida == 7:
                limpar_tela()
                print("SING OUT - SISTEMA ENCERRADO!\n\n")
                break
             
            
            else:
                print("\n [ERROR]: Opção inválida! Digite um número de 1 a 6.\n")


        except ValueError:
                print("\n [ERROR]: Digite apenas números\n")









# ========= TESTAR ADICIONAR MANUALMENTE LIVROS ===== #

if __name__ == "__main__":
    inicializando_sistema_add()
    apresentar_menu()
 
"""
APRENDIZADO;
1. Repetir o mesmo nome da variavel cada vez que se executa a função cadastrar_livro, dá problema?:
✔ A variável livro é apenas uma referência temporária.
✔ Cada Livro() criado é um novo objeto independente.
✔ A lista guarda os objetos, não as variáveis.
✔ Não existe risco de sobrescrever livros cadastrados antes.

2. __str__ não funcionou, ao imprimir a lista livros. executava <object>
 __str__ só funciona quando você imprime cada objeto individualmente.
 Python usa outro método quando imprime listas: __repr__.

.lower() transforma em letras minúsculas.

datetime.now() - pega a data e hora atuais do sistema.
strftime("%Y-%m-%d %H:%M:%S")
strftime() formata a data/hora para o formato que você quiser.
"""
