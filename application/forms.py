from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired

class AddRecipe(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired(message="You must supply a recipe name.")])
    submit = SubmitField('Add Recipe')

    