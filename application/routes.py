from application import app, db
from application.forms import AddRecipe, AddIngredient, AddInstructions
from application.models import Recipes, Instructions, Ingredients
from flask import render_template, request, redirect, url_for

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/recipes')
def recipes():
    recipes = Recipes.query.all()
    return render_template('recipes.html', recipes=recipes)

@app.route('/add-recipe', methods= ['GET', 'POST'])
def add_recipe():
    form = AddRecipe()
    if request.method == 'POST':
        name = form.recipe_name.data
        time = form.recipe_time.data
        serving = form.servings.data
        recipe = Recipes(recipe_name = name, recipe_time = time, servings = serving)
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('add_i'))
    return render_template('add_recipe.html', form=form)

@app.route('/add-ingredients', methods=['GET', 'POST'])
def add_i():
    form = AddIngredient()
    recipes = Recipes.query.order_by(Recipes.recipe_id.desc()).all()
    for recipe in recipes:
        form.recipe.choices.append((recipe.recipe_id, recipe.recipe_name))
    if request.method == 'POST':
        ing_quant = form.i_name.data
        recipe_id = form.recipe.data
        ingredient = Ingredients(ingredient_name_quantity = ing_quant, recipe_id = recipe_id)
        db.session.add(ingredient)
        db.session.commit()
        return redirect(url_for('add_i'))
    return render_template('add_ingredient.html', form=form)


@app.route('/add-instructions', methods=['GET', 'POST'])
def add_inst():
    form = AddInstructions()
    recipes = Recipes.query.order_by(Recipes.recipe_id.desc()).all()
    for recipe in recipes:
        form.recipe.choices.append((recipe.recipe_id, recipe.recipe_name))
    if request.method == 'POST':
        stp = form.step.data
        inst = form.instruction.data
        recipe_id = form.recipe.data
        instruction = Instructions(step = stp, instruction = inst, recipe_id = recipe_id)
        db.session.add(instruction)
        db.session.commit()
        return redirect(url_for('add_inst'))
    return render_template('add_instruction.html', form=form)




