# API REST de Usuários

## Como testar

1. Acesse a [api](https://userapi-web.herokuapp.com/).

2. Utilize o [Insomnia](https://insomnia.rest/download) ou o [Postman](https://www.postman.com/downloads/) para realizar as requisições HTTP.

3. Para consultar um usuário especifico utilize a url `https://userapi-web.herokuapp.com/users/<id>` com o metodo `GET` do `Insomnia` ou `Postman`.

4. Para adicionar um novo usuário, selecione o formato `JSON` no corpo da requisição da ferramenta da sua escolha, informe os dados e o metodo `POST` com a url `https://userapi-web.herokuapp.com/users/` ou `https://userapi-web.herokuapp.com/`.

5. Para editar os dados de algum usuário, selecione o formato `JSON` no corpo da requisição da ferramenta da sua escolha, descreva as alterações e o metodo `PUT` com a url `https://userapi-web.herokuapp.com/users/<id do usuario a ser editado>`.

6. Para deletar um usuário selecione o metodo `DELETE` e informe o id do usuário a ser deletado na url `https://userapi-web.herokuapp.com/users/<id>`.

7. Ao acessar a url `https://userapi-web.herokuapp.com/` serão listados todos os usuários cadastrados.

## Clonando e editando o projeto

1. Faça clone do projeto para a sua maquina.
    ```zsh
        $ git clone https://github.com/faamaral/user_api.git
    ```

2. Com o python instalado em sua maquina, entre no diretorio do projeto clonado e crie um ambiente virtual para o projeto.
    > no Linux siga esses passos.
    - Instale o virtualenv caso não o tenha instalado.

        ```zsh
            $ sudo apt install python3-venv
        ```
    - Crie o ambiente virtual.

        ```zsh
            python3 -m venv nome-do-seu-ambiente-virtual
        ```

    - Ative o ambiente virtual.

        ```zsh
            source nome-do-seu-ambiente-virtual/bin/activate
        ```
    > No windows siga esses passos.
    - Instale o virtualenv caso não o tenha instalado.

        ```
            pip install virtualenv
        ```
    - Crie o seu ambiente virtual.
        ```
            virtualenv nome_do_ambiente_virtual
        ```
    - Ative o ambiente virtual.

        ```
            nome_do_ambiente_virtual/Scripts/Activate
        ```
    A visualização no terminal onde você digitou os comandos deverá se parecer com o seguinte.

    ```zsh
        (nome_do_ambiente_virtual) ~/user/user_api(main) > 
    ``` 

3. Instale as dependencias do projeto.
    > execute o seguinte comando
    ```
        $ pip install -r requirements.txt
    ```
4. Execute a aplicação em sua maquina.

    ```
        python3 run.py
    ```

Agora voce pode modificar e testar a aplicação do projeto normalmente.