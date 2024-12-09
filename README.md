# Desafio-MVC
Desafio Arquitetura de Software e Padrão MVC

## Sobre o desafio

<aside>
💡 Como tivemos um módulo completo, **não** vamos descrever detalhadamente rotas e propriedades dos registros a serem criadas, mas sim, as regras e requisitos que a API deve ter.

O motivo disso é para vocês **também** exercitarem ****o desenvolvimento e a estruturação dessa parte.

</aside>

A ideia desse desafio é criar uma API para um banco contendo operações para as tabelas de Pessoa Jurídica e Pessoa Física

Criação de um sistema bancário com clientes:

- Pessoas Físicas
- Pessoas Jurídicas

### Regras da aplicação

- A aplicação deve estar conectada a um banco SQLite;
- O projeto deve conter uma interface Cliente, com os métodos: Sacar dinheiro e Realizar extrato.
- As controllers devem possuir testes unitários para garantir que estão funcionando conforme devem funcionar.
- Deverá ser possível: Criar e listar usuários.

### Regras de negócio

- O método “sacar dinheiro” deve possuir um limite máximo menor em Pessoa física do que para pessoa jurídica

### Conceitos que pode praticar

- MVC
- Testes unitários (e quem sabe de integração 👀)
- Criação e integração com banco de dados SQLite