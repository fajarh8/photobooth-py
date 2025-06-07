from django.db import models
from booth.models import Photo

# Create your models here.
class PrintQueue(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    printed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    printed_at = models.DateTimeField(null=True, blank=True)
