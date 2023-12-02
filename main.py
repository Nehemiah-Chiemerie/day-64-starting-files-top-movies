from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods= ["GET", "POST"])
def add():
    if request.method == "POST":
    #     CREATE RECORD
        new_movie = Movie(
            title="Phone Booth",
            year=2002,
            description="Publicist Stuart Shepard finds himself trapped in a phone booth, "
                        "pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, "
                        "Stuart's negotiation with the caller leads to a jaw-dropping climax.",
            rating=7.3,
            ranking=10,
            review="My favourite character was the caller.",
            img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        )
        db.session.add(new_movie)
        db.session.commit()
    return render_template("add.html")


if __name__ == '__main__':
    app.run(debug=True)


# Flask==2.3.2
# flask==2.2.2
# flask_sqlalchemy==3.0.5
# flask-sqlalchemy==2.5.1
# Werkzeug<=2.1.2


# Flask==2.3.2
# Flask-SQLAlchemy>=3.0.2
# SQLAlchemy==1.4
# Flask==3.0.0