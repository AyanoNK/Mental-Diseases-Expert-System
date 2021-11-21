#!/usr/bin/python
# coding: utf-8
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from flask_sqlalchemy import SQLAlchemy
from calculate import calculate_registry


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost/expert"
db = SQLAlchemy(app)


class Enfermedad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return '<name %r>' % self.name


class Consultas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_1 = db.Column(db.Boolean, nullable=False)
    question_2 = db.Column(db.Boolean, nullable=False)
    question_3 = db.Column(db.Boolean, nullable=False)
    question_4 = db.Column(db.Boolean, nullable=False)
    question_5 = db.Column(db.Boolean, nullable=False)
    question_6 = db.Column(db.Boolean, nullable=False)
    question_7 = db.Column(db.Boolean, nullable=False)
    question_8 = db.Column(db.Boolean, nullable=False)
    question_9 = db.Column(db.Boolean, nullable=False)
    question_10 = db.Column(db.Boolean, nullable=False)
    question_11 = db.Column(db.Boolean, nullable=False)
    question_12 = db.Column(db.Boolean, nullable=False)
    question_13 = db.Column(db.Boolean, nullable=False)
    enfermedad_id = db.Column(db.ForeignKey('enfermedad.id'))

    def __repr__(self):
        return '<Consulta %r>' % self.id


# 200 OK
# 201 Created
# 400 Bad Request
# 500 Internal Server Error <- error suyo

def validate_entry(content):
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
    return None


def get_enfermedad(name):
    known_disease = Enfermedad.query.filter_by(name=name).first()
    if not known_disease:
        new_disease = Enfermedad(name=name)
        db.session.add(new_disease)
        db.session.commit()
        return new_disease
    return known_disease


@app.route('/', methods=['POST'])
def entry_point():
    content = request.data.decode("UTF-8")
    content = json.loads(content)

    # revisar que por lo menos una pregunta sea verdadera
    validate_content = validate_entry(content)
    if validate_content:
        return validate_content

    # Revisar si ya está el registro
    check_consulta = Consultas.query.filter_by(
        question_1=content['question_1'],
        question_2=content['question_2'],
        question_3=content['question_3'],
        question_4=content['question_4'],
        question_5=content['question_5'],
        question_6=content['question_6'],
        question_7=content['question_7'],
        question_8=content['question_8'],
        question_9=content['question_9'],
        question_10=content['question_10'],
        question_11=content['question_11'],
        question_12=content['question_12'],
        question_13=content['question_13'],
    ).first()

    if not check_consulta:
        calculated_response = calculate_registry(content)
        new_disease = get_enfermedad(calculated_response['Enfermedad'])
        new_consult = Consultas(question_1=content['question_1'],
                                question_2=content['question_2'],
                                question_3=content['question_3'],
                                question_4=content['question_4'],
                                question_5=content['question_5'],
                                question_6=content['question_6'],
                                question_7=content['question_7'],
                                question_8=content['question_8'],
                                question_9=content['question_9'],
                                question_10=content['question_10'],
                                question_11=content['question_11'],
                                question_12=content['question_12'],
                                question_13=content['question_13'],
                                enfermedad_id=new_disease.id)
        db.session.add(new_consult)
        db.session.commit()
        return calculated_response
    # get the enfermedad name from
    known_disease = Enfermedad.query.filter_by(
        id=check_consulta.enfermedad_id).first()
    return {'Enfermedad': known_disease.name}


if __name__ == '__main__':
    app.run(debug=True)
