import os
import json

from flask import Blueprint, request
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
    def post(self):
        data = json.loads(request.data)
        index = len(users) + 1
        data['id'] = index
        users.append(data)
        file_rw.write_json('user_api/users.json', users)
        return users[index-1]

class User(Resource):
    def get(self, id):
        response = None
        for list_item in users:
            if list_item['id'] == id:
                response = list_item
                
        return response

    def put(self, id):
        data = json.loads(request.data)
        response = None
        i = 0
        for list_item in users:
            if list_item['id'] == id:
                users[i] = data 
                response = users[i]
            i+=1 
                           
        file_rw.write_json('user_api/users.json', users)
        return response
    
    def delete(self, id):
        response = None
        i = 0
        for list_item in users:
            if list_item['id'] == id:
                users.pop(i) 
                response = {
                    'status': 200,
                    'mensagem': 'usuario excluido com sucesso'
                }
            i+=1 
                           
        file_rw.write_json('user_api/users.json', users)
        return response

    

api.add_resource(ListUser, '/','/users/')
api.add_resource(User, '/users/<int:id>/')

