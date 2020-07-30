from app import db

class HelloWorld(db.Model):
  id = db.Column(db.Integer, primary_key=True)