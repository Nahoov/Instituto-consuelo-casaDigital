class Funcionario:
    def __init__(self, nome, sobrenome, cargo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cargo = cargo

    def __str__(self):
        return f'{self.nome}, {self.sobrenome},{self.cargo}'
    
funcionario1 = Funcionario('nahomi', 'ribas', ' desenvolvedora')

print(funcionario1)


class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano





numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nomes = [ "nahomi", "dimas", "gabriel", "hector"]

anos = [2004, 2025]

#soma de todos os impares de 0 a 10
soma_impares = 0

for i in numeros:
   if i % 2 != 0:
        soma_impares +=i

print(soma_impares)

#lista de 10 a 0 decrescente
for numero in range(10, 0, -1):
    print (numero)

#funcao de tabuada
#numero_tabuada = int(input('digite o número da tabuada que deseja visualizar: '))
#for i in range (0, 11):
    #resultado = numero_tabuada * i
    #print(f'{numero_tabuada} x {i} = {resultado}')


# . Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos.
#  Utilize um bloco try-except para lidar com possíveis exceções.


soma = 0

try:
    for numero in numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


#. Construa um código que calcule a média dos valores em uma lista.
#Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")

except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
    """
    ZeroDivisionError é uma exceção específica que ocorre quando há uma tentativa de divisão por zero. 
    Este bloco except é destinado a lidar especificamente com esse tipo de erro.

    """
except Exception as e:
    print(f"Ocorreu um erro: {e}")
