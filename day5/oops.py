class Book:
    def __init__(self, title, author, pages, price):
        # Constructor
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self):
        # User-friendly print
        return f"📘 '{self.title}' by {self.author}"

    def __repr__(self):
        # Developer-friendly representation
        return f"Book('{self.title}', '{self.author}', {self.pages}, {self.price})"

    def __len__(self):
        # Length of book (pages)
        return self.pages

    def __eq__(self, other):
        # Check equality by title, author, and pages
        return (
            self.title == other.title and
            self.author == other.author and
            self.pages == other.pages
        )

    def __add__(self, other):
        # Add two books = combined pages + combined price
        new_title = self.title + " & " + other.title
        new_author = self.author + " & " + other.author
        new_pages = self.pages + other.pages
        new_price = self.price + other.price
        return Book(new_title, new_author, new_pages, new_price)

    def __del__(self):
        # Destructor (runs when object is deleted)
        print(f"❌ Book '{self.title}' has been deleted")


# ✅ Let's use the class now

book1 = Book("Python Basics", "Raj", 300, 399)
book2 = Book("Advanced Python", "Raj", 450, 599)

# __str__ demonstration
print(book1)  # 📘 'Python Basics' by Raj

# __repr__ demonstration
print(repr(book2))  # Book('Advanced Python', 'Raj', 450, 599)

# __len__ demonstration
print(len(book1))  # 300

# __eq__ demonstration
print(book1 == book2)  # False

# __add__ demonstration
combined = book1 + book2
print(combined)         # 📘 'Python Basics & Advanced Python' by Raj & Raj
print(len(combined))    # 750
print(combined.price)   # 998

# __del__ demonstration
del book1  # ❌ Book 'Python Basics' has been deleted
