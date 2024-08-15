>>> from bookshelf.models import Book
>>> retrieve_book = Book.objects.get(title = "1984")
>>> print(retrieve_book)
# Expected outcome : [<Book: 1984 by George Orwell year 1949>]>

