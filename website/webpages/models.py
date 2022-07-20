from django.db import models
from django.utils import timezone
# Create your models here.
class job(models.Model):
    name = models.CharField(max_length = 300)
    job_type =  models.CharField(max_length = 200)
    contacts = models.IntegerField()
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name