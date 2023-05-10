import uuid
from django.db import models

class Problem(models.Model):
    difficulty_type=(
        ('easy','Easy Problem'),
        ('medium','Medium Problem'),
        ('hard','Hard Problem')
    )
    concerned_website=(
        ('leetcode','Leetcode'),
        ('codechef','Codechef'),
        ('gfg','GeekForGeeks')
    )
    title=models.CharField(max_length=200)
    tags=models.ManyToManyField('Tag',blank=True)
    website=models.CharField(max_length=200,choices=concerned_website,default='leetcode')
    difficulty=models.CharField(max_length=200,choices=difficulty_type)
    source_link=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,
                    primary_key=True,editable=False)
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,
                    primary_key=True,editable=False)
    
    def __str__(self):
        return self.name
