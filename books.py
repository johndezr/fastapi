from fastapi import Body, FastAPI

app = FastAPI()

books = [
  {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_year": 1925
  },
  {
    "id": 2,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "published_year": 1960
  },
  {
    "id": 3,
    "title": "1984",
    "author": "George Orwell",
    "published_year": 1949
  }
]

@app.get("/books")
async def get_books():
  return books

@app.get("/books/{id}")
async def get_book(id: int):
  for book in books:
    if book.id == id:
      return book
  return {"error": "Book not found"}
  
@app.get("/books/{book_author}/")
async def get_book_by_author_query_year(book_author: str, year: int):
  books_query = []
  for book in books:
    if book.author.casefold() == book_author.casefold() and book.published_year == year:
      books_query.append(book)
  return books_query
  
@app.post("books/create_book")
async def create_book(new_book = Body()):
  books.append(new_book)
  return new_book
  
@app.put("books/update_book")
async def update_book(updated_book = Body()):
  for i in range(len(books)):
    if books[i].id == updated_book.id:
      books[i] = updated_book
      return updated_book
  return {"error": "Book not found"}

@app.delete("books/{id}")
async def delete_book(id: int):
  for i in range(len(books)):
    if books[i].id == id:
      books.pop(i)
      return {"message": "Book deleted"}
  return {"error": "Book not found"}

      
    