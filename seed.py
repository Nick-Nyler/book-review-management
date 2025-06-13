from app import app, db
from models import Author, Book, Review

with app.app_context():
    db.drop_all()
    db.create_all()

    author1 = Author(name="George Orwell")
    author2 = Author(name="J.K. Rowling")

    book1 = Book(title="1984", publication_year=1949, author=author1)
    book2 = Book(title="Animal Farm", publication_year=1945, author=author1)
    book3 = Book(title="Harry Potter and the Sorcerer's Stone", publication_year=1997, author=author2)
    book4 = Book(title="Harry Potter and the Chamber of Secrets", publication_year=1998, author=author2)

    review1 = Review(rating=5, comment="Excellent!")
    review2 = Review(rating=4, comment="Very good read")
    review3 = Review(rating=3, comment="Interesting concept")
    review4 = Review(rating=4, comment="Loved it!")
    review5 = Review(rating=2, comment="Not for me")
    review6 = Review(rating=5, comment="Masterpiece!")

    book1.reviews.extend([review1, review2])
    book2.reviews.append(review3)
    book3.reviews.extend([review4, review5])
    book4.reviews.append(review6)

    db.session.add_all([author1, author2, book1, book2, book3, book4])
    db.session.commit()
