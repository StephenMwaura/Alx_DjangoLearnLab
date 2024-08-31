from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'Book' ,BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("", BookList.as_view(), name="book_list_view"),

]
