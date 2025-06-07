from django.db import models
from booth.models import UserSession

# Create your models here.
class PaymentTransaction(models.Model):
    session = models.OneToOneField(UserSession, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    response_data = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)
