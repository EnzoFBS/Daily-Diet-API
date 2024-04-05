import datetime
from database import db

class User(db.Model):
  # id (int), username (text), password (text), role (text)
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False, unique=True)
  email = db.Column(db.String(80), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
