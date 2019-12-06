from api.serializers import FileSerializer
from api.models import Photo
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FileUploadParser
import django_filters.rest_framework


class PhotosList(ModelViewSet):

    parser_classes = [MultiPartParser, FileUploadParser]
    serializer_class = FileSerializer

    queryset = Photo.objects.all()

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['date', 'size']

    def perform_create(self, serializer):
        serializer.save(img=self.request.data.get('img'))

        return Response(True, status=status.HTTP_201_CREATED)