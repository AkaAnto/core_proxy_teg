from main import db
from random import randint


class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(250),)
    name = db.Column(db.String(50))
    identifier = db.Column(db.String(20), unique=True)
    
    def __init__(self, url, name, identifier):
        self.url = url
        self.name = name
        self.identifier = identifier

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<id %s %s>' % (self.id, self.name)


class Account(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey(Client.id), primary_key=True)
    identifier = db.Column(db.String(10), unique=True)
    account_type = db.Column(db.Enum(u'Ahorro', u'Corriente'), default=u'Corriente')
    balance = db.Column(db.Numeric(10,2))
    
    def __init__(self, client_id, balance, account_type):
        self.balance = balance
        self.client_id = client_id
        self.account_type = account_type

    def save(self):
        self.identifier = str(self.generate_account_number())
        db.session.add(self)
        db.session.commit()

    def generate_account_number():
        return randint(10**(9), (10**9)-1)

    def __repr__(self):
        return '<# %s Balance %d>' % (self.identifier, self.balance)