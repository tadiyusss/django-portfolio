import os

from django.db import models


class UploadedAsset(models.Model):
    file_id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to="assets/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

    def delete(self, *args, **kwargs):
        if self.file and os.path.isfile(self.file.path):
            os.remove(self.file.path)

        super().delete(*args, **kwargs)