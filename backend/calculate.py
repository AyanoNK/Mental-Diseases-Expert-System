from flask import jsonify


def calculate_registry(content):

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
        return {'Enfermedad': "No aplica"}
