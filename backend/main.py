#!/usr/bin/python
# coding: utf-8
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def entry_point():
    return {'Hola': 'mundo'}


if __name__ == '__main__':
    app.run(debug=True)
