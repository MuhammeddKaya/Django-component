from django.db import models
from django.utils.text import slugify


class Links(models.Model):
    Title = models.CharField(max_length=45)
    Description = models.CharField(max_length=150)
    Link = models.CharField(max_length=500)
    HTMLIcon = models.TextField(max_length=1000)
    Slug = models.SlugField(max_length=1000, unique=True, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)
    IsDeleted = models.BooleanField(default=False)


    class Meta:
       db_table="Links"

    def __str__(self):
        return self.Title
    
    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Title)
        return super().save(*args, **kwargs)
    


