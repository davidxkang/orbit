from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gabekatz:plantlife@python-orbit.ckxebk8g2hgg.us-west-2.rds.amazonaws.com:5432/postgres'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)

  def __init__(self, username):
    self.username = username

  def __repr__(self):
    return '<User %r>' % self.username


@app.route('/')

def index():
  return "Hello World!"

if __name__ == "__main__":
  app.run()

