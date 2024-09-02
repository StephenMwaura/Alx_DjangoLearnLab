from rest_framework import serializers
from datetime import datetime
from .models import Book
from .models import Author
class BookSerializer(serializers.ModelSerializer): # converts complex data into json or deserilizers. The modelserilizer allow the crud operations.
    class Meta: # must be defined 
        model = Book
        fields = '__all__' # all fields of the Book model are shown
    def validate(self , data): # checks if the published_year of the Book model is not in the future.
        if data['published_year'] > datetime.now().year:
            raise serializers.ValidationError("Published year cannot be in the future.")
        return data

class AuthorSerializer(serializers.ModelSerializer):
    # this instance will include all books related to the author
    books = BookSerializer(many = True, read_only = True) # nested serializer of the BookSerializer due to presence of foreign key.
    class Meta:
        model = Author
        fields = [
            'name','books'
        ]