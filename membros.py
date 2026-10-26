from database import conexao
from time import sleep
from datetime import datetime, date

def validar_nome(nome_usuario):
    if len(nome_usuario) < 3 or not nome_usuario[0].isalpha() or ' ' not in nome_usuario:
        raise ValueError
    return nome_usuario.title().strip()
def validar_email(email_usuario):
    if len(email_usuario) == 0 or '@' not in  email_usuario or email_usuario.count('@') > 1 or not email_usuario[0].isalpha() or '.' not in email_usuario or email_usuario.count('.') > 2:
        raise ValueError
    return email_usuario.lower().strip()
def validar_sexo(sexo_usuario):
    sexo_usuario = sexo_usuario.upper().strip()
    if sexo_usuario not in ['M', 'F'] or len(sexo_usuario) < 1:
        raise ValueError
    return sexo_usuario
def validar_salario(salario_usuario):
    if ',' in salario_usuario:
        salario_usuario = salario_usuario.replace(',', '.')
    if len(salario_usuario) < 1 or len(salario_usuario) > 25:
        raise ValueError
    salario = float(salario_usuario)
    if salario < 1621:
        raise ValueError
    return salario
def validar_idade(data_nascimento_usuario):
    data_objeto = datetime.strptime(data_nascimento_usuario, "%d/%m/%Y")
    data_atual = date.today()
    idade = data_atual.year - data_objeto.year # calcula idade com o ano atual - ano de nascimento
    #comparo o mês e dia atual com o mês e dia de nascimento
    ja_fez_aniversario = (data_atual.month, data_atual.day) >= (data_objeto.month, data_objeto.day)
    # se o mês e dia atual não for maior que o mês e dia de nascimento, diminuo 1 ano de idade
    if not ja_fez_aniversario:
        idade -= 1
    if idade < 18:
        raise ValueError
    #passo a idade para o padrão do banco de dados
    data_nascimento = data_objeto.strftime("%Y-%m-%d")
    return data_nascimento

def cadastrar():
    with conexao.cursor() as cursor:
        while True:
            try:
                nome = str(input('>> Nome Completo: ')).strip().title()
                validar_nome(nome)
                break
            except ValueError:
                print('Nome inválido. Por favor tente novamente.')
                continue
        while True:
            try:
                data = input('>> Digite a data de nascimento no formato [ DD/MM/AAAA ]: ').strip()
                data_nascimento = validar_idade(data)
                break
            except ValueError:
                print('Data inválida! Por favor, tente novamente.')
                continue
        while True:
            try:
                email = input('>> Email: ').strip().lower()
                validar_email(email)
                break
            except ValueError:
                print('Email Inválido! Por favor, tente novamente.')
        while True:
            try:
                sexo = str(input('>> Sexo: ')).strip().upper()
                validar_sexo(sexo)
                break
            except ValueError:
                print('Sexo inválido. Por favor, tente novamente.')
                continue
        while True:
            try:
                salario_texto = input('>> Salário: R$ ').strip()
                salario = validar_salario(salario_texto)
                break
            except ValueError:
                print('Salário inválido! Por favor, tente novamente.')
        comando_sql = '''INSERT INTO colaboradores (
        nome, data_nascimento, email, sexo, salario) VALUES (
        %s, %s, %s, %s, %s)'''
        dados_cliente = (nome, data_nascimento, email, sexo, salario)
        cursor.execute(comando_sql, dados_cliente)
        conexao.commit()
        print('Cadastrando...')
        sleep(0.8)
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
            while True:
                try:
                    busca_usuario = int(input('Informe o ID, por gentileza: '))
                    break
                except ValueError:
                    print('Erro! digite apenas números.')
                    print('-' * 40)
                    continue
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
            print(f'  ID:{busca_usuario} corresponde ao colaborador: {resultado_busca}.')
        print('=' * 60)
