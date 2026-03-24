from library import Library

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Display Members")
        print("7. Search Books")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            copies = int(input("Copies: "))
            book = book(book_id, title, author, copies)
            if library.add_book(book):
                print("Book added successfully!")
            else:
                print("Book ID already exists.")

        elif choice == "2":
            member_id = input("Member ID: ")
            name = input("Name: ")
            member = Member(member_id, name)
            if library.add_member(member):
                print("Member added successfully!")
            else:
                print("Member already exists.")
        
        elif choice == "3":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            if library.issue_book(member_id, book_id):
                print("Book issued successfully!")
            else:
                print("Failed to issue book.")
        
        elif choice == "4":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            if library.return_book(member_id, book_id):
                print("Book returned successfully!")
            else:
                print("Failed to return book")

        elif choice == "5":
            for book_info in library.display_books():
                print(book_info)
        
        elif choice == "6":
            for member_info in library.display_members():
                print(member_info)
        
        elif choice == "7":
            query = input("Search query: ")
            results = library.search_books(query)
            if results:
                for results in results:
                    print(results)
            else:
                print("No books found.")
        
        elif choice == "8":
            break

        else:
            print("Invalid choice. please try again")

if __name__ == "__main__":
    main()