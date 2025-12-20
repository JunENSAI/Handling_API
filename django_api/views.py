from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.throttling import ScopedRateThrottle

    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'heavy_view'