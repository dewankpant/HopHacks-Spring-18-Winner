#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from api import func

app = Flask(__name__)
api = Api(app)


class books(Resource):
    def get(self,query):
        return jsonify(func(query))

api.add_resource(books, '/books/<query>') # Route_1


if __name__ == '__main__':
     app.run()
