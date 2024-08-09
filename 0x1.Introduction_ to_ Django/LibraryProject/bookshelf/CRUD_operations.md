### Create Operation

from bookshelf.models import Book
book1 = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)
# Successfully created a book instance and saved it to the database.

### from retrieve_md document
>>> from bookshelf.models import Book
>>> retrieve_book = Book.objects.all()
>>> print(retrieve_book)
# Expected outcome : [<Book: 1984 by George Orwell year 1949>]>


### from update.md document
>>> book_update = Book.objects.get(title = "1984")
>>> book_update.title = "Nineteen Eighty-Four"
>>> book_update.save()

# Expected outcome 
>>> print(retrieve_book)
 # [<Book: Nineteen Eighty-Four by George Orwell year 1949>]>

 
### from delete_md 
>>> delete_book = Book.objects.get(title = "Nineteen
 Eighty-Four")
>>> delete_book.delete()
(1, {'bookshelf.Book': 1})

# Expected outcome 
 # print(retrieve_book)
  # <[]> no book present

