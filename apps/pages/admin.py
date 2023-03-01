from apps.pages.models import Pages
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin


admin.site.register(Pages,DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)