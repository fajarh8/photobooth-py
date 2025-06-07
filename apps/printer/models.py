from django.db import models
from apps.booth.models import UserSession, Photo

# —————————————————————————————————————————————
#  Antrian Cetak
# —————————————————————————————————————————————
class PrintJob(models.Model):
    session     = models.ForeignKey(UserSession, on_delete=models.CASCADE, related_name="print_jobs")
    photo       = models.ForeignKey(Photo, on_delete=models.CASCADE)
    is_printed  = models.BooleanField(default=False)
    requested_at = models.DateTimeField(auto_now_add=True)
    printed_at  = models.DateTimeField(null=True, blank=True)
