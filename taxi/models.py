from django.db import models


# Create your models here.

class Taxis(models.Model):
    name = models.CharField(max_length=50)
    lasname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    number = models.CharField(max_length=10)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    license = models.CharField(max_length=100)

    # image=models.ImageField()
    def __str__(self):
        return self.name


class Account(models.Model):
    login = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13, verbose_name='nomber')

    def __str__(self):
        return self.username
