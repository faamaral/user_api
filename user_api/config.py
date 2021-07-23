''' 
Descricao :
	Arquivo responsavel pela configurações globais da aplicação
Aluno :
	Fabiano Amaral Alves
Data :
	22 / 07 / 2021
'''

import os

key = os.urandom(24)

SECRET_KEY=key
FLASK_ENV='production'
FLASK_DEBUG=False




