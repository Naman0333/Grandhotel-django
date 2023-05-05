from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.exceptions import ValidationError


class Room(models.Model):
    ROOM_TYPES = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('triple', 'Triple'),
        ('quad', 'Quad'),
        ('queen', 'Queen'),
        ('king', 'King'),
        ('suite', 'Suite'),
    )

    room_type = models.CharField(choices=ROOM_TYPES, max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    beds = models.PositiveIntegerField()
    max_guests = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/room_images/')
    available = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.room_type} Room ({self.beds} Beds)'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'

class Booking(models.Model):
    room_type = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()
    num_of_guests = models.IntegerField(default=1)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('booking_detail', args=[str(self.id)])
        
    def __str__(self):
        return f"{self.name} - {self.room_type}"

class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/facility_images')

    def __str__(self):
        return self.name
    
class Dining(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/dining_images')
    price_range = models.CharField(max_length=50)

    def __str__(self):
        return self.name

