from member import Member
from book import Book

# Bibloteks klasse: Styre bøger, medlemmer, samt håndtere oprettelse og fjernelse af bøger
class Library:
    def __init__(self, books=None, members=None):
        self.books = books if books is not None else {}
        self.members = members if members is not None else{}
        self.next_book_id = 1
        self.next_member_id = 1
        if self.books:
            self.next_book_id = max(self.books.keys()) + 1
        if self.members:
            self.next_member_id = max(self.members.keys()) + 1 

#Funktion til at oprette bøger i bibloteket
    def add_book(self, title, author, copies):
        for book in self.books.values():
            if book.title.lower() == title.lower() and book.author.lower() == author.lower():
                print("A book with the same title and author already exists, if you want to update press 2")
                return None
        book_id = self.next_book_id
        self.next_book_id += 1      #dette giver book_id automatisk og giver derfor et unikt id
        book = Book(book_id, title, author, copies)
        self.books[book_id] = book
        return book_id

#Funktion til at fjerne bøger fra bibloteket   
    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False

#Funktion til at opdatere bøger  
    def update_book(self, book_id, title=None, author=None, copies=None):
        if book_id not in self.books:
            print(f"Book with ID {book_id} not found.")
            return False
        book = self.books[book_id]

        if title is not None:
            if not title.strip():
                print("Title cannot be empty.")
                return False
            book.title = title

        if author is not None:
            if not author.strip():
                print("Author cannot be empty.")
                return False
            book.author = author

        if copies is not None:
            if copies < 0:
                print("Copies cannot be negative.")
                return False
            book.copies = copies

        return True

#Funktion til at oprette medlemmer
    def add_member(self, name):
        member_id = self.next_member_id
        self.next_member_id += 1
        member = Member(member_id, name)
        self.members[member_id] = member
        return member_id

#Funktion til at fjerne medlemmer   
    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            return True
        return False

#Funktion til at opdatere medlemmer    
    def update_member(self, member_id, name=None):
        if member_id not in self.members:
            print(f"Member with ID {member_id} not found.")
            return False
        member = self.members[member_id]

        if name is not None:
            if not name.strip():
                print("Name cannot be empty.")
                return False
            member.name = name

        return True

#Funktion til at låne bøger ud
    def issue_book(self, member_id, book_id):
        if member_id not in self.members:
            print(f"Member with ID {member_id} not found.")
            return False

        if book_id not in self.books:
            print(f"Book with ID {book_id} not found.")
            return False

        book = self.books[book_id]
        if book.copies <= 0:
            print(f"Book with ID {book_id} is not available.")
            return False

        return self.members[member_id].borrow_book(book)
    
#Funktion til at aflevere bøger   
    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print(f"Member with ID {member_id} not found.")
            return False

        if book_id not in self.books:
            print(f"Book with ID {book_id} not found.")
            return False

        book = self.books[book_id]
        return self.members[member_id].return_book(book)

#Funktion til at vise bøger i bibloteket   
    def display_books(self):
        return [book.display_info() for book in self.books.values()]

#Funktion til at vise medlemmer i bibloteket   
    def display_members(self):
        return [member.display_info() for member in self.members.values()]

#Funktion til at søge efter bøger i bibloteket   
    def search_books(self, query):
        return [book.display_info() for book in self.books.values()
                if query.lower() in book.title.lower() or query.lower() in book.author.lower()]


