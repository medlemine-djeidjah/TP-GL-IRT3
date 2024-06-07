<<<<<<< HEAD
from django.db import models

# Create your models here.
=======
from django.db import models

<<<<<<< HEAD
# Create your models here.
=======
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.make} {self.model}"

class CarPart(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
>>>>>>> 5dc325a283b77d22535eae61e57aa24aaa759670
>>>>>>> main
