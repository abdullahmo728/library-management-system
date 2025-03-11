class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book, library_books):
        if book in library_books:
            if len(self.borrowed_books) < 3:  
                self.borrowed_books.append(book)
                library_books.remove(book)
                print(f"{self.name} borrowed: {book}")
            else:
                print("Borrowing limit reached (3 books).")
        else:
            print("Book not available.")

    def return_book(self, book, library_books):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library_books.append(book)
            print(f"{self.name} returned: {book}")
        else:
            print("You haven't borrowed this book.")

    def check_borrowed_books(self):
        if self.borrowed_books:
            print(f"Books borrowed by {self.name}: {', '.join(str(book) for book in self.borrowed_books)}")
        else:
            print(f"{self.name} has not borrowed any books.")


class PremiumMember(LibraryMember):
    def borrow_book(self, book, library_books):
        if book in library_books:
            if len(self.borrowed_books) < 5:  
                self.borrowed_books.append(book)
                library_books.remove(book)
                print(f"{self.name} (Premium) borrowed: {book}")
            else:
                print("Borrowing limit reached (5 books).")
        else:
            print("Book not available.")
