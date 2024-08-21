from bookshelf.models import Book
>>> delete_book = Book.objects.get
(title = "Nineteen
 Eighty-Four")
>>> delete_book.delete()
(1, {'bookshelf.Book': 1})

# Expected outcome 
 # print(retrieve_book)
  # <[]> no book present