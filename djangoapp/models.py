from django.db import models



class Rishab(models.Model):
    name=models.CharField(max_length=50),
    age=models.IntegerField()
    sex=models.CharField(max_length=10)
    color=models.CharField(max_length=30)
  
    
    
