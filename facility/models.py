from datetime import datetime, timedelta

from django.db import models

# Create your models here.

def get_expired_date() -> datetime:
    return datetime.today() + timedelta(weeks=4)


class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.PositiveIntegerField()
    expired_date = models.DateField(default=get_expired_date)

    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.description}\nCost: {self.cost}\nExpired_date: {self.expired_date.strftime('%Y-%m-%d')}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.description}"



