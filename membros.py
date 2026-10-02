from database import conexao
from time import sleep
from datetime import datetime

def cadastrar():
    with conexao.cursor() as cursor:
        while True:
            try:
                nome = str(input('>> Nome Completo: ')).strip().title()
                if len(nome) < 3 or not nome[0].isalpha() or ' ' not in nome:
                    raise ValueError
            except ValueError:
                print('Nome inválido. Por favor tente novamente.')
                continue
            else:
                break
        while True:
            ano_atual = datetime.today().year
            try:
                data = input('>> Digite a data de nascimento no formato [ DD/MM/AAAA ]: ').strip()
                #strptime verifica automaticamente se a data é valida, por exemplo, se não foi digitado o dia 29 no mês 02
                data_objeto = datetime.strptime(data, "%d/%m/%Y")
                #calculo da idade com o ano atual - o ano informado pelo usuario
                idade = ano_atual - data_objeto.year
                #com o strftime eu ordeno a data para o padrão do banco de dados
                data_nascimento = datetime.strftime(data_objeto, "%Y-%m-%d")
                if idade < 18:
                    raise ValueError
                break
            except ValueError:
                print('Data inválida! Por favor, tente novamente.')
                continue
        while True:
            try:
                email = input('>> Email: ').strip().lower()
                if '@' not in  email or email.count('@') > 1 or not email[0].isalpha() or len(email) == 0 or '.' not in email or email.count('.') > 2:
                    raise ValueError
                break
            except ValueError:
                print('Email Inválido! Por favor, tente novamente.')
        while True:
            try:
                sexo = str(input('>> Sexo: ')).strip().upper()
                if sexo not in ['M', 'F'] or len(sexo) < 1:
                    raise ValueError
                break
            except ValueError:
                print('Sexo inválido. Por favor, tente novamente.')
                continue
        while True:
            try:
                salario_texto = input('>> Salário: R$ ').strip()
                if ',' in salario_texto:
                    salario_texto = salario_texto.replace(',', '.')
                if len(salario_texto) < 1 or len(salario_texto) > 25:
                    raise ValueError
                salario = float(salario_texto)
                if salario < 1621:
                    raise ValueError
                break
            except ValueError:
                print('Salário inválido! Por favor, tente novamente.')
        comando_sql = '''INSERT INTO colaboradores (
        nome, data_nascimento, email, sexo, salario) VALUES (
        %s, %s, %s, %s, %s)'''
        dados_cliente = (nome, data_nascimento, email, sexo, salario)
        cursor.execute(comando_sql, dados_cliente)
        conexao.commit()
        print('Colaborador cadastrado com sucesso!')
        print('=' * 60)
def listar():
    with conexao.cursor(dictionary=True) as cursor:
        consulta_linhas = '''SELECT COUNT(*) AS linhas FROM colaboradores'''
        cursor.execute(consulta_linhas)
        quantidade_linhas = cursor.fetchone()['linhas']
        if quantidade_linhas == 0:
            print('>> Nenhum colaborador cadastrado até o momento.')
            print('=' * 60)
            return
        print('LISTANDO TODOS OS COLABORADORES...')
        sleep(1)
        consulta_nomes = '''SELECT id, nome FROM colaboradores'''
        cursor.execute(consulta_nomes)
        resultado_clientes = cursor.fetchall()
        for cliente in resultado_clientes:
            print(f'  ID:{cliente['id']:<4}  {cliente['nome']}')
        print('=' * 60)
def buscar():
    cont = 0
    with conexao.cursor(dictionary=True) as cursor:
        while True:
            busca_usuario = int(input('Informe o ID, por gentileza: '))
            consulta_usuario = f'SELECT IFNULL(MAX(nome), "Inexistente") AS nome FROM colaboradores WHERE id = %s'  
            cursor.execute(consulta_usuario, (busca_usuario, ))
            resultado_busca = cursor.fetchone()['nome']
            if resultado_busca == 'Inexistente':
                print('>> ID inválido. Por favor, tente novamente.')
                cont += 1
            else:
                break
            if cont == 3:
                print('>> Limite de tentativas excedido. Retornando ao menu principal.')
                break
        if cont != 3:
            print(f'  Colaborador "{resultado_busca}" encontrado com sucesso!')
        print('=' * 60)
