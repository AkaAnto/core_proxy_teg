from flask import request
from flask import json
from main import app
from views import ClientView

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/client/<identifier>', methods=['GET'])
def client_detail(identifier):
    client = ClientView.get_client_with_identifier(identifier)
    data = {'name': client.name, 'identifier': client.identifier}
    response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    return response

@app.route('/client', methods=['POST'])
def client_create():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        identifier = data.get('identifier')
        ClientView.add_client(name=name, identifier=identifier)
        response = app.response_class(
            response=json.dumps(data),
            status=201,
            mimetype='application/json'
        )
    return response

app = app