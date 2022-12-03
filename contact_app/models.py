from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self) -> str:
        return self.email