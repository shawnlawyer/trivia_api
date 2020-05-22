from app import db

class Category(db.Model):

    __tablename__ = 'Categories'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)

    _default_fields = [
        "type",
    ]

    def __init__(self, type):
        self.type = type

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def format(self):
        return {
            'id': self.id,
            'type': self.type
        }

    def __repr__(self):
        return '<Category %r>' % self.name
