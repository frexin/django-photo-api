from api.models import Photo
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ['date', 'place', 'img']
