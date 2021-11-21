#!/usr/bin/python
# coding: utf-8
from flask import Flask, request, Response, jsonify
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


# 200 OK
# 201 Created
# 400 Bad Request
# 500 Internal Server Error <- error suyo

@app.route('/', methods=['POST'])
def entry_point():
    content = request.data.decode("UTF-8")

    content = json.loads(content)
    # revisar que por lo menos una pregunta sea verdadera
    answer = {
        "Enfermedad": None
    }

    if content is None or not content:
        return jsonify(Enfermedad='No hay datos.')

    questions = [
        'question_1',
        'question_2',
        'question_3',
        'question_4',
        'question_5',
        'question_6',
        'question_7',
        'question_8',
        'question_9',
        'question_10',
        'question_11',
        'question_12',
        'question_13'
    ]

    if not all([True if item in content else False for item in questions]):
        return jsonify(Error="Faltan datos.")

    if content['question_1']:
        if content['question_2'] or content['question_3']:
            if content['question_2']:
                return {'Enfermedad': 'Psicosis derivada de una condición médica general'}
            if content['question_3']:
                return {'Enfermedad': 'Psicosis inducida por sustancias'}
        elif content['question_4']:
            if not content['question_7'] or content['question_9']:
                if content['question_8']:
                    return {'Enfermedad': 'Esquizofrenia'}
                else:
                    return {'Enfermedad': 'Transtorno esquizofreniforme'}
            else:
                if content['question_10']:
                    return {'Enfermedad': 'Trastorno esquizoafectivo'}
                else:
                    return {'Enfermedad': 'Trastorno del estado de ánimo con psicosis'}
        else:
            if content['question_5']:
                if content['question_11']:
                    if content['question_13']:
                        return {'Enfermedad': 'Trastorno delirante'}
                    else:
                        return {'Enfermedad': 'Psicosis sin especificar'}
                else:
                    if content['question_12']:
                        return {'Enfermedad': 'Trastorno del estado de ánimo con psicosis'}
                    else:
                        return {'Enfermedad': 'Psicosis sin especificar'}

            else:
                if content['question_6']:
                    return {'Enfermedad': 'Trastorno de psicosis breve'}
                else:
                    return {'Enfermedad': 'Psicosis sin especificar'}
    else:
        answer["Enfermedad"] = "No aplica"


if __name__ == '__main__':
    app.run(debug=True)
