from flask import Flask, request, jsonify
# from models.user import User
# from models.meal import Meal
from database import db

app = Flask(__name__)
# # app.config['SECRET_KEY'] = "your_secret_key"

# db.init_app(app)

@app.route("/")
def helloWorld():
    return "Hello world"


if __name__ == '__main__':
  app.run(debug=True)