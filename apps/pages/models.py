from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from apps.genaralApp.models import Language


LAYOUT_CHOICES=(
    ('_layout01.html', 'Layout-1'),
    ('_layout02.html', 'Layout-2'),
    ('_layout03.html', 'Layout-3'),
    ('_layout04.html', 'Layout-4'),
)



# Create your models here.
class Pages(MPTTModel):
    home = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    PageTitle = models.CharField(max_length=250)
    PageName = models.SlugField(max_length=512, unique=True, allow_unicode=True)
    PageText = models.TextField(blank=True, null=True)
    PageOrder = models.IntegerField(default=0)
    PageRedirect = models.CharField(max_length=2083, null=True, blank=True)
    Keywords = models.TextField(default="")
    Description = models.TextField(default="")
    IsEnable = models.BooleanField(default=True)
    IsMenu = models.BooleanField(default=False)
    IsUnit = models.BooleanField(default=False)
    Layout = models.CharField(max_length=14,choices=LAYOUT_CHOICES, default='_layout01.html')
    Slug = models.SlugField(max_length=1000, unique=True, blank=True)
    Language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, null=True)
    Created_at = models.DateTimeField(auto_now_add=True)



    class MPTTMeta:
        order_insertion_by = ['home']


    class Meta:
       db_table="Pages"

    def __str__(self):
        return self.PageTitle
    
    def save(self, *args, **kwargs):
        self.Slug = slugify(self.PageTitle)
        return super().save(*args, **kwargs)
    

