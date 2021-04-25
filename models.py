from main import db
from random import randint

class ProxyModel(object):

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


class Client(db.Model, ProxyModel):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(250),)
    name = db.Column(db.String(50))
    identifier = db.Column(db.String(20), unique=True)
    
    def __init__(self, url, name, identifier):
        self.url = url
        self.name = name
        self.identifier = identifier

    def __repr__(self):
        return '<id %s %s>' % (self.id, self.name)


class Account(db.Model, ProxyModel):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey(Client.id), primary_key=True)
    identifier = db.Column(db.String(10), unique=True)
    account_type = db.Column(db.Enum(u'Ahorro', u'Corriente'), default=u'Corriente')
    balance = db.Column(db.Numeric(10,2))
    
    def __init__(self, client_id, balance, account_type):
        self.balance = balance
        self.client_id = client_id
        self.account_type = account_type
        if not self.id:
            self.identifier = str(self.generate_account_number())

    def generate_account_number(self):
        return randint(0, (10**9)-1)

    def get_balance_as_string(self):
        return str(self.balance)

    def __repr__(self):
        return '<# %s Balance %d>' % (self.identifier, self.balance)