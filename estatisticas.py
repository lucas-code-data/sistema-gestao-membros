from database import conexao
from time import sleep

def relatorio():
    #cursor onde transforma as colunas em dicionários
    #with evita de dar confusão/atrito com outros cursores de modulos diferentes
    with conexao.cursor(dictionary=True) as cursor:
        #verificação se a tabela não está vazia
        consulta_linhas = '''SELECT COUNT(id) AS linhas FROM colaboradores'''
        cursor.execute(consulta_linhas)
        quantidade_linhas = cursor.fetchone()['linhas']
        if quantidade_linhas < 1:
            print('>> Nenhum colaborador cadastrado até o momento.')
            print('=' * 60)
            return 
        #caso haja dados na tabela o return não encerra a função, dando seguimento
        print('LISTANDO ESTATISTICAS DO SISTEMA...')
        sleep(1)
        #realizo todas as consultas com o select
        consulta_funcionarios = 'SELECT COUNT(id) as total_funcionarios FROM colaboradores'
        consulta_salario = 'SELECT SUM(salario) as total_salario FROM colaboradores'
        consulta_media_salario = 'SELECT AVG(salario) as media_salario FROM colaboradores'
        consulta_genero_masc = 'SELECT COUNT(sexo) as total_masc FROM colaboradores WHERE sexo = %s'
        consulta_genero_fem = 'SELECT COUNT(sexo) as total_fem FROM colaboradores WHERE sexo = %s'
        #executo todas as buscas e depois coloco-as em uma variavel com sua chave respectiva
        cursor.execute(consulta_funcionarios)
        total_funcionarios = cursor.fetchone()['total_funcionarios']
        cursor.execute(consulta_salario)
        total_salario = cursor.fetchone()['total_salario']
        cursor.execute(consulta_media_salario)
        AVG_salario = cursor.fetchone()['media_salario']
        cursor.execute(consulta_genero_masc, ('M', ))
        total_masculino = cursor.fetchone()['total_masc']
        cursor.execute(consulta_genero_fem, ('F', ))
        total_feminino = cursor.fetchone()['total_fem']
        print(f'Total de colaboradores cadastrados: {total_funcionarios}')
        print(f'Folha de pagamento de R${total_salario}, sendo a média salarial de R${AVG_salario}')
        print(f'Divisão por genêro: {total_masculino} Homens e {total_feminino} Mulheres')
        #ordeno os funcionarios pela data em que foram cadastrados e mostro na tela
        consulta_funcionarios = 'SELECT id, nome FROM colaboradores ORDER BY data_nascimento ASC LIMIT 1'
        cursor.execute(consulta_funcionarios)
        antigo = cursor.fetchone()
        print(f'Colaborador mais velho: ID:{antigo['id']}    {antigo['nome']}')
        print('=' * 60)