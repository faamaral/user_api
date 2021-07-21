import os

from flask import Blueprint
from flask_restful import Resource, Api

from user_api.file import file_rw

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

users = file_rw.read_json('user_api/users.json')
print(users)
print(type(users))

class ListUser(Resource):
    def get(self):
        return users

class User(Resource):
    def get(self, id):
        response = None
        for list_item in users:
            if list_item['id'] == id:
                response = list_item
            else:
                response = {
                    'status': 'falha',
                    'mensagem': 'usuário não encontrado'
                    }
        return response

api.add_resource(ListUser, '/users/')
api.add_resource(User, '/users/<int:id>/')

