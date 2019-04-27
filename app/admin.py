from django.contrib import admin
from app.models import *
from markdownx.admin import MarkdownxModelAdmin


class ConfigAdmin(admin.ModelAdmin):

    list_display = ('key', 'value')
    # readonly_fields = ()
    fields = ('key', 'value')

    def key(self, instance):
        return instance

    def value(self, instance):
        return instance


admin.site.register(Config, ConfigAdmin)
admin.site.register(Post, MarkdownxModelAdmin)
