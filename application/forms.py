from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length


class AddRecipe(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired(message="You must supply a recipe name."), Length(min=1, max=50)])
    recipe_time = StringField('Recipe Time', validators=[DataRequired(message="You must supply a recipe time."), Length(min=1, max=50)])
    servings = IntegerField('Servings', validators=[DataRequired(message="You must supply an estimated number of servings.")])
    submit = SubmitField('Submit')

class AddIngredient(FlaskForm):
    i_name = StringField('Ingredient & quantity', validators=[DataRequired(message="You must supply an ingredient name anad its quantity"), Length(min=1, max=50)])
    recipe = SelectField('Add to recipe:', choices=[], validators=[DataRequired(message="You must choose a recipe.")])
    submit = SubmitField('Add Ingredient ')

class AddInstructions(FlaskForm):
    step = StringField('Step Number', validators=[DataRequired(message="You must provide the step number"), Length(min=1, max=10)])
    instruction = StringField('Write your instructions here:', validators=[DataRequired(message="You must provide an instruction"), Length(min=1, max=1000)])
    recipe = SelectField('Add to recipe:', choices=[], validators=[DataRequired(message="You must choose a recipe.")])
    submit = SubmitField('Submit')

class UpdateInstructions(FlaskForm):
    inst_step = StringField('Step Number', validators=[DataRequired(message="You must provide the step number"), Length(min=1, max=10)])
    inst = StringField('Instruction', validators=[DataRequired(message="You must provide an instruction"), Length(min=1, max=1000)])
    submit = SubmitField('Update Instruction')


class SelectRecipe(FlaskForm):
    recipe_id = SelectField('Recipe', choices=[], validators=[DataRequired(message="Choose a recipe.")])
    submit = SubmitField('Choose Recipe')

