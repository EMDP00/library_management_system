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
            self.next_book_id = max(self.members.keys()) + 1 

    def add_book(self, title, author, copies):
        for book in self.books.values():
            if book.title.lower() == title.lower() and book.author.lower() == author.lower():
                print("A book with the same title and author already exists, if you want to update press 2")
        book_id = self.next_book_id
        self.next_book_id += 1
        book = Book(book_id, title, author, copies)
        self.books[book_id] = book
        return book_id
    
    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False
    
    def update_book(self, book_id, title=None, author=None, copies=None):
        if book_id in self.books:
            book = self.books[book_id]
            if title:
                if not title.strip():
                    print("Title cannot be empty.")
                    return False
                book.title = title
            if author:
                if not author.strip():
                    print("Author cannot be empty.")
                    return False
                book.author = author
            if copies is not None:
                if copies <0:
                    print("Copies cannot be negative.")
                    return False
                book.copies = copies
            return True
        return False
    
    def update_book(self, book_id, title=None, author=None, copies=None):
        if book_id in self.books:
            book = self.books[book_id]
            if title is not None and title.strip():
                book.title = title
            if author is not None and author.strip():
                book.author = author
            if copies is not None and copies >= 0:
                book.copies = copies
            return True
        return False

    def add_member(self, name):
        member_id = self.next_member_id
        self.next_member_id += 1
        member = Member(member_id, name, [])
        self.members[member_id] = member
        return member_id
    
    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            return True
        return False
    
    def update_member(self, member_id, name=None):
        if member_id in self.members:
            member = self.members[member_id]
            if name:
                if not name.strip():
                    print("Name Cannot be empty.")
                    return False
                member.name = name
            return True
        return False
    
    def issue_book(self, member_id, book_id):
        book_id = int(book_id)
        member_id = int(member_id)
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            return member.borrow_book(book)
        return False
    
    def return_book(self, member_id, book_id):
        book_id = int(book_id)
        member_id = int(member_id)
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            return member.return_book(book)
        return False
    
    def display_books(self):
        return [book.display_info() for book in self.books.values()]
    
    def display_members(self):
        return [member.display_info() for member in self.members.values()]
    
    def search_books(self, query):
        return [book.display_info() for book in self.books.values()
                if query.lower() in book.title.lower() or query.lower() in book.author.lower()]


