# Bog Klasse: Styre bøger i et biblotek, deres attributes og functioner
class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

#Funktion til at vise information om bøger
    def display_info(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Copies: {self.copies}"

#Funktion til at updatere antal copier
    def update_copies(self, amount):
        self.copies += amount


