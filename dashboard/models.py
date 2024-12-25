from django.db import models
from django.contrib.auth.models import User
import os

class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='django_portfolio/static/languages', null = False)
    name = models.CharField(max_length=100, null = False)
    background_color = models.CharField(max_length=100, null = False)
    short_description = models.TextField(null = False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)
    
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=100, null = False)
    sub_heading = models.CharField(max_length=100, null = False)
    description = models.TextField(null = False)
    image = models.ImageField(upload_to='django_portfolio/static/projects', null = False)
    name = models.CharField(max_length=100, null = False)
    demo_url = models.URLField(blank=True, null=True)
    source_url = models.URLField(blank=True, null=True)
    languages = models.ManyToManyField(Language)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str_(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)
    
class Testimonial(models.Model):
    testimonial_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null = False)
    image = models.ImageField(upload_to='django_portfolio/static/testimonials', null = False)
    position = models.CharField(max_length=100, null = False)
    company = models.CharField(max_length=100, null = False)
    message = models.TextField(null = False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

class UploadedAsset(models.Model):
    file_id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='django_portfolio/static/assets', null = False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    
    def delete(self, *args, **kwargs):
        if self.file and os.path.isfile(self.file.path):
            os.remove(self.file.path)
        super().delete(*args, **kwargs)
    
class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null = False)
    subheading = models.CharField(max_length=100, null = False)
    image = models.ImageField(upload_to='django_portfolio/static/blogs', null = False)
    content = models.TextField(null = False)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)