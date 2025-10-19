from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime, date


class MainImageCarousel(models.Model):
    cecypharm_title = models.CharField(max_length=255, blank=True, null=True)
    cecypharm_description = models.TextField()
    cecypharm_slug = models.SlugField (max_length=255,blank=True, null=True)
    cecypharm_image = models.FileField(upload_to='main_image/') 
    cecypharm_publish_date = models.DateTimeField (auto_now_add= True)
    cecypharm_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['cecypharm_publish_date']
    
    def __str__(self):
        return self.cecypharm_title + ' | ' + str(self.cecypharm_author)
    
    def get_absolute_url(self):
        return reverse('home',)
