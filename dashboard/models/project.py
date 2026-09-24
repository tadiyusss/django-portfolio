import os

from django.db import models

from .language import Language


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=100)
    sub_heading = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    name = models.CharField(max_length=100)
    demo_url = models.URLField(blank=True, null=True)
    source_url = models.URLField(blank=True, null=True)
    languages = models.ManyToManyField(Language)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)

        super().delete(*args, **kwargs)