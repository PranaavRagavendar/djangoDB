from django.db import models
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync

class Member(models.Model):
    staffname = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    name1 = models.CharField(max_length=20)
    name2 = models.CharField(max_length=20)
    name3 = models.CharField(max_length=20)

    def __str__(self):
     return self.staffname+ ' ' +self.subject+ ' ' +self.name1+ ' ' +self.name2+ ' ' +self.name3
 
 
class Login(models.Model):
   
    email = models.EmailField(max_length=20)
    password= models.CharField(max_length=20)
     
    def __str__(self):
        return self.email 
 
 
 
class Notification(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    notification = models.TextField(max_length=100)
    is_seen =models.BooleanField(default=False)
    
    
    
    
    
     
     