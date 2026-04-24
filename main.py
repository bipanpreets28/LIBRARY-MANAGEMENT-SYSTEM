from add_books import add_book
from return_books import return_book
from issue_books import issue_book
from show_books import show_book

def library():
    while True:
        print("\n====== LIBRARY MENU ======")
        print("1. Add Books")
        print("2. Show Books")
        print("3. Issue Books")
        print("4. Return Books")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice.isdigit():
            choice = int(choice)
            
            if choice == 1:
                add_book()
            elif choice == 2:
                show_book()
            elif choice == 3:
                issue_book()
            elif choice == 4:
                return_book()
            elif choice == 5:
                print("Thank You")
                break
            else:
                print("Invalid choice!!!")
        else:
            print("Invalid Input!!!")

library()