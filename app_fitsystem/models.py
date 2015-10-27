from django.db import models
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=False, default=timezone.now().strftime("%d.%m.%Y"))
    last_payment = models.DateField(blank=False, default=timezone.now().strftime("%d.%m.%Y"))
    payment_date = models.DateTimeField(
            blank=True, null=True)


    def pay(self):
        self.last_payment = timezone.now()
        self.save()

    def __str__(self):
        return self.name