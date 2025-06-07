import uuid
from django.db import models

# Create your models here.
class UserSession(models.Model):
    session_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField()
    is_paid = models.BooleanField(default=False)
    payment_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

class Frame(models.Model):
    name = models.CharField(max_length=100)
    preview_image = models.ImageField(upload_to='frames/')
    active = models.BooleanField(default=True)

class Filter(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    code = models.CharField(max_length=100)  # nama filter untuk diterapkan via PIL/opencv

class Photo(models.Model):
    session = models.ForeignKey(UserSession, on_delete=models.CASCADE, related_name='photos')
    frame = models.ForeignKey(Frame, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='photos/')
    is_final = models.BooleanField(default=False)  # true jika sudah dipilih user
    created_at = models.DateTimeField(auto_now_add=True)

class PhotoFilter(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
