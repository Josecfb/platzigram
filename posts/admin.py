from django.contrib import admin
from django.db import models

from posts.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','user','title','photo','created' )