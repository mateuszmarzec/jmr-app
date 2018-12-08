from django.contrib import admin

from shortener.models import LongUrl


class LongUrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'shortcut')


admin.site.register(LongUrl, LongUrlAdmin)
