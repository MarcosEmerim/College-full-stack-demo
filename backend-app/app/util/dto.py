from flask_restx import Namespace, fields


class cadeirasDto:
    api = Namespace('cadeiras', description='cadeiras related operations')
    user = api.model('cadeiras_details', {
        'nome': fields.String(required=True, description='nome'),
        'creditos': fields.Integer(required=True, description='creditos'),
        'unidade_id': fields.Integer(description='unidade')
    })

class unidadeDto:
    api = Namespace('unidade', description='unidade related operations')
    user_auth = api.model('unidade_details', {
        'n_unidade': fields.Integer(required=True, description='n_unidade'),
        'cidade': fields.String(required=True, description='cidade'),
        'cadeiras_id': fields.Nested(fields.Integer(required=True), as_list=True),
    })