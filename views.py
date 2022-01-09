from decimal import *
from models import Client, Account, AccountTransaction



class ClientView(object):

    @staticmethod
    def get_client_with_identifier(identifier):
        return Client.query.filter_by(identifier=identifier).first()

    @staticmethod
    def add_client(request_data):
        name = request_data.get('name')
        identifier = request_data.get('identifier')
        new = Client(url='www.notfound.com', name=name, identifier=identifier)
        new.save()
        return new


class AccountView(object):

    @staticmethod
    def get_account_with_identifier(identifier):
        account = Account.query.filter_by(identifier=identifier).first()
        account.balance = account.get_balance_as_string()
        return account

    @staticmethod
    def add_account(request_data):
        client_identifier = request_data.get('client_identifier')
        client = ClientView.get_client_with_identifier(client_identifier)
        balance = request_data.get('balance')
        account_type = request_data.get('account_type')
        new = Account(client_id=client.id, balance=balance, account_type=account_type)
        new.save()
        response = {'balance': new.get_balance_as_string(), 'client': client_identifier, 
                    'type': new.account_type, 'number': new.identifier}
        return response


class AccountTransactionView(object):

    @staticmethod
    def get_transaction_with_identifier(identifier):
        transaction = AccountTransaction.query.filter_by(identifier=identifier).first()
        sender = Account.query.filter_by(id=transaction.sender_account_id).first()
        reciever = Account.query.filter_by(id=transaction.reciever_account_id).first()
        response = {'type': transaction.account_transaction_type, 'sender':sender.identifier, 
        'reciever': reciever.identifier, 'amount': transaction.get_amount_as_string(),
        'created': transaction.created, 'details': transaction.details}
        return response

    @staticmethod
    def validate_transaction(sender_account, amount):
        return Decimal(sender_account.balance) > Decimal(amount)

    @staticmethod
    def add_transaction(request_data):
        sender_account_identifier = request_data.get('sender_account_number')
        sender_account = AccountView.get_account_with_identifier(sender_account_identifier)
        reciever_account_identifier = request_data.get('reciever_account_number')
        reciever_account = AccountView.get_account_with_identifier(reciever_account_identifier)
        account_transaction_type = request_data.get('account_transaction_type')
        amount = Decimal(request_data.get('amount'))
        details = request_data.get('details')
        if AccountTransactionView.validate_transaction(sender_account, amount):
            new = AccountTransaction(sender_account_id=sender_account.id, reciever_account_id=reciever_account.id, 
                                    account_transaction_type=account_transaction_type, amount=amount, details=details)
            new.save()
            response = {'amount': new.get_amount_as_string(), 'sender': sender_account_identifier, 
                        'reciever': reciever_account_identifier, 'number': new.identifier}
        else:
            response = {'message': 'Problem creating transaction'}
        return response
