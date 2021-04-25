from flask import request
from flask import json
from main import app
from views import ClientView, AccountView

@app.route('/health')
def health():
    response = app.response_class(
        response=json.dumps({'message': 'ok'}),
        status=200,
        mimetype='application/json'
    )
    return response

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
        try:
            ClientView.add_client(data)
            response = app.response_class(
                response=json.dumps(data),
                status=201,
                mimetype='application/json'
            )
        except Exception as e:
            data = {'exception': str(e)}
            response = app.response_class(
                response=json.dumps(data),
                status=400,
                mimetype='application/json'
            )
    return response

@app.route('/account/<identifier>', methods=['GET'])
def account_detail(identifier):
    account = AccountView.get_account_with_identifier(identifier)
    data = {'type': account.account_type, 'balance': account.balance}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/account', methods=['POST'])
def account_create():
    if request.method == 'POST':
        data = request.get_json()
        try:
            new = AccountView.add_account(data)
            response = app.response_class(
                response=json.dumps(new),
                status=201,
                mimetype='application/json'
            )
        except Exception as e:
            data = {'exception': str(e)}
            response = app.response_class(
                response=json.dumps(data),
                status=400,
                mimetype='application/json'
            )
    return response

app = app