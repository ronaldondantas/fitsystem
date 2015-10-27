from django.db import models
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    last_payment = models.DateField(
            default=timezone.now)
    payment_date = models.DateField(
            default=timezone.now)

    def pay(self):
        self.last_payment = timezone.now()
        self.save()

    def __str__(self):
        return self.name