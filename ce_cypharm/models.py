from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime, date


#This model is for the fist carousel image
class MainImageCarousel(models.Model):
    cecypharm_title = models.CharField(max_length=255, blank=True, null=True)
    cecypharm_description = models.TextField()
    cecypharm_slug = models.SlugField (max_length=255,blank=True, null=True)
    cecypharm_image = models.FileField(upload_to='main_image/') 
    cecypharm_publish_date = models.DateTimeField (auto_now_add= True)
    cecypharm_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['-cecypharm_publish_date']
    
    def __str__(self):
        return self.cecypharm_title + ' | ' + str(self.cecypharm_author)
    
    def get_absolute_url(self):
        return reverse('home',)

#This model is for the fist image what we offer  
class CecypharmFirstCategoryImage(models.Model):
    first_category_cecypharm_title = models.CharField(max_length=255, blank=True, null=True)
    first_category_cecypharm_description = models.TextField()
    first_category_cecypharm_slug = models.SlugField (max_length=255,blank=True, null=True)
    first_category_cecypharm_image = models.FileField(upload_to=' first_image/') 
    first_category_cecypharm_publish_date = models.DateTimeField (auto_now_add= True)
    first_category_cecypharm_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['-first_category_cecypharm_publish_date']
    
    def __str__(self):
        return self.first_category_cecypharm_title + ' | ' + str(self.first_category_cecypharm_author)
    
    def get_absolute_url(self):
        return reverse('home',)

# Appointment model of ce-cyoharm
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
    
    
    
#This model is for the second image what we offer  
class CecypharmSecondCategoryImage(models.Model):
    second_category_cecypharm_title = models.CharField(max_length=255, blank=True, null=True)
    second_category_cecypharm_description = models.TextField()
    second_category_cecypharm_slug = models.SlugField (max_length=255,blank=True, null=True)
    second_category_cecypharm_image = models.FileField(upload_to=' second_image/') 
    second_category_cecypharm_publish_date = models.DateTimeField (auto_now_add= True)
    second_category_cecypharm_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['-second_category_cecypharm_publish_date']
    
    def __str__(self):
        return self.second_category_cecypharm_title + ' | ' + str(self.second_category_cecypharm_author)
    
    def get_absolute_url(self):
        return reverse('home',)