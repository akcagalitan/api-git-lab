
from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title