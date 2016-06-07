from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import os

# def set_path(instance, filename):
# 	return os.path.join("image","profile",filename)

# Create your models here.

class Domain(models.Model):
        username = models.OneToOneField(User, null=True)
	domain = models.CharField(max_length=1000, blank=False, null=True)

	def __unicode__(self):
		return self.domain

class Profile(models.Model):
	username = models.OneToOneField(User,null=True)
	firstname = models.CharField(max_length=30, blank=True, null=True)
	lastname = models.CharField(max_length=30, blank=True, null=True)
	gender = models.IntegerField(default=0, blank=True, null=True)
       	dob = models.DateField(blank=True, verbose_name="DOB", null=True)
	profileimage = models.FileField( blank=True, null=True)

	def __unicode__(self):
		list=[self.firstname,self.lastname]
		str=",".join(list)
		return str

class Database(models.Model):
        domain = models.CharField(max_length=100,blank=True,null=True)
        categary = models.CharField(max_length=100, blank=True, null=True)
        company = models.CharField(max_length=100, blank=True, null=True)
        url = models.URLField(max_length=200, blank=True, null=True) 
        end_date=models.DateField(blank=True,null=True)
        def __unicode__(self):
		return self.company       

class Newinternship(models.Model):
        domain=models.CharField(max_length=100,blank=True,null=True)
        newintern=models.IntegerField(blank=True,null=True)
        def __unicode__(self):
                return self.newintern

User.profile = property(lambda u: Profile.objects.get_or_create(username=u)[0])
User.domain = property(lambda u: Domain.objects.get_or_create(username=u)[0])
