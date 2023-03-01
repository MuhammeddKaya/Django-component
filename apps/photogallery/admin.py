from django.contrib import admin
from apps.photogallery.models import GalleryPhoto, PhotoGallery
# Register your models here.

admin.site.register(GalleryPhoto)
admin.site.register(PhotoGallery)