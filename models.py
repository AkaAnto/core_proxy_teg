from main import db


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