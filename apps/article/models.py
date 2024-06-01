from django.db import models
from apps.user.models import Account
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=225)

    slug = models.SlugField(unique=True, null=True, blank=True, max_length=225)

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title  


class Tag(models.Model):
    title = models.CharField(max_length=225)        

    def __str__(self):
        return self.title


class Article(models.Model):
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=225)
    
    title = models.CharField(max_length=225)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="Article/")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("single", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.title)
            
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Comment(models.Model):    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    website = models.URLField(null=True,blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.name
    