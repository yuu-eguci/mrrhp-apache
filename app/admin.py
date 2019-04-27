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


class CodeAdmin(admin.ModelAdmin):
    list_display = ('code',)


class PostAdmin(MarkdownxModelAdmin):
    list_display = ('title_ja', 'code', 'publish_at')
    ordering = ('created_at',)
    search_fields = ('title_ja', 'code', 'publish_at')


admin.site.register(Config, ConfigAdmin)
admin.site.register(Tag, CodeAdmin)
admin.site.register(Year, CodeAdmin)
admin.site.register(Post, PostAdmin)
