from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

class PhotoGallery(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.ImageField(upload_to='Albüm', blank=True,default='assets/img/slide/slide-1.jpg')  #  Image olacak 
    Slug = models.SlugField(max_length=1000, unique=True, blank=True)
    IsDeleted = models.BooleanField(default=False)
    IsActive = models.BooleanField(default=True)
    PublishedAt = models.DateTimeField(default=timezone.now)


    class Meta:
       db_table="PhotoGallery"

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.Title

   

# class GalleryPhoto(models.Model):
#     Album = models.ForeignKey(PhotoGallery, on_delete=models.PROTECT, verbose_name="Albüm")    
#     Photo = models.ImageField(upload_to='uploadfiles/Albümİmage', blank=True)
#     IsDeleted = models.BooleanField(default=False)
#     IsActive = models.BooleanField(default=True)

#     class Meta:
#        db_table="GalleryPhoto"


#     def __str__(self):
#         return self.

class Video(models.Model):
    Title = models.CharField(max_length=255)
    Link = models.URLField(blank=False) #  Image olacak 
    Slug = models.SlugField(max_length=1000, unique=True, blank=True)
    IsDeleted = models.BooleanField(default=False)
    IsActive = models.BooleanField(default=True)

    class Meta:
       db_table="Video"


    def __str__(self):
        return self.Title