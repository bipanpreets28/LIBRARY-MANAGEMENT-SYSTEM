from utils import books, issued_books

def return_book():
    if len(issued_books) == 0:
        print("No issued books")
    else:
        book_name = input("Enter book you want to return: ").strip().upper()
        
        if book_name in issued_books:
            data = issued_books[book_name]
            allowed_days = data["days"]
            
            used_days = int(input("Enter number of days used: "))
            
            fine = 0
            if used_days > allowed_days:
                extra_days = used_days - allowed_days
                
                for i in range(1, extra_days + 1):
                    fine += 10 * i
            
            del issued_books[book_name]
            books[book_name] = True
            
            print(f"Book - {book_name} returned successfully")
            print(f"Used Days: {used_days}")
            
            if fine > 0:
                print(f"Late return! Fine = Rs.{fine}")
            else:
                print("Returned on time. No fine.")
        else:
            print("No such issued book found")