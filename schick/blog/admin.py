from django.db import models
from django.contrib import admin
from tinymce.widgets import TinyMCE
from schick.blog.models import Blog, Post



class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("headline",)}
	search_fields = ("headline", "organization", "byline", "description")
admin.site.register(Post, PostAdmin)
	
class Media:
        js = ['/tiny_mce/tiny_mce.js', '/js/textareas.js']

class BlogAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
admin.site.register(Blog, BlogAdmin)
