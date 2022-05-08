from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils import timezone


class Config(models.Model):

    key = models.CharField(
        verbose_name='Config key name',
        max_length=30,
        blank=True,
        null=True,
        unique=True,
    )
    value = models.CharField(
        verbose_name='Config value',
        max_length=100,
        blank=True,
        null=True,
    )


class Tag(models.Model):

    def __str__(self):
        """On the admin page of model which uses Tag as a foreignkey,
        dropdown displays this."""
        return self.code

    code = models.CharField(
        verbose_name='Tag code, used for url for example',
        max_length=20,
        blank=False,
        null=False,
        unique=True,
    )

    name_ja = models.CharField(
        verbose_name='Tag name in Japanese',
        max_length=20,
        blank=False,
        null=False,
    )

    name_en = models.CharField(
        verbose_name='Tag name in English',
        max_length=20,
        blank=False,
        null=False,
    )

    count = models.IntegerField(
        verbose_name='How many posts belongs to this tag.',
        blank=True,
        null=True,
    )


class Year(models.Model):

    def __str__(self):
        """On the admin page of model which uses Year as a foreignkey,
        dropdown displays this."""
        return self.code

    code = models.CharField(
        verbose_name='Year code, used for url for example',
        max_length=20,
        blank=False,
        null=False,
        unique=True,
    )

    count = models.IntegerField(
        verbose_name='How many posts belongs to this year.',
        blank=True,
        null=True,
    )


class Post(models.Model):

    @classmethod
    def available(cls):
        return (cls.objects
                .filter(publish_at__lte=timezone.now()))

    code = models.CharField(
        verbose_name='Post code, used for url for example',
        max_length=50,
        blank=False,
        null=False,
        unique=True,
    )

    publish_at = models.DateTimeField(
        verbose_name='Date to publish',
        blank=True,
        null=True,
    )

    tag = models.ForeignKey(
        Tag,
        verbose_name='Tag for this post',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        default=1,
    )

    year = models.ForeignKey(
        Year,
        verbose_name='Year for this post',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    title_ja = models.CharField(
        verbose_name='Title in Japanese',
        max_length=100,
        blank=True,
        null=True,
    )

    title_en = models.CharField(
        verbose_name='Title in English',
        max_length=100,
        blank=True,
        null=True,
    )

    body_ja = MarkdownxField(
        verbose_name='Body in Japanese',
        help_text='Markdown',
        blank=True,
        null=True,
    )

    body_en = MarkdownxField(
        verbose_name='Body in English',
        help_text='Markdown',
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        auto_now=True,
    )

    thumbnail = models.CharField(
        verbose_name='Thumbnail image name',
        max_length=50,
        blank=True,
        null=True,
    )

    html = models.TextField(
        verbose_name='Body written with html, this column is used when markdown column is empty',
        blank=True,
        null=True,
    )

    def get_markdownified_body_ja(self):
        return markdownify(self.body_ja)

    def get_markdownified_body_en(self):
        return markdownify(self.body_en)


class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        verbose_name='属する記事',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    comment_at = models.DateTimeField(
        verbose_name='Commented date',
        blank=True,
        null=True,
    )

    name = models.CharField(
        verbose_name='Commenter name',
        max_length=50,
        blank=True,
        null=True,
    )

    body = models.TextField(
        verbose_name='Body',
        blank=True,
        null=True,
    )


class Link(models.Model):
    """The model for displaying bidirectional link."""

    parent_post = models.ForeignKey(
        Post,
        verbose_name='Parent post',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        # related_name argument is needed when one model has foreignkeys of same model.
        related_name='parent_post',
    )

    linked_post = models.ForeignKey(
        Post,
        verbose_name='Post kept by parent post',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='linked_post',
    )
