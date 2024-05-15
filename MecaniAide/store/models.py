from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=50)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def update_total_price(self):
        total_price = sum(part.price for part in self.car_parts.all())
        self.total_price = total_price
        self.save()

    def __str__(self):
        return self.order_number

class CarPart(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='car_parts', default=None)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.order:
            self.order.update_total_price()

    def __str__(self):
        return self.name
