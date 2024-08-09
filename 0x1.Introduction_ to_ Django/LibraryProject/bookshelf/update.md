>>> book_update = Book.objects.get(title = "1984")
>>> book_update.title = "Nineteen Eighty-Four"
>>> book_update.save()

# Expected outcome 
>>> print(retrieve_book)
 # [<Book: Nineteen Eighty-Four by George Orwell year 1949>]>