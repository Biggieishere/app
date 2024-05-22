from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class review(models.Model):
    review = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username}: {self.review}"


class blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = RichTextField()
    time = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=100)
    images= models.ImageField(upload_to='images/',blank=True)
    
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

     
class chat(models.Model):
    messages = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.messages
    
 
