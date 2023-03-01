from django.db import models
from django.utils.text import slugify
from apps.pages.models import Pages


# Create your models here.



class Component(models.Model):
    ComponentFile = models.CharField(max_length=45)
    ComponentName = models.CharField( max_length=150)
    IsActive = models.BooleanField(default=True)
    IsForUsers = models.BooleanField(default=0)

    class Meta:
        db_table="Component"
        
    def __str__(self):
        return self.ComponentName


LOCATION_CHOICES=(
    ('01H', 'Header'),
    ('02L', 'Left'),
    ('03C', 'Content'),
    ('04R', 'Right'),

)


class ComponentsPages(models.Model):
    ComponentLocation = models.CharField(max_length=3, choices=LOCATION_CHOICES)
    ComponentOrder = models.IntegerField(default=0)
    Component = models.ForeignKey(Component, on_delete=models.DO_NOTHING, related_name="componentsofpage")
    Page = models.ForeignKey(Pages, on_delete=models.DO_NOTHING)
        
    class Meta:
        db_table="ComponentsPages"
        
    def __str__(self):
        return f"{self.ComponentLocation}-{self.Component.ComponentName}-{self.Page.PageName}"
