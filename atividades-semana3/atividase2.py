import pandas as pd
import numpy as np
import csv
import json
"""
Desenvolva um sistema de notas que:

Leia dados de alunos de um CSV (nome, nota1, nota2, nota3)
Calcule a média de cada aluno
Determine se foi aprovado (média ≥ 7.0)
Gere um relatório em JSON com estatísticas da turma:
Quantidade de aprovados/reprovados
Média geral da turma
Maior e menor nota
Use funções separadas para cada operação
"""


# ==== Lendo dados =====#
df = pd.read_csv("atividades-semana3/alunos.csv")


# ================ Criando novas colunas ============================ #


df['Média'] = ((df['nota1'] + df['nota2'] + df['nota3']) / 3).round(1)

df['Status'] = np.where(df["Média"] >= 7, "Aprovado", "Reprovado")

print(df)


#==== FUNÇÕES PARA O RELATÓRIO ===#
def verificar_qtd_status(dataframe):
    aprovados = dataframe[dataframe["Status"] == "Aprovado"]
    reprovados = dataframe[dataframe["Status"] == "Reprovado"]
    
    dicionario = {"Quantidade de Aprovados": len(aprovados),
                  "Quantidade de Reprovados": len(reprovados)
                 }
    print(dicionario)

    return dicionario


def media_geral(dataframe):
    media = round(float(dataframe["Média"].mean()), 2)

    dicionario = {"Media geral dos alunos": media}
    print(dicionario)

    return dicionario



def verificar_notas(dataframe):
    maior_nota = (dataframe["Média"].max())

    menor_nota = (dataframe["Média"].min())

    dicionario = {"Maior nota": maior_nota,
                  "Menor nota": menor_nota
                 }
    return dicionario


#===== USANDO FUNÇÕES =====#

qtd_status = verificar_qtd_status(df)

media_geral = media_geral(df)

notas = verificar_notas(df)

mood_json = [qtd_status, media_geral, notas]

# ===FUNÇÃO PARA CRIAR O RELATÓRIO ==#

path = "atividades-semana3/estatisticas_turma.json"

def criar_relatorio_json(path, formato_json):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(formato_json, file, indent=4)
        print("JSON criado com sucesso!")

# ========== CRIANDO O ARQUIVO

criar_relatorio_json(path, mood_json)



"""
Aprendizado;

Apresentei problemas na ordem dos argumentos no json.dump, a forma correta:
json.dump(*formato_json*, *caminho path*, indent=4) SEMPRE dessa forma.


Função	       |O que faz	               |Retorno	      |Usada quando
json.dump()	  |Escreve JSON em um arquivo  |Nada	      |Você quer salvar em arquivo.json
json.dumps() |Converte JSON para string	   |String JSON	  |Você quer imprimir, enviar, exibir ou manipular como texto

"""



