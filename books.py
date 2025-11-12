from idlelib.query import Query

from fastapi import FastAPI, HTTPException
app = FastAPI()

BOOKS=[
{"Title": "Midnight's Children" ,"Author" :"Salman Rushdie"},
{"Title": "A Suitable Boy" ,"Author" :"Vikram Seth"},
{"Title": "The Ministry of Utmost Happiness","Author":"Arundhati Roy"},
{"Title": "Malgudi Days","Author": "R.K. Narayan"},
{"Title": "The White Tiger","Author": "Aravind Adiga"},
{"Title": "The Interpreter of Maladies","Author": "Jhumpa Lahiri"}
]

@app.get("/")
async def first_api():
    return {"message": "Welcome To My World"}

@app.get("/show_books")
async def read_book():
    return BOOKS

@app.get("/books/{book_title}")
async def read_all_books(book_title:str):
    for book in BOOKS:
        if book["Title"].casefold() == book_title.casefold():
            return book

@app.get("/books1/{book_title}")
async def read_all_books1(book_title:str):  #type hinting
    for book in BOOKS:
        if book.get('Title').casefold() == book_title.casefold():
            return book
    # ← notice this is outside the loop now
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books2/{book_author}")
async def read_all_books2(book_author:str):
    for book in BOOKS:
        if book.get('Author').casefold() == book_author.casefold():
            return book
    raise HTTPException(status_code=404, detail="Author not found")

@app.get("/books3/{book_author}")
async def read_all_books3(book_author:str):
    books_by_author = [
        book for book in BOOKS
        if book.get('Author').casefold() == book_author.casefold()
    ]
    if books_by_author:
        return books_by_author
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books4/{search_term}")
async def search_books(search_term: str):
    query_lower = search_term.casefold()

    results = [
        book for book in BOOKS
        if query_lower in book.get('Title', '').casefold()
        or query_lower in book.get('Author', '').casefold()
    ]
    if results:
        return results
    raise HTTPException(status_code=404, detail="No matching books found")

@app.get("/add_book")
async def add_book_via_url(title: str, author: str):
    new_book = {"Title": title, "Author": author}
    for book in BOOKS:
        if book["Title"].casefold() == title.casefold():
            raise HTTPException(status_code=400, detail="Book already exists")
    BOOKS.append(new_book)
    return {"message": "Book added successfully", "book": new_book}

@app.get("/delete_book/{book_title}")
async def delete_book_via_get(book_title: str):
    for i, book in enumerate(BOOKS):
        if book["Title"].casefold() == book_title.casefold():
            deleted_book = BOOKS.pop(i)
            return {"message": "Book deleted successfully", "book": deleted_book}
    raise HTTPException(status_code=404, detail="Book not found")





