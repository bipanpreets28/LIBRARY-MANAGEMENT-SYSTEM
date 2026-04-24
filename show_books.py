from utils import books

def show_book():
    if len(books) == 0:
        print("No books available this time!!!")
    else:
        print("\nAvailable Books-->")
        for book in books:
            print(f"- {book}")