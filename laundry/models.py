from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=10, default='customer', editable=True)

    def __str__(self):
        return self.name

class Laundry(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='laundry/files/laundries')
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name