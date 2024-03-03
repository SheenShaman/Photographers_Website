from django.contrib import admin

from main.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content', 'image', 'creation_date', 'is_published')
