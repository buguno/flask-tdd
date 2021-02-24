from flask import request
from flask_restful import Resource


class Login(Resource):
    def post(self):
        bodyJson = request.get_json()

        username = bodyJson["data"]["username"]
        password = bodyJson["data"]["password"]

        if username == "admin" and password == "flask":
            return {"menssagem": "sucesso!"}
        else:
            return {"menssagem": "erro!"}
