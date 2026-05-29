import pyodbc
from fastapi import FastAPI

app = FastAPI()

books = [{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": True},
         {"title": "To kill a mockingbird", "author": "Harper Lee", "available": True},
         {"title": "The alchemist", "author": "Paulo Coelho", "available": True},
         {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "available": True},
         {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "available": False},
         {"title": "Of Mice and Men", "author": "John Steinbeck", "available": True},
         {"title": "1984", "author": "George Orwell", "available": True},
         {"title": "Pride and Prejudice", "author": "Jane Austen", "available": True},
         {"title": "The Hobbit", "author": "J.R.R. Tolkien", "available": False}];

# Function to establish a connection to the SQL Server database
def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=BooksDB;"
        "Trusted_Connection=yes;"
    )
    return conn   


# Home Route
@app.get("/")
def home():
    conn = get_connection()  # Establish connection to the database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    return {"message": "Welcome to the Book API!"}

# Get all books
@app.get("/books")
def get_books():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT Title, Author, Available FROM Books")
    rows = cursor.fetchall()

    conn.close()

    return [
        {"title": row[0], "author": row[1], "available": bool(row[2])}
        for row in rows
    ]  

# To return only available books
@app.get("/books/available")
def get_available_books():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT Title, Author, Available FROM Books WHERE Available = 1")
    rows = cursor.fetchall()

    conn.close()

    return [
        {"title": row[0], "author": row[1], "available": bool(row[2])}
        for row in rows
    ]

# To check the availability of a specific book by title
@app.get("/books/{title}")
def check_book_availability(title: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT Title, Author, Available FROM Books WHERE Title = ?", (title,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return {
            "title": row[0],
            "author": row[1],
            "available": bool(row[2])
        }
    return {"error": "Book not found"}

# To update the title of a book. (Put/Patch)
@app.put("/books/{title}")
def update_book_title(title: str, new_title: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE Books SET Title = ? WHERE Title = ?", (new_title, title))
    conn.commit()

    conn.close()

    return {"message": "Book title updated successfully"}

# To delete a book by title
@app.delete("/books/{title}")
def delete_book(title: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Books WHERE Title = ?", (title,))
    conn.commit()

    conn.close()

    return {"message": "Book deleted successfully"}
