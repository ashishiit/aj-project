from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField(max_length = 300)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add = True)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('(?P<id_num>\d+)/', kwargs={'id_num':self.id})