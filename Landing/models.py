from django.db import models
from django.utils import timezone
# Create your models here.


class Exp(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField(default=timezone.localdate())
    end_date = models.DateField(default=timezone.localdate())
    position = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.title



class School(models.Model):
    scname = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.localdate())
    end_date = models.DateField(default=timezone.localdate())
    major = models.CharField(max_length=100)
    second_major = models.CharField(max_length=100)

    def __str__(self):
        return self.scname