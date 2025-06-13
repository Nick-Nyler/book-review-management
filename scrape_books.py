import requests
from bs4 import BeautifulSoup
from app import app, db
from models import Author, Book

def scrape_books():
    url = 'https://www.gutenberg.org/ebooks/search/?sort_order=downloads'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    with app.app_context():
        added_books = 0
        for book_item in soup.select(".booklink")[:5]:
            title = book_item.select_one(".title").text.strip()
            author_name = book_item.select_one(".subtitle").text.strip()

            author = Author.query.filter_by(name=author_name).first()
            if not author:
                author = Author(name=author_name)
                db.session.add(author)

            book = Book(title=title, publication_year=1900, author=author) 
            db.session.add(book)
            added_books += 1

        db.session.commit()
        return added_books

@app.route('/scrape', methods=['GET'])
def scrape_route():
    count = scrape_books()
    return jsonify({"message": f"Added {count} books"})
