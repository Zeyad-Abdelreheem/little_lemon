from django.db import models

# Create your models here.

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField()

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'
