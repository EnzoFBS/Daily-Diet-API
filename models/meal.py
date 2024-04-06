import datetime
from database import db

class Meal(db.Model):
  # id (int), username (text), password (text), role (text)
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  description = db.Column(db.String(200), nullable=False)
  date_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
  is_included_in_diet = db.Column(db.Boolean, default=False)

