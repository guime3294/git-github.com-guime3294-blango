from django.contrib import admin
from blog.models import Tag, Post, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'summary')

class CommentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("creator")}
    list_display = ('creator', 'content')

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
