from django.contrib import admin
from app.models import *
from markdownx.admin import MarkdownxModelAdmin
from app.bizlogic import image_bizlogic, tag_bizlogic, year_bizlogic
from app.usrlib import common
from django.utils.html import format_html


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
    list_display = ('title_ja', 'publish_page_link', 'publish_at')
    ordering = ('-created_at',)
    search_fields = ('title_ja', 'code', 'publish_at')

    def save_model(self, request, obj, form, change):
        """Describe what you want to do before saving.
        request : For example, <WSGIRequest: POST '/admin/app/post/1/change/'>
        obj     : For example, Post object (1)
        form    : form html data
        change  : For example, True
        """

        # Create thumbnail.
        image_bizlogic.generate_thumbnail(request.POST['thumbnail'])

        # Update count column on Tag and Year tables.
        tag_bizlogic.update_count()
        year_bizlogic.update_count()

        super().save_model(request, obj, form, change)

    def publish_page_link(self, obj):
        """Display page link on admin page Post list."""
        return format_html(f'<a href="/ja/{obj.code}">{obj.code}</a>')
    publish_page_link.short_description = 'CODE AND LINK TO PAGE'


admin.site.register(Config, ConfigAdmin)
admin.site.register(Tag, CodeAdmin)
admin.site.register(Year, CodeAdmin)
admin.site.register(Post, PostAdmin)
