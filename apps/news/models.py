from django.db import models
from django.utils.text import slugify


# Create your models here.
class News(models.Model):
    Title = models.CharField(max_length=250)
    Text = models.TextField(blank=True)
    News_image = models.ImageField(upload_to='uploadfiles/Newsİmage', blank=True)
    News_file = models.FileField(upload_to='uploadfiles/Newsfile', blank=True)
    Slug = models.SlugField(max_length=1000, unique=True, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)
    IsDeleted = models.BooleanField(default=False)


    class Meta:
       db_table="News"

    def __str__(self):
        return self.Title
    
    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Title)
        return super().save(*args, **kwargs)