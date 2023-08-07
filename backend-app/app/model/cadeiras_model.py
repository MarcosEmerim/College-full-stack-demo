from app import db

class Cadeiras(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "cadeiras"

    # TODAS AS TABELAS TEM ESSA COLUNA
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    nome = db.Column(db.String(255), unique=True, nullable=False)
    creditos = db.Column(db.Integer, nullable=False)

    unidades = db.relationship('Unidade', secondary='RelacaoCadeiraUnidade', back_populates='cadeiras', uselist=True)

    def __init__(self, nome, creditos):
        self.nome = nome
        self.creditos = creditos
        #self.unidade_id = unidade_id
        
    def __repr__(self):
        return "<cadeiras '{}'>".format(self.nome)

class RelacaoCadeiraUnidade(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "relacaoCadeiraUnidade"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unidade_id = db.Column(db.Integer, db.ForeignKey('unidade.id'), nullable=False)
    cadeiras_id = db.Column(db.Integer, db.ForeignKey('cadeiras.id'), nullable=False)

    def __init__(self, cadeiras_id, unidade_id):
        self.cadeiras_id = cadeiras_id
        self.unidade_id = unidade_id
        
    def __repr__(self):
        return "<Cadeira '{}'>".format(self.nome)
