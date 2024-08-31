from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'Book' ,BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("", BookList.as_view(), name="book_list_view"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
