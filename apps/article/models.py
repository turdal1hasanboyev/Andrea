from django.db import models
from ..user.models import Account


class Category(models.Model):
    title = models.CharField(max_length=225)
    
    def __str__(self):
        return self.title  


class Tag(models.Model):
    title = models.CharField(max_length=225)        

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="Article/")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    website = models.URLField(null=True,blank=True)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name