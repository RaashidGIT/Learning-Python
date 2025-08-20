library_books = {"The Great Gatsby", "1984", "To Kill a Mockingbird", "Moby Dick", "Pride and Prejudice"}

while True:
    print("\nLibrary Book Tracker")
    print("1. Add a new book")
    print("2. Issue (remove) a book")
    print("3. Show all available books")
    print("4. Show total number of books")
    print("5. Check if a book is available")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        book = input("Enter book name to add: ").strip()
        if book in library_books:
            print(f"'{book}' is already in the library.")
        else:
            library_books.add(book)
            print(f"'{book}' has been added.")

    elif choice == '2':
        book = input("Enter book name to issue: ").strip()
        if book in library_books:
            library_books.remove(book)
            print(f"'{book}' has been issued.")
        else:
            print(f"'{book}' is not available in the library.")

    elif choice == '3':
        if library_books:
            print("\nAvailable books:")
            for b in library_books:
                print("-", b)
        else:
            print("No books available in the library.")

    elif choice == '4':
        print(f"Total number of books: {len(library_books)}")

    elif choice == '5':
        book = input("Enter book name to check: ").strip()
        if book in library_books:
            print(f"'{book}' is available in the library.")
        else:
            print(f"'{book}' is NOT available in the library.")

    elif choice == '6':
        print("Exiting Library Book Tracker.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
