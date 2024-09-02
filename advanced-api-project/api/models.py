from django.db import models

# Create your models here.
class Author(models.Model): # the author model which contains the name ot the author of the book model
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Book(models.Model): # Book model contains the title of the book and the year it was published.
    title = models.CharField(max_length=30)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE , related_name="books") # the author is a foreign key since it references to the author model .The name of the author.
    def __str__(self):
        return self.title 