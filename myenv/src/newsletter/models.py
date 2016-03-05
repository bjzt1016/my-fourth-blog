from django.db import models

# Create your models here.
class  SignUp(models.Model):
	email=models.EmailField()
	full_name=models.CharField(max_length=2000,blank=True,null=True)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)
	
    #This is for instances of the actual model itself,
    #so instance class instances are the model
	def __str__(self): #python3.3 is __str__;python2.7 is __unicode__
		return self.email