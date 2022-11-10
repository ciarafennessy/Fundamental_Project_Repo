from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired


class AddRecipe(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired(message="You must supply a recipe name.")])
    recipe_time = StringField('Recipe Time', validators=[DataRequired(message="You must supply a recipe time.")])
    servings = IntegerField('Servings', validators=[DataRequired(message="You must supply an estimated number of servings.")])
    submit = SubmitField('Submit')

class AddIngredient(FlaskForm):
    i_name = StringField('Ingredient & quantity', validators=[DataRequired(message="You must supply an ingredient name anad its quantity")])
    recipe = SelectField('Add to recipe:', choices=[])
    submit = SubmitField('Add Ingredient ')

class AddInstructions(FlaskForm):
    step = StringField('Step Number')
    instruction = StringField('Write your instructions here:')
    submit = SubmitField('Submit')