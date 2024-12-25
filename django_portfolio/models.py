from django.db import models
from django.utils import timezone

class Newsletter(models.Model):
    newsletter_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
