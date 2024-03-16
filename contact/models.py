from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.first_name
