from django.contrib import admin
from .models import Post, Tag, User

# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(User)
