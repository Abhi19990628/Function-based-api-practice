from django.db import models



class Rishab(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    sex=models.CharField(max_length=10)
    color=models.CharField(max_length=30)
  
    
    
[
  {
    "name": "John",
    "age": 30,
    "sex": "Male",
    "color": "Blue"
  },
  {
    "name": "Alice",
    "age": 25,
    "sex": "Female",
    "color": "Red"
  }
]
