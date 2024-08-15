from .models import Author, Book, Library , Librarian

def query_by_author(author_name):
 try:
  
   author = Author.objects.get(name = author_name)
   books = Book.objects.filter(author = author)
   return books
 except :
   return f"Author does not exist"

def list_books():
    library_books = Book.objects.all()
    return library_books
def librarian_for_library(library_name):
   lib = Library.objects.get(name= library_name)
   libra = Librarian.objects.get(library = lib)
   return libra
