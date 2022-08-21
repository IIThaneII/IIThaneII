from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
    
db.create_all()

class MyDataRequired(DataRequired):
    field_flags = ()

class CafeForm(FlaskForm):
    book = StringField('Book Name', validators=[MyDataRequired()])
    author = StringField('Book Author', validators=[MyDataRequired()])
    rate = StringField('Rating', validators=[MyDataRequired()])
    submit = SubmitField('Add Book')

class EditForm(FlaskForm):
    rate = StringField('New Rating', validators=[MyDataRequired()])
    submit = SubmitField('Edit Rating')

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        new_book = Book(title=form.book.data, author=form.author.data, rating=form.rate.data)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route('/edit_rating/<id>', methods=['POST', 'GET'])
def edit_rating(id):
    edit_form = EditForm()
    book_to_update = Book.query.get(id)
    if edit_form.validate_on_submit():
        book_to_update = Book.query.get(id)
        book_to_update.rating = edit_form.rate.data
        db.session.commit() 
        return redirect(url_for('home'))
    return render_template('edit_rating.html', book=book_to_update, form=edit_form)

@app.route('/delete_book/<id>')
def delete_book(id):
    book_to_delete = Book.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)