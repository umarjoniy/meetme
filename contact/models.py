from django.db import models


# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Subscribers(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
