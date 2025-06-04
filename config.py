import os

SECRET_KEY = 'alura'

# Configura conexão com o Banco de dados
SGBD = 'mysql+mysqlconnector'
usuario = 'root'
senha = 'XMbbv5vpx'
servidor = 'localhost'
database = 'jogoteca'

SQLALCHEMY_DATABASE_URI = f'{SGBD}://{usuario}:{senha}@{servidor}/{database}'


UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'