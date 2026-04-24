from utils import books

def add_book():
    book_name = input("Enter book name to be added: ").strip().upper()
    if book_name in books:
        print("Book already exists.")
    else:
        books[book_name] = True
        print(f"Book - {book_name} added successfully.")