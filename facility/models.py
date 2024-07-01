from datetime import timedelta, date
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

"""
have to add new model for facilities which is already taken by employee and expired date is related to that table

"""

def get_expired_date() -> date:
    exp_date = date.today() + timedelta(weeks=4)
    return exp_date


class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.description}\nCost: {self.cost}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.description}"


class Order(models.Model):
    date = models.DateField(auto_now=True)
    expired_date = models.DateField(default=get_expired_date)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    facilities = models.ManyToManyField(Facility)



