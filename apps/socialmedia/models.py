from django.db import models
from django.utils.text import slugify


class Socialmedia(models.Model):
    Title = models.CharField(max_length=45)
    Description = models.CharField(max_length=150)
    Icon = models.TextField(null=True)
    Code = models.TextField()
    #Slug = models.SlugField(max_length=1000, unique=True, blank=True)
    #Created_at = models.DateTimeField(auto_now_add=True)
    #IsActive = models.BooleanField(default=True)
    #IsDeleted = models.BooleanField(default=False)


    class Meta:
       db_table="Socialmedia"

    def __str__(self):
        return self.Title
    
    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Title)
        return super().save(*args, **kwargs)