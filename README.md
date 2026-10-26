Sistema de Gestão de Colaboradores
Aplicação de terminal desenvolvida em Python com integração ao MySQL para praticar operações CRUD, validação de dados, organização em módulos e consultas SQL.
Funcionalidades
- Cadastrar colaboradores com validação e normalização dos dados.
- Listar colaboradores cadastrados.
- Buscar um colaborador pelo ID.
- Consultar estatísticas do sistema:
  - total de colaboradores;
  - folha de pagamento e média salarial;
  - distribuição por sexo;
  - colaborador mais velho, conforme a data de nascimento.
- Editar dados de um colaborador existente.
- Excluir colaboradores por ID, com confirmação antes da remoção.
- Tratar situações como tabela vazia, ID inexistente e entradas inválidas.
Tecnologias
- Python
- MySQL
- mysql-connector-python
- Git e GitHub
Estrutura do projeto
sistema-gestao-membros/
├── main.py          # Menu principal e fluxo da aplicação
├── database.py      # Configuração da conexão MySQL
├── membros.py       # Cadastro, listagem, busca, edição e exclusão
├── estatisticas.py  # Consultas e relatório estatístico
├── README.md
└── .gitignore
Requisitos
- Python 3 instalado.
- MySQL Server instalado e em execução.
- Banco de dados sistema_gestao.
- Tabela colaboradores com as colunas utilizadas pelo projeto: id, nome, data_nascimento, email, sexo e salario.
- Pacote mysql-connector-python.
Este repositório não inclui a criação automática do banco ou da tabela. Prepare a estrutura no seu MySQL antes de executar o programa.

Como executar
1. Clone o repositório e entre na pasta do projeto.
2. Instale a dependência:
   python -m pip install mysql-connector-python
3. Configure a conexão no database.py para o seu ambiente local. Não coloque senhas reais no código nem as envie para o GitHub. Para uma versão futura, considere carregar as credenciais por variáveis de ambiente.
4. Execute:
   python main.py
O que pratiquei
- Integração de Python com MySQL.
- Consultas SQL com SELECT, INSERT, UPDATE, DELETE, WHERE, ORDER BY, COUNT, SUM, AVG e LIMIT.
- Consultas parametrizadas com placeholders %s.
- Uso de cursores, fetchone() e fetchall().
- Funções, módulos, dicionários e estruturas de repetição/condição.
- Validação, normalização e conversão de dados.
- Tratamento de entradas inválidas e organização do código por responsabilidade.
- Versionamento com Git e GitHub.
Escopo e limitações
Este é um projeto educacional de terminal, criado para consolidar fundamentos de Python e SQL. A configuração do banco e a tabela precisam ser preparadas manualmente. O projeto pode ser ampliado futuramente com testes automatizados, configuração de credenciais por variáveis de ambiente e documentação de criação do esquema do banco.
Autor
Lucas Silva — projeto desenvolvido como parte dos meus estudos de Python e MySQL.