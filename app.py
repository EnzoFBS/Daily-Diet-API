from flask import Flask, request, jsonify
# from models.user import User
from models.meal import Meal
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/daily-diet-flask'
db.init_app(app)  


@app.route("/")
def helloWorld():
    return "Hello world"
  
  
@app.route("/diet", methods=["POST"])
def create_diet():
  data = request.json
  name = data.get("name")
  description = data.get("description")
  print(f"dados recebidos: {data}")
  
  if name and description:
    meal = Meal(name = name, description = description)
    db.session.add(meal)
    db.session.commit()
    return jsonify({"message": "Refeição cadastrada com sucesso"})
  
  return jsonify({"message": "Dados invalidos"}), 400

  
  
@app.route("/diet", methods=["GET"])
def get_all_diets():
  totalDiets = Meal.query.all()
  print(totalDiets)
  
  if totalDiets:
    diet_list = []
    for diet in totalDiets:
        diet_data = {
            "id": diet.id,
            "name": diet.name,
            "description": diet.description,
            "is_included_in_diet": diet.is_included_in_diet
        } 
        diet_list.append(diet_data)
        
        
    return jsonify(diet_list)

  return jsonify({"message": "Dados invalidos"}), 400

@app.route("/diet/<int:id_meal>", methods=["GET"])
def getMealById(id_meal):
  meal = Meal.query.get(id_meal)
  
  if meal:
    return {
      "name" : meal.name,
      "description": meal.description,
      "is_included_in_diet": meal.is_included_in_diet
    }
  return jsonify({"message": "Meal not found"}), 404 


@app.route("/diet/<int:id_meal>", methods=["DELETE"])
def deleteMeal(id_meal):
  meal = Meal.query.get(id_meal)
  
  if meal:
    db.session.delete(meal)
    db.session.commit()
    return jsonify({"message": f"A dieta de {meal.name} foi deletada com sucesso"})
  
  return jsonify({"message": "Dieta não encontrada"}), 404


@app.route("/diet/<int:id_meal>", methods=["PUT"])
def updateMeal(id_meal):
  data = request.json
  meal = Meal.query.get(id_meal)
  
  if data and meal:
    meal.name = data.get("name")
    meal.description = data.get("description")
    meal.is_included_in_diet = data.get("is_included_in_diet", meal.is_included_in_diet)
    
    db.session.commit()
    return jsonify({"message": f"Dieta {id_meal} atualizado com sucesso"})
  
  return jsonify({"message": "Dieta não encontrada"}), 404
    
 
  
  
   


if __name__ == '__main__':
  app.run(debug=True)