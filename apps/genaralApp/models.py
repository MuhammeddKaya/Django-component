from django.db import models
from django.contrib.sites.models import Site
from django.utils.text import slugify



# Create your models here.
class Template(models.Model):
    TemplateName = models.CharField(max_length=80)
    IsActive = models.BooleanField(default=False)

    class Meta:
        db_table="Template"
    
    def __str__(self):
        return self.TemplateName
    

class Domain(models.Model):  
    DomainName = models.CharField(max_length=100)
    Site = models.OneToOneField(Site, on_delete=models.SET_NULL, null=True, verbose_name='Site',related_name='Site')
    Template = models.ForeignKey(Template, on_delete=models.DO_NOTHING, verbose_name='Template')
    IsActive = models.BooleanField( default=True)

    class Meta:
        db_table="Domain"
    
    def __str__(self):
        return self.DomainName


class Language(models.Model):
    LanguageCode = models.CharField(max_length=10)
    LanguageName = models.CharField(max_length=100)
    IsActive = models.BooleanField(default=True)

    class Meta:
        db_table="Language"
    
    def __str__(self):
        return self.LanguageName


class FAQ(models.Model):
    '''Sıkça sorulan sorular modeli'''
    Question = models.TextField()
    Answer = models.TextField()
    Order = models.PositiveIntegerField(default=1)
    IsDeleted = models.BooleanField(default=False)
    IsActive = models.BooleanField(default=True)


    class Meta:
       db_table="FAQ"

    def __str__(self):
        return self.Question
    
    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Question)
        return super().save(*args, **kwargs)


class Post(models.Model):
    Name = models.CharField(max_length=30)
    SurName = models.CharField(max_length=30)
    Email= models.EmailField()
    Comment = models.TextField()
    IsCreated=models.TimeField(auto_now_add=True)
        
    class Meta:
        db_table="Post"
        
    def __str__(self):
        return f"{self.Name}-{self.SurName}-{self.Email}"