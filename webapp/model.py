from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mark(db.Model):
    __tablename__ = 'mark'
  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))

    def __repr__(self):
        return '{}'.format(self.name)


class CarModel(db.Model):
    __tablename__ = 'model'
  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    mark_id = db.Column(db.Integer)

    def __repr__(self):
        return '{}'.format(self.name)
