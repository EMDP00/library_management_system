from library import Library
from book import Book
from member import Member

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Add Member")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Display Books")
        print("8. Display Members")
        print("9. Search Books")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            copies = int(input("Copies: "))
            book_id = library.add_book(title, author, copies)
            print(f"Book added succesfully! ID: {book_id}")
        
        elif choice == "2":
            book_id = int(input("Enter Book ID to update: "))
            title = input("Put new Title (leave blank to skip): ")
            author = input("Put new Author (leave blank to skip): ")
            copies = input("Put amount of Copies (leave blank to skip): ")
            copies = int(copies) if copies else None
            if library.update_book(book_id, title if title else None, author if author else None, copies):
                print("Book updated succesfully!")
            else:
                print("Failed to update book.")

        elif choice == "3":
            member_id = int(input("Member ID: "))
            name = input("Name: ")
            member = Member(member_id, name, [])
            if library.add_member(member):
                print("Member added successfully!")
            else:
                print("Member already exists.")
        
        elif choice == "4":
            member_id = int(input("Enter Member ID to update: "))
            name = input("New Name (leave blank to skip): ")
            if library.update_member(member_id, name if name else None):
                print("Member updated successfully!")
            else:
                print("Failed to update member.")

        elif choice == "5":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            if library.issue_book(member_id, book_id):
                print("Book issued successfully!")
            else:
                print("Failed to issue book.")
        
        elif choice == "6":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            if library.return_book(member_id, book_id):
                print("Book returned successfully!")
            else:
                print("Failed to return book")

        elif choice == "7":
            for book_info in library.display_books():
                print(book_info)
        
        elif choice == "8":
            for member_info in library.display_members():
                print(member_info)
        
        elif choice == "9":
            query = input("Search query: ")
            results = library.search_books(query)
            if results:
                for results in results:
                    print(results)
            else:
                print("No books found.")
        
        elif choice == "10":
            break

        else:
            print("Invalid choice. please try again")

if __name__ == "__main__":
    main()