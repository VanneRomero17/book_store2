from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_permissions(self):
      if self.action in ['list', 'retrieve']:
        permission_classes = [permissions.AllowAny]
      else:
          permission_classes = [IsAuthenticated]
      return [permission() for permission in permission_classes]


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookAuthorViewSet(viewsets.ModelViewSet):
    serializer_class = BookAuthorSerializer
    queryset = BookAuthor.objects.all()
