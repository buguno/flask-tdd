from flask import Flask
from flask_restful import Api

from resources import hello

app = Flask(__name__)
api = Api(app)

api.add_resource(hello.Hello, "/")

if __name__ == "__main__":
    app.run(debug=True)
