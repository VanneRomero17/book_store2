from django.urls import include, path
from rest_framework import routers

# Definición de vistas
from .views import *

# Creación del router
router = routers.DefaultRouter()

# Registro de vistas
router.register(r'genres', GenreViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'books-authors', BookAuthorViewSet)

# Definición de URLpatterns
urlpatterns = [
    path("api/v1/", include(router.urls)),
]
