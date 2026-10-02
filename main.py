import membros
import estatisticas
from time import sleep

print('=' * 60)
print(f'{"GESTÃO DE COLABORADORES":^40}')
print('=' * 60)
while True:
    print('''1. Cadastrar novo colaborador
2. Listar todos os colaborador cadastrados
3. Buscar colaborador por ID
4. Estatisticas do sistema
5. Encerrar programa''')
    print('=' * 60)
    escolha_usuario = input('Opção desejada: ').strip()
    print('=' * 60)
    if escolha_usuario == '1':
        membros.cadastrar()
    elif escolha_usuario == '2':
        membros.listar()
    elif escolha_usuario == '3':
        membros.buscar()
    elif escolha_usuario == '4':
        estatisticas.relatorio()
    elif escolha_usuario == '5':
        print('ENCERRANDO...')
        sleep(1)
        print('SISTEMA ENCERRADO COM SUCESSO!')
        break
    else:
        print('Opção inválida. Por favor, tente novamente!')
        print('=' * 60)