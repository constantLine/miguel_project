from flask import Flask, render_template, flash, redirect, url_for, request
from config import Config
from forms2 import LoginForm
app = Flask(__name__)
app.config.from_object(Config)

""""
@app.route('/')
def day_to_win():
    return 'ha=ha-ha'


@app.route('/index')
def index(title='zero'):
    user = {'username': 'Эльдар Рязанов'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', user=user, title=title, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)

"""


@app.route('/index')
def index(name='Kostya', title='Page'):
    return render_template('base2.html', name=name, title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        flash(f'At {form.datetime.data} user {form.username.data} logged with email: {form.email.data} and he want {"to be a remembering" if form.remember_me else "to be a not remembering"}')
        return redirect(url_for('index'))
    return render_template('login2.html', form=form)


if __name__ == '__main__':
    app.run(debug='True')
