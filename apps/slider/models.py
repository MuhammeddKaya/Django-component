from django.db import models
from django.utils.text import slugify




class Slider(models.Model):
    Title = models.CharField( max_length=250)
    Text = models.TextField()
    Description = models.TextField(blank=True, null=True,  help_text="Bu kısım web sayfasında gözükmeyecektir. Sadece bilgilendirme amaçlıdır. ")
    Image = models.ImageField(upload_to='sliderImage', blank=True,default='assets/img/slide/slide-1.jpg')
    StartDate = models.DateTimeField()
    EndDate = models.DateTimeField()
    Slug = models.SlugField(max_length=1000, unique=True, blank=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)
    IsDeleted = models.BooleanField(default=False)


    class Meta:
       db_table="Slider"

    def __str__(self):
        return self.Title
    
    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Title)
        return super().save(*args, **kwargs)