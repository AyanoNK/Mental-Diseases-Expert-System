#!/usr/bin/python
# coding: utf-8
from flask import Flask, request, Response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# 200 OK
# 201 Created
# 400 Bad Request
# 500 Internal Server Error <- error suyo

@app.route('/', methods=['GET'])
def entry_point():
    content = request.get_json(silent=True)
    # revisar que por lo menos una pregunta sea verdadera
    if content is None:
        return Response("gonorrea", status=400, mimetype='application/json')

    return {'Hola': 'mundo'}


if __name__ == '__main__':
    app.run(debug=True)
