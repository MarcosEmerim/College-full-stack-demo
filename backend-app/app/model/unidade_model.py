from app import db

class Unidade(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "unidade"

    # TODAS AS TABELAS TEM ESSA COLUNA
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    cidade = db.Column(db.String(255), unique=True, nullable=False)
    n_unidade = db.Column(db.Integer, nullable=False)

    cadeiras = db.relationship('cadeiras', secondary='RelacaoCadeiraUnidade', back_populates='unidades', uselist=True)

    def __init__(self, cidade, n_unidade):
        self.cidade = cidade
        self.n_unidade = n_unidade
        #self.unidade_id = unidade_id
        
    def __repr__(self):
        return "<unidade '{}'>".format(self.n_unidade)