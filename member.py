from book import Book
# Medlems klasse: Styre medlemmer i et biblotek, deres attributes og funktioner
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

#Funktion til at vise information om bøger
    def display_info(self):
        return f"ID: {self.member_id}, Name: {self.name}, Borrowed Books: {[book.book_id for book in self.borrowed_books]}"

#Funktion til at låne bøger til medlemmer
    def borrow_book(self, book):
        if book in self.borrowed_books:
            print("Book already borrowed by this member.")
            return False
        if book.copies > 0:
            self.borrowed_books.append(book)
            book.update_copies(-1)
            return True
        return False

#Funktion til at fjerne bøger fra medlemmer
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.update_copies(1)
            return True
        return False
    

