from django.db import models
from django.contrib.sites.models import Site


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


#class FAQ(models.Model):
#    '''Sıkça sorulan sorular modeli'''
#    Question = models.TextField()
#    Answer = models.TextField()
#    Order = models.PositiveIntegerField(default=1)
#    IsDeleted = models.BooleanField(default=False)
#    IsActive = models.BooleanField(default=True)
#    Page = models.ForeignKey(Pages, on_delete=models.PROTECT, verbose_name="Sayfa", related_name="faqs")
#
#    class Meta:
#       db_table="FAQ"
#
#    def __str__(self):
#        return self.Question
    