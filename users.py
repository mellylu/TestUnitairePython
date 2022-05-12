from settings import *
import json

db = SQLAlchemy(app)

class User(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sexe = db.Column(db.String(1), nullable=False)

    def __init__(self, name, age, sexe):
        self.name = name
        self.age = age
        self.sexe = sexe

    def json(self):
        return {'id': self.id, 'name': self.name,
                'age': self.age, 'sexe': self.sexe}

    def add_user( _name, _age, _sexe):
        new_user = User(name=_name, age=_age, sexe=_sexe)
        db.session.add(new_user)
        db.session.commit()

    def get_all_users():
        return [User.json(user) for user in User.query.all()]

    def get_user(_id):
        return [User.json(User.query.filter_by(id=_id).first())]

    def update_user(_id, _name, _age, _sexe):
        user_to_update = User.query.filter_by(id=_id).first()
        user_to_update.name = _name
        user_to_update.age = _age
        user_to_update.sexe = _sexe
        db.session.commit()

    def delete_user(_id):
        User.query.filter_by(id=_id).delete()
        db.session.commit()