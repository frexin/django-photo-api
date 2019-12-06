from rest_framework.test import APITestCase
from api.models import Photo
from rest_framework.test import APIClient
from django.conf import settings
import os

settings.MEDIA_ROOT = 'test_uploads'


class PhotosTests(APITestCase):

    client = APIClient()
    url = '/api/photos/'

    def setUp(self):
        photo = Photo(place='spb', img='cube.png', date='2019-12-06T11:44:05.575178Z')
        photo.save()

        photo = Photo(place='moscow', img='cup.jpg', date='2019-11-06T10:44:05.575178Z')
        photo.save()

    def test_photos_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEquals(len(response.data), 2)

    def test_photos_filter(self):
        response = self.client.get(self.url, {"size": 53687})

        self.assertEqual(response.status_code, 200)
        self.assertEquals(len(response.data), 1)

    def test_one_photo(self):
        response = self.client.get(self.url + '1/')

        photo = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEquals(photo['place'], 'spb')
        self.assertEquals(photo['img'], 'http://testserver/uploads/cube.png')

    def test_upload_photo(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(this_dir, os.pardir, 'test_uploads/cube.png')

        test_file = open(path, 'rb')
        data = {"img" : test_file, "place": "omsk"}

        response = self.client.post(self.url, data, format='multipart')

        self.assertEquals(response.status_code, 201)
        self.assertIn('place', response.data)
        self.assertIn('img', response.data)