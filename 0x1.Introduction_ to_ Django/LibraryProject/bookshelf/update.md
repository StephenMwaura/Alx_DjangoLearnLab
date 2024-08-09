>>> book = Book.objects.get(title = "1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()

# Expected outcome 
>>> print(retrieve_book)
 # [<Book: Nineteen Eighty-Four by George Orwell year 1949>]>