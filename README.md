# Sistema de Gestão de Colaboradores

Projeto desenvolvido por **Lucas Silva** durante meus estudos de Python e MySQL. Esta é a **V2** do sistema, com organização em módulos, cadastro, listagem, busca por ID e relatório estatístico.

## Sobre o projeto

O Sistema de Gestão de Colaboradores é uma aplicação de terminal que permite cadastrar colaboradores em um banco de dados MySQL e consultar informações sobre os registros cadastrados.

O projeto tem finalidade educacional e está em desenvolvimento. As funcionalidades de edição e exclusão ainda não fazem parte desta versão.

## Funcionalidades da V2

- Cadastro de colaboradores.
- Validações básicas dos dados informados no cadastro.
- Listagem de colaboradores cadastrados.
- Busca de colaborador por ID.
- Relatório estatístico com:
  - total de colaboradores cadastrados;
  - folha de pagamento;
  - média salarial;
  - quantidade de colaboradores por sexo (M/F);
  - colaborador mais velho, de acordo com a data de nascimento.
- Mensagem específica quando não há colaboradores cadastrados na listagem ou no relatório estatístico.
- Menu interativo no terminal.

## Tecnologias utilizadas

- Python
- MySQL
- `mysql-connector-python`
- Git e GitHub

## Organização dos arquivos

```text
sistema-gestao-membros/
├── main.py          # Menu principal e fluxo da aplicação
├── database.py      # Conexão com o banco de dados MySQL
├── membros.py       # Cadastro, listagem e busca de colaboradores
├── estatisticas.py  # Consultas e relatório estatístico
├── README.md
└── .gitignore
```

## Requisitos

- Python instalado.
- MySQL Server instalado e em execução.
- Um banco de dados MySQL chamado `sistema_gestao`.
- A tabela `colaboradores` criada com as colunas utilizadas pelo sistema: `id`, `nome`, `data_nascimento`, `email`, `sexo` e `salario`.
- O pacote `mysql-connector-python` instalado.

## Configuração e execução

1. Clone o repositório ou baixe os arquivos do projeto.
2. Crie o banco de dados `sistema_gestao` no MySQL e configure a tabela `colaboradores` com as colunas indicadas acima.
3. Instale o conector do MySQL para Python:

   ```bash
   pip install mysql-connector-python
   ```

4. Configure a conexão no `database.py` com os dados do seu ambiente local. **Não publique senhas reais nem outras credenciais no GitHub.** Para um projeto compartilhado, prefira configurar credenciais por variáveis de ambiente.
5. Execute o arquivo principal a partir da pasta do projeto:

   ```bash
   python main.py
   ```

> Observação: este projeto utiliza uma conexão local com MySQL. O banco de dados e a tabela precisam existir antes da execução. Os dados de acesso devem ser configurados por quem executar o projeto.

## O que pratiquei neste projeto

- Integração de Python com MySQL.
- Consultas SQL com `SELECT`, `INSERT`, `WHERE`, `ORDER BY`, `COUNT`, `SUM`, `AVG` e `LIMIT`.
- Consultas parametrizadas com placeholders `%s`.
- Uso de cursores e recuperação de resultados com `fetchone()` e `fetchall()`.
- Estruturas condicionais e de repetição.
- Criação e uso de funções e módulos Python.
- Validação de entradas do usuário.
- Conversão e formatação de datas.
- Organização do código por responsabilidade.
- Uso de Git e GitHub para versionamento.

## Próximas melhorias — V3

- [ ] Implementar edição de colaboradores com `UPDATE`.
- [ ] Implementar exclusão de colaboradores com `DELETE` e confirmação antes da remoção.
- [ ] Fortalecer as validações de entrada e o tratamento de erros.
- [ ] Melhorar a configuração segura das credenciais do banco de dados.
- [ ] Ampliar os testes dos fluxos e dos casos inválidos.

---

Desenvolvido por **Lucas Silva** como parte dos meus estudos de Python e MySQL.