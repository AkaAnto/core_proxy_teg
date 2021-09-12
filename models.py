from main import db
from random import randint
from decimal import *


class ProxyModel(object):

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


class Client(db.Model, ProxyModel):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
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

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    client_id = db.Column(db.Integer, db.ForeignKey(Client.id), primary_key=True, unique=True)
    identifier = db.Column(db.String(10), unique=True)
    account_type = db.Column(db.Enum(u'Ahorro', u'Corriente', name=u'type_account'), default=u'Corriente')
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
        return '<# %s Cuenta %d>' % (self.identifier, self.get_balance_as_string())


class AccountTransaction(db.Model, ProxyModel):
    __tablename__ = 'account_transaction'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    sender_account_id = db.Column(db.Integer, db.ForeignKey(Account.id), primary_key=True)
    reciever_account_id = db.Column(db.Integer, db.ForeignKey(Account.id), primary_key=True)
    identifier = db.Column(db.String(10), unique=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    account_transaction_type = db.Column(db.Enum(u'P2P', u'P2B', name='transaction_type'), default=u'P2B')
    amount = db.Column(db.Numeric(10,2))
    details = db.Column(db.String(100), default="No details")
    
    def __init__(self, sender_account_id, reciever_account_id, account_transaction_type, amount, details="No details"):
        self.sender_account_id = sender_account_id
        self.reciever_account_id = reciever_account_id
        self.account_transaction_type = account_transaction_type
        self.amount = amount
        self.details = details

    def generate_transaction_number(self):
        return randint(0, (10**9)-1)

    def get_amount_as_string(self):
        return str(self.amount)

    def save(self):
        if not self.id:
            self.identifier = str(self.generate_transaction_number())
            if self.execute_transaction():
                super().save()
        else:
            self.amount = self.get_amount_as_string()

    def execute_transaction(self):
        try:
            sender_account = Account.query.filter_by(id=self.sender_account_id).first()
            reciever_account = Account.query.filter_by(id=self.reciever_account_id).first()
            sender_account.balance = Decimal(sender_account.balance) - Decimal(self.amount)
            sender_account.save()
            reciever_account.balance = Decimal(reciever_account.balance) + Decimal(self.amount)
            reciever_account.save()
            return True
        except Exception as e:
            raise Exception("Problem executing transaction: %s" % str(e))

    def __repr__(self):
        return '# %s Transferencia %s' % (self.identifier, self.get_amount_as_string())