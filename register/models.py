from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
	username=models.CharField(max_length=50,default='LetField')
	user=models.OneToOneField(to=User,on_delete=models.CASCADE,primary_key=True)
	First_name=models.CharField(max_length=50)
	Last_name=models.CharField(max_length=50)
	Birthdate=models.DateField()
	Image=models.ImageField(upload_to='profilepic',null=True)
	Bio=models.TextField()
	
	def __str__(self):
		return self.First_name+" "+self.Last_name
	