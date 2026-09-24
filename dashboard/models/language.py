import os

from django.db import models


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="media/languages")
    name = models.CharField(max_length=100)
    background_color = models.CharField(max_length=100)
    short_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)

        super().delete(*args, **kwargs)