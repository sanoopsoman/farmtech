from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Login(AbstractUser):
    usertype=models.CharField(max_length=40)
    viewpaassword=models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.username
    
class Farmer(models.Model):
    farmer=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=30, null=True)
    email=models.EmailField()
    mob=models.IntegerField()
    address=models.TextField()
    img=models.ImageField(upload_to="gallery", null=True)
    gender=models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.name
    
class Farmtech(models.Model):
    farm=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=30, null=True)
    email=models.EmailField()
    mob=models.IntegerField()
    img=models.ImageField(upload_to="gallery", null=True)
    gender=models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.name
    