from django.db import models
from django.utils import timezone


# Create your models here.

class Position(models.Model):
    nameposition = models.CharField(max_length=150)
    created = models.DateTimeField(default=timezone.now()) #decimal do mysql

    def __str__(self):
        return self.nameposition

class Users(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(default=timezone.now()) #decimal do mysql
    position = models.ForeignKey(Position, related_name="user", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
class Comments(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500) # varchar do mysql
    date = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True) # datetime default now() do mysql
    user = models.ForeignKey(Users, related_name="user", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

class Equipment(models.Model):
    name = models.CharField(max_length=150) # varchar do mysql
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True) # datetime default now() do mysql
    comments = models.ForeignKey(Comments, related_name="comments", on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
