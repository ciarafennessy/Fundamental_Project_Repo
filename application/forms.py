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
    recipe = SelectField('Add to recipe:', choices=[])
    submit = SubmitField('Submit')

class UpdateInstructions(FlaskForm):
    inst_step = StringField('Step Number', validators=[DataRequired(message="This field cannot be left blank")])
    inst = StringField('Instruction', validators=[DataRequired(message="This field cannot be left blank")])
    submit = SubmitField('Update Instruction')


class SelectRecipe(FlaskForm):
    recipe_id = SelectField('Recipe', choices=[])
    submit = SubmitField('Choose Recipe')