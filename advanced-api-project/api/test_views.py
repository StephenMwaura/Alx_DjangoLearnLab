from rest_framework.test import  APIClient ,  APITestCase # for testing
from .models import Book , Author # the models being tested
from .views import BookCreateView
from django.urls import reverse # reverse url names into actual urls
from rest_framework import status # used for testing status code
from django.contrib.auth.models import User # used for authentication
class BookAPITests(APITestCase): # creatig a test for testing the api actions
    def setUp(self): # called before each test
      # creating a test client to test Api requests
      self.client = APIClient
      # creating a test user with a username and password to test for authentication
      self.user = User.objects.create_user(username='usertest' , password='testpassword')
      # logging in as the test user
      self.client.login(username='usertest' , password='testpassword')
      # creating an author
      self.author = Author.objects.create(name = "Test Author")

      #creating some sample books
      self.book1 = Book.objects.create(
         title = "Testing", author = self.author , published_year = 2010
      )
      self.book2 = Book.objects.create( # creating books instance the author comes from the above self.author
         title = "Test2" , author = self.author , published_year = 2006
      )

      def tearDown(self):
         # logging out after each and every test
         self.client.logout()

    def test_creating_book(self):
       url = reverse('books/create') # defining the url
       data = { # contains the information of the new book
          "title" : "Testing Book",
          "author": self.author.id,
          "published_year": 2020
       }

       response = self.client.post(url,data,format='json') # simulates sending a post request to the server to create a new book
    # check status code 201 created
       self.assertEqual(response.status_code , status.HTTP_201_CREATED)

       # verifying that the book is saved corretly
       self.assertEqual(Book.objects.count(),3)
       self.assertEqual(Book.objects.get(title = "Testing Book").title, "Testing Book")

       def test_get_books(self):
          url = reverse('books')

        # send a get request to retrieve all books
          response = self.client.get(url) # it opens the books url to see if it will function
          # checks if the status code is 200 ok
          # the response used in the below code is the one for the client
          self.assertEqual(response.status_code, status.HTTP_200_OK)
        # checks if two books are returned
          self.assertEqual(len(response.data),2)

          def test_update_book(self):
             # gets the url for updating the book by its id

            url = reverse('books/update', kwargs = {'pk':self.book1.id})
              # define the data for updating the book

            data = {
                "title" : "Updated title",
                "author" : self.author.id, 
                "published_year" : 2020
             }
            # send a put rquest to update the book
            response = self.client.put(url, data, format='json')

            # checks if the status code is correct
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.book1.refresh_from_db() # we reload the book
            self.assertEqual(self.book1.title, "Updated title")

            def test_delete_book(self):
               url = reverse('books/delete' , kwargs={'pk':self.book1.id})

               response = self.client.delete(url) # sends a delete request to remove the book
               # after deleting we check if the status code is 204 no content since it is deleted
               self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

            # authentication tests
            def test_unauthenticated(self):
               # logging the user out so as to show the unauthenticated error
               self.client.logout()
               url = reverse('books/create')
               data = {
                    "title": "Unauthorized Book",
                    "author": self.author.id,
                    "published_year": 2023
                }
               response = self.client.post(url, data, format='json')

                # Check if the status code is 403 Forbidden
               self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


               
          



       