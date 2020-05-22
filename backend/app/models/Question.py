from app import db

class Question(db.Model):

    __tablename__ = 'Questions'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    answer = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('Categories.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('questions'))
    difficulty = db.Column(db.Integer)

    _default_fields = [
        "question",
    ]

    def __init__(self, question, answer, category_id, difficulty):
        self.question = question
        self.answer = answer
        self.category_id = category_id
        self.difficulty = difficulty

    def format(self):
        return {
          'id': self.id,
          'question': self.question,
          'answer': self.answer,
          'category_id': self.category.id,
          'category': self.category.type,
          'difficulty': self.difficulty
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<Question %r>' % self.id
