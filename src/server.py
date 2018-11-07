from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask import Flask, render_template, flash, request
from cache import process_input

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = ''

class ReusableForm(Form):
    name = TextField('Movie Name:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def beer_movie():
    form = ReusableForm(request.form)

    print (form.errors)
    if request.method == 'POST':
        name = request.form['name']

        if form.validate():
            flash(process_input(name))
        else:
            flash('All the form fields are required.')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()