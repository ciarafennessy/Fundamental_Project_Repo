from application import db


class Recipes(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), nullable=False)
    recipe_time = db.Column(db.String(50), nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    recipe_instruction = db.relationship('Instructions', backref='recInstructBr')
    recipe_ingredient = db.relationship('Ingredients', backref='recIngredBr')
    

class Instructions(db.Model):
    instruction_id = db.Column(db.Integer, primary_key=True)
    step = db.Column(db.String(10), nullable=False)
    instruction = db.Column(db.String(1000), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))

class Ingredients(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_name_quantity = db.Column(db.String(50), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
  




    




