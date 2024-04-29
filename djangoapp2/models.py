from django.db import models

class Abhishek(models.Model):
    name=models.CharField(max_length=10)
    age= models.IntegerField()
    sex=models.CharField(max_length=20)
    color=models.CharField(max_length=20)