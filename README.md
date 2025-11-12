📚 Books API — FastAPI Project

A simple REST API built using FastAPI that allows users to view, search, add, and delete books.
This project demonstrates API routing, path parameters, query parameters, JSON responses, and error handling with HTTP status codes.

✅ Features

✔ Get a welcome message
✔ View all books
✔ Search a book by title
✔ Search a book by author
✔ Search by keyword in title or author
✔ Add a new book (via URL/query params)
✔ Delete a book by title
✔ Proper error handling using HTTPException

✅ Tech Stack

Language: Python

Framework: FastAPI

Server: Uvicorn

Response Format: JSON

✅ Endpoints
Method	Endpoint	Description
GET	/	Welcome message
GET	/show_books	Returns list of all books
GET	/books/{book_title}	Search a book by exact title
GET	/books2/{book_author}	Search a book by exact author
GET	/books4/{search_term}	Keyword search (title or author)
GET	/add_book?title=&author=	Add a new book
GET	/delete_book/{book_title}	Delete book by title
✅ Example JSON Response
{
  "Title": "Malgudi Days",
  "Author": "R. K. Narayan"
}

✅ How to Run
pip install fastapi uvicorn
fastapienv\Scripts\activate.bat
uvicorn books:app --reload


Then open browser:
👉 http://127.0.0.1:8000

✅ File Used

books.py — contains all FastAPI routes and in-memory books list

✅ Future Improvements

✅ Move data to database (MySQL / SQLite)
✅ Add POST/PUT/DELETE instead of GET for write operations
✅ User authentication

✅ Skills Demonstrated

✔ FastAPI routing
✔ JSON formatting
✔ Path & query parameters
✔ Error handling
✔ API testing
