from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# Simularea unei baze de date cu o listă de dicționare
recipes = []

# Formular pentru adăugarea unei rețete
class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    submit = SubmitField('Add Recipe')

# Pagina principală
@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

# Formularul de adăugare a unei rețete
@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        new_recipe = {
            'title': form.title.data,
            'ingredients': form.ingredients.data,
            'instructions': form.instructions.data
        }
        recipes.append(new_recipe)
        return redirect(url_for('index'))
    return render_template('recipe_form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
