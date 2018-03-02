from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    # sets use for tempaltes in template file and calls using render_
    user = {'username': 'Justin'}
    posts =[
        {
        'author':{'username': 'Winky'},
        'body': 'Seoul is a beauty city'
        },
        {
        'author': {'username': ' Wayne'},
        'body': 'The origin or Karct-do'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)