from rest_framework import serializers
from .models import BookModel

class BookModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'