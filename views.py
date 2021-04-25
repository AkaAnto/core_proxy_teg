from models import Client, Account


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