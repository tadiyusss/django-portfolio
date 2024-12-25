from django.contrib import admin
from .models import *

# allow editing of Language model in the admin panel

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['language_id', 'image', 'name', 'short_description', 'background_color', 'created_at']
    search_fields = ['name', 'short_description']
    list_filter = ['created_at']
    

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'heading', 'sub_heading', 'description', 'image', 'name', 'demo_url', 'source_url', 'created_at']
    search_fields = ['heading', 'sub_heading', 'description', 'name']
    list_filter = ['created_at']

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['testimonial_id', 'name', 'image', 'position', 'company', 'message', 'created_at']
    search_fields = ['name', 'position', 'company', 'message']
    list_filter = ['created_at']

class UploadedAssetsFormAdmin(admin.ModelAdmin):
    list_display = ['file_id', 'file', 'created_at']
    search_fields = ['file']
    list_filter = ['created_at']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_id', 'title', 'subheading', 'image', 'content', 'published', 'created_at']
    search_fields = ['title', 'content']
    list_filter = ['created_at']

admin.site.register(Blog, BlogAdmin)
admin.site.register(UploadedAsset, UploadedAssetsFormAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Language, LanguageAdmin)