import unittest
from book import Book
from member import Member
from library import Library

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(1, "Hobitten", "J.R.R. Tolkien", 3)

    def test_update_copies_to_zero(self):
        """Antal kopier kan blive 0"""
        self.book.update_copies(-3)
        self.assertEqual(self.book.copies, 0)

    def test_display_info(self):
        """Viser korrekt boginfo"""
        info = self.book.display_info()
        self.assertIn("Hobitten", info)
        self.assertIn("J.R.R. Tolkien", info)

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member = Member(1, "Alice")
        self.book = Book(1, "Hobitten", "J.R.R. Tolkien", 2)

    def test_borrow_book(self):
        """Medlem kan låne en bog"""
        result = self.member.borrow_book(self.book)
        self.assertTrue(result)
        self.assertIn(self.book, self.member.borrowed_books)
        self.assertEqual(self.book.copies, 1)

    def test_return_book(self):
        """Medlem kan aflevere en lånt bog"""
        self.member.borrow_book(self.book)
        result = self.member.return_book(self.book)
        self.assertTrue(result)
        self.assertNotIn(self.book, self.member.borrowed_books)
        self.assertEqual(self.book.copies, 2)

    def test_borrow_book_no_copies(self):
        """Bog med 0 kopier kan ikke lånes"""
        self.book.copies = 0
        result = self.member.borrow_book(self.book)
        self.assertFalse(result)

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book_id = self.library.add_book("Hobitten", "J.R.R. Tolkien", 3)
        self.member_id = self.library.add_member("Alice")

    def test_add_book(self):
        """Bog tilføjes korrekt"""
        self.assertIsNotNone(self.book_id)
        self.assertIn(self.book_id, self.library.books)

    def test_add_duplicate_book(self):
        """Duplikat bog (samme titel + forfatter) afvises"""
        result = self.library.add_book("Hobitten", "J.R.R. Tolkien", 1)
        self.assertIsNone(result)

    def test_issue_book(self):
        """Bog udlånes korrekt"""
        result = self.library.issue_book(self.member_id, self.book_id)
        self.assertTrue(result)

    def test_return_book(self):
        """Bog afleveres korrekt"""
        self.library.issue_book(self.member_id, self.book_id)
        result = self.library.return_book(self.member_id, self.book_id)
        self.assertTrue(result)

    def test_search_books_by_title(self):
        """Søgning på titel virker"""
        results = self.library.search_books("Hobitten")
        self.assertEqual(len(results), 1)

if __name__ == "__main__":
    unittest.main()