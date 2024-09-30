from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookListCreateAPIView


router = DefaultRouter() # creates the url for the crud opertions.
router.register(r'Book' ,BookViewSet , BookListCreateAPIView) # creates the url for the models and saves them in the router.

urlpatterns = [
    path('api/', include(router.urls)),
 
]
