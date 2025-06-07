import uuid
from datetime import timedelta
from django.db import models
from django.utils import timezone
from apps.adminpanel.models import AdminConfig, CollageDesign, CollageSlot, Filter

# —————————————————————————————————————————————
#  Sesi User
# —————————————————————————————————————————————
class UserSession(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    design      = models.ForeignKey(CollageDesign, null=True, blank=True, on_delete=models.SET_NULL)
    started_at  = models.DateTimeField(null=True, blank=True)
    expires_at  = models.DateTimeField(null=True, blank=True)
    email       = models.EmailField(null=True, blank=True)
    is_paid     = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)

    def start(self):
        dur_minutes = AdminConfig.get_duration()
        self.started_at = timezone.now()
        self.expires_at = self.started_at + timedelta(minutes=dur_minutes)
        self.save()

    def is_active(self):
        return self.started_at and timezone.now() < self.expires_at

# —————————————————————————————————————————————
#  Hasil Foto & Video
# —————————————————————————————————————————————
class Photo(models.Model):
    session     = models.ForeignKey(UserSession, on_delete=models.CASCADE, related_name="photos")
    slot        = models.ForeignKey(CollageSlot, on_delete=models.CASCADE)
    image       = models.ImageField(upload_to="photos/")
    is_final    = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)

class LivePhotoVideo(models.Model):
    session    = models.ForeignKey(UserSession, on_delete=models.CASCADE, related_name="live_videos")
    video_file = models.FileField(upload_to="live_videos/")
    created_at = models.DateTimeField(auto_now_add=True)

class PhotoFilter(models.Model):
    photo      = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="applied_filters")
    filter     = models.ForeignKey(Filter, on_delete=models.CASCADE)