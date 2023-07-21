from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_title=models.CharField(max_length=50)
    post_cat=models.CharField(max_length=50)
    post_publish_date=models.DateField()
    
