from api.serializers import FileSerializer
from api.models import Photo
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
import django_filters.rest_framework


# class CsrfExemptSessionAuthentication(SessionAuthentication):
#     def enforce_csrf(self, request):
#         return None


class PhotosList(ModelViewSet):

    parser_classes = [MultiPartParser, FileUploadParser]
    serializer_class = FileSerializer

    queryset = Photo.objects.all()

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['date', 'size']

    def perform_create(self, serializer):
        serializer.save(img=self.request.data.get('img'))

        return Response(True, status=status.HTTP_201_CREATED)

    # def get_queryset(self):



    #
    # def get(self, request):
    #     photos = Photo.objects.all()
    #     serializer = PhotoSerializer(photos, many=True)
    #
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #
    #     serializer = FileSerializer(data=request.data)
    #     obj = serializer.instance
    #
    #     # import pdb; pdb.set_trace()
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
