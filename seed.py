from app import app, db
from models import Author, Book, Review

def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()
 
        author1 = Author(name='Jane Austen')
        author2 = Author(name='Mark Twain')
        db.session.add_all([author1, author2])
        db.session.commit()

        book1 = Book(title='Pride and Prejudice', publication_year=1813, author_id=author1.id)
        book2 = Book(title='Emma', publication_year=1815, author_id=author1.id)
        book3 = Book(title='The Adventures of Tom Sawyer', publication_year=1876, author_id=author2.id)
        book4 = Book(title='Adventures of Huckleberry Finn', publication_year=1884, author_id=author2.id)
        db.session.add_all([book1, book2, book3, book4])
        db.session.commit()

        review1 = Review(rating=5, comment='Amazing romance novel!')
        review2 = Review(rating=4, comment='Really enjoyed the characters.')
        review3 = Review(rating=3, comment='Good but a bit slow.')
        review4 = Review(rating=5, comment='A classic adventure!')
        review5 = Review(rating=4, comment='Fun and engaging.')
        review6 = Review(rating=5, comment='A masterpiece!')
        db.session.add_all([review1, review2, review3, review4, review5, review6])
        db.session.commit()

        book1.reviews.extend([review1, review2])
        book2.reviews.append(review3)
        book3.reviews.extend([review4, review5])
        book4.reviews.append(review6)
        db.session.commit()

        print('Database seeded successfully!')

if __name__ == '__main__':
    seed_database()