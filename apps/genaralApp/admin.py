from django.contrib import admin
from apps.genaralApp.models import Domain, Template, Language, FAQ

# Register your models here.
admin.site.register(Domain)
admin.site.register(Template)
admin.site.register(Language)
admin.site.register(FAQ)