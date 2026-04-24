from utils import books, issued_books

def issue_book():
    if len(books) == 0:
        print("No book available")
    else:
        book_name = input("Enter book to be issued: ").strip().upper()
        
        if book_name in books:
            student = input("Enter student name: ").strip().title()
            days = int(input("Enter number of days for issue: "))
            
            issued_books[book_name] = {
                "student": student,
                "days": days
            }
            
            del books[book_name]
            
            print(f"Book - {book_name} issued successfully to {student}")
            print(f"Return within {days} days")
        else:
            print("No such book available")