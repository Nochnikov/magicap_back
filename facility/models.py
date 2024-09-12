from datetime import timedelta, date
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

def get_expired_date() -> date:
    exp_date = date.today() + timedelta(weeks=4)
    return exp_date


class Benefit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    expired_date = models.DateField(default=get_expired_date)
    cost = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='benefits/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.description}\nCost: {self.cost}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='categories/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.description}"

    class Meta:
        verbose_name_plural = 'Categories'


class Order(models.Model):
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
    benefits = models.ManyToManyField(Benefit)


