from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Order(models.Model):
    order_number = models.CharField(max_length=50)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def update_total_price(self):
        total_price = sum(item.total_price for item in self.order_items.all())
        self.total_price = total_price
        self.save()

    def __str__(self):
        return self.order_number

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    part = models.ForeignKey('CarPart', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = self.part.price * self.quantity
        super().save(*args, **kwargs)
        self.order.update_total_price()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.order.update_total_price()


class CarPart(models.Model):
    CATEGORY_CHOICES = [
        ('Engine', 'Engine'),
        ('Tire', 'Tire'),
        ('Brake', 'Brake'),
        ('Battery', 'Battery'),
        ('Lighting', 'Lighting'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')

    def __str__(self):
        return self.name

@receiver(post_save, sender=CarPart)
def update_order_total_on_part_save(sender, instance, **kwargs):
    for order_item in instance.orderitem_set.all():
        order_item.save()

@receiver(post_delete, sender=OrderItem)
def update_order_total_on_item_delete(sender, instance, **kwargs):
    instance.order.update_total_price()

