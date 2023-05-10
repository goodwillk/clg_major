from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name=models.CharField(max_length=200,blank=False,null=False)
    last_name=models.CharField(max_length=200,blank=False,null=False)
    email=models.EmailField(max_length=500,blank=False,null=False)
    username=models.CharField(max_length=200,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    short_bio=models.CharField(max_length=200,blank=True,null=True)
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    social_github=models.CharField(max_length=200,blank=True,null=True)
    social_twitter=models.CharField(max_length=200,blank=True,null=True)
    social_linkedin=models.CharField(max_length=200,blank=True,null=True)
    social_stackoverflow=models.CharField(max_length=200,blank=True,null=True)
    social_facebook=models.CharField(max_length=200,blank=True,null=True)
    social_instagram=models.CharField(max_length=200,blank=True,null=True)
    social_portfolio=models.CharField(max_length=200,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.username)
    