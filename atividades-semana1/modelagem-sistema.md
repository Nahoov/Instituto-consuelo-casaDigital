# Exercícios semana 1

**Aluna**: Nahomi Lexamar Ribas Rodriguez

## 3. Modelagem de sistema
![Modelagem de sistema](./imagens/modelagem_sistema2.png)

**tipos de dados escolhidos para a tabela "pacientes":**

nome: VARCHAR(30) -> Esse tipo de dado permite até 30 caracteres no campo, se o nome inserido for menor, a memória guarda exatamente a quantidade digitada. Poderia ter adicionado outro campo com "sobrenome", mas não achei necessário no exercício agora.

endereço, cidade e estado: VARCHAR() -> pelo mesmo motivo de salvar até onde for digitado, se for menor que o limite.

cpf: CHAR(11) -> Esse tipo de dado, armazena exatamente 11 caracteres mesmo que vazios. Usei ele neste caso, pois todo cpf obrigatoriamente deve cumprir com 11 números.

data_nascimento: date -> Escolhi esse dado por ter a capacidade de armazenar datas.


**tipos de dados escolhidos para fichario**

complicacao: text() -> Esse tipo de dado armazena grandes textos, com muitos caractere e assim decidi escolher, para uma descrição completa da complicação do paciente.

**- Coloquei UNIQUE, no cpf**
**- As chaves estrangeiras se encontram no final da tabela, com chave**




