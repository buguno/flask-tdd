from flask import Flask
from flask_restful import Api

from resources import hello, login

app = Flask(__name__)
api = Api(app)

api.add_resource(hello.Hello, "/")
api.add_resource(login.Login, "/login")

if __name__ == "__main__":
    app.run(debug=True)
