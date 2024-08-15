from .models import Author, Book, Library , Librarian

def query_by_author(author_name):
 try:
  
   author = Author.objects.get(name = author_name)
   books = Book.objects.filter(author = author)
   return books
 except :
   return f"Author does not exist"

def List_all_books_in_a_library(library_name):
  books = Library.objects.get(name = library_name) , books.all()
    
def librarian_for_library(library_name):
   lib = Library.objects.get(name= library_name)
   libra = Librarian.objects.get(library = lib)
   return libra
