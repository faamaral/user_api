''' 
Descricao :
	Arquivo responsavel por registrar uma blueprint no flask
Aluno :
	Fabiano Amaral Alves
Data :
	22 / 07 / 2021
'''

from user_api.views.user import api_bp

def init_app(app):
    app.register_blueprint(api_bp)

