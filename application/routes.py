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

@app.route('/recipe-<int:rid>')
def recipe(rid):
    recipe = Recipes.query.filter_by(recipe_id=rid).first()
    maxid = Recipes.query.order_by(Recipes.recipe_id.desc()).first().recipe_id
    return render_template('recipe.html', recipe=recipe, maxid=maxid)


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
    recipes = Recipes.query.all()
    for recipe in recipes:
        form.recipe.choices.append((recipe.recipe_id, recipe.recipe_name))
    if request.method == 'POST':
        ing_quant = form.i_name.data
        recipe_id = form.recipe.data
        ingredient = Ingredients(ingredient_name_quantity = ing_quant)
        db.session.add(ingredient, recipe_id)
        db.session.commit()
        return redirect(url_for('add_i'))
    return render_template('add_ingredient.html', form=form)


@app.route('/add-instructions/<int:rid>', methods=['GET', 'POST'])
def add_inst(rid):
    form = AddInstructions()
    if request.method == 'POST':
        step = form.step.data
        instruction = form.step.data
        rid = Recipes.query.filter_by(id=instruction.recipe_id).first().recipe_id
        db.session.commit()
        return redirect(url_for('recipe', rid=rid))
    return render_template('update_options.html', form=form)


