from django.contrib import admin
from apps.photogallery.models import PhotoGallery, Video #GalleryPhoto
# Register your models here.

#admin.site.register(GalleryPhoto)
admin.site.register(PhotoGallery)
admin.site.register(Video)