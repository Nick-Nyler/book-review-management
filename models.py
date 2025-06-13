from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

book_reviews = db.Table('book_reviews',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('review_id', db.Integer, db.ForeignKey('review.id'))
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    publication_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    reviews = db.relationship('Review', secondary=book_reviews, backref='books')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)
