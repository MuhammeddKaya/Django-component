from django.contrib import admin
from apps.genaralApp.models import Domain, Template, Language

# Register your models here.
admin.site.register(Domain)
admin.site.register(Template)
admin.site.register(Language)