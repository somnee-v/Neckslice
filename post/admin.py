from django.contrib import admin
from post.models import Comment, Post

# Register your models here.
admin.site.register(Comment)
admin.site.register(Post)