from flask import Flask, jsonify, request, abort
from flask_migrate import Migrate
from models import db, Author, Book, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([
        {
            "id": b.id,
            "title": b.title,
            "publication_year": b.publication_year,
            "author": b.author.name,
            "reviews": [
                {"id": r.id, "rating": r.rating, "comment": r.comment}
                for r in b.reviews
            ]
        }
        for b in books
    ])

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        abort(404)
    return jsonify({
        "id": book.id,
        "title": book.title,
        "publication_year": book.publication_year,
        "author": book.author.name,
        "reviews": [
            {"id": r.id, "rating": r.rating, "comment": r.comment}
            for r in book.reviews
        ]
    })

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    try:
        book = Book(
            title=data['title'],
            publication_year=data['publication_year'],
            author_id=data['author_id']
        )
        db.session.add(book)
        db.session.commit()
        return jsonify({"message": "Book created", "id": book.id}), 201
    except:
        abort(400)

@app.route('/books/<int:book_id>', methods=['PATCH'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        abort(404)
    data = request.get_json()
    book.title = data.get('title', book.title)
    book.publication_year = data.get('publication_year', book.publication_year)
    db.session.commit()
    return jsonify({"message": "Book updated"})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        abort(404)
    for review in book.reviews:
        db.session.delete(review)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book and associated reviews deleted"})



if __name__ == "__main__":
    app.run(debug=True )