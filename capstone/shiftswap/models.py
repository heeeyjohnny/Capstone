from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_contractor = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    company = models.CharField(max_length=200)
    company_location = models.CharField(max_length=150)

    def __str__(self):
        return self.username


class JobCard(models.Model):
    type = models.CharField(max_length=200)
    employer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='jobcard_location')
    description = models.CharField(max_length=400, blank=True)
    date = models.DateField(null=True, blank=True, default=None)
    start_time = models.TimeField(default=None)
    end_time = models.TimeField(default=None)
    pay = models.FloatField(default=0.00)

    def __str__(self):
        return self.type
