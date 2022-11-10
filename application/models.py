from application import db


class Recipes(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50))
    recipe_time = db.Column(db.Integer)
    servings = db.Column(db.Integer)
    recipe_instruction = db.relationship('Instructions', backref='recInstructBr')
    recipe_ingredients = db.relationship('Recipes_Ingredients', backref='recIngBr')


class Instructions(db.Model):
    instruction_id = db.Column(db.Integer, primary_key=True)
    instruction = db.Column(db.String(1000))
    step = db.Column(db.String(10))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))

class Ingredients(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(20))
    ingredient_recipe = db.relationship('Recipes_Ingredients', backref='ingRecBr')


class Recipes_Ingredients(db.Model):
    recipe_ingredient_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.String(50))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'))
    




