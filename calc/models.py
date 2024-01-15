from django.db import models


# Create your models here.

#index.html page


class Education(models.Model):
	degree= models.CharField(max_length=255)
	institute= models.CharField(max_length=255)
	startDate= models.DateField() 
	endDate= models.DateField()

class Experience(models.Model):
	img= models.ImageField(upload_to='images/')
	position= models.CharField(max_length=255)
	institute= models.CharField(max_length=255)
	startDate= models.DateField() 
	endDate= models.DateField()
	

class Publication(models.Model):
	img= models.ImageField(upload_to='images/')
	category= models.CharField(max_length=100)
	url= models.URLField()
	title= models.CharField(max_length=255)
	desc= models.TextField()
	date= models.DateField()
	
#blog_single.html page

class Blog(models.Model):
	img= models.ImageField(upload_to='images/')
	title= models.CharField(max_length=255)
	scholarurl= models.URLField()
	author= models.CharField(max_length=255)
	tag= models.CharField(max_length=50)	
	desc= models.TextField()
	articleurl= models.URLField()


#project.html page

class Project(models.Model):
	category=models.CharField(max_length=50)
	client=models.CharField(max_length=150)
	projectDate= models.DateField()
	projectUrl= models.URLField()

	projectTitle=models.CharField(max_length=255)
	img1= models.ImageField(upload_to='images/')
	img2= models.ImageField(upload_to='images/')
	img3= models.ImageField(upload_to='images/')
	desc= models.TextField()

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
	
