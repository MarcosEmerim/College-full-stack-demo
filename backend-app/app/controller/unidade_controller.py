from flask import request
from flask_restx import Resource

from app.util.dto import unidadeDto
from app.service.unidade_service import listar_todas_unidade, criar_unidade, editar_unidade, excluir_unidade

api = unidadeDto.api
#_unidade = unidadeDto.unidade

@api.route('/')
class unidade(Resource):
    def post(self):
        data = request.json
        return criar_unidade(data)

    @api.marshal_list_with(unidadeDto, envelope='data')
    def get(self):
        return listar_todas_unidade()


@api.route('/<id_unidade>')
@api.param('id_unidade', 'id da unidade')
class unidadeComId(Resource):
    def put(self, id_unidade):
        data = request.json
        return editar_unidade(id_unidade, data)    

    def delete(self, id_unidade):
        return excluir_unidade(id_unidade)

