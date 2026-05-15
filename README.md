# Ex01 Django ORM Web Application
## Date: 15-05-2026

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```python
admin.py
from django.contrib import admin
from .models import FoodOrder

@admin.register(FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_id',
        'customer_name',
        'food_item',
        'quantity',
        'price',
        'delivery_address',
        'order_status'
    )
models.py
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

DEVELOPED BY: SAKTHIVEL K
REGISTER NO: 212225240133
```


## OUTPUT

<img width="1883" height="929" alt="image" src="https://github.com/user-attachments/assets/25009938-3f44-4d00-b3c1-b7979b5853d3" />



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
