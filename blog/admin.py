from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'view')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Post)
admin.site.register(Comment)