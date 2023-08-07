from flask import request
from flask_restx import Resource

from app.util.dto import cadeirasDto
from app.service.cadeiras_service import listar_todas_cadeiras, criar_cadeiras, editar_cadeiras, excluir_cadeiras

api = cadeirasDto.api

@api.route('/')
class cadeiras(Resource):
    def post(self):
        data = request.json
        return criar_cadeiras(data)

    @api.marshal_list_with(cadeirasDto, envelope='data')
    def get(self):
        return listar_todas_cadeiras()


@api.route('/<id_cadeiras>')
@api.param('id_cadeiras', 'id da cadeiras')
class CategoriaComId(Resource):
    def put(self, id_cadeiras):
        data = request.json
        return editar_cadeiras(id_cadeiras, data)

    def delete(self, id_cadeiras):
        return excluir_cadeiras(id_cadeiras)