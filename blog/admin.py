from django.contrib import admin
from .models import Post, Comment

# Using Post models for register
admin.site.register(Post)

# Using Comment models for register
admin.site.register(Comment)