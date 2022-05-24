from django.contrib import admin

from webisland.models import Island


class IslandAdmin(admin.ModelAdmin):
    list_display = ['title', 'country', 'square', 'continent']


admin.site.register(Island, IslandAdmin)
