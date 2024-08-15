from .models import Author, Book, Library , Librarian

def Query_all_books_by_a_specific_author(author_name):
  author = Author.objects.get(name=author_name)
  books = Book.objects.filter(author=author)
  return books

def List_all_books_in_a_library(library_name):
  library = Library.objects.get(name=library_name)
  books = library.books.all()
  return books
    
def Retrieve_the_libranian_for_a_library(library_name):
   library = Library.objects.get(name=library_name)

   libranian = Librarian.objects.get(library=library)
   return Librarian
