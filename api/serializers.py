from api.models import Photo
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):

    # img = serializers.ImageField()
    # path_to_img = serializers.ImageField(source='img')
    # path_to_img = serializers.SerializerMethodField('img')

    class Meta:
        model = Photo
        fields = ['date', 'place', 'img']
