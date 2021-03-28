from django.db import models
from django.contrib.auth.models import User

class booksTable(models.Model):
    name=models.CharField(max_length=60)
    author=models.CharField(max_length=60)
    price=models.FloatField()
    publisher=models.CharField(max_length=60)


class bookUsers(models.Model):
    user=models.OneToOneField(User, on_delete= models.CASCADE)
    nickname=models.CharField(max_length=60 , null=False)
