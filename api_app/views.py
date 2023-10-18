from rest_framework import viewsets
from .models import BookModel
from .serializers import BookModelSerializer

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializer