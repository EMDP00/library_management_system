from member import Member

# Bibloteks klasse: Styre bøger, medlemmer, samt håndtere oprettelse og fjernelse af bøger
class Library:
    def __init__(self, books=None, members=None):
        self.books = books if books is not None else {}
        self.members = members if members is not None else{}

    def add_book(self, book):
        if book.book_id not in self.books:
            self.books[book.book_id] = book
            return True
        return False
    
    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False
    
    def update_book(self, book_id, title=None, author=None, copies=None):
        if book_id in self.books:
            book = self.books[book_id]
            if title:
                book.title = title
            if author:
                book.author = author
            if copies is not None:
                book.copies = copies
            return True
        return False
    
    def add_member(self, member):
        if member.member_id not in self.members:
            self.members[member.member_id] = member
            return True
        return False
    
    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            return True
        return False
    
    def update_member(self, member_id, name=None):
        if member_id in self.members:
            member = self.members[member_id]
            if name:
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


