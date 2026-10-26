import mysql.connector 

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Sua senha aqui',
    database = 'sistema_gestao',
)
