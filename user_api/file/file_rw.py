''' 
Descricao :
	Arquivo responsavel por manipular os arquivos json da aplicação
Aluno :
	Fabiano Amaral Alves
Data :
	22 / 07 / 2021
'''

import json
import os, sys

def write_json(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def read_json(filename):
    data = None
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    if data != None:
        return data