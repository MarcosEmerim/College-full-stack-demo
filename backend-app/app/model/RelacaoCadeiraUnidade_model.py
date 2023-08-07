from app import db

class RelacaoCadeiraUnidade(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "relacaoCadeiraUnidade"

    unidade_id = db.Column(db.Integer, db.ForeignKey('unidade.id'), nullable=False)
    cadeiras_id = db.Column(db.Integer, db.ForeignKey('cadeiras.id'), nullable=False)

    def __init__(self, cadeiras_id, unidade_id):
        self.cadeiras_id = cadeiras_id
        self.unidade_id = unidade_id
        
    def __repr__(self):
        return "<Cadeira '{}'>".format(self.nome)
