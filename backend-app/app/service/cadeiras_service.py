from app.model.cadeiras_model import Cadeiras
from app.extensions import db

def save_changes():
    db.session.add(data)
    db.session.commit()

def criar_cadeiras(data):
    nova_cadeira = Cadeiras(
        nome=data['nome'],
    )
    save_changes(nova_cadeira)
    return{"id": nova_cadeira.id}

def listar_todas_cadeiras():
    return Cadeiras.query.all()

def editar_cadeiras(id, data):
    cadeiras = Cadeiras.query.filter_by(id=id).first()
    cadeiras.nome = data['nome']
    save_changes(cadeiras)
    return{"id": cadeiras.id}

def excluir_cadeiras(id):
    cadeiras = Cadeiras.query.get(id)
    db.session.delete(categoria)
    db.session.commit()
    return { "id": categoria.id }