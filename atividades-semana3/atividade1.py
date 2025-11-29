import json
import os


"""
Crie um programa que:

Leia um arquivo de texto com uma lista de palavras (uma por linha)
Conte quantas palavras têm mais de 5 letras
Salve o resultado em um arquivo JSON com o formato
"""


palavras = []
palavras_maiores = []


file = "atividades-semana3/texto.txt"

path = "atividades-semana3/resultado.json" 

try:
	with open(file, 'r', encoding="utf-8") as arquivo:
		for linha in arquivo:
			linhas = linha.strip()
			palavras.append(linhas)

		for palavra in palavras:
			if len(palavra) > 5:
				palavras_maiores.append(palavra)

		dicionario ={"Total de palavras": len(palavras),
				    "Palavras maiores que 5 letras": len(palavras_maiores)
				    }
	

		with open(path, "w", encoding="utf-8") as file_json:
			json.dump(dicionario, file_json, indent=4)
			print("JSON salvo com sucesso")
			
except Exception as e:
	print(f"[ERROR] Ocorreu um erro ao abrir o arquivo: {e}")




#print(f"- Total de palavras: {len(palavras)} | \n- Palavras com mais de 5 letras: {len(palavras_maiores)} |")


