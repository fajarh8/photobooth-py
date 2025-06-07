from django.db import models
from apps.booth.models import UserSession
from django.utils import timezone

# —————————————————————————————————————————————
#  Email Delivery & URL Expiry
# —————————————————————————————————————————————
class EmailDelivery(models.Model):
    session       = models.OneToOneField(UserSession, on_delete=models.CASCADE, related_name="email_delivery")
    recipient     = models.EmailField()
    sent_at       = models.DateTimeField(auto_now_add=True)
    expiry_date   = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expiry_date