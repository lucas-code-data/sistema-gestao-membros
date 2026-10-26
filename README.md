# Sistema de Gestão de Colaboradores

**Aplicação de terminal desenvolvida em Python e MySQL para gerenciar registros de colaboradores, executar operações CRUD e consultar indicadores básicos do cadastro.**

Este projeto foi criado para colocar em prática conceitos estudados em Python e SQL, com foco na integração entre aplicação e banco de dados, validação de entradas e organização do código em módulos.

## Funcionalidades

| Funcionalidade | Descrição |
| --- | --- |
| **Cadastrar** | Registra colaboradores com validação e normalização dos dados informados. |
| **Listar** | Exibe os colaboradores cadastrados. |
| **Buscar por ID** | Consulta os dados de um colaborador específico. |
| **Editar** | Permite alterar informações de um colaborador existente. |
| **Excluir** | Remove um registro pelo ID, após confirmação. |
| **Estatísticas** | Apresenta indicadores calculados a partir dos registros do banco. |

### Indicadores disponíveis

- Total de colaboradores cadastrados;
- Soma dos salários (folha de pagamento);
- Média salarial;
- Distribuição dos colaboradores por sexo;
- Colaborador mais velho, com base na data de nascimento.

O sistema também contempla situações como ausência de registros, IDs inexistentes e entradas inválidas.

## Tecnologias utilizadas

- **Python** — lógica da aplicação e interação pelo terminal;
- **MySQL** — armazenamento e consultas dos dados;
- **mysql-connector-python** — comunicação entre Python e MySQL;
- **Git e GitHub** — versionamento e publicação do projeto.

## Estrutura do projeto

```text
sistema-gestao-membros/
├── main.py          # Menu principal e navegação
├── membros.py       # Cadastro, listagem, busca, edição e exclusão
├── estatisticas.py  # Consultas e indicadores do sistema
├── database.py      # Configuração da conexão com o MySQL
├── .gitignore
└── README.md
```

## Como executar

### Pré-requisitos

- Python 3;
- MySQL Server instalado e em execução;
- Biblioteca `mysql-connector-python`;
- Banco de dados `sistema_gestao` com a tabela `colaboradores`.

A tabela deve conter as colunas utilizadas pela aplicação: `id`, `nome`, `data_nascimento`, `email`, `sexo` e `salario`.

> **Atenção:** nesta versão, o banco de dados e a tabela precisam ser criados manualmente. O repositório ainda não fornece um script SQL de inicialização.

### Passo a passo

**1. Clone o repositório:**

```bash
git clone https://github.com/lucas-code-data/sistema-gestao-membros.git
cd sistema-gestao-membros
```

**2. Instale a biblioteca necessária:**

```bash
python -m pip install mysql-connector-python
```

**3. Prepare o banco de dados:** crie o banco `sistema_gestao` e a tabela `colaboradores` com os campos descritos acima, de acordo com os tipos esperados pelo código.

**4. Configure a conexão:** ajuste o arquivo `database.py` com as informações do seu MySQL local.

> **Segurança:** não publique senhas reais no GitHub. A configuração atual é voltada ao uso local; uma melhoria futura é utilizar variáveis de ambiente.

**5. Inicie o programa:**

```bash
python main.py
```

Depois, utilize o menu exibido no terminal para acessar as funcionalidades.

## Conceitos aplicados

Durante o desenvolvimento, pratiquei:

- **CRUD com SQL:** `INSERT`, `SELECT`, `UPDATE` e `DELETE`;
- **Consultas e agregações:** `WHERE`, `ORDER BY`, `COUNT`, `SUM`, `AVG` e `LIMIT`;
- **Integração Python–MySQL:** conexão, cursores e leitura de resultados;
- **Consultas parametrizadas:** passagem de valores por placeholders `%s`;
- **Organização do código:** funções, módulos e separação de responsabilidades;
- **Tratamento de entradas:** validação e normalização de informações fornecidas pelo usuário;
- **Versionamento:** acompanhamento da evolução do projeto com Git e GitHub.

## Escopo do projeto

O sistema tem **finalidade educacional** e foi desenvolvido para consolidar fundamentos de programação e banco de dados. Não é uma aplicação pronta para produção.

Possíveis evoluções incluem disponibilizar um `schema.sql`, automatizar testes e separar as credenciais da conexão por meio de variáveis de ambiente.

## Autor

**Lucas Silva**  
Estudante de Sistemas de Informação, desenvolvendo projetos para aprofundar conhecimentos em Python, SQL e análise de dados.

[Meu perfil no GitHub](https://github.com/lucas-code-data)
