from django.contrib import admin
from blog.models import Tag, Post, Comment, AuthorProfile


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'summary')

class CommentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("content",)}
    list_display = ('creator', 'content')

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(AuthorProfile)
