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
    start_date = models.DateTimeField(null=True, blank=True, default=None)
    end_date = models.TimeField(default=None)
    pay = models.FloatField(default=0.00)

    def __str__(self):
        return self.type
