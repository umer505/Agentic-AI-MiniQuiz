books = {
    "1984": {"author": "Orwell", "available": True},
    "Dracula": {"author": "Stoker", "available": True},
    "The Great Gatsby": {"author": "Fitzgerald", "available": True},
    "To Kill a Mockingbird": {"author": "Lee", "available": True},
    "The Catcher in the Rye": {"author": "Salinger", "available": True},
    "The Hobbit": {"author": "Tolkien", "available": True},
    "Fahrenheit 451": {"author": "Bradbury", "available": True},
    "Pride and Prejudice": {"author": "Austen", "available": True},
    "The Picture of Dorian Gray": {"author": "Wilde", "available": True},
    "Brave New World": {"author": "Huxley", "available": True},
    "The Lord of the Rings": {"author": "Tolkien", "available": True},
    "The Chronicles of Narnia": {"author": "Lewis", "available": True},
    "The Alchemist": {"author": "Coelho", "available": True},
    "The Da Vinci Code": {"author": "Brown", "available": True},
}

def display_books():
    print("\nAvailable Books:")
    for title, details in books.items():
        if details["available"]:
            print(f"{title} by {details['author']}")

def borrow_book(title):
    if title in books and books[title]["available"]:
        books[title]["available"] = False
        print(f"You have borrowed '{title}'.")
    else:
        print(f"Sorry, '{title}' is not available.")

def return_book(title):
    if title in books and not books[title]["available"]:
        books[title]["available"] = True
        print(f"You have returned '{title}'.")
    else:
        print(f"Sorry, '{title}' was not borrowed or does not exist.")

def add_book(title, author):
    if title not in books:
        books[title] = {"author": author, "available": True}
        print(f"'{title}' by {author} has been added to the library.")
    else:
        print(f"'{title}' already exists in the library.")

def view_borrowed_books():
    print("\nBorrowed Books:")
    for title, details in books.items():
        if not details["available"]:
            print(f"{title} by {details['author']}")


print("Welcome to the Library Book Management System!")
print("\nOptions:")

print("1. View all books")
print("2. Borrow a book")
print("3. Return a book")
print("4. Add a new book")
print("5. View borrowed books")
print("6. Exit")

while True:
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == '1':
        display_books()
    elif choice == '2':
        title = input("Enter the title of the book you want to borrow: ")
        borrow_book(title)
    elif choice == '3':
        title = input("Enter the title of the book you want to return: ")
        return_book(title)
    elif choice == '4':
        title = input("Enter the title of the new book: ")
        author = input("Enter the author of the new book: ")
        add_book(title, author)
    elif choice == '5':
        view_borrowed_books()
    elif choice == '6':
        print("Thank you for using the Library Book Management System!")
        break
    else:
        print("Invalid choice. Please try again.")