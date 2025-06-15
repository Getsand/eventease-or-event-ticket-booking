
# Create your models here.
from django.db import models
from django.utils import timezone
from authentification.models import User
from django.db import transaction

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.event.name}"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            event = Event.objects.select_for_update().get(pk=self.event.pk)
            if event.available_seats <= 0:
                raise ValueError("No seats available")
            event.available_seats -= 1
            event.save()
            super().save(*args, **kwargs)
