from database import cursor, conexao
from time import sleep

print('-' * 40)
print(f'{"SISTEMA DE GESTÃO DE MEMBROS":^40}')
print('-' * 40)
while True:
    print('''1. Cadastrar novo membro
2. Listar todos os Funcionários cadastrados
3. Buscar funcionário por ID
4. Estatisticas do sistema
5. Encerrar programa''')
    print('-' * 40)
    escolha_usuario = (input('Opção desejada: ')).strip()
    print('-' * 40)
    if escolha_usuario == '1':
        nome = str(input('Nome: ')).strip().title()
        data_nascimento = input('Data nascimento: ').strip()
        dividindo_data_nascimento = data_nascimento.split('/')
        data_formatada = f'{dividindo_data_nascimento[2]}-{dividindo_data_nascimento[1]}-{dividindo_data_nascimento[0]}'
        email = input('Email: ').strip()
        while True:
            sexo = str(input('Sexo: ')).strip().upper()[0]
            if sexo in 'MF':
                break
        salario = float(input('Salário: R$ '))
        comando_sql = '''INSERT INTO clientes (
        nome, data_nascimento, email, sexo, salario) VALUES (
        %s, %s, %s, %s, %s)'''
        dados_cliente = (nome, data_formatada, email, sexo, salario)
        cursor.execute(comando_sql, dados_cliente)
        conexao.commit()
        print('Funcionário cadastrado com sucesso!')
        print('-' * 40)
    elif escolha_usuario == '2':
        print('LISTANDO TODOS OS MEMBROS...')
        sleep(1)
        consulta_nomes = '''SELECT * FROM clientes'''
        cursor.execute(consulta_nomes)
        nomes_clientes = cursor.fetchall()
        for cliente in nomes_clientes:
            print(f'ID: {cliente[0]} {cliente[1]}')
        print('-' * 40)
    elif escolha_usuario == '3':
        busca_usuario = int(input('Informe o ID, por gentileza: '))
        consulta_nomes_id = 'SELECT id, nome FROM clientes'
        cursor.execute(consulta_nomes_id)
        id = cursor.fetchall()
        for cliente in id:
            if busca_usuario == cliente[0]:
                print(f'Cliente {cliente[1]} encontrado com sucesso!')    
        print('-' * 40)
    elif escolha_usuario == '4':
        print('LISTANDO ESTATISTICAS DO SISTEMA...')
        sleep(1)
        consulta_funcionarios = 'SELECT id FROM clientes'
        consulta_salario = 'SELECT salario FROM clientes'
        consulta_genero = 'SELECT sexo FROM clientes'
        cursor.execute(consulta_funcionarios)
        total_funcionarios = cursor.fetchall()
        cursor.execute(consulta_salario)
        total_salario = cursor.fetchall()
        cursor.execute(consulta_genero)
        total_generos = cursor.fetchall()
        print(f'Total de funcionários cadastrados: {len(total_funcionarios)}')
        folha_pagamento = 0
        for salario in total_salario:
            folha_pagamento += salario[0]
        print(f'Folha de pagamento de R${folha_pagamento:.2f}, sendo a média salarial de R${folha_pagamento / len(total_funcionarios):.2f}')
        total_homens = total_mulheres = 0
        for genero in total_generos:
            if genero[0] == 'M':
                total_homens += 1
            else:
                total_mulheres += 1
        print(f'Divisão por genêro: {total_homens} Homens e {total_mulheres} Mulheres')
        consulta_funcionarios = 'SELECT * FROM clientes WHERE id = 1'
        cursor.execute(consulta_funcionarios)
        funcionario_mais_antigo = cursor.fetchone()
        print(f'Funcionários mais antigo: ID: {funcionario_mais_antigo[0]} {funcionario_mais_antigo[1]}')
        print('-' * 40)
    elif escolha_usuario == '5':
        print('ENCERRANDO...')
        sleep(1)
        print('SISTEMA ENCERRADO COM SUCESSO!')
        break
    else:
        print('Opção inválida. Por favor, tente novamente!')
        print('-' * 40)