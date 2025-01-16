from django.db import models
from django.conf import settings


class Affiliate(models.Model):
    affiliate_id = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reward_amount = models.DecimalField(max_digits=16,
        decimal_places=5, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.affiliate_id