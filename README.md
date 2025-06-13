# 📚 Book Review Platform

A Flask application where users can manage **Books**, **Authors**, and **Reviews**, with optional **web scraping** to populate book data from the internet.

---

## 🚀 Features

- Models: `Author`, `Book`, and `Review` with proper relationships.
- CRUD API endpoints for managing books.
- Database migrations using Flask-Migrate.
- Seed script to populate sample data.
- Optional: Scrape book data using BeautifulSoup.
- JSON-based API responses.

---

## 🛠 Tech Stack

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite (default)
- BeautifulSoup4 (for optional scraping)
- Requests

---

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/book-review-platform.git
cd book-review-platform
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

```bash
export FLASK_APP=app.py  # Windows: set FLASK_APP=app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5. Seed the Database

```bash
python seed.py
```

---

## 🧪 API Endpoints

### 📘 Get All Books

```
GET /books
```

### 📕 Get a Specific Book by ID

```
GET /books/<book_id>
```

### ➕ Add a New Book

```
POST /books
Content-Type: application/json

{
  "title": "Example Book",
  "publication_year": 2024,
  "author_id": 1
}
```

### ✏️ Update a Book

```
PATCH /books/<book_id>
Content-Type: application/json

{
  "title": "Updated Title"
}
```

### ❌ Delete a Book

```
DELETE /books/<book_id>
```

---

## 🕸️ Optional: Web Scraping

To scrape books from a public site (like Project Gutenberg):

```
GET /scrape
```

It will scrape and insert new books and authors into the database.

---

## 📂 Project Structure

```
book-review-platform/
│
├── app.py              # Main Flask app
├── models.py           # SQLAlchemy models
├── seed.py             # Data seeding script
├── scrape_books.py     # Optional web scraping logic
├── requirements.txt    # Python dependencies
├── migrations/         # Auto-generated DB migration files
└── README.md           # Project overview
```

---

## 🧑‍💻 Author

Made for a coding exercise. Contributions welcome!

---

## 📜 License

MIT License