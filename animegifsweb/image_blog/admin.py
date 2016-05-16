from django.contrib import admin
from .models import RssUrl




class RssUrlAdmin(admin.ModelAdmin):
    list_display = ('rss_name', 'rss_url', 'active')
    list_editable = ('active',)
admin.site.register(RssUrl, RssUrlAdmin)