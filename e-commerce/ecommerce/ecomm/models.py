from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.customer_name

class Order(models.Model):
    customer = models.ForeignKey(Customer, default=1, related_name='customer_order', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, default=1, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item_name



