from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    content = StringField('Enter a brand or product name to get started', render_kw={"placeholder": "Mario Badescu Enzyme Cleansing Gel"})
    ingredient_content = TextAreaField('Search by ingredients', render_kw={"placeholder": "Copy and paste the ingredients label of your product, separated by a comma. E.g.) Denatured alcohol"})

    submit = SubmitField('Search')

class IngredientSearchForm(FlaskForm):
    content = StringField('Copy and paste the ingredients of your product, separated by a comma', validators=[DataRequired()])
    submit = SubmitField('Search')