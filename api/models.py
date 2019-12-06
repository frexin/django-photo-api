from django.db import models
from django.utils.html import format_html


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=200)
    size = models.IntegerField(default=0)

    img = models.ImageField(upload_to='%Y/%m/%d/')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.size = self.img.size

        super(Photo, self).save(force_insert, force_update, using, update_fields)

    def image_tag(self):
        return format_html('<img src="{}" />').format(self.img)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
