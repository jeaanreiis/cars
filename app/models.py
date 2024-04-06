from . import db


class Cars(db.Model):
    __tablename__ = 'vendas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True)
    modelo = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    valor = db.Column(db.String)
    descricao = db.Column(db.Text)
    anexo = db.Column(db.String(50))
    buy = db.relationship('Buy', backref='vendas')


class Buy(db.Model):
    __tablename__ = 'compras'

    id = db.Column(db.Integer, primary_key=True)
    carro_id = db.Column(db.Integer, db.ForeignKey('vendas.id'))
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(14), unique=True)
    telefone = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return '<Compra %r>' % self.nome
