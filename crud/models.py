from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()


admin.site.register(Person)