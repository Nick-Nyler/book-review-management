import requests
from bs4 import BeautifulSoup
from app import db
from models import Author, Book

def scrape_and_store_books():
    url = 'https://www.gutenberg.org/ebooks/search/?sort_order=downloads'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books_added = 0
    authors_added = 0

    book_items = soup.select('li.booklink')[:5]  
    for item in book_items:
        title_elem = item.select_one('span.title')
        author_elem = item.select_one('span.subtitle')
        
        if title_elem and author_elem:
            title = title_elem.text.strip()
            author_name = author_elem.text.strip()
            
            author = Author.query.filter_by(name=author_name).first()
            if not author:
                author = Author(name=author_name)
                db.session.add(author)
                db.session.commit()
                authors_added += 1
            
            book = Book(title=title, publication_year=1800, author_id=author.id)
            db.session.add(book)
            books_added += 1
    
    db.session.commit()
    return books_added, authors_added