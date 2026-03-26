from library import Library

#Main funktion til at initialisere og kører systemet
def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Remove Book")
        print("4. Add Member")
        print("5. Update Member")
        print("6. Remove Member")
        print("7. Issue Book")
        print("8. Return Book")
        print("9. Display Books")
        print("10. Display Members")
        print("11. Search Books")
        print("12. Exit")
    

        choice = input("Enter your choice: ")
    #Hvis brugeren vil oprette en bog i systemet med titel, forfatter og antal kopier
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            try:
                copies = int(input("Copies: "))
                book_id = library.add_book(title, author, copies)
                if book_id is not None:
                    print(f"Book added successfully! ID: {book_id}")
                else:
                    print("A book with the same title and author already exists.")
            except ValueError:
                print("Invalid input for copies. Please enter a valid number.")
    #Hvis Brugeren vil opdatere en bog med enten navn, titel, forfatter eller antal kopier 
        elif choice == "2":
            try:
                book_id = int(input("Enter Book ID to update: "))
                title = input("Put new Title (leave blank to skip): ")
                author = input("Put new Author (leave blank to skip): ")
                copies_input = input("Put amount of Copies (leave blank to skip): ")
                copies = int(copies_input) if copies_input.strip() else None
                if copies_input.strip() and not copies_input.isdigit():
                    print("Invalid input for copies. Please enter a valid number.")
                    continue
                if library.update_book(book_id, title if title.strip() else None, author if author.strip() else None, copies):
                    print("Book updated successfully!")
                else:
                    print("Failed to update book.")
            except ValueError:
                print("Invalid input for Book ID. Please enter a valid number.")
        
        # Hvis brugeren vil fjerne en bog fra systemet, dette gøres med book_id
        elif choice == "3":
            book_id = input("Enter Book ID to remove: ")
            try:
                book_id = int(book_id)
                if library.remove_book(book_id):
                    print("Book removed successfully!")
                else:
                    print("Failed to remove book.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        #Hvis brugeren vil oprette et medlem med navn, member_id bliver givet automatisk
        elif choice == "4":
            name = input("Name: ")
            member_id = library.add_member(name)
            print(f"Member added successfully! ID: {member_id}")

        #Hvis brugeren vil opdatere et medlems navn, med member_id
        elif choice == "5":
            try:
                member_id = int(input("Enter Member ID to update: "))
                name = input("New Name (leave blank to skip): ")
                if library.update_member(member_id, name if name.strip() else None):
                    print("Member updated successfully!")
                else:
                    print("Failed to update member.")
            except ValueError:
                print("Invalid input for Member ID. Please enter a valid number.")

        #Hvis brugeren vil fjerne et medlem med member_id
        elif choice == "6":
            member_id = input("Enter Member ID to remove: ")
            try:
                member_id = int(member_id)
                if library.remove_member(member_id):
                    print("Member removed successfully!")
                else:
                    print("Failed to remove member.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        #Hvis brugeren vil låne en bog til et medlem, her bruges member_id og book_id
        elif choice == "7":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            try:
                member_id = int(member_id)
                book_id = int(book_id)
                if library.issue_book(member_id, book_id):
                    print("Book issued successfully!")
                else:
                    print("Failed to issue book.")
            except ValueError:
                print("Invalid input. Please enter valid numbers for Member ID and Book ID.")

        #Hvis brugeren vil aflevere en bog fra et medlem, her bruges member_id og Book_id
        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            try:
                member_id = int(member_id)
                book_id = int(book_id)
                if library.return_book(member_id, book_id):
                    print("Book returned successfully!")
                else:
                    print("Failed to return book.")
            except ValueError:
                print("Invalid input. Please enter valid numbers for Member ID and Book ID.")

        #Hvis brugeren vil se hvilke bøger der er i bibloteket
        elif choice == "9":
            books = library.display_books()
            if books:
                for book_info in books:
                    print(book_info)
            else:
                print("No books in the library.")

        #Hvis brugeren vil se hvilke medlemmer der er i bibloteket
        elif choice == "10":
            members = library.display_members()
            if members:
                for member_info in members:
                    print(member_info)
            else:
                print("No members in the library.")

        #Hvis brugeren vil søge efter en specifik bog
        elif choice == "11":
            query = input("Search query: ")
            results = library.search_books(query)
            if results:
                for result in results:
                    print(result)
            else:
                print("No books found.")

        #Hvis systemet skal afslutte
        elif choice == "12":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()