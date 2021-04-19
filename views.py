from models import Client

class ClientView(object):

    @staticmethod
    def get_client_with_identifier(identifier):
        return Client.query.filter_by(identifier=identifier).first()

    @staticmethod
    def add_client(name, identifier):
        new = Client(url='www.notfound.com', name=name, identifier=identifier)
        new.save()