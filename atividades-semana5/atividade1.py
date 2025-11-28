"""
Nível Simples: Expandindo a API de Produtos
Descrição: Adicione dois novos endpoints à API de produtos:

GET /produtos/categoria/{categoria} - Lista produtos de uma categoria específica
PATCH /produtos/{id}/estoque - Atualiza apenas o estoque de um produto
O que se espera:

Código funcional e comentado
Testes realizados no Swagger UI com prints das respostas
Um arquivo RESPOSTA.md explicando:
Qual a diferença entre PUT e PATCH?
Por que usar um endpoint específico para atualizar estoque?
Critérios de avaliação:

Código funciona corretamente (40%)
Boas práticas aplicadas (30%)
Explicações claras e corretas (30%)
Nível Médio: Sistema de Autenticação Básico
Descrição: Implemente um sistema simples de autenticação para proteger os endpoints de criação, atualização e deleção:

Crie um modelo Usuario com: id, username, email, senha_hash
Implemente endpoints de registro e login
Proteja endpoints sensíveis (POST, PUT, DELETE) com autenticação básica
Requisitos técnicos:

Use passlib para hash de senhas
Use python-jose para gerar tokens JWT
Implemente um decorator/dependency @require_auth
Critérios de avaliação:

Funcionalidade completa (40%)
Segurança adequada (senha nunca armazenada em texto plano) (30%)
Organização do código (20%)
Documentação no código (10%)
Recursos úteis:

Documentação FastAPI sobre segurança: https://fastapi.tiangolo.com/tutorial/security/
"""