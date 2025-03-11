from library import Book, LibraryMember, PremiumMember


library_books = [
    Book("1984"),
    Book("To Kill a Mockingbird"),
    Book("The Great Gatsby"),
    Book("Moby Dick"),
    Book("Pride and Prejudice")
]

members = {
    "101": LibraryMember("Alice", "101"),
    "102": PremiumMember("Bob", "102")
}

def main():
    while True:
        action = input("\nEnter 'b' to borrow a book, 'r' to return a book, 'c' to check borrowed books, or 'exit' to quit: ").strip().lower()

        if action == "exit":
            print("Exiting... Goodbye!")
            break

        member_id = input("Enter your Member ID: ").strip()
        member = members.get(member_id)

        if not member:
            print("Invalid Member ID.")
            continue

        if action == "b":
            book_title = input("Enter book title to borrow: ").strip()
            book_to_borrow = next((book for book in library_books if book.title.lower() == book_title.lower()), None)

            if book_to_borrow:
                member.borrow_book(book_to_borrow, library_books)
            else:
                print("Book not found or already borrowed.")

        elif action == "r":
            book_title = input("Enter book title to return: ").strip()
            book_to_return = next((book for book in member.borrowed_books if book.title.lower() == book_title.lower()), None)

            if book_to_return:
                member.return_book(book_to_return, library_books)
            else:
                print("You haven't borrowed this book.")

        elif action == "c":
            member.check_borrowed_books()

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
