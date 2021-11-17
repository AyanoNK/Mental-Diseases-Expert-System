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

    answer = {"Enfermedad" : None}

    if content is None:
        return Response("gonorrea", status=400, mimetype='application/json')
    else:
        # Las preguntas ya implican que question_1 es verdadero 
        if content[question_2]:
            answer["Enfermedad"] = "Psicosis derivada de una condición médica general"
        elif content[question_3]:
            answer["Enfermedad"] = "Psicosis inducina por sustancias"

        # Las preguntas question_7 a question_10 ya implican que question_4 es verdadero 
        if content[question_7] == False or content[question_9]:
            if content[question_8]:
                answer["Enfermedad"] = "Esquizofrenia"
            else:
                answer["Enfermedad"] = "Trastorno esquizofreniforme"
        elif content[question_9]== False :
            if content[question_10]: # question_7: dos semanas de psicosis positiva
                answer["Enfermedad"] = "Trastorno psicoafectivo"
            else:
                answer["Enfermedad"] = "Trastorno del estado de ánimo con psicosis"

        # Las preguntas question_11 a question_13 ya implican que question_5 es verdadero 
        if content[question_11]:
            if content[question_13]:
                answer["Enfermedad"] = "Trastorno delirante"
            else:
                answer["Enfermedad"] = "Psicosis sin especificar"
        else:
            if content[question_12]:
                answer["Enfermedad"] = "Trastorno del estado de ánimo con psicosis"
            else:
                answer["Enfermedad"] = "Psicosis sin especificar"

        if content[question_6]:
            answer["Enfermedad"] = "Trastorno de psicosis breve"
        else:
            answer["Enfermedad"] = "Psicosis sin especificar"

    return answer

    #return {'Hola': 'mundo'}


if __name__ == '__main__':
    app.run(debug=True)
