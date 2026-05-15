from django.db import models

class FoodOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    delivery_address = models.TextField()
    order_status = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name