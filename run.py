'''
Descricao :
	Arquivo responsavel pela execução da aplicação
Aluno :
	Fabiano Amaral Alves
Data :
	22 / 07 / 2021
'''

import os

from user_api import app


def main():
    app_api = app.create_app()
    port = int(os.environ.get("PORT", 5000))
    app_api.run(host="0.0.0.0", port=port)

if __name__ == '__main__':
    main()