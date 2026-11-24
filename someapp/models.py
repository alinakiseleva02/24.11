from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):  
    full_name = models.CharField(max_length=255)

class Service(models.Model): 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('new', 'Новая'),
            ('confirmed', 'Подтверждено'),
            ('completed', 'Завершено'),
        ],
        default='new',
        editable=False,
    )