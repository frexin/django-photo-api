from django.contrib import admin
from api.models import Photo
from imagekit.admin import AdminThumbnail
from django.utils.html import format_html


class PhotoAdmin(admin.ModelAdmin):
    pass

    list_display = ['id', 'thumbnail', 'place']

    image_display = AdminThumbnail(image_field='img')
    image_display.short_description = 'Image'

    fields = ['image_display']
    readonly_fields = ['image_display']

    def thumbnail(self, obj):
        return format_html('<img src="/uploads/{}" style="width: 130px; \
                           height: 100px"/>'.format(obj.img))


admin.site.register(Photo, PhotoAdmin)