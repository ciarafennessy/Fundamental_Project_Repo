from application import app, db
from application.forms import AddRecipe, AddIngredient, AddInstructions, UpdateInstructions, SelectRecipe
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

@app.route('/update-instructions/<int:instid>', methods=['GET', 'POST'])
def update_inst(instid):
    form = UpdateInstructions()
    if request.method == 'POST':
        inst_step = form.inst_step.data
        inst = form.inst.data
        instruct_id = instid
        instruct = Instructions.query.filter_by(instruction_id = instid).first()
        rid = Recipes.query.filter_by(recipe_id=instruct.recipe_id).first().recipe_id
        instruct.step = inst_step
        instruct.instruction = inst
        db.session.commit()
        return redirect(url_for('recipe', rid=rid))
    return render_template('update_instructions.html', form=form)
    
@app.route('/choose-recipe', methods=['GET', 'POST'])
def select_recipe():
    form = SelectRecipe()
    for recipe in Recipes.query.all():
        form.recipe_id.choices.append((recipe.recipe_id, recipe.recipe_name))
        if request.method == 'POST':
            rid = form.recipe_id.data
            return redirect(url_for('recipe', rid=rid))
    return render_template('select_recipe.html', form=form)

@app.route('/delete-recipe/<int:rid>')
def delete_recipe(rid):
    recipe = Recipes.query.filter_by(recipe_id=rid).first()
    instructions = recipe.recipe_instruction
    ingredients = recipe.recipe_ingredient
    db.session.delete(recipe)
    for instruction in instructions:
        db.session.delete(instruction)
    for ingredient in ingredients:
        db.session.delete(ingredient)
    db.session.commit()
    return redirect(url_for('recipes'))