def editar():
    with conexao.cursor(dictionary=True) as cursor:
        consulta_linhas = '''SELECT COUNT(*) AS linhas FROM colaboradores'''
        cursor.execute(consulta_linhas)
        quantidade_linhas = cursor.fetchone()['linhas']
        if quantidade_linhas == 0:
            print('>> Nenhum colaborador cadastrado até o momento.')
            print('=' * 60)
            return
        cont = 0
        while True:
            while True:
                try:
                    id_colaborador = int(input('Selecione o ID do colaborador que deseja editar: '))
                    break
                except ValueError:
                    print('Erro! Digite apenas números.')
                    print('-' * 40)
                    continue
            print('-' * 40)
            consulta_usuario = '''SELECT IFNULL(MAX(nome), 'Invalido') AS nome FROM colaboradores WHERE id = %s'''
            cursor.execute(consulta_usuario, (id_colaborador, ))
            resultado_busca = cursor.fetchone()['nome']
            if resultado_busca == 'Invalido':
                print('>> ID inválido. Por favor, tente novamente.')
                cont += 1
            else:
                busca_usuario = '''SELECT * FROM colaboradores WHERE id = %s'''
                cursor.execute(busca_usuario, (id_colaborador, ))
                dados_colaborador = cursor.fetchone()
                print('Informações atuais do colaborador:')
                sleep(0.5)
                for chave, valor in dados_colaborador.items():
                    print(f'{chave.capitalize().replace('_', ' ')}:  {valor}')
                    sleep(0.5)
                break
            if cont == 3:
                print('>> Limite de tentativas excedido. Retornando ao menu principal.')
                print('-' * 40)
                break
        if cont == 3:
            return
        print('-' * 40)
        print(f'''Selecione o que deseja editar do colaborador "{dados_colaborador['nome']}":
1. Nome
2. Data de nascimento
3. E-mail
4. Sexo
5. Salário
6. Retornar ao menu''')
        while True:
            try:
                escolha_edit = int(input('Sua escolha [APENAS NÚMEROS]: '))
                if escolha_edit < 1 or escolha_edit > 6:
                    raise ValueError
                break
            except ValueError:
                print('Erro! Digite apenas números do 1 ao 6.')
                print('-' * 40)
                continue
        if escolha_edit == 6:
            print('>> Retornando ao menu principal!')
            print('=' * 60)
            return
        colunas = {
            1: {'coluna': 'nome', 'validar': validar_nome},
            2: {'coluna': 'data_nascimento', 'validar': validar_idade},
            3: {'coluna': 'email', 'validar': validar_email},
            4: {'coluna': 'sexo', 'validar': validar_sexo},
            5: {'coluna': 'salario', 'validar': validar_salario}
        }
        while True:
            try:
                novo_dado = input(f'Informe o novo {colunas[escolha_edit]['coluna'].capitalize().replace("_", " ")}: ')
                resultado_validacao = colunas[escolha_edit]['validar'](novo_dado)
                novo_dado = resultado_validacao
                break
            except ValueError:
                print('>> Dado inválido! Por favor, tente novamente.')
                continue
        coluna_correta = colunas[escolha_edit]['coluna']
        codigo_sql = f'''UPDATE colaboradores SET {coluna_correta} = %s WHERE id = %s LIMIT 1'''
        cursor.execute(codigo_sql, (novo_dado, id_colaborador, ))
        print('-' * 40)
        linhas_modificadas = cursor.rowcount
        if linhas_modificadas == 0 and escolha_edit != 6:
            print('>> Nenhum dado alterado devido a duplicação do mesmo. Retornando ao menu principal!')
            print('-' * 40)
        else:
            print(f'Quantidade de linhas modificadas: {linhas_modificadas}')
            conexao.commit()
            print('-' * 40)
            print('Dados atualizados com sucesso! Mostrando os dados atuais do colaborador:')
            sleep(0.5)
            consulta_dados = '''SELECT * FROM colaboradores WHERE id = %s'''
            cursor.execute(consulta_dados, (id_colaborador, ))
            dados_atualizados = cursor.fetchone()
            for chave, valor in dados_atualizados.items():
                print(f'{chave.capitalize().replace("_", " ")}:  {valor}')
                sleep(0.5)
            print('=' * 60)
def excluir():
    with conexao.cursor(dictionary=True) as cursor:
        consulta_linhas = '''SELECT COUNT(*) AS linhas FROM colaboradores'''
        cursor.execute(consulta_linhas)
        quantidade_linhas = cursor.fetchone()['linhas']
        if quantidade_linhas == 0:
            print('>> Nenhum colaborador cadastrado até o momento.')
            print('=' * 60)
            return
        cont = 0
        while True:
            while True:
                try:
                    id_usuario = int(input('Informe o ID do colaborador que deseja excluir: '))
                    break
                except ValueError:
                    print('>> ID inválido! Por favor, digite apenas números.')
                    print('-' * 40)
                    continue
            consulta_id = '''SELECT * FROM COLABORADORES WHERE id = %s'''
            cursor.execute(consulta_id, (id_usuario, ))
            resultado_consulta_id = cursor.fetchone()
            if resultado_consulta_id is None:
                print('Colaborador não encontrado! Por favor, tente novamente.')
                print('-' * 40)
                cont += 1
            else:
                print(f'Colaborador >> ID:{resultado_consulta_id['id']}  {resultado_consulta_id['nome']} << encontrado com sucesso.')
                print('-' * 40)
                while True:
                    try:
                        confirmar_exclusao = input(f'Confirmar exclusão do colaborador {resultado_consulta_id['nome']} [ APENAS SIM OU NÃO ]: ').strip().upper()
                        if confirmar_exclusao == 'NAO':
                            confirmar_exclusao = 'NÃO'
                        if confirmar_exclusao not in ['SIM', 'NÃO']:
                            raise ValueError
                        break
                    except ValueError:
                        print('>> Erro! Digite apenas SIM ou Não.')
                break
            if cont == 3:
                print('>> Limite de tentativas excedido! Retornando ao menu principal.')
                print('-' * 40)
                break
        if cont == 3:
            return
        if confirmar_exclusao == 'NÃO':
            print('>> Colaborador não excluido do sistema! Retornando ao menu principal.')
            print('-' * 40)
            return
        codigo_sql = '''DELETE FROM colaboradores WHERE id = %s'''
        cursor.execute(codigo_sql, (id_usuario, ))
        conexao.commit()
        print('Colaborador exlcuido do sistema com sucesso! Retornando ao menu principal')
        print('-' * 40)
