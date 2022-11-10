from application import app, db
from application.forms import AddRecipe
from application.models import Recipes, Instructions, Ingredients, Recipes_Ingredients
from flask import render_template, request, redirect, url_for

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/recipes')
def questions():
    recipes = Recipes.query.all()
    return render_template('recipes.html', recipes=recipes)

@app.route('/add-recipe', methods= ['GET', 'POST'])
def add_recipe():
    form = AddRecipe()
    if request.method == 'POST':
        name = form.recipe_name.data
        recipe = Recipes(recipe_name = name)
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('add_r'))
    return render_template('add_recipe.html', form=form)