from django.contrib import admin
from app.models import (
    Config,
    Tag,
    Year,
    Post,
)
from markdownx.admin import MarkdownxModelAdmin
from app.bizlogic import (
    image_bizlogic,
    tag_bizlogic,
    year_bizlogic,
    link_bizlogic,
)
from django.utils.html import format_html
from app.usrlib import date_utils


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

    def get_changeform_initial_data(self, request):

        # NOTE: Model の default=date_utils.get_current_year_id() に頼らず、
        #       編集ページ表示時のデフォルト値を動的にするために追加。
        #       新規編集のときのみ初期値を current_year にします。
        return {'year': date_utils.get_current_year_id()}

    def save_model(self, request, obj, form, change):
        """Describe what you want to do before saving.
        request : For example, <WSGIRequest: POST '/admin/app/post/1/change/'>
        obj     : For example, Post object (1)
        form    : form html data
        change  : For example, True

        Request as well as obj has edited data. How to get old values? I don't know.
        """

        # Create thumbnail.
        # Using obj.thumbnail, when thumbnail form is empty it will get not empty string but None.
        image_bizlogic.generate_thumbnail(request.POST['thumbnail'])

        # Update count column on Tag and Year tables.
        tag_bizlogic.update_count()
        year_bizlogic.update_count()

        # Create bidirectional link.
        link_bizlogic.register_link(obj)

        super().save_model(request, obj, form, change)

    def publish_page_link(self, obj):
        """Display page link on admin page Post list."""
        return format_html(f'<a href="/ja/{obj.code}">{obj.code}</a>')
    publish_page_link.short_description = 'CODE AND LINK TO PAGE'


admin.site.register(Config, ConfigAdmin)
admin.site.register(Tag, CodeAdmin)
admin.site.register(Year, CodeAdmin)
admin.site.register(Post, PostAdmin)
