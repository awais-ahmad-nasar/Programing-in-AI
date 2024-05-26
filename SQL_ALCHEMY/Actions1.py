
######<><><<><> SIMPLE CODE <>><><<>###########

#...................Add and show data..........................
from sqlalchemy.orm import sessionmaker
from model1 import Book, engine

Session = sessionmaker(bind=engine)
s = Session()

def addBook():
    book = Book(id=3, title='PAI', author='Anees')
    s.add(book)
    s.commit()

def allBook():
    books = s.query(Book).all()
    for book in books:
        print(f"Book ID: {book.id}, Book Title: {book.title}, Book Author: {book.author}")

# Add a book to the database
addBook()
allBook()


#####################################################################################
#.....................Delete a Record....................

Session = sessionmaker(bind=engine)
s = Session()

def addBook():
    book = Book(title='C++', author='John')
    s.add(book)
    s.commit()

def deleteBook(book_id):
    book = s.query(Book).filter(Book.id == book_id).first()
    if book:
        s.delete(book)
        s.commit()
    else:
        print(f"Book with ID {book_id} not found.")

def allBook():
    books = s.query(Book).all()
    for book in books:
        print(f"Book ID: {book.id}, Book Title: {book.title}, Book Author: {book.author}")


allBook()
deleteBook(1)  # Delete a book by ID
print("\nAfter Delete the Record now All Books\n")
allBook()



######<><><<><> little bit SIMPLE CODE <>><><<>###########



Session = sessionmaker(bind=engine)
s = Session()

def addBook(id, title, author):
    book = Book(id=id, title=title, author=author)
    s.add(book)
    s.commit()

def allBook():
    books = s.query(Book).all()
    for book in books:
        print(f"Book ID: {book.id}, Book Title: {book.title}, Book Author: {book.author}")

# Add multiple books to the database
addBook(2, 'Csharp', 'Ibrahim')
addBook(3, 'Python', 'Mike')
addBook(4, 'JavaScript', 'Sara')

# Print out all the books in the database
allBook()


#...........................OR............................
Session = sessionmaker(bind=engine)
s = Session()

def addBook(id, title, author):
    book = Book(id=id, title=title, author=author)
    s.add(book)
    s.commit()

def allBook():
    books = s.query(Book).all()
    for book in books:
        print(f"Book ID: {book.id}, Book Title: {book.title}, Book Author: {book.author}")

# Add multiple books to the database
while True:
    id = int(input("Enter the ID of the book (or press 's' to stop adding books): "))
    if id == 's':
        break
    if id < 1:
        print("Invalid ID. Try again.")
        continue
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    addBook(id, title, author)

# Print out all the books in the database
allBook()


