from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-movies-collection.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=False, nullable=False)
    year = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(5000), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True, unique=False)
    img_url = db.Column(db.String(250), nullable=False)

db.create_all()

## After adding the new_movie the code needs to be commented out/deleted.
## So you are not trying to add the same movie twice.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

class MyDataRequired(DataRequired):
    field_flags = ()

class EditForm(FlaskForm):
    rating = StringField('Your rating e.g.7.5/10', validators=[MyDataRequired()])
    review = StringField('Your review', validators=[MyDataRequired()])
    submit = SubmitField('Done')

class AddForm(FlaskForm):
    m_title = StringField('Movie Title', validators=[MyDataRequired()])
    submit = SubmitField('Done')

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    all_movies.reverse()
    for i in range(len(all_movies)):
        #This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = i+1
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route('/edit', methods=['POST', 'GET'])
def edit():
    edit_form = EditForm()
    movie_id = request.args.get("id")
    movie_to_update = Movie.query.get(movie_id)
    if edit_form.validate_on_submit():
        movie_to_update.rating = float(edit_form.rating.data)
        movie_to_update.review = edit_form.review.data
        db.session.commit() 
        return redirect(url_for('home'))
    return render_template('edit.html', form=edit_form)

@app.route('/delete/')
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        parameters = {
            'page': 1,
            'language': 'en-US',
            'api_key': '65935e0240814d9b0186b1b388628598',
            'include_adult': False,
            'query': add_form.m_title.data
        }
        response = requests.get(url='https://api.themoviedb.org/3/search/movie', params=parameters)
        response.raise_for_status()
        movies = response.json()
        return render_template('select.html', movies=movies)
    return render_template('add.html', form=add_form)

@app.route('/select')
def selected_movie():
    movie_id = request.args.get("m_id")
    response = requests.get(url=f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=65935e0240814d9b0186b1b388628598')
    response.raise_for_status()
    movie = response.json()
    new_movie = Movie(
        title=movie["original_title"],
        year=movie["release_date"][:4],
        description=movie["overview"],
        rating=float(movie["vote_average"]),
        ranking = 0,
        img_url=f'https://image.tmdb.org/t/p/w500{movie["poster_path"]}',
        review= f'None{random.randint(0, 100)}',
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
