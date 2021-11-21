

class TransactionBlock():
    __tablename__ = 'transaction_block'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey(AccountTransaction.id), primary_key=True, unique=True)
    transaction_hash = db.Column(db.String(300), unique=True)
    previous_block_hash = db.Column(db.String(300), unique=True)
    block_hash = db.Column(db.String(300), unique=True)
    index = db.Column(db.String(10), unique=True)
    timestamp = db.Column(db.String(20), unique=True)

    def __init__(self, transaction):

        if not self.id:
            self.identifier = str(self.generate_account_number())

    def get_block_hash(self):
        block = {
         'id': self.id,
         'transaction_id': self.transaction_id,
         'index': self.index,
         'timestamp': self.timestamp,
         'previous_hash': self.previous_hash,
        }
        hex_hash = TransactionBlock.json_hash(block)
        return hex_hash

    @staticmethod
    def get_transaction_hash(transaction):
        transaction_json = {
         'sender_account_id': transaction.sender_account_id,
         'sender_account_id': transaction.sender_account_id,
        }
        hex_hash = TransactionBlock.json_hash(transaction_json)
        return hex_hash

    @staticmethod
    def json_hash(json_data):
        string_object = json.dumps(json_data, sort_keys=True)
        block_string = string_object.encode()
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        return hex_hash


    def __repr__(self):
        return '<# %s Cuenta %d>' % (self.identifier, self.get_balance_as_string())
