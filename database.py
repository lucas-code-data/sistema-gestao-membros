import mysql.connector 

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'SUA SENHA AQUI',
    database = 'sistema_gestao',
)

cursor = conexao.cursor()