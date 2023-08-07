from app.model.unidade_model import Unidade
from app.extensions import db

def save_changes():
    db.session.add(data)
    db.session.commit()

def criar_unidade(data):
    nova_unidade = Unidade(
        n_unidade=data['n_unidade'],
    )
    save_changes(nova_unidade)
    return{"id": nova_unidade.id}

def listar_todas_unidade():
    return Unidade.query.all()

def editar_unidade(id, data):
    unidade = Unidade.query.filter_by(id=id).first()
    unidade.n_unidade = data['n_unidade']
    save_changes(unidade)
    return{"id": unidade.id}

def excluir_unidade(id):
    unidade = Unidade.query.get(id)
    db.session.delete(categoria)
    db.session.commit()
    return { "id": categoria.id }