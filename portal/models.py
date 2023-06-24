from django.db import models
from django.contrib.auth.models import User
import random
from .utils import getSeat

CLASSES_CHOICES = (
    ("1a"," AC First Class (1A)"),
    ("2a","AC 2 Tier (2A)"),
    ("3a","AC 3 Tier (3A)"),
    ("3e","AC 3 Economy (3E)"),
    ("sl","Sleeper (SL)"),
    ("2s","Second Sitting (2S)"),
)


def generate_pnr_number():
    while True:
        pnr_number = random.randint(1000000000, 9999999999)
        obj = Booking.objects.filter(pnr=pnr_number)
        if not obj:
            return pnr_number

class Booking(models.Model):
    pnr = models.PositiveIntegerField(default=generate_pnr_number)
    train = models.CharField(max_length=500)
    name = models.CharField(max_length=255)
    mobile_no = models.PositiveBigIntegerField()
    source = models.CharField(max_length=500)
    destination = models.CharField(max_length=155)
    date = models.DateField()
    classs = models.CharField(max_length=255, choices=CLASSES_CHOICES)
    total_fare = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default=getSeat)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name