from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Article(models.Model):
	title 	= models.CharField(max_length=100)
	author 	= models.CharField(max_length=100)
	email 	= models.EmailField()
	date 	= models.DateTimeField(auto_now_add=True)

class User(AbstractUser):
	first_name = models.CharField(max_length=100)
	last_name  = models.CharField(max_length=100)
	email 	   = models.EmailField()
	password   = models.TextField(max_length=200)
	username   = None
		

